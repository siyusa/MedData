import pydicom
import numpy as np
dc_rd = pydicom.dcmread("data\IM-0001-0375.dcm")
data = np.array(dc_rd.pixel_array)
print(data.shape)



