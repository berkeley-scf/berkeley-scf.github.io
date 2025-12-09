---
title: "Software for Macs (Apple Silicon)"
---

With the M-series Macs, Apple is now using its own chips, referred to
as *Apple silicon*. These have a different architecture, ARM64, than
standard x86-64 chips, such as those produced by Intel and AMD.

The chips are very fast (generally faster on a per-core basis than
the cores on our Linux servers) and also provide a matrix coprocessor
(AMX) for fast matrix operations and an integrated GPU that provide [Apple's Metal Performance Shaders (MPS) framework](https://developer.apple.com/documentation/metalperformanceshaders) for programming. Note that using MPS can speed up operations in some cases, but the number of GPU cores is much less than on NVIDIA and other GPUs.

To take full advantage of the M-series chips on your own machine, you'll want to use software
built for the chips, as discussed below. Non-ARM64 programs will work on the new Apple Silicon-based machines by automatically making use
of Apple's Rosetta2 system to translate machine code from ARM64 to
x86_64, but you can expect some decrease in performance. 




(m-series-anaconda)=
### Conda/Mamba for Mac ARM64-based machines 

We recommend installing Miniforge, which
[provides versions for ARM64](https://conda-forge.org/download/).  

You can also use [Anaconda/Miniconda with
ARM64 support](https://www.anaconda.com/blog/new-release-anaconda-distribution-now-supporting-m1),
installing with the  [64-Bit (Apple silicon) installer](https://www.anaconda.com/products/distribution#Downloads)

In addition you will probably want to [set up numpy to use Apple's Accelerate vecLib BLAS](../kb/linear-algebra-using-blas/#configuring-use-of-a-fast-blas) rather than openBLAS (although numpy with openBLAS performs reasonably well).

### Using the Mac GPU (MPS) with Python packages

You may also want to use the Mac GPU with Python packages such as JAX and PyTorch that can offload computations to a GPU. This requires that the Python package support the Metal (MPS) backend.

While JAX can use Metal (MPS) if you install the `jax-metal` and `ml_dtypes` packages, there seem to be a number of [compatibility issues that make this difficult or infeasible](https://github.com/jax-ml/jax/issues/27062) as of late 2025.

Torch should automatically provide support for the Mac GPU. You may need to explicitly set the device to be "mps" instead of "cpu". In some basic testing we have done, using "mps" rather than "cpu" for intensive linear algebra computations did not make much difference, but it's probably worth experimenting on your own workflows. 


(m-series-r)=
### R for Mac ARM64-based machines

[CRAN provides versions for Apple silicon](https://cran.r-project.org/bin/macosx/).

As of recent R versions, installation from CRAN will [automatically use Apple's Accelerate vecLib BLAS](./kb/linear-algebra-using-blas/#configuring-use-of-a-fast-blas) rather than the very slow default BLAS provided with R, but you may want to [check that vecLib BLAS is being used](./kb/linear-algebra-using-blas/#checking-use-of-a-fast-blas).
