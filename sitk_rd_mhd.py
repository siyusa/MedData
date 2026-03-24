import SimpleITK as sitk
img = sitk.ReadImage("data\patient098_4CH_sequence.mhd")
data = sitk.GetArrayFromImage(img)
print(data.shape)

