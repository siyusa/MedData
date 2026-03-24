import SimpleITK as sitk
filename = 'data/patient45_ED.nii.gz'
img = sitk.ReadImage(filename)
for key in img.GetMetaDataKeys():
    print(key,img.GetMetaData(key))

#读取图像矩阵
#data = sitk.GetArrayFromImage(img)
#获取体素大小
#spacing = img.GetSpacing()
# 获取坐标图像原点
#origin = img.GetOrigin()
# 获取图像方位
#direction = img.GetDirection()

#print(spacing, origin, direction)




