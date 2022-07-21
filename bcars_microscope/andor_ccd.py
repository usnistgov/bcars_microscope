import sys
import traceback


import numpy as np
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore

from ui.ui_andor_setup import Ui_Dialog as Ui_AndorConfig
# from PyQt5.QtGui import QCloseEvent

from pyAndorSDK2 import atmcd, atmcd_codes, atmcd_errors

from bcars_microscope import dark_style_sheet as stylesheet

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

err_codes = atmcd_errors.Error_Codes

__all__ = ['AndorNewton970', 'DialogAndorConfig']

# Steps from LabView initialize
# 1. Init SDK
# 2. Get SDK software info (3 parts)
# 3. Get Camera Handle
# 4. Cooler on, set temp, set fan mode
# 5. Set Acuqisition Mode
# 6. Set output amplifier (EM or Conventional)
# 7. Set AD Chan = 0
# 8. Set horizontal shift speed
# 9. Set preamp gain
# 10. Set VS shift speed
# 11. Set VS amplitude
# 12. Set trigger mode
# 13. Set exposure time
# 14. Set frame transfer mode = Off
# 15. Set shutter
# 16. Set image flip
# 17. Set single-track or not
# 18. Set read mode
# 19. Get read out time for FVB or get read timings

# def get_amplifier_list():
#     ret_code, n_amps = sdk.GetNumberAmp()
#     return [sdk.GetAmpDesc(k, 21)[1] for k in range(n_amps)]

# def get_ad_speed_list():
#     sdk.GetHSSpeed()


def andor_err_code_str(code):
    """ Return the associated text of an error code """
    return err_codes(code).name


