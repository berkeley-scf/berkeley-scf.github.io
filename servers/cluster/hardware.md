---
title: "Cluster hardware"
---
The cluster has thousands of (logical) cores, divided into 'partitions'
of nodes of similar hardware/capabilities. In our newer machines, each
'core' is actually a hardware thread, as we have hyperthreading enabled,
so the number of physical cores per machine is generally half that
indicated in the Hardware tab below.

If you'd like to run multi-core jobs without hyperthreading, please
contact us for work-arounds.

Here are the details of the nodes in the various partitions.

- 256 of the cores are in the 'low' partition.
  - 8 nodes with 32 cores and 256 GB RAM per node.
  - By default jobs submitted to the cluster will run here.
- 96 of the cores are in the 'high' partition.
  - 4 nodes with 24 cores (12 physical cores) and 128 GB RAM per node.
  - Newer (but not new) and faster nodes than in the 'low' partition.
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
  partition on a remote cluster located in Texas.
  - 5 servers each with 256 cores (128 physical cores) and 1 TB RAM.
  - Newer and faster cores than in the 'high' partition.
  - Very fast disk I/O (using NVMe SSDs) to files located in /data.
  - Jobs are subject to preemption at any time and will be cancelled in
    that case without warning (more details below).
- 256 cores are available on a preemptible basis in the 'epurdom'
  partition.
  - The `frodo` and `samwise` servers each have 128 cores (64
    physical cores) and 528 GB RAM.
- Additional GPU servers in the 'yugroup', 'yss', and 'songmei'
  partitions.
- 64 cores are in the 'lowmem' partition, intended to supplement our
  other partitions, particularly during heavy cluster usage.
  - 4 nodes, 16 cores and 12-16 GB RAM per node.
  - Older, slower nodes that are comparable to, or a bit slower than,
    the nodes in the 'low' partition.
  - Only suitable for jobs that have low memory needs, but you should
    feel free to request an entire node for jobs needing more memory,
    even if your code will only use one or a few cores.

We have a number of [GPU servers](/servers/gpu-servers) that are part of the
cluster.
