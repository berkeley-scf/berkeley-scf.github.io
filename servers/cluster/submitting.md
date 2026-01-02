---
title: Basic Job Submission
---
This page describes how to submit jobs to the cluster.

## Slurm configuration and job restrictions

The cluster has multiple partitions, corresponding to groups of nodes.
The different partitions have different hardware and job restrictions as
discussed here:

:::{table} Partition Restrictions
:label: partition-restrictions
| Partition      | Max cores<br>per user (running) | Max cores<br>per job | Max CPU memory<br>per job | Time limit | Preembtible |
|----------------|----------------------------|-------------------|----------------------|------------|-------------|
| high (default)     | 96                     | 24     | 128 GB           | 7 days     | No          |
| low                | 256                    | 32     | 256 GB           | 28 days    | No          |
| gpu[^perf]         | 8                      | 8      | 6 GB             | 28 days    | No          |
| berkeleynlp[^perf] | 384                    | 128    | 1.5 TB | 28 days[^bnlp-i]     | Yes[^pe] |
| epurdom[^perf]     | 256                    | 128    | 528 GB           | 28 days    | Yes[^pe]    |
| jsteinhardt[^perf] | varied                 | varied | varied[^js-mem]  | 28 days    | Yes[^pe]    |
| yugroup[^perf]     | varied                 | varied | varied           | 28 days    | Yes[^pe]    |
| yss[^perf]         | 224                    | varied | 528 GB           | 28 days    | Yes[^pe]    |
:::

