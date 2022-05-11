import traceback
from time import sleep
from hypothesis import settings

import numpy as np

from pyAndorSDK2 import atmcd, atmcd_codes, atmcd_errors

err_codes = atmcd_errors.Error_Codes


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
                   'ad_channel': 1,
                   'hs_speed_idx' : 0,
                   'vs_speed_idx' : 0,
                   'vs_shift_amp' : 0,
                   'preamp_gain_idx' : 2,
                   'read_mode': 'FULL_VERTICAL_BINNING',
                   'trigger_mode': 'INTERNAL',
                   'shutter_mode': 'PERMANENTLY_OPEN',
                   'acquisition_mode': 'RUN_TILL_ABORT'}

    default_imaging = default_fvb.copy()
    default_imaging.update({'read_mode': 'IMAGE'})

    default_imaging_trigd = default_imaging.copy()
    default_imaging_trigd.update({'trigger_mode':'EXTERNAL'})
    
    default_fvb_trigd = default_fvb.copy()
    default_fvb_trigd.update({'trigger_mode':'EXTERNAL'})

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
        self.mode_codes['acquisition'] = {k.name:k.value for k in atmcd_codes.Acquisition_Mode}
        self.mode_codes['read'] = {k.name:k.value for k in atmcd_codes.Read_Mode}
        self.mode_codes['shutter'] = {k.name:k.value for k in atmcd_codes.Shutter_Mode}
        self.mode_codes['trigger_mode'] = {k.name:k.value for k in atmcd_codes.Trigger_Mode}

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
        output.update({'{}.{}'.format(prefix,k): self.settings[k] for k in self.settings if not isinstance(self.settings[k], dict)})
        
        # output.update({'{}.{}'.format(prefix,kk): self.settings[k][kk] for kk in self.settings[k] for k in self.settings if isinstance(self.settings[k], dict)})

        # Manually set things:
        output['CCD.cooler'] = self.settings['cooler']
        output['CCD.fanmode'] = 'full'

        output['CCD.temperature.actual'] = round(self.sdk.GetTemperatureStatus()[1],2)
        output['CCD.temperature.set'] = round(self.sdk.GetTemperatureStatus()[2],2)
        output['CCD.amplifier_idx'] = [self.sdk.GetAmpDesc(num,25)[1] for num in range(self.sdk.GetNumberAmp()[1])].index(self.settings['amplifier'])
        output['CCD.HS_shift_frequency'] = '{} MHz'.format(self.sdk.GetHSSpeed(self.settings['ad_channel'],
                                                           output['CCD.amplifier_idx'],
                                                           self.settings['hs_speed_idx'])[1])
        output['CCD.VS_shift_time'] = '{} us'.format(self.sdk.GetVSSpeed(self.settings['vs_speed_idx'])[1])
        output['CCD.preamp_gain'] = self.sdk.GetPreAmpGain(self.settings['preamp_gain_idx'])[1]
        for k in self.mode_codes:
            for kk in self.mode_codes[k]:
                output['CCD.modecode.{}.{}'.format(k,kk)] = self.mode_codes[k][kk]
        return output

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
        print('')
        ret_code = self.sdk.SetAcquisitionMode(self.mode_codes['acquisition'][self.settings['acquisition_mode']])
        ret_code_list.append(ret_code)
        print('Set Acquisition Mode: {} -- {}: {}'.format(self.settings['acquisition_mode'], ret_code, andor_err_code_str(ret_code)))

        n_ads = self.sdk.GetNumberADChannels()[1]  # Number of A/D's
        n_amps = self.sdk.GetNumberAmp()[1]  # Number of amplifiers
        print('Camera Capabilities:')
        for num_ad in range(n_ads):
            for num_amp in range(n_amps):
                for num_speeds in range(self.sdk.GetNumberHSSpeeds(num_ad, num_amp)[1]):
                    name_amp = self.sdk.GetAmpDesc(num_amp,21)[1]
                    print('Amp: {} ({}); AD: {}; Speed: {} MHz ({})'.format(name_amp, num_amp, num_ad, self.sdk.GetHSSpeed(num_ad, num_amp, num_speeds)[1], num_speeds))
        print('')
        # Set output amplifier (0 EM or 1 Conventional)
        ret_code = self.sdk.SetOutputAmplifier(self.settings['amplifier_idx'])
        ret_code_list.append(ret_code)
        print('Set Amplifier: {} -- {}: {}'.format(self.settings['amplifier_idx'], ret_code, andor_err_code_str(ret_code)))

        # print(get_amplifier_list())
        # Set AD Chan = 0
        ret_code = self.sdk.SetADChannel(self.settings['ad_channel'])
        ret_code_list.append(ret_code)
        print('Set AD Channel: {} -- {}: {}'.format(self.settings['ad_channel'], ret_code, andor_err_code_str(ret_code)))

        # Set horizontal shift speed (MHz)
        ret_code = self.sdk.SetHorizontalSpeed(self.settings['hs_speed_idx'])
        ret_code_list.append(ret_code)
        print('Set Horizontal Shift Speed: {} -- {}: {}'.format(self.settings['hs_speed_idx'], ret_code, andor_err_code_str(ret_code)))

        # Set preamp gain
        print('Number of Gains: {}'.format(self.sdk.GetNumberPreAmpGains()[1]))
        for num_gain in range(self.sdk.GetNumberPreAmpGains()[1]):
            print('Index: {}; Gain: {}x'.format(num_gain, self.sdk.GetPreAmpGain(num_gain)[1]))
        ret_code = self.sdk.SetPreAmpGain(self.settings['preamp_gain_idx'])
        ret_code_list.append(ret_code)
        print('Set Pre-Amp Gain: {} -- {}: {}'.format(self.settings['preamp_gain_idx'], ret_code, andor_err_code_str(ret_code)))

        # Set VS shift speed ??
        print(self.sdk.GetNumberVSSpeeds()[1])
        for num_speeds in range(self.sdk.GetNumberVSSpeeds()[1]):
            print('Index: {}; Vertical Shift Speed: {}us'.format(num_speeds, self.sdk.GetVSSpeed(num_speeds)[1]))
        
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
        ret_code =  self.sdk.SetExposureTime(self.settings['exposure_time'])
        ret_code_list.append(ret_code)
        print('Set Exposure Time: {} -- {}: {}'.format(self.settings['exposure_time'], ret_code, andor_err_code_str(ret_code)))

        # Set frame transfer mode = Off (0)
        ret_code =  self.sdk.SetFrameTransferMode(0)
        ret_code_list.append(ret_code)
        print('Frame Transfer Mode: OFF -- {}: {}'.format(ret_code, andor_err_code_str(ret_code)))

        # Set shutter
        ret_code =  self.sdk.SetShutter(0, self.mode_codes['shutter'][self.settings['shutter_mode']],0,0)
        ret_code_list.append(ret_code)
        print('Shutter Mode: {} -- {}: {}'.format(self.mode_codes['shutter'][self.settings['shutter_mode']], ret_code, andor_err_code_str(ret_code)))

        # Set image flip
        ret_code =  self.sdk.SetImageFlip(0,0)
        ret_code_list.append(ret_code)
        print('Set Image Flip: OFF, OFF -- {}: {}'.format(ret_code, andor_err_code_str(ret_code)))

        # Set single-track or not
        # ret_code =  self.sdk.SetSingleTrack()
        
        # Set read mode
        # 0 Full Vertical Binning; 1: Multi-Track; 2: Random-Track; 3: Single-Track; 4: Image
        ret_code = self.sdk.SetReadMode(self.mode_codes['read'][self.settings['read_mode']])
        ret_code_list.append(ret_code)
        print('Read Mode: {} -- {}: {}'.format(self.mode_codes['read'][self.settings['read_mode']], ret_code, andor_err_code_str(ret_code)))
        if self.settings['read_mode'] == 'FULL_VERTICAL_BINNING':
            self.is_fvb_or_sgl_track = True
        else:
            self.is_fvb_or_sgl_track = False

        
        ret_code, self.n_cols, self.n_rows = self.sdk.GetDetector()
        ret_code_list.append(ret_code)
        print('Detector Size: ({}, {})'.format(self.n_rows, self.n_cols))
        # Oddly, SetImage was needed. Maybe there's a default binning
        if self.is_fvb_or_sgl_track:
            ret_code =  self.sdk.SetImage(1, 1, 1, self.n_rows, 1, 1)
        else:
            ret_code =  self.sdk.SetImage(1, 1, 1, 1600, 1, 200)
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
        except Exception as e:
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
        except Exception as e:
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
            n_images = last_img-first_img
        else:
            n_images = last_img-first_img + 1

        # print('New Images: {}:{}'.format(first_img, last_img))

        return ret_code, n_images, first_img, last_img

    @property
    def sgl_image_size(self):
        if self.is_fvb_or_sgl_track == True:
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
        (ret_code, arr, validfirst, validlast) = self.sdk.GetImages16(last_img-k+1, last_img, allImageSize)
        return (ret_code, arr.astype(np.uint16), validfirst, validlast)

    def get_first_n_images16(self, k=1):
        """ Get k last images"""
        _, n_images, first_img, _ = self.get_num_new_images()
        allImageSize = self.sgl_image_size * k
        (ret_code, arr, validfirst, validlast) = self.sdk.GetImages16(first_img, first_img+k-1, allImageSize)
        return (ret_code, arr.astype(np.uint16), validfirst, validlast)

