---
title: "Nicing jobs (setting the priority level of a job)"
---
When running jobs on the computer servers, or remotely on any SCF
machine, we ask that you nice the job to priority level 39 (nice value
19). In general this will happen by default on the compute servers. Jobs
that are not niced run at priority level 20. If you need to nice a job
yourself, here's how you do it.

For example, suppose one wanted to run R in the background with nice
value of 19 while using bash:

``` programlisting
% nice -n 19 R CMD BATCH --no-save code.R job.log &
```

For more information on the commands, see '**man nice**'.

If you need to nice a process while it is running, look up the PID as
described above and run:

``` programlisting
% renice +19 PID
```
