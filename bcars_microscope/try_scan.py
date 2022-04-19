import traceback
from time import sleep
from timeit import default_timer as timer
from numpy import ceil

from andor_ccd import AndorNewton970, andor_err_code_str
from pyAndorSDK2 import atmcd_errors, atmcd_codes
err_codes = atmcd_errors.Error_Codes

from pipython import GCS2Commands, GCSDevice, pitools
import traceback
from time import sleep


def do_scan(pixel_time=None, set_wavegen=False):
    pidevice = GCSDevice('E-545')
    try:
        pidevice.ConnectUSB('PI E-517 Display and Interface SN 0114071272')
        print(pidevice.qIDN())
        # print(pidevice.qPOS())
        # pidevice.MOV({'X':90})
        # print(pidevice.qPOS())
        # pidevice.WAV_LIN(1,1,50,'X',0, 198, 1, 50)
        # print(pidevice.qPOS())
        
        fast_axis_start_stop_steps = [1,199,300]
        pidevice.MOV({'X':1})
        pidevice.gcscommands.WAV_LIN(table=1, firstpoint=0, numpoints=fast_axis_start_stop_steps[2], append='X', speedupdown=0, 
                                     amplitude=fast_axis_start_stop_steps[1]-fast_axis_start_stop_steps[0], 
                                     offset=fast_axis_start_stop_steps[0], seglength=fast_axis_start_stop_steps[2])
        if pixel_time:
            print('Per pixel acquisition time: {}'.format(pixel_time))
            wavegen_rate = int(ceil(pixel_time/40e-6))
            print('Approximate wavegen rate: {}'.format(wavegen_rate))
            if set_wavegen:
                pidevice.gcscommands.WTR(1, wavegen_rate, 0)
        print('Rate: {}'.format(pidevice.gcscommands.qWTR(1)))
        
        # Default CTO: CTO 1 1 0.1 2 1 3 4 4 0 5 0.0 6 1.0 7 1 12 1 
        # 12 is a mystery
        print('CTO (X-axis): {}'.format(pidevice.gcscommands.qCTO()[1]))
        # WAV 1 X LIN 100 198 1 100 0 0

        # Bit pattern 4 3 2 1 0
        # So we want bit-0 and bit-3 to be high
        # Therefore 8 + 1 = 9
        # Used 11 in the past, but I don't think bit-2 is appropriate
        pidevice.gcscommands.WGO(1,mode=9)
        # temp = pidevice.gcscommands.IsMoving()
        # print('Is moving: {}'.format(any([temp[t] for t in temp])))
        # if pixel_time:
        #     # print('Sleep: {}'.format(fast_axis_start_stop_steps[-1]*pixel_time))
        #     sleep(fast_axis_start_stop_steps[-1]*pixel_time)
        # else:
        #     sleep(2)

        # Best I can do is < 100 ms difference with theoretical wait time using
        # delay of 90% of theory delay and polling every 10 ms
        tmr = timer()
        pitools.waitontarget(pidevice, timeout=10, predelay=fast_axis_start_stop_steps[-1]*pixel_time*0.9, polldelay=0.01)
        tmr -= timer()
        temp = pidevice.gcscommands.IsMoving()
        print('Is moving: {}'.format(any([temp[t] for t in temp])))
        print('Waited {} sec'.format(-tmr))
        print('Calculated Wait Time: {}'.format(fast_axis_start_stop_steps[-1]*pixel_time))
        print(pidevice.gcscommands.qWTR())

        # Servo update time (should be 40 us for E-545)
        # Hex: 0E000200 Dec: 234881536
        pidevice.gcscommands.WTR(2, 100, 0)
        print('Servo update times (All Axes): {} sec'.format(pidevice.gcscommands.qSPA(1, params=234881536)[1][234881536]))
        print('Wavegen servo time multiplier (X): {}'.format(pidevice.gcscommands.qWTR(1)[1][0]))
        print('Wavegen servo time multiplier (Y): {}'.format(pidevice.gcscommands.qWTR(2)[2][0]))
        print('Wavegen servo time multiplier (Z): {}'.format(pidevice.gcscommands.qWTR(3)[3][0]))
        print(pidevice.gcscommands.qWTR(1))
        print(pidevice.gcscommands.qWTR(2))
        print(pidevice.gcscommands.qWTR())
        pidevice.MOV({'X':1})
        # print(pidevice.qPOS())
    except Exception as e:
        print(traceback.format_exc())
        pidevice.CloseConnection()
    else:
        pidevice.CloseConnection()
        

if __name__ == '__main__':
    # print(AndorNewton970.default_imaging)
    ccd = AndorNewton970(settings_kwargs=AndorNewton970.default_fvb_trigd)
    try:
        ccd.settings.update({'exposure_time':0.0035})
        ccd.sdk.SetFastExtTrigger(1)
        ccd.initialize_default()
        ccd.sdk.SetFastExtTrigger(1)
        # ccd.sdk.SetTriggerMode(1)
        # print(atmcd_codes.Trigger_Mode.EXTERNAL.value)
        ccd.sdk.PrepareAcquisition()
    except Exception as e:
        print('ERROR: {}'.format(traceback.format_exc()))
        ret_code = ccd.sdk.ShutDown()
        print("Function Shutdown returned {}: {}".format(ret_code, err_codes(ret_code).name))
    else:
        ret_code = ccd.sdk.StartAcquisition()
        print('Starting Acquisition: {} -- {}'.format(ret_code, andor_err_code_str(ret_code)))
        do_scan(pixel_time=ccd.net_acquisition_time, set_wavegen=True)
        # ccd.sdk.WaitForAcquisition()
        sleep(1)
        ccd.sdk.AbortAcquisition()
        
        
        ret_code, first_img, last_img = ccd.sdk.GetNumberNewImages()
        print('New Images: {}:{}'.format(first_img, last_img))

        ret_code, first_img, last_img = ccd.sdk.GetNumberAvailableImages()
        print('New Images: {}:{}'.format(first_img, last_img))

        if ccd.is_fvb_or_sgl_track == True:
            sgl_image_size = ccd.n_cols
        else:
            sgl_image_size = ccd.n_rows * ccd.n_cols
        
        n_images = last_img-first_img + 1
        allImageSize = sgl_image_size * n_images

        (ret_code, arr, validfirst, validlast) = ccd.sdk.GetImages16(first_img, last_img, allImageSize)
        # arr = arr.reshape((n_images, sgl_image_size))
        # del arr
        print('Single_image size: {}'.format(sgl_image_size))
        print("Function GetImages16 returned {}; array shape = {}; array type: {}; size = {}".format(andor_err_code_str(ret_code), arr.shape, arr.dtype, allImageSize))
        print('arr[0]: {}'.format(arr[0]))
        ccd.sdk.FreeInternalMemory()
        ret_code, first_img, last_img = ccd.sdk.GetNumberAvailableImages()
        print('Post-Abort N New Images: {} -- {}: {}'.format(last_img - first_img + 1, ret_code, andor_err_code_str(ret_code)))
        ret_code = ccd.sdk.ShutDown()
        print("Function Shutdown returned {}: {}".format(ret_code, err_codes(ret_code).name))
        # print(ccd.__dict__)

