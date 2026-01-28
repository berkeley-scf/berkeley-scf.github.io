---
title: "GPU Jobs"
---

The SCF hosts a number of GPUs, available only by submitting a job
through our Slurm scheduling software. The GPUs are quite varied in
their hardware configurations (different generations of GPUS, with
different speeds and GPU memory). We have [documented the GPU
servers](../gpu-servers#research-group-gpus) to guide you in selecting which GPU you may want
to use. One GPU is available to all SCF users on an equal basis and 
many other GPUs purchased by research groups that are available to group members at 
regular priority and to other SCF users at lower (preemptible) priority. 

## Preemption

Members of each research  group have priority access to the GPUs of their group.
Other SCF users can submit jobs that use these GPUs, but those
jobs will be preempted (killed) if higher-priority jobs need access to
the GPUs. Jobs are cancelled when preemption happens, but they will be
requeued and should
restart when the needed resources become available. If you see that your
job is not being requeued, please contact us.

## General GPU job submission info

### Basic GPU requests

To use the GPUs, you need to submit a job via our Slurm scheduling
software. In doing so, you need to specifically request that your job
use the GPU as follows using the `--gpus` flag (the older `--gres=gpu:1`
syntax also works):

```{code} shell
sbatch --partition=<partition> --gpus=1 job.sh
```

where you'll need to replace `<partition>` with either `gpu` (
for access to the single old GPU
we have available for equal use by all SCF users) or [one of these research group partitions](../gpu-servers.md#research-group-gpus),
as discussed in more detail below.

Once it starts your job will have exclusive access to the GPU and its
memory. If another user is using the GPU, your job will be queued until
the current job finishes.

[Interactive jobs](./submitting.md#interactive-jobs) should use that same `--gpus` flag with the usual `srun`
syntax for an interactive job.

```{code} shell
srun --pty --partition=<partition> --gpus=1 /bin/bash
```


### Requesting multiple GPUs

In partitions with more than one GPU (see next section; this does not include the `gpu`
partition), you can request multiple GPUs by replacing the "1" after `--gpus=`
with the number needed. 

Note that in most cases you would want all the
GPUs to be on the same machine, which you can guarantee either by using
`--gpus-per-node` in place of `--gpus` or by including the
`--nodes=1` flag in addition to the `--gpus` flag.

### GPU partitions

You will need to specify the partition to use for your job, using the `-p` or `--partition` flag, and
choosing a partition that contains servers with GPUs.

For members of specific research groups, this will generally be the [partition
associated with the group](../gpu-servers.md#research-group-gpus).

If you are submitting a job that could be preempted, you may
want to first check on overall GPU usage in each partition when deciding which
partition to submit to.

We have a helper script, `sgpus`, that will give overall GPU usage:

```{code} shell-session
paciorek@gandalf:~> sgpus
NODELIST       PARTITION     GPUs      GPUs_USED               
lorax          berkeleynlp   H200:8    H200:6 
horton         berkeleynlp   H200:8    H200:0
roo            gpu           TITAN:1   TITAN:1      
sunstone       jsteinhardt   A4000:8   A4000:0    
smokyquartz    jsteinhardt   A4000:8   A4000:5  
shadowfax      jsteinhardt   RTX2080:8 RTX2080:1    
smaug          jsteinhardt   RTX8000:2 RTX8000:0  
saruman        jsteinhardt   A100:10   A100:7 
balrog         jsteinhardt   A100:8    A100:0     
rainbowquartz  jsteinhardt   A5000:8   A5000:0    
feanor         songmei       H200:8    H200:1       
luthien        yss           A100:4    A100:4     
beren          yss           A100:8    A100:2     
morgoth        yugroup       TITAN:2   TITAN:0    
merry          yugroup       GTX:1     GTX:1        
treebeard      yugroup       A100:1    A100:1       
```

If you don't care what partition a job runs on, you can specify multiple
partitions. In some cases one might want to specify a particular GPU
type as well. For example to request an A100 on any of the partitions
with A100 GPUs:

```{code} shell
sbatch --partition=yss,jsteinhardt,yugroup --gpus=A100:1 job.sh
```


(tiered-qos)=
### Tiered priority and preemption (QoS)

In some research group partitions, there are multiple tiers of priority access
available through the `preemptive_high` and `preemptive` Slurm QoS. 

In some research groups, all group members have access to both QoS 
and in other groups some group members can only use `preemptive`.
By default, jobs will run under the highest priority QoS available
to a user.

Jobs submitted to `preemptive_high` and `preemptive` can preempt
jobs running by non-group members if there are not enough resources to run
the submitted job. In turn, jobs submitted to `preemptive_high` can preempt jobs running
in `preemptive`. 

Users of  `preemptive_high` can use at most 8
GPUs at a time in the `preemptive_high` QoS. Additional jobs
will be queued. Such users can also submit to the `preemptive` QoS,
(which has  no limit on the number of GPUs used, apart from hardware
availability), using submission syntax like this:

```{code} shell
sbatch -p jsteinhardt -q preemptive --gpus=1 job.sh
```


### CPUs per task

If you need more than one CPU for your GPU-using job, please request that using the
`--cpus-per-task` flag. The value you specify actually requests that
number of hardware threads, but with the caveat that a given job is
allocated all the threads on a given core to avoid contention between
jobs for a given physical core. So the default of `-c 1` allocates one
physical core and two hardware threads. Your CPU usage will be
restricted to the number of threads you request. 

As an example, if a machine had 48 CPUs (actually 48 threads and 24
physical cores as discussed above) and 8 GPUs, there are 6 CPUs per GPU.
You could request more than 6 CPUs per GPU for your job, but note that
if other group members do the same, it's possible that the total number
of CPUs may be fully used before all the GPUs are used.


### Requesting a specific GPU type

Given the heterogenity in the GPUs available on some partitions (`jsteinhardt` and `yugroup`), 
or if you are submitting a job to multiple partitions,
you may want to request use of a specific GPU type. To do so, you can add the type to the `--gpus` flag, e.g.,
requesting an A100 GPU:

```{code} shell
sbatch --partition=jsteinhardt --gpus=A100:1 job.sh
```

### Monitoring use

If you want to interactively logon to the GPU node to check on compute
or memory use of an sbatch job that uses the GPU, you can ssh directly
to the node (this is only possible if you have a running job on the
node). This will give you an shell running in the context of your
original job.

Some tools that you can use to monitor GPU use from the shell include `nvidia-smi` commands, e.g.,

```{code} shell
nvidia-smi -q -d UTILIZATION,MEMORY -l 1
```

and the [`gpustat` utility](https://github.com/wookayin/gpustat), available for installation via Python's `pip` installer.

### Software

There are many ways to [set up your code to use the GPU](../../software/gpu-software.md).

(steinhardt-remote-cluster)=
### Steinhardt group remote cluster

In addition to the GPU resources listed above, an additional 40 A100
GPUs (on 5 servers) are available at a remote cluster hosted in a
co-location facility in Washington state. These resources are operated
in similar fashion as the GPUs in the `jsteinhardt` partition, available
on a preemptible basis, with priority access for group members.

To request access, either by a group member or a non-group member,
please email consult@stat.berkeley.edu.

To connect to the remote cluster, ssh to `lambda.stat.berkeley.edu`.
Note that one cannot access the cluster via JupyterHub.

The configuration of these servers is the same as other SCF machines,
but the filesystem is distinct. Here are the key similarities and
differences from running jobs on the SCF (local) cluster.

- One can login with your SCF credentials.
- All software installed by the SCF is available and should be similar
  to that on the SCF (local) cluster. Software updates trail those on the SCF.
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
  group members can run at most 8 GPUs in `preemptive_high` at a
  time. Non-group members only have access to the `normal` QoS.


## Research group details

This section provides some details of usage for particular research groups.

### Steinhardt Group

In addition to the GPUs available in the `jsteinhardt` partition,
group members have priority access to the group's [co-located remote cluster](#steinhardt-remote-cluster).

Group members have access to [tiered preemption](#tiered-qos).

In addition to the notes below, more details on optimal use of these
servers can be obtained from the guide prepared by Steinhardt group
members and the SCF and available by contacting one of us.

The `smaug`, `saruman`, and `balrog` GPUs have a lot of GPU memory and are
primarily intended for training very large models (e.g., ImageNet not
CIFAR10 or MNIST), but it is fine to use these GPUs for smaller problems
if `shadowfax`, `sunstone`, `rainbowquartz`, and `smokyquartz` are busy.

By default, if you do not specify a GPU type or a particular GPU server,
Slurm will try to run the job on `shadowfax`, `sunstone`, `rainbowquartz`, or
`smokyquartz`, unless they are busy. 

### Song Mei Group

`feanor` has a very large, very fast (NVMe) disk with 6.6 TB of storage
available to group members via the `/data` directory. For jobs that do
a lot of I/O, it may speed things up to read and write from `/data`
rather than home or scratch directories. One can also put data into
`/tmp` or `/var/tmp` temporarily for fast I/O, though the amount of
space there is limited (less than 1 TB total across all users).

Some group members have access to [tiered preemption](#tiered-qos).

### Berkeley NLP Group

`lorax` and `horton` have four very large and fast 14TB NVMe disks
available to group members via the `/data` directory. For jobs that do a
lot of I/O, it may speed things up to read and write from `/data` rather
than home or scratch directories. One can also put data into `/tmp` or
`/var/tmp` temporarily for fast I/O, though the amount of space there is
limited (less than 1 TB total across all users).

Some group members have access to [tiered preemption](#tiered-qos).


