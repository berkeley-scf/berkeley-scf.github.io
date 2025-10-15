---
title: "GPU Jobs"
---
 The SCF hosts a number of GPUs, available only by submitting a job
through our SLURM scheduling software. The GPUs are quite varied in
their hardware configurations (different generations of GPUS, with
different speeds and GPU memory). We have [documented the GPU
servers](/servers/gpu-servers) to guide you in selecting which GPU you may want
to use.

General job submission info  
To use the GPUs, you need to submit a job via our SLURM scheduling
software. In doing so, you need to specifically request that your job
use the GPU as follows using the 'gpus' flag (the older `--gres=gpu:1`
syntax also works):

```{code} shell
sbatch --partition=gpu --gpus=1 job.sh
```

Note that the partition to use will vary, as discussed in the other tabs
given in this set of tabbed information.

Once it starts your job will have exclusive access to the GPU and its
memory. If another user is using the GPU, your job will be queued until
the current job finishes.

Interactive jobs should use that same gpus flag with the usual srun
syntax for an interactive job.

```{code} shell
srun --pty --partition=gpu --gpus=1 /bin/bash
```

Given the heterogenity in the GPUs available, you may want to request use of a
specific GPU type. To do so, you can add the type to the 'gpus' flag, e.g.,
requesting an A100 GPU:

```{code} shell
sbatch --partition=jsteinhardt --gpus=A100:1 job.sh
```

If you don't care what partition a job runs on, you can specify multiple
partitions. In some cases one might want to specify a particular GPU
type as well. For example to request an A100 on any of the partitions
with GPUs:

```{code} shell
sbatch --partition=yss,jsteinhardt,yugroup --gpus=A100:1 job.sh
```

If you want to interactively logon to the GPU node to check on compute
or memory use of an sbatch job that uses the GPU, you can ssh directly
to the node (this is only possible if you have a running job on the
node). This will give you an shell running in the context of your
original job and you can then use nvidia-smi commands, e.g.,

```{code} shell
nvidia-smi -q -d UTILIZATION,MEMORY -l 1
```

There are many ways to [set up your code to use the GPU](/gpu).

In partitions with more than one GPU (which does not include the `gpu`
partition), you can request multiple GPUs by replacing the "1" above
with the number needed. Note that in most cases you would want all the
GPUs to be on the same machine, which you can guarantee either by using
`--gpus-per-node` in place of `--gpus` or by including the
`--nodes=1` flag in addition to the `--gpus` flag.

## Standard GPUs  

One GPU is generally available to all SCF users; it is hosted on the
server named *roo*. To submit a job that uses that GPU, you should
submit to the `gpu` partition. See the other items below for other GPUs
available on the SCF for which access is prioritized for members of
certain faculty groups.

The GPUs formerly hosted on scf-sm20 and scf-sm21 have been retired, so
there are no longer GPUs available through the `high` partition.

## High-performance GPUs  

Additional GPUs have been obtained by the Steinhardt, Song, and Yu lab
groups. Most of these GPUs have higher performance (either speed or GPU
memory) than our standard GPUs.

Members of the lab group have priority access to the GPUs of their
group. Other SCF users can submit jobs that use these GPUs but those
jobs will be preempted (killed) if higher-priority jobs need access to
the GPUs. Jobs are cancelled when preemption happens. If you want your
job to be automatically started again (i.e., started from the beginning)
when the node becomes available you can add the "--requeue" flag when
you submit via sbatch.

To submit jobs requesting access to these GPUs, you need to specify
either the *jsteinhardt*, *yss* or *yugroup* partitions. Here's an
example:

```{code} shell
sbatch --partition=jsteinhardt --gpus=1 job.sh
```

To use multiple GPUs for a job (only possible when using a server with
more than one GPU, namely scf-sm21, smaug, shadowfax, balrog, saruman,
sunstone, rainbowquartz, smokyquartz, treebeard, and morgoth), simply
change the number 1 after *--gpus=* to the number desired.

To request a specific GPU type, you can add that to the gpus flag, e.g.,
here requesting an A100:

```{code} shell
sbatch -p jsteinhardt --gpus=A100:1 job.sh
```

If you need more than one CPU, please request that using the
--cpus-per-task flag. The value you specify actually requests that
number of hardware threads, but with the caveat that a given job is
allocated all the threads on a given core to avoid contention between
jobs for a given physical core.

Furthermore, you can specify multiple partitions in your job submission,
which avoids the need to carefully determine which partition your job
might start most quickly in. For example, to request an A100 from all of
the A100s on the SCF:

