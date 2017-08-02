import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit
import numpy
import time

r = [2, 5000]
for n in r:
    a=numpy.float32(numpy.random.randn(n,n))
    b=numpy.float32(numpy.random.randn(n,n))

    a_gpu = gpuarray.to_gpu(a)
    b_gpu = gpuarray.to_gpu(b)

    tic=time.time()
    axbGPU = gpuarray.dot(a_gpu, b_gpu)
    toc = time.time() - tic
    print(toc)

