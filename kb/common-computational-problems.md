---
title: "Common computational problems"
---
Here are some computational problems commonly encountered on the compute
servers and cluster and some solutions or workarounds.

- **Your cluster job won't start**
  - Your account may not have been given access to the cluster. Please
    email <trouble@stat.berkeley.edu>.
  - See also the next common problem listed just below.
- **Your cluster job is stuck at the top of the queue and other jobs
  start before it**
  - Jobs requesting multiple cores may not start because not enough
    cores become available at once. The Slurm scheduler will try to
    accumulate sufficient cores for your job to start, but other smaller
    jobs may start before yours if the scheduler determines that doing
    so will not delay the start of your job. Unfortunately, because we
    don't require time limits, Slurm has limited information with which
    to make this determination. So particularly for jobs requesting many
    cores, this may happen. 
- **R hangs when using profiling**
  - This is likely a conflict between's Rprof() and the threaded BLAS
    used by R for linear algebra. Solutions include (1) disabling
    threading ([see here for more details](./linear-algebra-using-blas.md)) and (2) not
    using profiling.
