import SimpleITK as sitk
img = sitk.ReadImage("data\patient098_4CH_sequence.mhd")
sitk.WriteImage(img,'data/patient098_4CH_sequence.nii.gz')
