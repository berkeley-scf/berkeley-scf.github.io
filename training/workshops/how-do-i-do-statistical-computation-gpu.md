---
title: "How do I do statistical computation on a GPU?"
---
## Overview on using GPUs

GPUs provide the opportunity to do massively parallel computation, in
particular executing the same computations on many inputs. To do this,
you either need access to a machine with an installed GPU and
appropriate software libraries, or you need to use a virtual machine in
the cloud.

### GPU Resources

- The SCF has a GPU installed on one of the nodes (roo) of our
  [cluster](/servers/cluster) as well as a large number of
  other GPUs purchased by or donated to specific faculty members that
  are also available for use on a preemptible basis.
- The campus-wide [Savio
  cluster](http://research-it.berkeley.edu/services/high-performance-computing)
  has GPU nodes.
- GPUs are available through NSF's ACCESS network of supercomputers and
  on commercial cloud providers such as Amazon's AWS and Google cloud.
  Email us for more information.

We have more details on the [SCF GPUs and on using GPUs on Savio](/servers/gpu).

For the most part, researchers tend not to program directly on a GPU but
to use libraries such as PyTorch and JAX for Python (also CUDA.jl for
Julia) that make use of GPU(s) without one having to specifically write
GPU code. However, [the parallelization
tutorial](https://computing.stat.berkeley.edu/tutorial-parallelization)
provides some information about programming directly on a GPU.
