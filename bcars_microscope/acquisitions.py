""" I envision this being where various acquisition types (e.g., RT spectra, raster, etc) will be placed """


import traceback
from time import sleep
from timeit import default_timer as timer

from andor_ccd import AndorNewton970, andor_err_code_str
from pyAndorSDK2 import atmcd_errors, atmcd_codes
err_codes = atmcd_errors.Error_Codes

from pipython import GCS2Commands, GCSDevice, pitools

# class RealTimeSpectra:
#     def __init__(self):


# ccd = AndorNewton970(settings_kwargs=AndorNewton970.default_fvb_trigd)
#     try:
#         ccd.settings.update({'exposure_time':0.0035})
#         ccd.sdk.SetFastExtTrigger(1)
#         ccd.initialize_default()
#         ccd.sdk.SetFastExtTrigger(1)
#         # ccd.sdk.SetTriggerMode(1)
#         # print(atmcd_codes.Trigger_Mode.EXTERNAL.value)
#         ccd.sdk.PrepareAcquisition()
#     except Exception as e:
#         print('ERROR: {}'.format(traceback.format_exc()))
#         ret_code = ccd.sdk.ShutDown()
#         print("Function Shutdown returned {}: {}".format(ret_code, err_codes(ret_code).name))
#     else:
#         ret_code = ccd.sdk.StartAcquisition()
#         print('Starting Acquisition: {} -- {}'.format(ret_code, andor_err_code_str(ret_code)))
#         do_scan(pixel_time=ccd.net_acquisition_time, set_wavegen=True)
#         # ccd.sdk.WaitForAcquisition()
#         sleep(1)
#         ccd.sdk.AbortAcquisition()
        
        
#         ret_code, first_img, last_img = ccd.sdk.GetNumberNewImages()
#         print('New Images: {}:{}'.format(first_img, last_img))

#         ret_code, first_img, last_img = ccd.sdk.GetNumberAvailableImages()
#         print('New Images: {}:{}'.format(first_img, last_img))

#         if ccd.is_fvb_or_sgl_track == True:
#             sgl_image_size = ccd.n_cols
#         else:
#             sgl_image_size = ccd.n_rows * ccd.n_cols
        
#         n_images = last_img-first_img + 1
#         allImageSize = sgl_image_size * n_images

#         (ret_code, arr, validfirst, validlast) = ccd.sdk.GetImages16(first_img, last_img, allImageSize)
#         # arr = arr.reshape((n_images, sgl_image_size))
#         # del arr
#         print('Single_image size: {}'.format(sgl_image_size))
#         print("Function GetImages16 returned {}; array shape = {}; array type: {}; size = {}".format(andor_err_code_str(ret_code), arr.shape, arr.dtype, allImageSize))
#         print('arr[0]: {}'.format(arr[0]))
#         ccd.sdk.FreeInternalMemory()
#         ret_code, first_img, last_img = ccd.sdk.GetNumberAvailableImages()
#         print('Post-Abort N New Images: {} -- {}: {}'.format(last_img - first_img + 1, ret_code, andor_err_code_str(ret_code)))
#         ret_code = ccd.sdk.ShutDown()
#         print("Function Shutdown returned {}: {}".format(ret_code, err_codes(ret_code).name))
#         # print(ccd.__dict__)


import datetime
import time
import threading


class TestThreading(object):
    def __init__(self, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            # More statements comes here
            print(datetime.datetime.now().__str__() + ' : Start task in the background')

            time.sleep(self.interval)

tr = TestThreading()
time.sleep(1)
print(datetime.datetime.now().__str__() + ' : First output')
time.sleep(2)
print(datetime.datetime.now().__str__() + ' : Second output')