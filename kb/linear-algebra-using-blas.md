---
title: "Linear Algebra using BLAS"
---
This documentation covers using fast parallelized linear algebra in R,
Python, and Julia. All of these rely on the BLAS library for basic
linear algebra calculations and can make use of fast parallel versions
of the BLAS, usually OpenBLAS, MKL, or (for MacOS) Apple's Accelerate
(vecLib) BLAS. 

The OpenBLAS
threaded BLAS is installed on all the compute servers, including the
cluster. This allows parallelization of linear algebra routines, in
particular any linear algebra done in R, via a mechanism known as
threading. For Python, numpy on the SCF uses OpenBLAS as well

In some cases using multiple threads can actually slow down a job, or
more commonly, can give negligible speed-up. It's worth testing your job
using a single thread vs. multiple threads to see what the speed-up is.

## Modifying the number of threads used

For any software using OpenBLAS, MKL, or Apple's Accelerate framework,
you can restrict your job to a single thread by setting the appropriate
environment variable before starting your job. To restrict to a single
thread, do the following at the command line (in bash):

```{code} bash
# OpenBLAS (do this on the SCF)
export OMP_NUM_THREADS=1

# MKL
export MKL_NUM_THREADS=1

# Apple Accelerate (vecLib BLAS)
export VECLIB_MAXIMUM_THREADS=1
```

Or you could set that to some other number.

In R, you can also use the `RhpcBLASctl` package, which provides
`blas_get_num_threads()` and `blas_set_num_threads()`.

In Julia, you can also use `LinearAlgebra.BLAS.get_num_threads()`
and `LinearAlgebra.BLAS.set_num_threads()`

## Checking use of a fast BLAS

::::{tab-set}

:::{tab-item} R

You can use `sessionInfo()` to check use of a fast, parallelized BLAS.
On Linux, it should generally be clear if it is using OpenBLAS or MKL.
E.g., here we see use of OpenBLAS:

```{code} R
> sessionInfo()
R version 4.3.0 (2023-04-21)
Platform: x86_64-pc-linux-gnu (64-bit)
Running under: Ubuntu 22.04.1 LTS

Matrix products: default
BLAS:   /usr/lib/x86_64-linux-gnu/openblas-pthread/libblas.so.3
LAPACK: /usr/lib/x86_64-linux-gnu/openblas-pthread/libopenblasp-r0.3.20.so;  LAPACK version 3.10.0
```

On MacOS, if you are using the Accelerate vecLib BLAS, you should see something like this (note the path for BLAS indicating "Accelerate" and "vecLib"):

```{code} R
> sessionInfo()
R version 4.4.0 (2024-04-24)

Platform: aarch64-apple-darwin20

Running under: macOS Sonoma 14.6.1


Matrix products: default

BLAS:   /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBLAS.dylib 
LAPACK: /Library/Frameworks/R.framework/Versions/4.4-arm64/Resources/lib/libRlapack.dylib;  LAPACK version 3.12.0
```

Alternatively (this would potentially be the case with older versions of R), there may be cases where if you look at the files in the directory containing the BLAS
and LAPACK dylib files, you can  see that `libRblas.dylib`
is symbolically linked to the Accelerate (vecLib) BLAS dylib file, as is seen here:


