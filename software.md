---
title: "Software"
---

The SCF provides a variety of software on SCF machines and software is also
available for you to install on your own machine, including for ARM64-based
Macs.

We can [help install other software](/software/install) you might need, either in your home directory or system-wide.

## SCF Software

The SCF has been a primary testing site for some of the most important
statistical packages now in use. It was the first primary test site for
the 'S' statistical language, and a primary test site for the UNIX
version of SAS.

The primary computational software currently supported by SCF includes:

- R (including an extensive set of packages from CRAN), RStudio, and [RStudio via a web browser](software/rstudio)
- [Python](software/python) (the Miniforge distribution, including an extensive set of packages)
- [Jupyter notebooks](/access/jupyterhub) (IPython and R, among others)
- [MATLAB](software/matlab) (including all Mathworks toolboxes)
- [Julia](software/julia)
- [Mathematica](/software/mathematica), including *Wolfram Alpha Pro*
- Packages with [GPU support](/servers/gpu-servers#software),
  often used for machine learning, including PyTorch and Jax for Python.

In addition, we support standard software used in research and teaching,
including vim, emacs, LaTeX (and LyX), and Perl, among others. Other
supported resources include:

- standard compilers for C, C++, Fortran, and other languages,
- [fast, threaded linear algebra libraries](/faqs/linear-algebra-and-parallelized-linear-algebra-using-blas) (OpenBLAS and ACML)
- support for [parallel programming](/training/workshops/how-do-i-do-parallel-programming), including MPI and openMP,
- other computational software, including JAGS and Stan.
- [hosting of Shiny repositories](/faqs/hosting-shiny-app)
- [Running Docker containers via enroot](/software/containers) (or possibly udocker).

Finally, we can generally install software needed for teaching or
research by our users, including R, Python, Julia, and MATLAB
packages, [upon request](mailto:consult@stat.berkeley.edu). And we try
to keep up with useful new software as it becomes available.

Note that access to some software (in particular machine learning and
GPU-using software, and switching between versions of Python) is
controlled via [Linux environment modules](/faqs/environment-modules)

## Campus Distributed Software

Note that software for installation on personal machines can be obtained
from the campus-wide [Software Central site](http://ist.berkeley.edu/software-central).

### MATLAB

[Install MATLAB](/faqs/how-can-i-install-matlab-my-computer) on your own computer, or contact SCF staff for assistance.

### Self Service

If you have a UC-owned Mac, you can use the Casper Self Service
application to install the Adobe Creative Suite (Photoshop, Illustrator,
etc.), Adobe Acrobat Professional, Microsoft Office, and other
commercial and free software. This is especially useful if you need to
install a lot of common software like Google Chrome, Cyberduck, and
Dropbox on your computer since you can easily install them all through
this one application. Contact SCF staff for assistance.

(m1-software)=
## Software for Mac ARM64-based Machines (Apple Silicon M1 and M2 Macs)

With the M1 and M2 Macs, Apple is now using its own chips, referred to
as *Apple Silicon*. These have a different architecture, ARM64, than
standard x86-64 chips, such as those produced by Intel and AMD.

Some software is now available to run natively on the new architecture.
In particular:

- You can use [Anaconda with ARM64 support to run Python](/software/conda#m1-anaconda)
- You can install the [ARM64 version of R from CRAN](https://cran.r-project.org/bin/macosx/).

Non-ARM64 programs will work on the new Apple Silicon-based machines by
automatically making use of Apple's Rosetta2 system to translate machine
code from ARM64 to x86-64, but you can expect some decrease in
performance relative to ARM64-based software. 
