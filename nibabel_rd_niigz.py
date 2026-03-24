import nibabel as nib
filename = 'data/patient45_ED.nii.gz'
img = nib.load(filename)
#header= img.header
#print(header)
data = img.get_fdata()
print(data.shape)