class AndorNewton970:
    """ Andor Newton 970 Settings EMCCD model """
    default_fvb = {'cooler': True,
                   'exposure_time': 0.0035,
                   'temperature': -70,
                   'amplifier': 'Conventional',
                   'hs_speed': 2.5,
                   'vs_speed_idx': 0,
                   'vs_shift_amp': 0,
                   'preamp_gain_idx': 2,
                   'baseline_clamping': True,
                   'readout_mode': 'FULL_VERTICAL_BINNING',
                   'trigger_mode': 'INTERNAL',
                   'shutter_mode': 'PERMANENTLY_OPEN',
                   'acquisition_mode': 'RUN_TILL_ABORT'}

    default_imaging = default_fvb.copy()
    default_imaging.update({'readout_mode': 'IMAGE'})

    default_imaging_trigd = default_imaging.copy()
    default_imaging_trigd.update({'trigger_mode': 'EXTERNAL'})

    default_fvb_trigd = default_fvb.copy()
    default_fvb_trigd.update({'trigger_mode': 'EXTERNAL'})

    defaults = default_fvb.copy()

    if defaults['amplifier'] == 'Conventional':
        defaults['amplifier_idx'] = 1
    elif defaults['amplifier'] == 'ElectronMultiplying':
        defaults['amplifier_idx'] = 0
    else:
        raise ValueError('Valid Amplifiers are Conventional and ElectronMultiplying')

    def __init__(self, initialized_sdk=None, settings_kwargs=None):
        self.sdk = initialized_sdk
        if initialized_sdk is not None:
            print('Using pre-initialized SDK reference')

        self.name = 'Andor Newton 970'
        self.is_fvb_or_sgl_track = None
        self.n_rows = None
        self.n_cols = None
        self.mode_codes = {}
        self.mode_codes['acquisition'] = {k.name: k.value for k in atmcd_codes.Acquisition_Mode}
        self.mode_codes['read'] = {k.name: k.value for k in atmcd_codes.Read_Mode}
        self.mode_codes['shutter'] = {k.name: k.value for k in atmcd_codes.Shutter_Mode}
        self.mode_codes['trigger_mode'] = {k.name: k.value for k in atmcd_codes.Trigger_Mode}

        self.settings = self.defaults.copy()

        # print('===== {}'.format(settings_kwargs))
        if settings_kwargs:
            # print('Updating: {}'.format(settings_kwargs))
            self.settings.update(settings_kwargs)

    def init_sdk(self, force=False):
        """ Initialize the sdk """
        if (self.sdk is not None) & (not force):
            print('Cannot initialize SDK: already initialized. Use force parameter if needed.')
        else:
            self.sdk = atmcd()
            ret_code = self.sdk.Initialize("")  # Initialize camera
            print('Initialize SDK {}: {}'.format(ret_code, andor_err_code_str(ret_code)))
            return ret_code

    @property
    def meta(self):
        output = {}
        prefix = 'CCD'
        # Prepend prefix to settings and put in meta
        output.update({'{}.{}'.format(prefix, k): self.settings[k] for k in self.settings if not isinstance(self.settings[k], dict)})

        # output.update({'{}.{}'.format(prefix,kk): self.settings[k][kk] for kk in self.settings[k] for k in self.settings if isinstance(self.settings[k], dict)})

        # Manually set things:
        output['CCD.cooler'] = self.settings['cooler']
        output['CCD.fanmode'] = 'full'

        output['CCD.temperature.actual'] = round(self.sdk.GetTemperatureStatus()[1], 2)
        output['CCD.temperature.set'] = round(self.sdk.GetTemperatureStatus()[2], 2)
        output['CCD.amplifier_idx'] = [self.sdk.GetAmpDesc(num, 25)[1] for num in range(self.sdk.GetNumberAmp()[1])].index(self.settings['amplifier'])
        output['CCD.HS_shift_frequency'] = '{} MHz'.format(self.settings['hs_speed'])
        output['CCD.VS_shift_time'] = '{} us'.format(self.sdk.GetVSSpeed(self.settings['vs_speed_idx'])[1])
        output['CCD.preamp_gain'] = self.sdk.GetPreAmpGain(self.settings['preamp_gain_idx'])[1]
        output['CCD.baseline_clamping'] = (self.sdk.GetBaselineClamp()[1] == 1)
        for k in self.mode_codes:
            for kk in self.mode_codes[k]:
                output['CCD.modecode.{}.{}'.format(k, kk)] = self.mode_codes[k][kk]
        return output

    def get_hs_speed_info(self):
        amp_type_idx = self.settings['amplifier_idx']

        self._hs_speed_idx_dict = {}

        n_ads = self.sdk.GetNumberADChannels()[1]  # Number of A/D's
        # print('Camera Capabilities:')
        for num_ad in range(n_ads):
            for num_speeds in range(self.sdk.GetNumberHSSpeeds(num_ad, amp_type_idx)[1]):
                # name_amp = self.sdk.GetAmpDesc(amp_type_idx, 21)[1]
                # print('Amp: {} ({}); AD: {}; Speed: {} MHz ({})'.format(name_amp, amp_type_idx, num_ad, self.sdk.GetHSSpeed(num_ad, amp_type_idx, num_speeds)[1], num_speeds))
                self._hs_speed_idx_dict[self.sdk.GetHSSpeed(num_ad, amp_type_idx, num_speeds)[1]] = {'ad_channel': num_ad, 'hs_speed_idx': num_speeds}

    def set_hs_speed(self):
        if not self._hs_speed_idx_dict:
            self.get_hs_speed_info()

        ad_speed_idx_dict = self._hs_speed_idx_dict[self.settings['hs_speed']]

        ret_code = self.sdk.SetADChannel(ad_speed_idx_dict['ad_channel'])
        print('Set AD Channel: {} -- {}: {}'.format(ad_speed_idx_dict['ad_channel'], ret_code, andor_err_code_str(ret_code)))

        # Set horizontal shift speed (MHz)
        ret_code = self.sdk.SetHorizontalSpeed(ad_speed_idx_dict['hs_speed_idx'])
        print('Set Horizontal Shift Speed: {} -- {}: {}'.format(ad_speed_idx_dict['hs_speed_idx'], ret_code, andor_err_code_str(ret_code)))

    def init_camera(self):
        ret_code_list = []

        if self.settings['cooler']:
            # Cooler on
            ret_code = self.sdk.CoolerON()
            print('Cooler ON: {}: {}'.format(ret_code, andor_err_code_str(ret_code)))

        else:
            ret_code = self.sdk.CoolerOFF()
            print('Cooler OFF: {}: {}'.format(ret_code, andor_err_code_str(ret_code)))

        ret_code_list.append(ret_code)
        del ret_code

        # Set Temperature
        ret_code = self.sdk.SetTemperature(self.settings['temperature'])
        ret_code_list.append(ret_code)
        print('Set temperature: {} -- {}: {}'.format(self.settings['temperature'], ret_code, andor_err_code_str(ret_code)))

        # Set fan mode
        # 0: fan on full; (1) fan on low; (2) fan off (2)
        ret_code = self.sdk.SetFanMode(0)
        ret_code_list.append(ret_code)
        print('Fan Mode: Full -- {}: {}'.format(ret_code, andor_err_code_str(ret_code)))

        # Set Acuqisition Mode
        # 1 Single Scan 2 Accumulate 3 Kinetics 4 Fast Kinetics 5 Run till abort

        ret_code = self.sdk.SetAcquisitionMode(self.mode_codes['acquisition'][self.settings['acquisition_mode']])
        ret_code_list.append(ret_code)
        print('Set Acquisition Mode: {} -- {}: {}'.format(self.settings['acquisition_mode'], ret_code, andor_err_code_str(ret_code)))

        # Set output amplifier (0 EM or 1 Conventional)
        ret_code = self.sdk.SetOutputAmplifier(self.settings['amplifier_idx'])
        print('Set Amplifier: {} -- {}: {}'.format(self.settings['amplifier_idx'], ret_code, andor_err_code_str(ret_code)))

        self.get_hs_speed_info()
        self.set_hs_speed()

        # Set preamp gain
        print('Number of Gains: {}'.format(self.sdk.GetNumberPreAmpGains()[1]))
        ret_code = self.sdk.SetPreAmpGain(self.settings['preamp_gain_idx'])
        ret_code_list.append(ret_code)
        print('Set Pre-Amp Gain: {} -- {}: {}'.format(self.settings['preamp_gain_idx'], ret_code, andor_err_code_str(ret_code)))

        # Set baseline clamping
        ret_code = self.sdk.SetBaselineClamp(int(self.settings['baseline_clamping']))
        ret_code_list.append(ret_code)
        print('Set Baseline Clamping: {} -- {}: {}'.format(self.settings['baseline_clamping'], ret_code, andor_err_code_str(ret_code)))

        # self.sdk.GetNumberVSSpeeds
        ret_code = self.sdk.SetVSSpeed(self.settings['vs_speed_idx'])
        ret_code_list.append(ret_code)
        print('Set Vertical Shift Speed: {} -- {}: {}'.format(0, ret_code, andor_err_code_str(ret_code)))

        # 11. Set VS amplitude
        ret_code = self.sdk.SetVSAmplitude(self.settings['vs_shift_amp'])
        ret_code_list.append(ret_code)
        print('Set Vertical Shift Ampltiude: {} -- {}: {}'.format(0, ret_code, andor_err_code_str(ret_code)))

        # 12. Set trigger mode
        # 0: Internal; 1: External; 6: External Start; 7: External Exposure (Bulb)
        # 9: External FVB EM (only valid for EM Newton models in FVB mode)
        # 10: Software Trigger 11: External Charge Shifting
        # print(self.mode_codes['trigger_mode'])
        # print(self.settings['trigger_mode'])
        # ret_code = self.sdk.SetTriggerMode(self.mode_codes['trigger_mode'][self.settings['trigger_mode']])
        # ret_code_list.append(ret_code)
        # print('Set Trigger Mode: {} -- {}: {}'.format(self.mode_codes['trigger_mode'][self.settings['trigger_mode']],
        #                                               ret_code, andor_err_code_str(ret_code)))

        # # 0: Off; 1: On
        ret_code = self.sdk.SetFastExtTrigger(1)
        # ret_code_list.append(ret_code)
        print('Set Fast External Trigger: ON -- {}: {}'.format(ret_code, andor_err_code_str(ret_code)))
        # ret_code_trig, ret_code_fast = self.set_fast_external_trigger()
        # ret_code_trig = self.set_internal_trigger()
        ret_code = self.sdk.SetTriggerMode(self.mode_codes['trigger_mode'][self.settings['trigger_mode']])

        # Set exposure time
        ret_code = self.sdk.SetExposureTime(self.settings['exposure_time'])
        ret_code_list.append(ret_code)
        print('Set Exposure Time: {} -- {}: {}'.format(self.settings['exposure_time'], ret_code, andor_err_code_str(ret_code)))

        # Set frame transfer mode = Off (0)
        ret_code = self.sdk.SetFrameTransferMode(0)
        ret_code_list.append(ret_code)
        print('Frame Transfer Mode: OFF -- {}: {}'.format(ret_code, andor_err_code_str(ret_code)))

        # Set shutter
        ret_code = self.sdk.SetShutter(0, self.mode_codes['shutter'][self.settings['shutter_mode']], 0, 0)
        ret_code_list.append(ret_code)
        print('Shutter Mode: {} -- {}: {}'.format(self.mode_codes['shutter'][self.settings['shutter_mode']], ret_code, andor_err_code_str(ret_code)))

        # Set image flip
        ret_code = self.sdk.SetImageFlip(0, 0)
        ret_code_list.append(ret_code)
        print('Set Image Flip: OFF, OFF -- {}: {}'.format(ret_code, andor_err_code_str(ret_code)))

        # Set single-track or not
        # ret_code = self.sdk.SetSingleTrack()

        # Set read mode
        # 0 Full Vertical Binning; 1: Multi-Track; 2: Random-Track; 3: Single-Track; 4: Image
        ret_code = self.sdk.SetReadMode(self.mode_codes['read'][self.settings['readout_mode']])
        ret_code_list.append(ret_code)
        print('Read Mode: {} -- {}: {}'.format(self.mode_codes['read'][self.settings['readout_mode']], ret_code, andor_err_code_str(ret_code)))
        if self.settings['readout_mode'] == 'FULL_VERTICAL_BINNING':
            self.is_fvb_or_sgl_track = True
        else:
            self.is_fvb_or_sgl_track = False

        ret_code, self.n_cols, self.n_rows = self.sdk.GetDetector()
        ret_code_list.append(ret_code)
        print('Detector Size: ({}, {})'.format(self.n_rows, self.n_cols))
        # Oddly, SetImage was needed. Maybe there's a default binning
        if self.is_fvb_or_sgl_track:
            ret_code = self.sdk.SetImage(1, 1, 1, self.n_rows, 1, 1)
        else:
            ret_code = self.sdk.SetImage(1, 1, 1, 1600, 1, 200)
        ret_code_list.append(ret_code)
        print('Set Image Dimensions: {}: {}'.format(ret_code, andor_err_code_str(ret_code)))

        # 19. Get read out time for FVB or get read timings
        read_out_time = self.sdk.GetReadOutTime()[1]
        print('ReadOut Time: {:.6f} sec'.format(read_out_time))
        print('Exposure Time: {} sec'.format(self.sdk.GetAcquisitionTimings()[1]))
        print('Accumulate Time: {} sec'.format(self.sdk.GetAcquisitionTimings()[2]))
        print('Kinetic Time: {} sec'.format(self.sdk.GetAcquisitionTimings()[3]))
        print('Estimated total time per acquisition: {}'.format(self.net_acquisition_time))

        frame_rate = 1 / self.net_acquisition_time
        print('Frame Rate: {} Hz'.format(frame_rate))

        print('Size of Circular Buffer: {}'.format(self.sdk.GetSizeOfCircularBuffer()[1]))

        ret_code = self.sdk.PrepareAcquisition()
        ret_code_list.append(ret_code)
        print('Prepare Acquisition: {}: {}'.format(ret_code, andor_err_code_str(ret_code)))
        return ret_code_list

    def init_all(self):
        """Initialize both SDK and CCD (Andor)"""
        ret_sdk = self.init_sdk()
        ret_camera_list = self.init_camera()
        # print(ret_sdk, ret_camera_list)
        return (ret_sdk == err_codes.DRV_SUCCESS) & (ret_camera_list.count(err_codes.DRV_SUCCESS) == len(ret_camera_list))

    @property
    def net_acquisition_time(self):
        # Exposure time + readout time
        return self.sdk.GetReadOutTime()[1] + self.sdk.GetAcquisitionTimings()[1]

    def set_fast_external_trigger(self):
        """ Set CCD to fast external trigger """
        try:
            self.settings['trigger_mode'] = 'EXTERNAL'
            ret_code_trig = self.sdk.SetTriggerMode(self.mode_codes['trigger_mode'][self.settings['trigger_mode']])
            print('Set Trigger Mode: {} -- {}: {}'.format(self.mode_codes['trigger_mode'][self.settings['trigger_mode']],
                                                          ret_code_trig, andor_err_code_str(ret_code_trig)))
            self.sdk.EnableKeepCleans(0)
            ret_code_fast = self.sdk.SetFastExtTrigger(1)
            print('Set Fast External Trigger: ON -- {}: {}'.format(ret_code_fast, andor_err_code_str(ret_code_fast)))
            self.sdk.SetKineticCycleTime(0)
        except Exception:
            print(traceback.format_exc())
        return (ret_code_trig, ret_code_fast)

    def set_internal_trigger(self):
        """ Set CCD to internal triggering """
        print('Turn on internal triggering')
        try:
            self.settings['trigger_mode'] = 'INTERNAL'
            ret_code_trig = self.sdk.SetTriggerMode(self.mode_codes['trigger_mode'][self.settings['trigger_mode']])
            print('Set Trigger Mode: {} -- {}: {}'.format(self.mode_codes['trigger_mode'][self.settings['trigger_mode']],
                                                          ret_code_trig, andor_err_code_str(ret_code_trig)))
        except Exception:
            print(traceback.format_exc())
        return ret_code_trig

    @property
    def is_external_trigger(self):
        return self.settings['trigger_mode'] == 'EXTERNAL'

    @property
    def is_internal_trigger(self):
        return self.settings['trigger_mode'] == 'INTERNAL'

    def shutdown(self):
        self.sdk.FreeInternalMemory()
        ret_code = self.sdk.ShutDown()
        print('Shutting Down CCD')
        return ret_code

    def start_acquisition(self):
        ret_code = self.sdk.StartAcquisition()
        print('Starting Acquisition: {} -- {}'.format(ret_code, andor_err_code_str(ret_code)))
        return ret_code

    def stop_acquisition(self):
        ret_code = self.sdk.AbortAcquisition()
        print('Aborting Acquisition: {} -- {}'.format(ret_code, andor_err_code_str(ret_code)))
        return ret_code

    def free_memory(self):
        ret_code = self.sdk.FreeInternalMemory()
        print('Free Internal Memory: {} -- {}'.format(ret_code, andor_err_code_str(ret_code)))
        return ret_code

    def get_num_new_images(self):
        """ ret_code, n_images, first_img, last_img """
        ret_code, first_img, last_img = self.sdk.GetNumberNewImages()
        # ret_code, first_img, last_img = self.sdk.GetNumberAvailableImages()
        # print('New Images: {}:{}'.format(first_img, last_img))

        if first_img == 0:
            n_images = last_img - first_img
        else:
            n_images = last_img - first_img + 1

        # print('New Images: {}:{}'.format(first_img, last_img))

        return ret_code, n_images, first_img, last_img

    @property
    def sgl_image_size(self):
        if self.is_fvb_or_sgl_track is True:
            return self.n_cols
        else:
            return self.n_rows * self.n_cols

    def get_all_images16(self):
        """ Get all available images """
        _, n_images, first_img, last_img = self.get_num_new_images()
        allImageSize = self.sgl_image_size * n_images
        (ret_code, arr, validfirst, validlast) = self.sdk.GetImages16(first_img, last_img, allImageSize)
        return (ret_code, arr.astype(np.uint16), validfirst, validlast)

    def get_last_n_images16(self, k=1):
        """ Get k last images"""
        _, n_images, _, last_img = self.get_num_new_images()
        allImageSize = self.sgl_image_size * k
        (ret_code, arr, validfirst, validlast) = self.sdk.GetImages16(last_img - k + 1, last_img, allImageSize)
        return (ret_code, arr.astype(np.uint16), validfirst, validlast)

    def get_first_n_images16(self, k=1):
        """ Get k last images"""
        _, n_images, first_img, _ = self.get_num_new_images()
        allImageSize = self.sgl_image_size * k
        (ret_code, arr, validfirst, validlast) = self.sdk.GetImages16(first_img, first_img + k - 1, allImageSize)
        return (ret_code, arr.astype(np.uint16), validfirst, validlast)


