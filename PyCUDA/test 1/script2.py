import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit
import numpy
import time
import matplotlib.pyplot as plt

r = list(range(2,10)) + list(range(20, 190, 10)) + list(range(200, 4200, 200))
t_cpu = []
t_gpu = []
t_gpu_tot = []

for n in r:
    a=numpy.float32(numpy.random.randn(n,n))
    b=numpy.float32(numpy.random.randn(n,n))

    tic=time.time()
    numpy.dot(a,b)
    toc=time.time()-tic
    t_cpu.append(toc)
    print(toc,"CPU")

    tic2 = time.time()
    a_gpu = gpuarray.to_gpu(a)
    b_gpu = gpuarray.to_gpu(b)
    tic=time.time()
    axbGPU = gpuarray.dot(a_gpu, b_gpu)
    toc=time.time()-tic
    toc2 = time.time() - tic
    t_gpu.append(toc)
    t_gpu_tot.append(toc2)
    print(toc,"GPU")

plt.plot(r, t_cpu, label="CPU time")
plt.plot(r, t_gpu, label="GPU time without data conversion")
plt.plot(r, t_gpu_tot, label="GPU time with data conversion")
plt.xlabel("Matrix Size")
plt.ylabel('Time (s)')
plt.title('Matrix Multiplication Time')
plt.text(0, max(t_cpu)*0.7,  r'GPU w/o prep : min = {:.2e} - max = {:.2e}'.format(min(t_gpu[1:]), max(t_gpu[1:])), fontsize=10)
plt.text(0, max(t_cpu)*0.65, r'GPU w prep : min = {:.2e} - max = {:.2e}'.format(min(t_gpu_tot[1:]), max(t_gpu_tot[1:])), fontsize=10)
plt.text(0, max(t_cpu)*0.6,  r'CPU : min = {:.2e} - max = {:.2e}'.format(min(t_cpu), max(t_cpu)), fontsize=10)
plt.text(0, max(t_cpu)*0.55,  r'GPU init : {:.2e}'.format(t_gpu_tot[0]), fontsize=10)
plt.legend()
plt.savefig('foo.png')
plt.show()