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

See the [first table](#gpu-server-specs) below for information about the GPU servers and the [second table](#gpu-server-additional-specs) for more detailed
information related to local disk, GPU-to-GPU interconnect, and location/latency.

With regard to the latency, note that some GPU machines are located at the NASA Ames facility approximately 75 km from Berkeley,
where the SCF fileservers hosting home and scratch directories (via NFS) are located. This distance results in a two microsecond latency that when working with many (often small) files (including Conda/Mamba-related work) can sometimes cause slowness and laggy behavior. [Local disks are available to group members](./cluster/gpus/#research-group-details) to help work around this problem.

#### GPU server specs

| Partition     | Machine Name            | GPU Type (Number of GPUs) | GPU Memory |
|---------------|----------------------|---------------------------|------------|
| `jsteinhardt` | `cubbins`[^fqdn]     | H200 (8)                  | 144 GB     |
| `jsteinhardt` | `mcfuzz`[^fqdn]      | H200 (8)                  | 144 GB     |
| `jsteinhardt` | `mooney`[^fqdn]      | H200 (8)                  | 144 GB     |
| `jsteinhardt` | `sneetches`[^fqdn]   | H200 (8)                  | 144 GB     |
| `jsteinhardt` | `balrog`             | A100 (8)                  | 40 GB      |
| `jsteinhardt` | `saruman`            | A100 (10)                 | 80 GB      |
| `jsteinhardt` | `rainbowquartz`      | A5000 (8)                 | 24 GB      |
| `jsteinhardt` | `smokyquartz`        | A4000 (8)                 | 16 GB      |
| `jsteinhardt` | `sunstone`           | A4000 (8)                 | 16 GB      |
| `jsteinhardt` | `smaug`              | Quadro RTX 8000 (1)       | 48 GB      |
| `jsteinhardt` | `shadowfax`          | GeForce RTX 2080 Ti (8)   | 11 GB      |
| `yugroup`     | `treebeard`          | A100 (1)                  | 40 GB      |
| `yugroup`     | `merry`              | GeForce GTX TITAN X (1)   | 12 GB      |
| `yugroup`     | `morgoth`            | Titan Xp (1)              | 12 GB      |
| `yugroup`     | `morgoth`            | Titan X (Pascal) (1)      | 12 GB      |
| `yss`         | `luthien`            | A100 (4)                  | 80 GB      |
| `yss`         | `beren`              | A100 (8)                  | 80 GB      |
| `songmei`     | `feanor`[^fqdn]      | H200 (8)                  | 144 GB     | 
| `berkeleynlp` | `horton`[^fqdn]      | H200 (8)                  | 144 GB     | 
| `berkeleynlp` | `lorax`[^fqdn]       | H200 (8)                  | 144 GB     | 


[^fqdn]: Requires the fully qualified domain name when connecting, i.e., `ssh {hostname}.stat.berkeley.edu`.

#### GPU server additional specs

| Partition     | Machine Name         | GPU-to-GPU Interconnect | Local storage[^disk] | Location |
|---------------|----------------------|-------------------------|------------|----------|
| `jsteinhardt` | `cubbins`[^fqdn]     | NVSwitch                | 14 TB NVME     | NASA Ames[^latency] |
| `jsteinhardt` | `mcfuzz`[^fqdn]      | NVSwitch                | 14 TB NVME     | NASA Ames[^latency] |
| `jsteinhardt` | `mooney`[^fqdn]      | NVSwitch                | 14 TB NVME     | NASA Ames[^latency] |
| `jsteinhardt` | `sneetches`[^fqdn]   | NVSwitch                | 14 TB NVME     | NASA Ames[^latency] |
| `jsteinhardt` | `balrog`             | NVLink (pairs)          | 3.5 TB spinning| Berkeley |
| `jsteinhardt` | `saruman`            | NVLink (pairs)          | 7 TB NVME      | Berkeley  |
| `jsteinhardt` | `rainbowquartz`      | A5000 (8)               | 3.5 TB NVME    | Berkeley  |
| `jsteinhardt` | `smokyquartz`        | A4000 (8)               | 3.5 TB NVME    | Berkeley  |
| `jsteinhardt` | `sunstone`           | A4000 (8)               | 3.5 TB NVME    | Berkeley  |
| `jsteinhardt` | `smaug`              | NVLink (pairs)          | 2 TB NVME      | Berkeley  |
| `jsteinhardt` | `shadowfax`          | None                    | 3.6 TB spinning|  Berkeley  |
| `yugroup`     | `treebeard`          | N/A                     |       | Berkeley  |
| `yugroup`     | `merry`              | N/A                     |       | Berkeley  |
| `yugroup`     | `morgoth`            | N/A                     |       | Berkeley  |
| `yugroup`     | `morgoth`            | N/A                     |       | Berkeley  |
| `yss`         | `luthien`            | None                    |       | Berkeley  |
| `yss`         | `beren`              | NVLink (pairs)          |       | Berkeley  |
| `songmei`     | `feanor`[^fqdn]      | NVSwitch                | 6.6 TB NVME    | NASA Ames[^latency] |
| `berkeleynlp` | `horton`[^fqdn]      | NVSwitch                | 56 TB NVME     | NASA Ames[^latency] |
| `berkeleynlp` | `lorax`[^fqdn]       | NVLink (pairs)          |  56 TB NVME    | NASA Ames[^latency] |


[^fqdn]: Requires the fully qualified domain name when connecting, i.e., `ssh {hostname}.stat.berkeley.edu`.
[^disk]: Storage available at `/data` to group members. In addition, all machines have 100s of GB available on local `/tmp` and `/var/tmp` on spinning disks, available to all users.
[^latency]: Note that some GPU machines are located at the NASA Ames facility approximately 75 km from Berkeley, where the SCF fileservers hosting home and scratch directories (via NFS) are located. This distance causes a two microsecond latency that when working with many (often small) files (including Conda/Mamba-related work) can sometimes cause slowness and laggy behavior. [Local disks are available to group members](./cluster/gpus/#research-group-details) to help work around this problem.