```{code} shell-session
$ ls -l /Library/Frameworks/R.framework/Versions/4.4-arm64/Resources/lib/
total 22216
-rwxrwxr-x  1 root  admin  5202304 Apr 24  2024 libR.dylib
drwxrwxr-x  3 root  admin       96 Apr 24  2024 libR.dylib.dSYM
-rwxrwxr-x  1 root  admin   193968 Apr 24  2024 libRblas.0.dylib
drwxrwxr-x  3 root  admin       96 Apr 24  2024 libRblas.0.dylib.dSYM
lrwxr-xr-x  1 root  admin       21 Nov 25 15:13 libRblas.dylib -> libRblas.vecLib.dylib
drwxrwxr-x  3 root  admin       96 Apr 24  2024 libRblas.dylib.dSYM
lrwxrwxr-x  1 root  admin       16 Jun 11  2024 libRblas.dylib.default -> libRblas.0.dylib
-rwxrwxr-x  1 root  admin   154464 Apr 24  2024 libRblas.vecLib.dylib
drwxrwxr-x  3 root  admin       96 Apr 24  2024 libRblas.vecLib.dylib.dSYM
-rwxrwxr-x  1 root  admin  1799872 Apr 24  2024 libRlapack.dylib
drwxrwxr-x  3 root  admin       96 Apr 24  2024 libRlapack.dylib.dSYM
-rw-rw-r--  1 root  admin   157712 Apr 24  2024 libgcc_s.1.1.dylib
-rwxrwxr-x  1 root  admin  1864864 Apr 24  2024 libgfortran.5.dylib
-rwxrwxr-x  1 root  admin  1613904 Apr 24  2024 libomp.dylib
-rwxrwxr-x  1 root  admin   366800 Apr 24  2024 libquadmath.0.dylib
drwxrwxr-x  3 root  admin       96 Apr 24  2024 pkgconfig
```
:::

:::{tab-item} Python

In Python, use of the BLAS is done via `numpy`. It can be a bit tricky
to check what BLAS is being used by numpy. `numpy.show_config()` may
give some indication but it can be hard to decipher. 

If numpy was installed via `conda` or `mamba`, you can look for
`libopenblas\*` or `libmkl\*` file(s) in the `lib` directory of
the Conda environment you are using. Their presence will generally
indicate that numpy is using that BLAS.

If numpy was installed via pip, you can look for `libopenblas\*`
file(s) in `lib/pythonX.Y/site-packages/numpy.libs` (Linux) or
`lib/pythonX.Y/site-packages/numpy/.dylibs` (MacOS) or a similar
location on Windows, where the location of `lib/...` should be the
`lib` directory associated with the Python installation you are using.

On MacOS, assuming you are using Conda (or Mamba), 
you may need to specifically see if the BLAS library package installed by Conda is 
the `accelerate` version, as seen below:

```{code} shell-session
$ conda list
<snip>
 libblas          3.11.0      2_h8d724d3_accelerate  conda-forge
<snip>
```

:::

:::{tab-item} Julia

Julia uses OpenBLAS for its basic linear algebra calculations.
:::

::::

## Configuring use of a fast BLAS

::::{tab-set}

:::{tab-item} R
For Linux, enable OpenBLAS by following [Section A.3 of the R Installation and Administration
Manual](https://cran.r-project.org/doc/manuals/r-release/R-admin.html#BLAS).

With MacOS, CRAN's R binary now comes with the 
comes the fast, threaded vecLib BLAS from Apple's Accelerate framework.
In the event this is not the case, you can [enable the Accelerate vecLib BLAS for R](https://cran.r-project.org/bin/macosx/RMacOSX-FAQ.html#Which-BLAS-is-used-and-how-can-it-be-changed_003f)
on your own Mac. You'll need
administrative privileges. 

If you install R via Conda on MacOS, it will by default use openBLAS and show reasonably good performance, but youwill probably want to use the Accelerate vecLib BLAS by running `conda -c conda-forge install libblas=*=*_newaccelerate`.

[On Windows, you can enable OpenBLAS with R](https://www.r-bloggers.com/2022/01/building-r-4-2-for-windows-with-openblas/) (or search for more up-to-date instructions online).

:::

:::{tab-item} Python

If you install numpy using Conda or Mamba, numpy will generally use
OpenBLAS (if using the `conda-forge` channel) or MKL (if using the
Anaconda default channel). While installing numpy, in the list of
packages being installed you should see either MKL or OpenBLAS
package(s) also being installed.

If you install numpy using pip, numpy will generally use OpenBLAS.

With MacOS, openBLAS should show reasonably good performance including on the M-series (Apple silicon) chips.
However you  will probably want use the fast, threaded vecLib BLAS from Apple's Accelerate framework.
which can be done by running `conda install -c conda-forge numpy "libblas=*=*accelerate"`.

:::

:::{tab-item} Julia
With Julia there is nothing to be done. Julia should use OpenBLAS
without any configuration needed.
:::

::::
