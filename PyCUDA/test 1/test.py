import pycuda.autoinit
import pycuda.driver as drv
import pycuda.gpuarray as gpuarray

from pycuda.compiler import SourceModule

import numpy
from time import time

# from skcuda import linalg
# linalg.init()


mod = SourceModule("""
__global__ void multiply_them(float *dest, float *a, float *b)
{
  const int i = threadIdx.x;
  dest[i] = a[i] * b[i];
}
""")

multiply_them = mod.get_function("multiply_them")

a = numpy.random.randn(4000).astype(numpy.float32)
b = numpy.random.randn(4000).astype(numpy.float32)
a_gpu = gpuarray.to_gpu(a)
b_gpu = gpuarray.to_gpu(b)

start = time()

dest = numpy.zeros_like(a)

multiply_them(
        drv.Out(dest), drv.In(a), drv.In(b),
        block=(400,1,1), grid=(1,1))

print(time()-start)



start2 = time()

dest2 = numpy.zeros_like(a)

dest2 = a * b

print(time()-start2)

# start3 = time()

# vr_gpu, w_gpu = linalg.eig(a_gpu, 'N', 'V')

# print(vr_gpu, w_gpu)
# print(time()-start3)
