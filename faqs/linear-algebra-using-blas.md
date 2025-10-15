---
title: "Linear Algebra using BLAS"
---
This documentation covers using fast parallelized linear algebra in R,
Python, and Julia. All of these rely on the BLAS library for basic
linear algebra calculations and can make use of fast parallel versions
of the BLAS, usually OpenBLAS, MKL, or (for MacOS) Apple's Accelerate
(vecLib) BLAS. 

<span id="cke_bm_1309S" style="display: none;"> </span>The OpenBLAS
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

    export OMP_NUM_THREADS=1         # OpenBLAS
    export MKL_NUM_THREADS=1         # MKL
    export VECLIB_MAXIMUM_THREADS=1  # Apple Accelerate for older Intel-based Macs; not relevant for M1/M2 Macs

Or you could set that to some other number.

Note that newer Macs (Apple Silicon-based M1 and M2 Macs) use the
Accelerate (vecLib) BLAS, but apparently they use the Mac's AMX
co-processor. This gives fast computation, but the calculations are not
using the regular CPU cores, so one doesn't use
\`VECLIB_MAXIMUM_THREADS\`.

In R, you can also use the \`RhpcBLASctl\` package, which provides
\`blas_get_num_threads()\` and \`blas_set_num_threads()\`.

In Julia, you can also use \`LinearAlgebra.BLAS.get_num_threads()\`
and \`LinearAlgebra.BLAS.set_num_threads()\`

## Checking use of a fast BLAS

<div class="bootstrap-tabs" tab-set-title="XYZ">

- <a href="#xyz-tab-1-name" class="tab-link"
  aria-controls="xyz-tab-1-name" data-toggle="tab" role="tab">R</a>
- <a href="#xyz-tab-2-name" class="tab-link"
  aria-controls="xyz-tab-2-name" data-toggle="tab" role="tab">Python</a>
- <a href="#xyz-tab-3-name" class="tab-link"
  aria-controls="xyz-tab-3-name" data-toggle="tab" role="tab">Julia</a>

<div class="tab-content">

<div id="xyz-tab-1-name" class="tab-pane active" role="tabpanel">

<div class="tab-pane-content">

You can use \`sessionInfo()\` to check use of a fast, parallelized BLAS.
On Linux, it should generally be clear if it is using OpenBLAS or MKL.
E.g., here we see use of OpenBLAS:

</div>

<div class="tab-pane-content">

    > sessionInfo()
    R version 4.3.0 (2023-04-21)
    Platform: x86_64-pc-linux-gnu (64-bit)
    Running under: Ubuntu 22.04.1 LTS

    Matrix products: default
    BLAS:   /usr/lib/x86_64-linux-gnu/openblas-pthread/libblas.so.3 
    LAPACK: /usr/lib/x86_64-linux-gnu/openblas-pthread/libopenblasp-r0.3.20.so;  LAPACK version 3.10.0

On MacOS, it may not be clear:

    > sessionInfo()
    R version 4.2.2 (2022-10-31)
    Platform: aarch64-apple-darwin20 (64-bit)
    Running under: macOS Ventura 13.6

    Matrix products: default
    LAPACK: /Library/Frameworks/R.framework/Versions/4.2-arm64/Resources/lib/libRlapack.dylib

However, if you look at the files in the directory containing the BLAS
and LAPACK dylib files, you should be able to see if \`libRblas.dylib\`
is symbolically linked to the Accelerate (vecLib) BLAS dylib file:

    $ ls -l /Library/Frameworks/R.framework/Versions/4.2-arm64/Resources/lib
    total 16504
    -rwxrwxr-x  1 root      admin  3988192 Oct 31  2022 libR.dylib
    drwxrwxr-x  3 root      admin       96 Oct 31  2022 libR.dylib.dSYM
    -rwxrwxr-x  1 root      admin   193440 Oct 31  2022 libRblas.0.dylib
    drwxrwxr-x  3 root      admin       96 Oct 31  2022 libRblas.0.dylib.dSYM
    lrwxr-xr-x  1 scflocal  admin       21 Nov 10  2022 libRblas.dylib -> libRblas.vecLib.dylib
    drwxrwxr-x  3 root      admin       96 Oct 31  2022 libRblas.dylib.dSYM
    -rwxrwxr-x  1 root      admin   154464 Oct 31  2022 libRblas.vecLib.dylib
    drwxrwxr-x  3 root      admin       96 Oct 31  2022 libRblas.vecLib.dylib.dSYM
    -rwxrwxr-x  1 root      admin  1711824 Oct 31  2022 libRlapack.dylib
    drwxrwxr-x  3 root      admin       96 Oct 31  2022 libRlapack.dylib.dSYM
    -rw-rw-r--  1 root      admin   157792 Oct 31  2022 libgcc_s.1.1.dylib
    -rwxrwxr-x  1 root      admin  1865904 Oct 31  2022 libgfortran.5.dylib
    -rwxrwxr-x  1 root      admin   367040 Oct 31  2022 libquadmath.0.dylib

 

</div>

</div>

<div id="xyz-tab-2-name" class="tab-pane" role="tabpanel">

<div class="tab-pane-content">

In Python, use of the BLAS is done via \`numpy\`. It can be a bit tricky
to check what BLAS is being used by numpy. \`numpy.show_config()\` may
give some indication but it can be hard to decipher. 

</div>

<div class="tab-pane-content">

 

</div>

<div class="tab-pane-content">

If numpy was installed via \`conda\` or \`mamba\`, you can look for
\`libopenblas\*\` or \`libmkl\*\` file(s) in the \`lib\` directory of
the Conda environment you are using. Their presence will generally
indicate that numpy is using that BLAS.

</div>

<div class="tab-pane-content">

 

</div>

<div class="tab-pane-content">

If numpy was installed via pip, you can look for \`libopenblas\*\`
file(s) in \`lib/pythonX.Y/site-packages/numpy.libs\` (Linux) or
\`lib/pythonX.Y/site-packages/numpy/.dylibs\` (MacOS) or a similar
location on Windows, where the location of \`lib/...\` should be the
\`lib\` directory associated with the Python installation you are using.

</div>

<div class="tab-pane-content">

 

</div>

</div>

<div id="xyz-tab-3-name" class="tab-pane" role="tabpanel">

<div class="tab-pane-content">

Julia uses OpenBLAS for its basic linear algebra calculations.

</div>

</div>

</div>

</div>

## Configuring use of a fast BLAS

<div class="bootstrap-tabs" tab-set-title="XYZ">

- <a href="#xyz-tab-1-name" class="tab-link"
  aria-controls="xyz-tab-1-name" data-toggle="tab" role="tab">R</a>
- <a href="#xyz-tab-2-name" class="tab-link"
  aria-controls="xyz-tab-2-name" data-toggle="tab" role="tab">Python</a>
- <a href="#xyz-tab-3-name" class="tab-link"
  aria-controls="xyz-tab-3-name" data-toggle="tab" role="tab">Julia</a>

<div class="tab-content">

<div id="xyz-tab-1-name" class="tab-pane" role="tabpanel">

<div class="tab-pane-content">

On a Linux machine, to enable openBLAS for R on your own Linux machine,
see [Section A.3 of the R Installation and Administration
Manual](https://cran.r-project.org/doc/manuals/r-release/R-admin.html#BLAS).

</div>

<div class="tab-pane-content">

 

</div>

<div class="tab-pane-content">

With MacOS, CRAN's R binary comes with a default BLAS that the R
developers recommend and a fast, threaded BLAS from Apple's Accelerate
framework. See
[here](https://cran.r-project.org/bin/macosx/RMacOSX-FAQ.html#Which-BLAS-is-used-and-how-can-it-be-changed_003f)
for information on how to enable the latter on your own Mac. You'll need
administrative privileges. Those instructions should work for newer M1
and M2-based Macs as well as older Macs using Intel processors.

</div>

<div class="tab-pane-content">

 

</div>

<div class="tab-pane-content">

To enable openBLAS with R on your own Windows machine, [these
instructions](https://www.r-bloggers.com/2022/01/building-r-4-2-for-windows-with-openblas/) may
be helpful.

</div>

</div>

<div id="xyz-tab-2-name" class="tab-pane" role="tabpanel">

<div class="tab-pane-content">

If you install numpy using Conda or Mamba, numpy will generally use
OpenBLAS (if using the \`conda-forge\` channel) or MKL (if using the
Anaconda default channel). While installing numpy, in the list of
packages being installed you should see either MKL or OpenBLAS
package(s) also being installed.

</div>

<div class="tab-pane-content">

 

</div>

<div class="tab-pane-content">

If you install numpy using pip, numpy will generally use OpenBLAS.

</div>

</div>

<div id="xyz-tab-3-name" class="tab-pane active" role="tabpanel">

<div class="tab-pane-content">

With Julia there is nothing to be done. Julia should use OpenBLAS
without any configuration needed.

</div>

</div>

</div>

</div>

###  
