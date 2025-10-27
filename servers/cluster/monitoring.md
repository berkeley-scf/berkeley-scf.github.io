---
title: Job Monitoring
---
You can monitor jobs on the cluster and usage of the different
partitions. We also provide several useful commands that give
commonly-needed information.

## How to Monitor Jobs  

The Slurm command squeue provides info on job status:

    arwen:~$ squeue
                 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
                   381      high   job.sh paciorek  R      25:28      1 scf-sm20
                   380      high   job.sh paciorek  R      25:37      1 scf-sm20

  
  
The following will tailor the output to include information on the
number of cores (the CPUs column below) being used as well as other
potentially useful information:

    arwen:~$ squeue -o "%.7i %.9P %.20j %.8u %.2t %l %.9M %.5C %.8r %.6D %R %p %q %b"
       JOBID PARTITION                 NAME     USER ST TIME_LIMIT      TIME  CPUS   REASON  NODES NODELIST(REASON) PRIORITY QOS GRES
         49       low                 bash paciorek  R 28-00:00:00   1:23:29     1     None      1 scf-sm00 0.00000017066486 normal (null)
         54       low              kbpew2v paciorek  R 28-00:00:00     11:01     1     None      1 scf-sm00 0.00000000488944 normal (null)

  
The 'ST' field indicates whether a job is running (R), failed (F), or
pending (PD). The latter occurs when there are not yet enough resources
on the system for your job to run.

Job output that would normally appear in your terminal session will be
sent to a file named slurm-{jobid}.out where {jobid} will be the
number of the job (visible via squeue as above).

If you would like to login to the node on which your job is running in
order to assess CPU or memory use, you have two options.

The easiest is that if (and only if) you have a job running on a node,
you can ssh directly to the node (from one of the SCF login servers).
The resulting ssh session will be associated with your existing job on
the node. One important caveat is that if your terminal on the login
server is through JupyterHub, you'll need to run `ssh -F none
{name_of_node}` rather than just `ssh {name_of_node}`. Note that
to ssh to the `feanor` and `lorax` GPU servers, you'll need to use
the full name, e.g. `feanor.stat.berkeley.edu`, and not just
`feanor`, unlike the other nodes.

Alternatively, you can run an interactive job within the context of your
existing job. First determine the job ID of your running job using
squeue and insert that in place of {jobid} in the following command:

    arwen:~$ srun --pty --jobid=<jobid> /bin/bash

In either case, you can then run top and other tools. 

To see a history of your jobs (within a time range), including reasons
they might have failed:

    sacct  --starttime=2021-04-01 --endtime=2021-04-30 \
    --format JobID,JobName,Partition,Account,AllocCPUS,State%30,ExitCode,Submit,Start,End,NodeList,MaxRSS

The MaxRSS column indicates memory usage, which can be very useful.

## How to Monitor Cluster Usage  

If you'd like to see how busy each node is (e.g., to choose what
partition to submit a job to), you can use `snodes` (which is an alias
for `-N -o "%.12N %.5a %.6t %C"`):

    arwen:~$ snodes
        NODELIST AVAIL  STATE CPUS(A/I/O/T)
          balrog    up    mix 50/46/0/96
           merry    up   idle 0/4/0/4
         morgoth    up    mix 1/11/0/12
        scf-sm00    up   idle 0/32/0/32
        scf-sm01    up   idle 0/32/0/32
        scf-sm02    up    mix 31/1/0/32
        scf-sm03    up   idle 0/32/0/32
        scf-sm10    up   idle 0/32/0/32
        scf-sm11    up   idle 0/32/0/32
        scf-sm12    up   idle 0/32/0/32
        scf-sm13    up   idle 0/32/0/32
        scf-sm20    up   idle 0/24/0/24
        scf-sm21    up   idle 0/24/0/24
        scf-sm22    up   idle 0/24/0/24
        scf-sm23    up   idle 0/24/0/24
       shadowfax    up   idle 0/48/0/48
           smaug    up   idle 0/64/0/64
       treebeard    up    mix 2/30/0/32

Here the A column indicates the number of cores used (i.e., active), I
indicates the number of inactive cores, and T the total number of cores
on the node.

To see the jobs running in a partition you can use `squeue` as
discussed in the previous drop-down, but specifying the partition with
`-p`, e.g., `-p high`.

To see GPU availability, you can use `sgpus`, which is an alias for
`sinfo` with some additional output processing.

    arwen:~$ sgpus
    NODELIST       PARTITION     GPUs      GPUs_USED               
    roo            gpu           TITAN:1   TITAN:1      
    smokyquartz    jsteinhardt   A4000:8   A4000:0    
    smaug          jsteinhardt   RTX8000:2 RTX8000:0  
    rainbowquartz  jsteinhardt   A5000:8   A5000:0    
    shadowfax      jsteinhardt   RTX2080:8 RTX2080:3
    sunstone       jsteinhardt   A4000:8   A4000:1      
    balrog         jsteinhardt   A100:8    A100:0     
    saruman        jsteinhardt   A100:8    A100:3   
    beren          yss           A100:8    A100:8     
    luthien        yss           A100:4    A100:4     
    morgoth        yugroup       TITAN:2   TITAN:0    
    merry          yugroup       GTX:1     GTX:1        
    treebeard      yugroup       A100:1    A100:1       

## Useful Slurm commands  

We've prepared a set of shortcut commands that wrap around `srun`,
`squeue`, `sinfo`, and `sacct` with some commonly-used options:

 - `slogin`: starts an interactive shell on a cluster node
 - `snodes`: prints the current usage of nodes on the cluster
 - `sjobs`: lists running jobs on the cluster
 - `shist`: provides information about completed (including failed) jobs
 - `sassoc`: gives information about user access to cluster partitions
 - `sgpus`: gives information about GPU availability.

For each of these commands, you can add the `-h` flag to see how to
use them. For example:

    gandalf:~$ slogin -h
    Usages:
    'slogin' to start an interactive job
    'slogin <jobid>' to start a shell on the node a job is running on
    'slogin <additional_arguments_to_run>' to start an interactive job with additional arguments to srun
