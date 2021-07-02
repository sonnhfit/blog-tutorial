import numpy as np
data = np.load('000101.npy')
data.astype("float32").tofile("binary.bin")
