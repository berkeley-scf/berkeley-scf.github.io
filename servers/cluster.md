---
title: "Linux Cluster"
---
The SCF operates a Linux cluster as our primary resource for users for
computational jobs.

The cluster is managed by the SLURM queueing software. SLURM provides a
standard batch queueing system through which users submit jobs to the
cluster. Jobs are typically submitted to SLURM using a user-defined
shell script that executes one's application code. Interactive use is
also an option. Users may also query the cluster to see job status. As
currently set up, the cluster is designed for processing single-core and
multi-core/threaded jobs, as well as jobs that are set up to use
multiple machines (aka 'nodes') within the cluster (i.e., distributed
memory jobs). All software running on SCF Linux machines is available on
the cluster. Users can also compile programs on any SCF Linux machine
and then run that program on the cluster.

The cluster is open to Department of Statistics faculty, grad students,
postdocs, and visitors using their SCF logon. Class account users do not
have access by default, but instructors can email
manager@stat.berkeley.edu to discuss access for their class.

All jobs that you run on the cluster need to be
[submitted via the Slurm scheduling software](/servers/cluster/submitting) from one of our
[Linux servers](login-servers). Slurm sends each job to run on a machine (aka a *node*) (or
machines) on one of the partitions in the cluster. A *partition* is a
collection of machines with similar hardware.

Please click on the bubbles below or see the subpages in the right-hand
side menu for more details.

::::{grid} 1 1 2 3

:::{card}
:link: servers/cluster/quick-start
:header: Quick start
```{image} ../images/MASTERS.svg
:alt: Abstract illustration using circles that look like shooting stars
:width: 100px
:align: center
```
Get up and running on the cluster.
:::

:::{card}
:link: servers/cluster/hardware
:header: Cluster hardware

```{image} ../images/HIRING_STUDENTS.svg
:alt: Abstract illustration that  looks like a pie chart.
:width: 100px
:align: center
```
Detailed information about the compute nodes in the cluster.
:::

:::{card}
:link: cluster/monitoring
:header: Monitoring

```{image} ../images/GIVE_TO_DEPT.svg
:alt: Abstract illustration that looks like points and an axis.
:width: 100px
:align: center
```
How to monitor jobs and activity on the cluster.
:::

:::{card}
:link: cluster/submitting
:header: Basic job submission

```{image} ../images/CONSULTING.svg
:alt: Abstract illustration using seven colored circles
:width: 100px
:align: center
```

How to submit cluster jobs using the Slurm scheduler.
:::

:::{card}
:link: servers/cluster/parallel
:header: Submitting parallel jobs

```{image} ../images/UNDERGRAD.svg
:alt: Abstract illustration using seven colored circles arranged in a geometric pattern.”
:width: 100px
:align: center
```
How to prepare and submit code to run in parallel.
:::

:::{card}
:link: cluster/gpus
:header: GPU jobs

```{image} ../images/FOR_ALMUNI.svg
:alt: Abstract illustration using dots a lines to form the Campanile
:width: 100px
:align: center
```
Submitting GPU jobs to our various partitions with GPU servers.
:::
::::

