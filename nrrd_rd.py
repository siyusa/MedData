import nrrd
filename = 'data/BallBinary30x30x30.nrrd'
data,header = nrrd.read(filename)
print(data.shape)
print(header)