```{code} shell
sbatch -p jsteinhardt,yugroup,yss --gpus=A100:1 job.sh
```

That said, preemption may be more likely in certain partitions depending
on how much activity there is at a given time and the number of GPUs in
the partitions.

Additionally, there are an another 40 A100 GPUs obtained by the
Steinhardt lab group at a remote cluster located in Washington state.
Details are given in the drop-down below.

## Steinhardt group  

The Steinhart group has priority access to the balrog, shadowfax, sunstone,
rainbowquartz, smokyquartz (8 GPUs each), saruman (8, eventually 10, GPUs), and
smaug (2 GPUs) GPU servers.

If you are in the group, simply submit jobs to the jsteinhardt partition
and you will automatically preempt jobs by users not in the group if
that is needed for your job to run.

Group members can also prioritize their jobs with respect to other jobs
by users in the Steinhardt group. By default jobs will run in the
`preemptive_high` Slurm QoS. Each user in the group can use at most 8
GPUs at a time in that default `preemptive_high` QoS. Additional jobs
will be queued. Group members can also submit to the `preemptive` QoS,
with no limit on the number of running jobs (apart from hardware
availability), using submission syntax like this:

```{code} shell
sbatch -p jsteinhardt -q preemptive --gpus=1 job.sh
```

Such jobs will still preempt jobs run by non-group members, but the jobs
can be preempted by jobs running in the `preemptive_high` QoS. 

In addition to the notes below, more details on optimal use of these
servers can be obtained from the guide prepared by Steinhardt group
members and the SCF and available by contacting one of us.

The smaug, saruman, and balrog GPUs have a lot of GPU memory and are
primarily intended for training very large models (e.g., ImageNet not
CIFAR10 or MNIST), but it is fine to use these GPUs for smaller problems
if shadowfax, sunstone, rainbowquartz, and smokyquartz are busy.

By default, if you do not specify a GPU type or a particular GPU server,
Slurm will try to run the job on shadowfax, sunstone, rainbowquartz, or
smokyquartz , unless they are busy. 

To request a specific GPU type, you can add that to the gpus flag, e.g.,
here requesting an A100:

```{code} shell
sbatch -p jsteinhardt --gpus=A100:1 job.sh
```

If you need more than one CPU, please request that using the
--cpus-per-task flag. The value you specify actually requests that
number of hardware threads, but with the caveat that a given job is
allocated all the threads on a given core to avoid contention between
jobs for a given physical core. So the default of "-c 1" allocates one
physical core and two hardware threads. Your CPU usage will be
restricted to the number of threads you request. 

As an example, since shadowfax has 48 CPUs (actually 48 threads and 24
physical cores as discussed above) and 8 GPUs, there are 6 CPUs per GPU.
You could request more than 6 CPUs per GPU for your job, but note that
if other group members do the same, it's possible that the total number
of CPUs may be fully used before all the GPUs are used. Similar
considerations hold for balrog (96 CPUs and 8 GPUs), saruman (104 CPUs
and 8 GPUs) and smaug (64 CPUs and 2 GPUs) as well as rainbowquartz,
smokyquartz and sunstone (all with 64 CPUs and 8 GPUs). That said,
that's probably a rather unlikely scenario.

To see what jobs are running on particular machines, so that you can
have a sense of when a job that requests a particular machine might
start: 

```{code} shell-session
    arwen:~> squeue -p jsteinhardt -o "%.9i %.20j %.12u %.2t %.11l %.11M %.11V %.5C %.8r %.6D %.20R %.13p %8q %b"
        JOBID                 NAME         USER ST  TIME_LIMIT        TIME SUBMIT_TIME  CPUS   REASON  NODES     NODELIST(REASON)      PRIORITY QOS      TRES_PER_NODE
      1077240                 bash nikhil_ghosh  R 28-00:00:00    12:51:48 2021-11-01T     1     None      1               balrog 0.00196710997 normal   gpu:1
      1077248              jupyter         awei  R 28-00:00:00     1:40:55 2021-11-01T     1     None      1               balrog 0.00092315604 preempti gpu:1
      1077121             train.sh andyzou_jiam  R 28-00:00:00  2-17:32:41 2021-10-29T    48     None      1               balrog 0.00027842330 preempti gpu:2
```

 

## Steinhardt group - remote cluster  

