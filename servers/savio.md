---
title: "Savio"
---
[Berkeley Research Computing](http://research-it.berkeley.edu/) runs the
[Savio high performance
cluster](http://research-it.berkeley.edu/services/high-performance-computing)
in collaboration with staff from LBL. Department members can make use of
the cluster in a few ways:

## The Statistics Condo

We have two regular nodes that serve as a beachhead onto the larger system. The nodes are
freely available to all members of the department and there is no yearly
core-hour time limit. Note that they were purchased some years ago and are not fast. Please see the [Savio
webpage](http://research-it.berkeley.edu/services/high-performance-computing)
for instructions on getting an account and submitting jobs, and email
<consult@stat.berkeley.edu> if you have questions. When filling out the
[account request
form](http://research-it.berkeley.edu/services/high-performance-computing/getting-account#Getting-User-Accounts),
please specify the `co_stat` account.

Let us know if you are interested in expanding the size of the
departmental condo.

### Submitting Jobs

When submitting jobs to the condo nodes, specify the `co_stat` account
and the `savio2` partition. Note that the
`savio2` partition is scheduled on a per-node basis.

Example:

- `sbatch -A co_stat -p savio2 my-job.sh`

### Bursting

If you need more cycles, you can "burst" onto unused campus nodes as
[Low Priority
jobs](https://docs-research-it.berkeley.edu/services/high-performance-computing/user-guide/running-your-jobs/#low-priority).
The limitations are that when the system is busy, these jobs will be
queued and:

- yield to (be passed by) other jobs with higher priorities,

- get preempted (interrupted) by pending higher priority jobs.

  > Preempted jobs can choose whether the job should be simply killed,
  > or be automatically requeued after it's killed, at submission time.
  > Please note that, since preemption could happen at any time, it
  > would be very beneficial if your job is capable of
  > checkpointing/restarting by itself, when you choose to requeue the
  > job. Otherwise, you may need to verify data integrity manually
  > before you want to run the job again.

## Faculty Compute Allowance (FCA)

Each faculty member receives 300,000 "service units" (approximately
300,000 core cpu hours) per year to run jobs at the regular priority. If
you run a job for 10 hours on a 32-core machine, it will cost
approximately 320 core hours (cost varies depending on the exact type of
machine being used). If your job only utilizes 4 cores on the same
32-core node, it will still cost 320 core hours since your job has
exclusive access to the node, unless run in either the savio2_htc or
savio2_gpu pools, which are scheduled on a per-core basis.

Faculty members can [request an FCA](https://research-it.berkeley.edu/services/high-performance-computing/faculty-computing-allowance).
Once the FCA is created, researchers working with the faculty member
(including graduate and undergraduate students, postdocs, and colleagues
outside of Berkeley) can [request
accounts](https://research-it.berkeley.edu/services/high-performance-computing/faculty-computing-allowance)
that can make use of the FCA.

### Recharge

Once you go beyond the FCA you can purchase more time through recharge
at \$0.01/hour, e.g. \$2,000 for an additional 200,000 core hours.

## Storage

Your Savio account has access to a 50 GB home directory, 200 GB of
shared project space (shared amongst all department members), and a
large scratch area. You can purchase more if needed, including large
amounts of disk space through the [condo storage
program](https://research-it.berkeley.edu/services/high-performance-computing/brc-condo-storage-service-savio),
which costs about \$5000 per 112 TB, good for five years.
