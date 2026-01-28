---
title: "GPU Servers"
---

## Hardware

The SCF operates one GPU available to all SCF users on an equal basis and many other GPUs purchased by research groups that are available to group members at regular priority and to other SCF users at lower (preemptible) priority. 

You need to [use
the Slurm scheduling software](cluster/gpus.md) to run
any job making use of the GPU. You may want to use an interactive
session to develop and test your GPU code. That same link also has
information on monitoring GPU usage of your job.

### General Access GPUs

#### *GPU* partition

We have one Titan Xp with 12 GB memory on one of our Linux servers
(roo), available through the *gpu* partition. 

#### Savio

Access to GPUs on Savio is available through the [Savio faculty
computing
allowance](http://research-it.berkeley.edu/services/high-performance-computing/faculty-computing-allowance).
Please contact SCF staff for more information.

### Research Group GPUs

The SCF also operates the following research group GPUs. These GPUs are owned by
individual faculty members, but anyone can run jobs on them. If you are
not a member of the lab group, your jobs will run on a preemptible basis,
which means they can be cancelled at any time by a higher-priority jobs.
These servers can be accessed by submitting to specific partition of interest using the [Slurm scheduling
software](cluster.md).

| Partition     | Machine Name            | GPU Type (Number of GPUs) | GPU Memory |
|---------------|-------------------------|---------------------------|------------|
| `jsteinhardt` | `balrog`                | A100 (8)                  | 40 GB      |
| `jsteinhardt` | `saruman`               | A100 (10)                 | 80 GB      |
| `jsteinhardt` | `rainbowquartz`         | A5000 (8)                 | 24 GB      |
| `jsteinhardt` | `smokyquartz`           | A4000 (8)                 | 16 GB      |
| `jsteinhardt` | `sunstone`              | A4000 (8)                 | 16 GB      |
| `jsteinhardt` | `smaug`                 | Quadro RTX 8000 (1)       | 48 GB      |
| `jsteinhardt` | `shadowfax`             | GeForce RTX 2080 Ti (8)   | 11 GB      |
| `lambda`      | Remote cluster [^lambda]      | A100 (40)                 | 80 GB      |
| `yugroup`     | `treebeard`             | A100 (1)                  | 40 GB      |
| `yugroup`     | `merry`                 | GeForce GTX TITAN X (1)   | 12 GB      |
| `yugroup`     | `morgoth`               | Titan Xp (1)              | 12 GB      |
| `yugroup`     | `morgoth`               | Titan X (Pascal) (1)      | 12 GB      |
| `yss`         | `luthien`               | A100 (4)                  | 80 GB      |
| `yss`         | `beren`                 | A100 (8)                  | 80 GB      |
| `songmei`     | `feanor`[^fqdn]             | H200 (8)                  | 144 GB     |
| `berkeleynlp` | `horton`[^fqdn]             | H200 (8)                  | 144 GB     |
| `berkeleynlp` | `lorax`[^fqdn]              | H200 (8)                  | 144 GB     |

[^lambda]: To use one of these five machines, one must specifically [connect to the remote cluster](cluster/gpus.md#steinhardt-remote-cluster), which is accessed separately from the other SCF resources.

[^fqdn]: Requires the fully qualified domain name when connecting, i.e., `ssh {hostname}.stat.berkeley.edu`.