# default_fvb = {'cooler': True,
#                 'exposure_time': 0.0035,
#                 'temperature': -70,
#                 'amplifier': 'Conventional',
#                 'ad_channel': 1,
#                 'hs_speed_idx' : 0,
#                 'vs_speed_idx' : 0,
#                 'vs_shift_amp' : 0,
#                 'preamp_gain_idx' : 2,
#                 'readout_mode': 'FULL_VERTICAL_BINNING',
#                 'trigger_mode': 'INTERNAL',
#                 'shutter_mode': 'PERMANENTLY_OPEN',
#                 'acquisition_mode': 'RUN_TILL_ABORT'}

class DialogAndorConfig(QDialog):
    def __init__(self, ccd):
        # Boilerplate stuff
        super().__init__()
        self.ui = Ui_AndorConfig()
        self.ui.setupUi(self)
        self.ccd = ccd

        if self.ccd is not None:
            self.populate_ui()
            self.ui_from_dict(self.ccd.settings)
            self.ui.comboBoxAmpType.currentIndexChanged.connect(self.change_amp_type)

    def change_amp_type(self):
        """ Amplifier changed: EM or Conventional """
        raise NotImplementedError

    def populate_ui(self):
        # Actual Exposure time
        _, temp, _, _ = self.ccd.sdk.GetAcquisitionTimings()
        self.ui.spinBox_Exposure.setValue(temp)
        del temp

        for k in atmcd_codes.Acquisition_Mode:
            self.ui.comboBoxAcquisitionMode.addItem(k.name)

        for k in atmcd_codes.Trigger_Mode:
            self.ui.comboBoxTriggerMode.addItem(k.name)

        for k in atmcd_codes.Read_Mode:
            self.ui.comboBoxReadoutMode.addItem(k.name)

        for num_speeds in range(self.ccd.sdk.GetNumberVSSpeeds()[1]):
            self.ui.comboBoxVS.addItem('{}'.format(self.ccd.sdk.GetVSSpeed(num_speeds)[1]))

        for num_voltages in range(self.ccd.sdk.GetNumberVSAmplitudes()[1]):
            self.ui.comboBoxVoltage.addItem('{}'.format(num_voltages))
        self.ui.comboBoxVoltage.setCurrentIndex(0)

        # HS Speed
        num_amp_type = self.ui.comboBoxAmpType.currentIndex()
        temp = []
        for num_ad in range(self.ccd.sdk.GetNumberADChannels()[1]):
            for num_speeds in range(self.ccd.sdk.GetNumberHSSpeeds(num_ad, num_amp_type)[1]):
                temp.append(float(self.ccd.sdk.GetHSSpeed(num_ad, num_amp_type, num_speeds)[1]))
        temp = np.sort(temp)
        for t in temp:
            self.ui.comboBoxHSRate.addItem('{}'.format(t))
        self.ui.comboBoxHSRate.setCurrentIndex(self.ui.comboBoxHSRate.count() - 1)
        del temp

        # Preamp Gain
        temp = self.ccd.sdk.GetNumberPreAmpGains()[1]
        for num in range(temp):
            self.ui.comboBoxPreAmpGain.addItem('{}'.format(self.ccd.sdk.GetPreAmpGain(num)[1]))
        self.ui.comboBoxPreAmpGain.setCurrentIndex(self.ui.comboBoxPreAmpGain.count() - 1)
        del temp

    def accept(self):
        if self.ccd is not None:
            self.ccd.settings.update(self.dict_from_ui)
            self.ccd.init_camera()

        super().accept()

    def reject(self):
        super().reject()

    @property
    def dict_from_ui(self):
        output_dict = {}
        output_dict['acquisition_mode'] = self.ui.comboBoxAcquisitionMode.currentText()
        output_dict['acquisition_mode_idx'] = self.ui.comboBoxAcquisitionMode.currentIndex()
        output_dict['trigger_mode'] = self.ui.comboBoxTriggerMode.currentText()
        output_dict['trigger_mode_idx'] = self.ui.comboBoxTriggerMode.currentIndex()
        output_dict['readout_mode'] = self.ui.comboBoxReadoutMode.currentText()
        output_dict['readout_mode_idx'] = self.ui.comboBoxReadoutMode.currentIndex()
        output_dict['exposure_time'] = self.ui.spinBox_Exposure.value()
        output_dict['vs_speed'] = self.ui.comboBoxVS.currentText()
        output_dict['vs_speed_idx'] = self.ui.comboBoxVS.currentIndex()
        output_dict['vs_shift_amp'] = int(self.ui.comboBoxVoltage.currentText())
        output_dict['vs_shift_amp_idx'] = self.ui.comboBoxVoltage.currentIndex()
        output_dict['preamp_gain'] = self.ui.comboBoxPreAmpGain.currentText()
        output_dict['preamp_gain_idx'] = self.ui.comboBoxPreAmpGain.currentIndex()
        output_dict['baseline_clamping'] = self.ui.checkBoxBaselineClamping.isChecked()
        output_dict['hs_speed_idx'] = self.ui.comboBoxHSRate.currentIndex()
        output_dict['hs_speed'] = float(self.ui.comboBoxHSRate.currentText())
        output_dict['amplifier'] = self.ui.comboBoxAmpType.currentText()
        output_dict['amplifier_idx'] = self.ui.comboBoxAmpType.currentIndex()
        output_dict['cooler'] = True  # TODO: Cooler into settings ui
        output_dict['temperature'] = -70  # TODO Temperature into settings ui

        return output_dict

    def ui_from_dict(self, settings_dict):
        """ Use a dictionary of settings to set the ui state"""
        self.ui.spinBox_Exposure.setValue(settings_dict['exposure_time'])

        self.ui.comboBoxAmpType.setCurrentIndex(settings_dict['amplifier_idx'])
        self.ui.comboBoxHSRate.setCurrentIndex(self.ui.comboBoxHSRate.findText('{}'.format(settings_dict['hs_speed'])))
        self.ui.comboBoxVS.setCurrentIndex(settings_dict['vs_speed_idx'])
        self.ui.comboBoxVoltage.setCurrentIndex(self.ui.comboBoxVoltage.findText('{}'.format(settings_dict['vs_shift_amp'])))
        self.ui.comboBoxPreAmpGain.setCurrentIndex(settings_dict['preamp_gain_idx'])
        self.ui.checkBoxBaselineClamping.setChecked(settings_dict['baseline_clamping'])
        readout_mode_idx = self.ui.comboBoxReadoutMode.findText(settings_dict['readout_mode'])
        self.ui.comboBoxReadoutMode.setCurrentIndex(readout_mode_idx)

        trigger_mode_idx = self.ui.comboBoxTriggerMode.findText(settings_dict['trigger_mode'])
        self.ui.comboBoxTriggerMode.setCurrentIndex(trigger_mode_idx)

        acq_mode_idx = self.ui.comboBoxAcquisitionMode.findText(settings_dict['acquisition_mode'])
        self.ui.comboBoxAcquisitionMode.setCurrentIndex(acq_mode_idx)


