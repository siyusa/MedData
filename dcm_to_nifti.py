import SimpleITK as sitk
folder_name = 'data'
series_reader = sitk.ImageSeriesReader()
fileNames = series_reader.GetGDCMSeriesFileNames(folder_name)
series_reader.SetFileNames(fileNames)
images = series_reader.Execute()
sitk.WriteImage(images,'data/1.nii.gz')

