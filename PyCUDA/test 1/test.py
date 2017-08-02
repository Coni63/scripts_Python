import pycuda.autoinit
import pycuda.driver as drv
import pycuda.gpuarray as gpuarray
from pycuda.compiler import SourceModule
from pycuda import driver, compiler, tools

import numpy
import time

def timeit(func):
    def timed(*args, **kw):
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()
        print('%r \n %r \n %r \n %2.6f sec \n' % \
              (func.__name__, args, kw, te-ts))
        return result
    return timed

@timeit
def GPU_mult(a, b):
    multiply_them(
            drv.Out(dest), drv.In(a), drv.In(b),
            block=(400,1,1), grid=(1,1))

@timeit
def CPU_mult(a, b):
    a * b

@timeit
def GPU_mult2(a, b):
    MatrixMulKernel(
            drv.Out(dest), drv.In(a), drv.In(b),
            block=(400,1,1), grid=(1,1))

@timeit
def CPU_mult2(a, b):
    numpy.dot(a, b)

mod = SourceModule("""
        __global__ void MatrixMulKernel(float *a, float *b, float *c)
        {
            int tx = threadIdx.x;
            int ty = threadIdx.y;

            float Pvalue = 0;

            for (int k = 0; k < %(MATRIX_SIZE)s; ++k) {
                float Aelement = a[ty * %(MATRIX_SIZE)s + k];
                float Belement = b[k * %(MATRIX_SIZE)s + tx];
                Pvalue += Aelement * Belement;
            }

            c[ty * %(MATRIX_SIZE)s + tx] = Pvalue;
        }

        __global__ void multiply_them(float * dest, float * a, float * b)
        {
            const int i = threadIdx.x;
            dest[i] = a[i] * b[i];
        }
""")

multiply_them = mod.get_function("multiply_them")
#MatrixMulKernel = mod.get_function("MatrixMulKernel")

a = numpy.random.randn(4000).astype(numpy.float32)
b = numpy.random.randn(4000).astype(numpy.float32)

dest = numpy.zeros_like(a)
dest2 = numpy.zeros_like(a)

a_gpu = gpuarray.to_gpu(a)
b_gpu = gpuarray.to_gpu(b)
c_gpu = gpuarray.to_gpu(dest)

GPU_mult(a_gpu, b_gpu)
CPU_mult(a, b)

# GPU_mult2(a_gpu, b_gpu, c_gpu)
# CPU_mult2(a, b)
