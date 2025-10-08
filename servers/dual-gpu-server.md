---
title: "Dual GPU Server"
---

In addition to our primary GPU, the SCF operates a Tesla K80 dual GPU
that has two GPUs, each with 12 Gb memory and 2496 CUDA cores. This
hardware was bought by Prof. Bin Yu and should only be used with
permission of Prof. Yu or SCF staff.

## Submitting GPU jobs

The hardware is hosted on the scf-sm21 node of our high-priority
cluster. To use one of the GPUs, one [submits to the cluster](/servers/cluster)
but using `-w scf-sm21` as the flag to point the job to
the dual GPU on scf-sm21.

One can submit a job that uses one of the two GPUs by using the flag
`--gres=gpu:1`. In this mode of operation, two separate jobs (which
could be submitted by one user or two users) can use the two GPUs, and
the queueing software will assign the jobs to separate GPUs.

## Using both GPUs for one job

It's also possible to run a job that uses both GPUs at once. The
remainder of this document describes how to do this using CUDA, Python,
and Matlab.

First, when submitting the job, include the flag `--gres=gpu:2` to
request both GPUs.

### CUDA

In CUDA in the host code, simply call `cudaSetDevice(0)` or
`cudaSetDevice(1)` and then do any data transfer or kernel
computations that you'd like. Operations on the GPUs will continue in
the background even if the host code is operating on the other GPU.

### Python

When using PyCUDA, one can transfer data and run kernels on each GPU,
switching back and forth as needed. Operations on the GPUs will continue
in the background even if the host code is operating on the other GPU.
Here's some example code:

```{code} python
import pycuda.driver as drv
from pycuda.compiler import SourceModule
drv.init()
dev0 = drv.Device(0) # set up for GPU 0
ctx0 = dev0.make_context() 
dev1 = drv.Device(1) # set up for GPU 1
ctx1 = dev1.make_context() 

ctx0.push()
# do data transfer and kernel operations (on GPU 0)
ctx0.pop()
ctx1.push()
# do data transfer and kernel operations (on GPU 1)
ctx1.pop()
```

### Matlab

In Matlab, to have multiple GPUs in use at once, you need to use parfor
to run multiple processes, with each one controlling a GPU. Here's some
example code:

```{code} matlab
parfor i = 1:gpuDeviceCount
  g = gpuDevice(i);
  % now do GPU-based operations
end
```

If you instead try to switch between GPUs using "gpuDevice()" on the
master process, operations and memory use will terminate on the GPU that
you switch away from.

### Machine learning packages

We haven't fully investigated this, but a quick online search suggests
the following.

1.  Caffe: When invoking caffe from the command line, one can specify
    `-gpu 0,1` to use both GPUs.
1.  Torch: You can switch between GPUs with `cutorch.setDevice()`. More details are
    available [here](https://github.com/torch/cutorch/issues/42).
1.  Tensorflow: Details can be found
    [here](https://www.tensorflow.org/versions/r0.7/how_tos/using_gpu/index.html).