if __name__ == '__main__':
    ccd = AndorNewton970(settings_kwargs={'exposure_time':0.0035, 'read_mode': 'FULL_VERTICAL_BINNING',
                                          'trigger_mode': 'EXTERNAL'})
    try:
        ret = ccd.init_all()

        print('==========================')
        ccd.sdk.EnableKeepCleans(0)
        ccd.sdk.SetKineticCycleTime(0)
        ccd.sdk.SetFastExtTrigger(1)
        read_out_time = ccd.sdk.GetReadOutTime()[1]
        print('ReadOut Time: {:.6f} sec'.format(read_out_time))
        print('Exposure Time: {} sec'.format(ccd.sdk.GetAcquisitionTimings()[1]))
        print('Accumulate Time: {} sec'.format(ccd.sdk.GetAcquisitionTimings()[2]))
        print('Kinetic Time: {} sec'.format(ccd.sdk.GetAcquisitionTimings()[3]))
        print('Estimated total time per acquisition: {}'.format(ccd.net_acquisition_time))
        print('==========================')
        # ccd.sdk.

        # ccd.sdk.EnableKeepCleans(1)
        # ccd.init_sdk()
        # ccd.init_camera()
    except Exception as e:
        print('ERROR: {}'.format(traceback.format_exc()))
        ret_code = ccd.shutdown()
        print("Function Shutdown returned {}: {}".format(ret_code, err_codes(ret_code).name))
    else:
        print('Meta data:\n{}'.format(ccd.meta))
        ret_code = ccd.start_acquisition()
        print('Starting Acquisition: {} -- {}'.format(ret_code, andor_err_code_str(ret_code)))
        # ccd.sdk.WaitForAcquisition()
        sleep(1)
        ccd.stop_acquisition()
        
        
        ret_code, n_images, first_img, last_img = ccd.get_num_new_images()
        if (first_img != 0) & (last_img != 0):
            print('New Images: {} [{}:{}]'.format(n_images, first_img, last_img))


            (ret_code, arr, validfirst, validlast) = ccd.get_all_images16()
            # arr = arr.reshape((n_images, sgl_image_size))
            # del arr
            print('Single_image size: {}'.format(ccd.sgl_image_size))
            allImageSize = n_images * ccd.sgl_image_size
            print("Function GetImages16 returned {}; array shape = {}; array type: {}; size = {}".format(andor_err_code_str(ret_code), arr.shape, arr.dtype, allImageSize))
            print('arr[0]: {}'.format(arr[0]))
        
    finally:
        ccd.free_memory()
        ret_code = ccd.shutdown()
        print("Function Shutdown returned {}: {}".format(ret_code, err_codes(ret_code).name))
        # print(ccd.__dict__)
