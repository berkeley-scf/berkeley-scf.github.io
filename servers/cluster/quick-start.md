---
title: "Quick Start"
---

This is a quick-start guide, intended to show the basic commands to get
up and running on the cluster. Please see the other pages on the sidebar for
detailed documentation on the SCF cluster.

### Connecting to the SCF

First, [ssh to one of the SCF's standalone Linux servers](../../access/ssh.md).
For example from a terminal on your Mac or Linux machine:

```{code} shell
ssh gandalf.berkeley.edu
```


Or use Putty or MobaXTerm from your Windows machine.

You can also start a terminal on an SCF machine via the
[SCF JupyterHub](../../access/jupyterhub.md).

All jobs that you run on the cluster need to be submitted via the Slurm
scheduling software from one of our Linux servers. Slurm sends each job
to run on a machine (aka a *node*) (or machines) on one of the
partitions in the cluster. A *partition* is a collection of machines
with similar hardware.

### Checking Cluster Usage

Once are logged onto an SCF server, you can submit a job (assuming you
are in a group that has permission to use the cluster).

But first we'll check usage on the cluster to get a sense for how busy
each partition is:

```{code} shell-session
paciorek@gandalf:~> sinfo
PARTITION   AVAIL  TIMELIMIT  NODES  STATE NODELIST
low*           up 28-00:00:0      8    mix scf-sm[00-03,10-13]
high           up 7-00:00:00      2    mix scf-sm[22-23]
high           up 7-00:00:00      2   idle scf-sm[20-21]
lowmem         up 28-00:00:0      3  down$ boromir,pooh,toad
lowmem         up 28-00:00:0      1  maint gollum
lowmem         up 28-00:00:0      3   idle ghan,hermione,shelob
gpu            up 28-00:00:0      1   idle roo
jsteinhardt    up 28-00:00:0      6    mix balrog,rainbowquartz,saruman,shadowfax,smokyquartz,sunstone
jsteinhardt    up 28-00:00:0      1   idle smaug
yss            up 28-00:00:0      1   idle luthien
yugroup        up 28-00:00:0      1    mix treebeard
yugroup        up 28-00:00:0      2   idle merry,morgoth
```

Alternatively, we have a wrapper script *snodes* that shows usage on a
per-node basis:

```{code} shell-session
paciorek@gandalf:~> snodes
      NODELIST    PARTITION AVAIL  STATE CPUS(A/I/O/T)
        balrog  jsteinhardt    up    mix 50/46/0/96
<snip>
      scf-sm00         low*    up    mix 24/8/0/32
      scf-sm01         low*    up    mix 25/7/0/32
<snip>
      scf-sm02         low*    up    mix 24/8/0/32
      scf-sm03         low*    up    mix 28/4/0/32
      scf-sm10         low*    up    mix 30/2/0/32
      scf-sm11         low*    up    mix 28/4/0/32
      scf-sm12         low*    up    mix 24/8/0/32
<snip>
```

Here 'A' is for 'active' (i.e., in use), 'I' is for 'idle' (i.e., not in
use), and 'T' is for the 'total' number of CPUs (aka *cores*) on the
node. 

### Interactive Jobs with srun

We can start an interactive job with *srun*. This will start an
interactive session that can use a single core (aka CPU) on one of the
machines in our (default) low partition, which contains older machines.
You'll see the prompt change, indicating you're now running on one of
the cluster machines (a machine named *scf-sm10* in this case). 

```{code} shell-session
paciorek@gandalf:~> srun --pty bash
paciorek@scf-sm10:~> 
```

When you're done with your computation, make sure to exit out of the
interactive session

```{code} shell
exit
```

We can instead start a job on the newer machines in the *high*
partition:

```{code} shell
srun -p high --pty bash
```

And we can start a job that needs four cores on a single machine using
the *cpus-per-task* (`-c`) flag:

```{code} shell
srun -c 4 --pty bash
```

Interactive jobs might take a while to start if the machines are busy
with other users' jobs.

### Batch jobs with sbatch

To run a background job, you need to create a job script. Here's a
simple one that requests four cores and then runs a Python script (which
should be set up to take advantage of four cores via parallelization in
some fashion):

```{code} bash
#!/bin/bash
#SBATCH -c 4
python code.py > code.pyout
```

When you submit the job, it will show you the job id. Here we assume the
code above is in a file `job.sh`:

```{code} shell-session
paciorek@gandalf:~> sbatch job.sh
Submitted batch job 47139
```

### Monitoring

You can now check if the job is running:

```{code} shell-session
paciorek@gandalf:~> squeue -u $(whoami)
         JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
         41377      high jupyterh paciorek  R 3-21:55:42      1 scf-sm22
         47139       low   job.sh paciorek  R       0:46      1 scf-sm11
```

If you see `R` under the `ST` column, the job is running. If you see
`PD` it is waiting in the queue.

Or you can use our *sjobs* wrapper script to see a richer set of
information about the running job(s):

```{code} shell-session
paciorek@gandalf:~> sjobs -u $(whoami)
         JOBID         USER                 NAME    PARTITION QOS      ST         REASON  TIME_LIMIT        TIME SUBMIT_TIME  CPUS  NODES     NODELIST(REASON)  PRIORITY FEATURES TRES_PER_NODE
         41377     paciorek           jupyterhub         high normal    R           None  7-00:00:00  3-22:39:36 2022-11-17T     1      1             scf-sm22 0.0022660 (null) N/A
         47139     paciorek               job.sh          low normal    R           None 28-00:00:00       44:40 2022-11-21T     4      1             scf-sm11 0.0022545 (null) N/A
```

To better understand CPU and memory use by the job, you can connect to
the node the job is running on and then use commands like *top* and
*ps*:

```{code} shell-session
paciorek@gandalf:~> srun --jobid 47139 --pty bash
paciorek@scf-sm10:~> top    # use Ctrl-C to exit top
paciorek@scf-sm10:~> exit
```

To cancel a running job:

```{code} shell-session
paciorek@gandalf:~> scancel 47139
```

To check details of recently-completed jobs:

```{code} shell-session
paciorek@gandalf:~> sacct -S 2022-11-01  # jobs started since Nov 1, 2022
       JobID    JobName  Partition    Account  AllocCPUS      State ExitCode 
------------ ---------- ---------- ---------- ---------- ---------- -------- 
47138              bash        low       site          1  COMPLETED      0:0 
47138.extern     extern                  site          1  COMPLETED      0:0 
47138.0            bash                  site          1  COMPLETED      0:0 
47139            job.sh        low       site          4    RUNNING      0:0 
47139.batch       batch                  site          4    RUNNING      0:0 
47139.extern     extern                  site          4    RUNNING      0:0 
```

Alternatively, use our *shist* wrapper for a richer set of information.
Of particular note, the *MaxRSS* column shows the maximum memory use.

```{code} shell-session
paciorek@gandalf:~> shist -S 2022-10-01   # using our wrapper
     User        JobID    JobName  Partition    Account  AllocCPUS      State     MaxRSS ExitCode              Submit               Start                 End    Elapsed  Timelimit        NodeList 
--------- ------------ ---------- ---------- ---------- ---------- ---------- ---------- -------- ------------------- ------------------- ------------------- ---------- ---------- --------------- 
 paciorek 47138              bash        low       site          1  COMPLETED                 0:0 2022-11-21T15:10:19 2022-11-21T15:10:19 2022-11-21T15:10:22   00:02:03 28-00:00:+        scf-sm10 
          47138.extern     extern                  site          1  COMPLETED    902352K      0:0 2022-11-21T15:10:19 2022-11-21T15:10:19 2022-11-21T15:10:22   00:03:03                   scf-sm10 
          47138.0            bash                  site          1  COMPLETED       540K      0:0 2022-11-21T15:10:19 2022-11-21T15:10:19 2022-11-21T15:10:22   00:03:03                   scf-sm10 
 paciorek 47139            job.sh        low       site          4    RUNNING                 0:0 2022-11-21T15:51:04 2022-11-21T15:51:05             Unknown   00:04:37 28-00:00:+        scf-sm11 
          47139.batch       batch                  site          4    RUNNING                 0:0 2022-11-21T15:51:05 2022-11-21T15:51:05             Unknown   00:04:37                   scf-sm11 
          47139.extern     extern                  site          4    RUNNING                 0:0 2022-11-21T15:51:05 2022-11-21T15:51:05             Unknown   00:04:37                   scf-sm11 
```

### Parallelization

Use the `-c` flag if you need all the cores on a single node.

In some cases your code may be able to parallelize across the cores on
multiple nodes. In this case you should use the *--ntasks* (`-n`) flag.
Here's a job script in which we ask for 20 cores, which may be provided
by Slurm on one or more machines:

```{code} bash
#!/bin/bash
#SBATCH -n 20
python code.py > code.pyout
```

It only makes sense to use `-n` if your code is set up to be able to run
across multiple machines (if you're not sure, it's likely that it won't
run on multiple machines).

You can use both `-c` and `-n` in some cases, such as if you wanted to
run Python or R in parallel with multiple processes and have each
process use multiple cores for threaded linear algebra. Here's a job
script asking for three tasks (suitable for starting three worker
processes) and four cores per task (suitable for running four software
threads per process):

```{code} bash
#!/bin/bash
#SBATCH -n 3
#SBATCH -c 4
python code.py > code.pyout
```

Slurm sets various environment variables inside the context of your
running job that you can then use in your code so that your code adapts
to whatever resources you requested. This is much better than
hard-coding things like the number of workers that you want to use in
your parallelized code. 

Here are a few that can be useful:

```{code} shell-session
env | grep Slurm
<snip>
SLURM_CPUS_PER_TASK=4
SLURM_NTASKS=3
SLURM_NNODES=2
SLURM_NODELIST=scf-sm[11-12]
<snip>
```

The job is using cores on two nodes, with four CPUs for each of three
tasks. Note that only code that is set up to run across multiple
machines will work in this situation.