if __name__ == '__main__':

    just_ui = False

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(stylesheet)

    if just_ui:
        window = DialogAndorConfig(ccd=None)
        ret = window.exec_()
        print(ret)
        # out = app.exec_()
    else:
        ccd = AndorNewton970()

        try:
            ret = ccd.init_all()
            window = DialogAndorConfig(ccd=ccd)
            ret = window.exec_()
            print('==============Pulling Current Settings=============')
            print(ccd.settings)
            print('===================================================')
            # out = app.exec_()  # Don't need with a modal dialog
        except Exception:
            print(traceback.format_exc())
        finally:
            ccd.free_memory()
            ret_code = ccd.shutdown()
            print("Function Shutdown returned {}: {}".format(ret_code, err_codes(ret_code).name))

    # ccd = AndorNewton970(settings_kwargs={'exposure_time':0.0035, 'readout_mode': 'FULL_VERTICAL_BINNING',
    #                                       'trigger_mode': 'EXTERNAL'})
    # try:
    #     ret = ccd.init_all()

    #     print('==========================')
    #     ccd.sdk.EnableKeepCleans(0)
    #     ccd.sdk.SetKineticCycleTime(0)
    #     ccd.sdk.SetFastExtTrigger(1)
    #     read_out_time = ccd.sdk.GetReadOutTime()[1]
    #     print('ReadOut Time: {:.6f} sec'.format(read_out_time))
    #     print('Exposure Time: {} sec'.format(ccd.sdk.GetAcquisitionTimings()[1]))
    #     print('Accumulate Time: {} sec'.format(ccd.sdk.GetAcquisitionTimings()[2]))
    #     print('Kinetic Time: {} sec'.format(ccd.sdk.GetAcquisitionTimings()[3]))
    #     print('Estimated total time per acquisition: {}'.format(ccd.net_acquisition_time))
    #     print('==========================')
    #     # ccd.sdk.

    #     # ccd.sdk.EnableKeepCleans(1)
    #     # ccd.init_sdk()
    #     # ccd.init_camera()
    # except Exception:
    #     print('ERROR: {}'.format(traceback.format_exc()))
    #     ret_code = ccd.shutdown()
    #     print("Function Shutdown returned {}: {}".format(ret_code, err_codes(ret_code).name))
    # else:
    #     print('Meta data:\n{}'.format(ccd.meta))
    #     ret_code = ccd.start_acquisition()
    #     print('Starting Acquisition: {} -- {}'.format(ret_code, andor_err_code_str(ret_code)))
    #     # ccd.sdk.WaitForAcquisition()
    #     sleep(1)
    #     ccd.stop_acquisition()
    #     ret_code, n_images, first_img, last_img = ccd.get_num_new_images()
    #     if (first_img != 0) & (last_img != 0):
    #         print('New Images: {} [{}:{}]'.format(n_images, first_img, last_img))
#
#
    #         (ret_code, arr, validfirst, validlast) = ccd.get_all_images16()
    #         # arr = arr.reshape((n_images, sgl_image_size))
    #         # del arr
    #         print('Single_image size: {}'.format(ccd.sgl_image_size))
    #         allImageSize = n_images * ccd.sgl_image_size
    #         print("Function GetImages16 returned {}; array shape = {}; array type: {}; size = {}".format(andor_err_code_str(ret_code), arr.shape, arr.dtype, allImageSize))
    #         print('arr[0]: {}'.format(arr[0]))

    # finally:
    #     ccd.free_memory()
    #     ret_code = ccd.shutdown()
    #     print("Function Shutdown returned {}: {}".format(ret_code, err_codes(ret_code).name))
    #     # print(ccd.__dict__)