In addition to the GPU resources listed above, an additional 40 A100
GPUs (on 5 servers) are available at a remote cluster hosted in a
co-location facility in Washington state. These resources are operated
in similar fashion as the GPUs in the *jsteinhardt* partition, available
on a preemptible basis, with priority access for group members.

To request access, either by a group member or a non-group member,
please email consult@stat.berkeley.edu.

To connect to the remote cluster, ssh to `lambda.stat.berkeley.edu`.
Note that one cannot access the cluster via JupyterHub.

The configuration of these servers is the same as other SCF machines,
but the filesystem is distinct. Here are the key similarities and
differences from running jobs on the SCF (local) cluster.

- One can login with your SCF credentials.
- All software installed by the SCF is available and should be identical
  to that on the SCF (local) cluster.
- The job submission process is the same as on the SCF (local) cluster.
- The home directories (and other parts of the filesystem) on this
  remote cluster are **separate** from those on the SCF.
  - You will need to copy over any data to the filesystem of the remote
    cluster.
  - If you've installed software yourself on the SCF, you'll need to
    reinstall or copy over to the remote cluster.
- The partition on the remote cluster is named *lambda*. However you
  don't need to specify it when submitting a job.
- As on the SCF (local) cluster, jobs submitted to the default
  `preemptive_high` QoS can preempt jobs in the `preemptive` QoS,
  which can in turm preempt jobs in the `normal` partition. Individual
  group members can run at most three jobs in `preemptive_high` at a
  time. Non-group members only have access to the `normal` QoS.

## Yu group  
The Yu group has priority access to GPUs located on merry (1 GTX GPU),
morgoth (2 TITAN GPUs), and treebeard (1 A100 GPU) servers. If you are
in the group, simply submit jobs to the *yugroup* partition and you will
automatically preempt jobs by users not in the group if it is needed for
your job to run.

To request a specific GPU type, you can add that to the gpus flag, e.g.,
here requesting an A100:

```{code} shell
sbatch -p yugroup --gpus=A100:1 job.sh
```

If you need more than one CPU, please request that using the
--cpus-per-task flag, but note that merry only has four CPUs. The value
you specify actually requests that number of hardware threads, but with
the caveat that a given job is allocated all the threads on a given core
to avoid contention between jobs for a given physical core. 

Please contact SCF staff or group members for more details.

## Yun Song group  
The Song group has priority access to the GPUs located on luthien  (4
A100 GPUs) and beren (8 A100 GPUs). If you are in the group, simply
submit jobs to the *yss* partition and you will automatically preempt
jobs by users not in the group if it is needed for your job to run.

If you need more than one CPU, please request that using the
--cpus-per-task flag. The value you specify actually requests that
number of hardware threads, but with the caveat that a given job is
allocated all the threads on a given core to avoid contention between
jobs for a given physical core. 

Please contact SCF staff or group members for more details.

## Song Mei group  

The Mei group has priority access to the GPUs located on feanor (8 H200
GPUs). If you are in the group, simply submit jobs to the *songmei*
partition and you will automatically preempt jobs by users not in the
group if it is needed for your job to run.

If you need more than one CPU, please request that using the
--cpus-per-task flag. The value you specify actually requests that
number of hardware threads, but with the caveat that a given job is
allocated all the threads on a given core to avoid contention between
jobs for a given physical core. 

feanor has a very large, very fast (NVMe) disk with 6.6 TB of storage
available to group members via the `/data` directory. For jobs that do
a lot of I/O, it may speed things up to read and write from `/data`
rather than home or scratch directories. One can also put data into
`/tmp` or `/var/tmp` temporarily for fast I/O, though the amount of
space there is limited (80-100 GB total across all users).

Please contact SCF staff or group members for more details.

## Berkeley NLP group  

The Berkeley NLP group has priority access to the GPUs located on lorax
(8 H200 GPUs). If you are in the group, simply submit jobs to the
*berkeleynlp* partition and you will automatically preempt jobs by users
not in the group if it is needed for your job to run.

If you need more than one CPU, please request that using the
--cpus-per-task flag. The value you specify actually requests that
number of hardware threads, but with the caveat that a given job is
allocated all the threads on a given core to avoid contention between
jobs for a given physical core. 

lorax has a four very large, very fast (NVMe) 14TB disks available to
group members via the `/data` directory. For jobs that do a lot of
I/O, it may speed things up to read and write from `/data` rather than
home or scratch directories. One can also put data into `/tmp` or
`/var/tmp` temporarily for fast I/O, though the amount of space there
is limited (80-100 GB total across all users).

Please contact SCF staff or group members for more details.
