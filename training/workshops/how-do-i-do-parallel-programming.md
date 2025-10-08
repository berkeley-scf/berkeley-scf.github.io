---
title: "How do I do parallel programming?"
---
## Overview of Parallel Programming

There are two basic flavors of parallel processing (leaving aside GPUs):
distributed memory and shared memory. With shared memory, multiple
processors (which I'll call cores) on a machine (your laptop, a server,
etc.) share the same memory. With distributed memory, you have multiple
nodes (e.g., in a Linux cluster), each with their own memory. Each node
generally has multiple cores. You can think of each node as a separate
computer connected by a fast network to the other nodes.

The SCF has prepared two tutorials, [one on use of Dask (and a bit on
Ray) in Python and the future package in
R](http://berkeley-scf.github.io/tutorial-dask-future) for
parallelization across one or more machines and another [somewhat more
general tutorial on parallelization in Python, R, MATLAB and
C/C++](https://berkeley-scf.github.io/tutorial-parallelization).   These
tutorials are much more up-to-date than the workshop material below, but
job submission is not discussed much in the tutorials.

### November 2016 workshop

A two-part tutorial with extensive information on: campus and department
computing resources, submitting jobs to the department and campus
cluster, and various parallel programming approaches/tools/strategies,
including demo code, are [available in the 2016 git
repository](https://github.com/berkeley-scf/parallel-scf-2016) (in
particular see the Download ZIP button on the lower right of that link
to get all the materials as a zip file). The [first
session](https://rawgit.com/berkeley-scf/parallel-scf-2016/master/session1.html)
is on computing resources and job submission, while the [second
session](http://rawgit.com/berkeley-scf/parallel-scf-2016/master/session2.html)
is on parallel programming approaches, tools, and strategies. You can
clone the repository with a git clone, which can be done from the
Linux/Mac command line as:

    git clone https://github.com/berkeley-scf/parallel-scf-2016

Videos of the [first](http://youtu.be/M2rHK3z8Sr0) and
[second](https://youtu.be/0z6Tx5obs_M) session are available.

### October 2015 workshop

[A 2015
tutorial](https://rawgit.com/berkeley-scf/parallel-scf-2015/master/parallel.html)
with extensive information on both flavors of parallel processing and on
how to submit jobs to the SCF Linux cluster, as well as demo code, are
[available in the 2015 git
repository](https://github.com/berkeley-scf/parallel-scf-2015) (in
particular see the Download ZIP button on the lower right of that link
to get all the materials as a zip file). You can clone the repository
with a git clone, which can be done from the Linux/Mac command line as:

    git clone https://github.com/berkeley-scf/parallel-scf-2015

### October 2014 workshop

[A 2014
tutorial](http://www.stat.berkeley.edu/scf/paciorek-parallel-2014.pdf)
with extensive information on both flavors of parallel processing and on
how to submit jobs to the SCF Linux cluster, as well as demo code, are
[available in the 2014 git
repository](https://github.com/berkeley-scf/parallel-workshop-2014) (in
particular see the Download ZIP button on the lower right of that link
to get all the materials as a zip file). You can clone the repository
with a git clone, which can be done from the Linux/Mac command line as:

    git clone https://github.com/berkeley-scf/parallel-workshop-2014

### 2012 and 2013 workshops

Before October 2014, we had older versions of this material provided
separately for shared memory and distributed memory parallel processing:

1.  For information on shared memory parallel programming, please see
    [these notes on the basics of shared memory parallel programming in
    R, Matlab, Python and
    C](http://www.stat.berkeley.edu/scf/paciorek-parallelWorkshop.pdf),
    and the [accompanying template
    code](http://www.stat.berkeley.edu/scf/paciorek-parallelWorkshopCode.zip) (most
    of the code is also embedded in the notes).
2.  For information on distributed memory parallel programming using
    message passing, such as with MPI, see [these
    notes](http://www.stat.berkeley.edu/scf/paciorek-distribComp.pdf) on
    the basics of distributed memory parallel programming in R and C,
    and the [accompanying template code
    files](http://www.stat.berkeley.edu/scf/paciorek-distribCompCode.zip)
    (most of the code is also embedded in the notes).
