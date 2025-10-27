---
title: "GPU Servers"
---

## Hardware

The SCF can help with access to several GPU resources:

The SCF operates one GPU available to all SCF users on an equal basis and many other GPUs purchased by research groups available to non-group members at lower priorty. 

You need to [use
the Slurm scheduling software](cluster/gpus.md) to run
any job making use of the GPU. You may want to use an interactive
session to develop and test your GPU code. That same link also has
information on monitoring GPU usage of your job.

### General Access GPUs

#### *GPU* partition

We have one Titan Xp with 12 GB memory on one of our Linux servers
(roo), available through the *gpu* partition. The GPUs formerly
available in the *high* partition have been retired as of March 2023.

#### Savio

Access to GPUs on Savio is available through the [Savio faculty
computing
allowance](http://research-it.berkeley.edu/services/high-performance-computing/faculty-computing-allowance).
Please contact SCF staff for more information.

### Research Group GPUs

The SCF also operates the following GPUs. These GPUs are owned by
individual faculty members, but anyone can run jobs on them. If you are
not a member of the lab group, your jobs will run on a preemptible basis,
which means they can be cancelled at any time by a higher-priority jobs.
These servers can be accessed by submitting to the *jsteinhardt*,
*yugroup*, *yss,* or *songmei* partitions using the [Slurm scheduling
software](cluster.md).

| Partition     | Machine Name            | GPU Type (Number of GPUs) | GPU Memory |
|---------------|-------------------------|---------------------------|------------|
| `jsteinhardt` | `balrog`                | A100 (8)                  | 40 GB      |
| `jsteinhardt` | `saruman`               | A100 (10)                 | 80 GB      |
| `jsteinhardt` | `rainbowquartz`         | A5000 (8)                 | 24 GB      |
| `jsteinhardt` | `smokyquartz`           | A4000 (8)                 | 16 GB      |
| `jsteinhardt` | `sunstone`              | A4000 (8)                 | 16 GB      |
| `jsteinhardt` | `smaug`                 | Quadro RTX 8000           | 48 GB      |
| `jsteinhardt` | `shadowfax`             | GeForce RTX 2080 Ti (8)   | 11 GB      |
| `lambda`      | Remote cluster [1]      | A100 (40)                 | 80 GB      |
| `yugroup`     | `treebeard`             | A100 (1)                  | 40 GB      |
| `yugroup`     | `merry`                 | GeForce GTX TITAN X(1)    | 12 GB      |
| `yugroup`     | `morgoth`               | Titan Xp (1)              | 12 GB      |
| `yugroup`     | `morgoth`               | Titan X (Pascal) (1)      | 12 GB      |
| `yss`         | `luthien`               | A100 (4)                  | 80 GB      |
| `yss`         | `beren`                 | A100 (8)                  | 80 GB      |
| `songmei`     | `feanor`[2]             | H200 (8)                  | 144 GB     |
| `berkeleynlp` | `lorax`[2]              | H200 (8)                  | 144 GB     |

[1] To use one of these five machines, one must specifically [connect to the remote cluster](cluster/gpus.md#steinhardt-remote-cluster),
which is accessed separately from the other SCF resources.

[2] Requires the fully qualified domain name, i.e., `{hostname}.stat.berkeley.edu`.

## Software

We provide the following software that will help you in making use of
the GPU:

- CUDA (version 12.8; other versions can be made available)
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

We use Linux [environment modules](../kb/environment-modules.md) to
manage the use of some GPU-based software, as seen below. 

For use Python packages that use the GPU for back-end computations,
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