:::{note} About cores per job
If you use software that can parallelize across multiple nodes (e.g., R packages that use MPI or the future package, Python's Dask or IPython Parallel, MATLAB, MPI), you can run individual jobs across more than one node. See [](#parallel-jobs).
:::

[^perf]: See [](#high-performance-partitions) or [GPU Jobs](gpus.md).

[^pe]: Preemptible when run at normal priority, as occurs for non-group members.

[^bnlp-i]: The berkeleynlp partition has a 24 hour time limit on interactive jobs, including those launched on JupyterHub.

[^js-mem]: Max CPU memory:
    - 288 GB (smaug)
    - 792 GB (balrog, rainbowquartz)
    - 1 TB (saruman)
    - 128 GB (various)
## Single-core jobs

Prepare a shell script containing the instructions you would like the
system to execute. 

The instructions here are for the simple case of submitting a job
without any parallelization; i.e., a job using a single core (CPU). When
submitted using the instructions in this section, such jobs will have
access to only a single core at a time. We also have [extensive
instructions](parallel.md) for submitting parallelized jobs and
automating the submission of multiple jobs.

For example a simple script to run an R program called 'simulate.R'
would contain these lines:

:::{code} bash
#!/bin/bash
R CMD BATCH --no-save simulate.R simulate.out
:::

Once logged onto a submit host, navigate to a directory within your home
or scratch directory (i.e., make sure your working directory is not in
`/tmp` or `/var/tmp`) and use the sbatch command with the name of the shell
script (assumed to be `job.sh` here) to enter a job into the queue:

:::{code} shell-session
$ sbatch job.sh
Submitted batch job 380
:::

Here the job and assigned job ID 380. Results that would normally be
printed to the screen via standard output and standard error will be
written to a file called slurm-380.out.

If you have many single-core jobs to run, there are [various ways to
automate submitting such jobs](/servers/cluster/parallel#automating-submission).

Note that Slurm is configured such that single-core jobs will have
access to a single physical core (including both hyperthreads on our new
machines), so there won't be any contention between the two threads on a
physical core. However, if you have many single-core jobs to run on the
high, jsteinhardt, or yugroup partitions; you might improve your
throughput by modifying your workflow so that you can one run job per
hyperthread rather than one job per physical core. You could do this by
taking advantage of [parallelization strategies in R, Python, or MATLAB
to distribute tasks across workers in a single
job](https://computing.stat.berkeley.edu/tutorial-parallelization), or you
could use [GNU parallel](/servers/cluster/parallel#gnu-parallel)
or [srun within
sbatch](/servers/cluster/parallel#srun).

Slurm provides a number of additional flags to control what happens; you
can see the man page for sbatch for help with these. Here are some
examples, placed in the job script file, where we name the job, ask for
email updates and name the output and error files:

:::{code} bash
#!/bin/bash
#SBATCH --job-name=myAnalysisName
#SBATCH --mail-type=ALL                       
#SBATCH --mail-user=blah@berkeley.edu
#SBATCH -o myAnalysisName.out #File to which standard out will be written
#SBATCH -e myAnalysisName.err #File to which standard err will be written
R CMD BATCH --no-save simulate.R simulate.Rout
:::
 
(parallel-jobs)=
## Parallel Jobs

One can use Slurm to [submit parallel code](/servers/cluster/parallel)
of a variety of types.

(high-performance-partitions)=
## High performance (CPU) partitions

### High partition vs. low partition

Both of these partitions have quite old machines.

While the machines in the high partition are faster than the machines in the low
partition, these machines are also quite old and will generally be slower
than the machines in the partitions for specific lab groups and (on a
per-core basis) than your laptop, particularly Apple Silicon Mac
laptops.

### epurdom partition

The `epurdom` partition has two nodes (`frodo` and `samwise`) with  recent CPUs
(128-core AMD EPYC) and 528 GB memory each.

You can request use of these nodes as follows:

:::{code} shell-session
arwen:~$ sbatch -p epurdom job.sh
Submitted batch job 380
:::


Purdom group members have priority access to these nodes. If you are in the
group, simply submit jobs to the epurdom partition and you will automatically
preempt jobs by users not in the group if it is needed for your job to run.

Non-group members can submit jobs as well, but jobs may be preempted (killed)
without warning if group member jobs need the resources being used.
Pre-emptible jobs are requeued when preemption happens and should
restart when the needed resources become available. If you see that your
job is not being requeued, please contact us.

If you need more than one CPU, please request that using the
`--cpus-per-task` flag. The value you specify actually requests that
number of hardware threads, but with the caveat that a given job is
allocated all the threads on a given core to avoid contention between
jobs for a given physical core.


### jsteinhardt partition

While the various nodes of the `jsteinhardt` partition are primarily intended
for use for their GPUs, many of them have newer CPUs, a lot of memory, and very
fast disk I/O to `/tmp` and `/var/tmp` using an NVMe SSD.

Non-group members can submit jobs as well, but jobs may be preempted (killed)
without warning if group member jobs need the resources being used.
Pre-emptible jobs are requeued when preemption happens and should
restart when the needed resources become available. If you see that your
job is not being requeued, please contact us.

For example to request use of one of these nodes, which are labelled as
`manycore` nodes:

:::{code} shell-session
arwen:~$ sbatch -p jsteinhardt -C manycore job.sh
Submitted batch job 380
:::

You can request specific resources as follows:

- `-C fasttmp` for access to fast disk I/O in `/tmp` and `/var/tmp`,
- `-C manycore` for access to many (64 or more) cores,
- `-C mem256g` for up to 256 GB CPU memory,
- `-C mem768g` for up to 768 GB CPU memory, and
- `-C mem1024g` for up to 1024 GB CPU memory.

Also note that if you need more disk space on the NVMe SSD on some but
not all of these nodes, we may be able to make available space on a much
larger NVMe SSD if you request it.

## Job not starting

The cluster is managed using the Slurm scheduling software. We configure
Slurm to try to balance the needs of the various cluster users.

Often there may be enough available CPU cores (aka 'resources') on the
partition, and your job will start immediately after you submit it.

However, there are various reasons a job may take a while to start. Here
are some details of how the scheduler works.

- If there aren't enough resources in a given partition to run a job
  when it is submitted, it goes into the queue. The queue is sorted
  based how much CPU time you've used over the past few weeks, using the
  'fair share' policy described below. Your jobs will be moved to a
  position in the queue below the jobs of users who have used less CPU
  time in recent weeks. This happens dynamically, so another user can
  submit a job well after you have submitted your job, and that other
  user's job can be placed higher in the queue at that time and start
  sooner than your job. If this were not the case, imagine the situation
  of a user sending 100s of big jobs to the system. They get into the
  queue and everyone submitting after that has to wait for a long time
  while those jobs are run, if other jobs can't get moved above those
  jobs in the queue.
- When a job at the top of the queue needs multiple CPU cores (or in
  some cases an entire node), then jobs submitted to that same partition
  that are lower in the queue will not start even if there are enough
  CPU cores available for those lower priority jobs. That's because the
  scheduler is trying to accumulate resources for the higher priority
  job(s) and guarantee that the higher priority jobs' start times
  wouldn't be pushed back by running the lower priority jobs.
- In some cases, if the scheduler has enough information about how long
  jobs will run, it will run lower-priority jobs on available resources
  when it can do so without affecting when a higher priority job would
  start. This is called backfill. It can work well on some systems but
  on the SCF and EML it doesn't work all that well because we don't
  require that users specify their jobs' time limits carefully. We made
  that tradeoff to make the cluster more user-friendly at the expense of
  optimizing throughput.

The 'fair share' policy governs the order of jobs that are waiting in
the queue for resources to become available. In particular, if two users
each have a job sitting in a queue, the job that will start first will
be that of the user who has made less use of the cluster recently
(measured in terms of CPU time). The measurement of CPU time downweights
usage over time, with a half-life of one month, so a job that ran a
month ago will count half as much as a job that ran yesterday. Apart
from this prioritization based on recent use, all users are treated
equally.

## Node maintenance and reservations

Periodically, we perform maintenance on cluster nodes, such as OS upgrades
or hardware repairs. During these times, we place a reservation on the
affected nodes in the SLURM scheduler.

When a reservation is active, you can still submit jobs as usual. The
scheduler will automatically choose an available node for your job in the
partition you specify. However, if you want to run the job on a node (via
the `-w` flag) with a reservation, and you want it to start before the
maintenance window, you must specify a time limit that ensures your job
will complete before the maintenance begins.

For example, if maintenance is scheduled in 48 hours:

:::{code} shell-session
$ sbatch -t 48:00:00 myjob.sh   # 48 hours
$ sbatch -t 1-6 myjobs.sh       # 1 day, 6 hours
:::

The scheduler will launch your job on nodes that can complete it in time,
or on nodes without reservations. You can check the status of nodes using
`sinfo`. During maintenance, affected nodes will have a status of `maint`.

## How to kill a job
First, find the job-id of the job, by typing squeue at the command line
of a submit host (see How to Monitor Jobs).

Then use scancel to delete the job (with id 380 in this case):

```{code} shell
scancel 380
```

## Interactive jobs

You can work interactively on a node from the Linux shell command line
by starting a job in the interactive queue.

The syntax for requesting an interactive (bash) shell session is:

```{code} shell
srun --pty /bin/bash
```

This will start a shell on one of the four nodes. You can then act as
you would on any SCF Linux compute server. For example, you might use
top to assess the status of one of your non-interactive (i.e., batch)
cluster jobs. Or you might test some code before running it as a batch
job. You can also transfer files to the local disk of the cluster node.

By default, to limit forgotten sessions, the time limit for interactive
jobs is set to 1 day (24 hours). If you need less or more time (up to
the [maximum time limits](#partition-restrictions)), you can
use the `-t` (or `--time`) flag. For example to run for two days:

```{code} shell
srun -t 2-00:00:00 --pty /bin/bash
```

If you want to run a program that involves a graphical interface
(requiring an X11 window), you need to add --x11 to your srun command.
So you could directly run MATLAB, e.g., as follows:

```{code} shell
srun --pty --x11 matlab
```

or you could add the `--x11` flag when requesting an interactive shell
session and then subsequently start a program that has a graphical
interface.

To run an interactive session in which you would like to use multiple
cores, do the following (here we request 4 cores for our use):

```{code} shell
srun --pty --cpus-per-task 4 /bin/bash
```

Note that `-c` is a shorthand for `--cpus-per-task`.

To transfer files to the local disk of a specific node, you need to
request that your interactive session be started on the node of interest
(in this case scf-sm20):

```{code} shell
srun --pty -p high -w scf-sm20 /bin/bash
```

Note that if that specific node has all its cores in use by other users,
you will need to wait until resources become available on that node
before your interactive session will start.

Finally, you can request multiple cores using `-c`, as with batch jobs. As
with batch jobs, you can change `OMP_NUM_THREADS` from its default of one,
provided you make sure that that the total number of cores used (number
of processes your code starts multiplied by threads per process) does
not exceed the number of cores you request.
