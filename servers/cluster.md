---
title: "Linux Cluster"
---
The SCF operates a Linux cluster as our primary resource for users for
computational jobs.

The cluster is managed by the Slurm queueing software. Slurm provides a
standard batch queueing system through which users submit jobs to the
cluster. Jobs are typically submitted to Slurm using a user-defined
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
[submitted via the Slurm scheduling software](./cluster/submitting.md) from one of our
[Linux servers](login-servers.md). Slurm sends each job to run on a machine (aka a *node*) (or
machines) on one of the partitions in the cluster. A *partition* is a
collection of machines with similar hardware.

