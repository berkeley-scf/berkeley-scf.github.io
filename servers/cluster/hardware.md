---
title: "Cluster hardware"
---
The cluster has thousands of (logical) cores, divided into 'partitions'
of nodes of similar hardware/capabilities. In our newer machines, each
'core' is actually a hardware thread, as we have hyperthreading enabled,
so the number of physical cores per machine is generally half that
indicated in the Hardware information given below.

If you'd like to run multi-core jobs without hyperthreading, please
contact us for work-arounds.

Here are the details of the nodes in the various partitions.

- 96 of the cores are in the 'high' partition.
  - 4 nodes with 24 cores (12 physical cores) and 128 GB RAM per node.
  - Newer (but not new) and faster nodes than in the 'low' partition.
  - By default jobs submitted to the cluster will run here.
- 256 of the cores are in the 'low' partition.
  - 8 nodes with 32 cores and 256 GB RAM per node.
- 256 cores are available on a preemptible basis in the 'epurdom'
  partition.
  - The `frodo` and `samwise` servers each have 128 cores (64
    physical cores) and 528 GB RAM.
- 504 cores are available on preemptible basis in the 'jsteinhardt'
  partition.
  - Many cores and (for some nodes) large memory on various nodes:
    - `shadowfax` has 48 cores (24 physical cores) and 132 GB RAM.
    - `smaug` has 64 cores (32 physical cores) and 288 GB RAM.
    - `balrog` has 96 cores (48 physical cores) and 792 GB RAM.
    - `sunstone` and `smokyquartz` each have 64 cores (32 physical
      cores) and 128 GB RAM.
    - `rainbowquartz` has 64 cores (32 physical cores) and 792 GB RAM.
    - `saruman` has 104 cores (52 physical cores) and 1 TB RAM.
  - Newer and perhaps somewhat faster cores than in the 'high'
    partition.
  - Very fast disk I/O (using NVMe SSDs) to files located in /tmp and
    /var/tmp.
  - Jobs are subject to preemption at any time and will be cancelled in
    that case without warning (more details below).
- 1280 cores are available on a preemptible basis in the 'lambda'
  partition on a remote cluster located in Washington state.
  - 5 servers each with 256 cores (128 physical cores) and 1 TB RAM.
  - Newer and faster cores than in the 'high' partition.
  - Very fast disk I/O (using NVMe SSDs) to files located in /data.
  - Jobs are subject to preemption at any time and will be cancelled in
    that case without warning (more details below).
- Additional GPU servers in the 'yugroup', 'yss', 'songmei', and 'berkeleynlp'
  partitions.

We have a number of [GPU servers](../gpu-servers) that are part of the
cluster.
