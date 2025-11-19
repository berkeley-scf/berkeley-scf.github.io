---
title: "GPU Software"
---

We provide the following software that will help you in making use of
the GPU:

- CUDA (versions 12.8 and 12.9; other versions can be made available)
- cuDNN (cuDNN 9.8.0 for CUDA 12.8; other versions can be made
  available)
- PyTorch (version 2.6.0 for Python 3.13 and version 2.2.1 for Python
  3.12)
- Jax (version 0.5.2 for Python 3.13 and 0.4.25 for Python 3.12)
- Tensorflow is not currently available for Python 3.13, but version
  2.16.1 is available for Python 3.12. Note that Tensorflow may not work
  on some of our old machines, but it should work on the cluster nodes
  as well as on gandalf and radagast among others.
- We can install additional or upgrade current software as needed. 

We use Linux [environment modules](./environment-modules.md) to
manage the use of some GPU-based software, as seen below. 

To use Python packages that use the GPU for back-end computations,
simply import the package in Python.

To program with CUDA and related packages directly, you'll need
to load CUDA as follows in order to be able to compile and run your
code:

- CUDA: to use CUDA directly in C or another language, invoke "module
  load cuda".
- cuDNN: cuDNN is available on the GPU servers without needing to load
  any modules.

If you have questions or would like additional GPU-related software installed,
please contact consult@stat.berkeley.edu.
