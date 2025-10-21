---
title: "Policies for using the compute servers"
---
The following policies pertain to the stand-alone compute servers apart
from the Linux cluster.

Please observe the following policies:

- Access to the compute servers is restricted to individuals who are
  familiar with running batch jobs in a UNIX/Linux environment. If you
  are not familiar with running jobs in this way, you can contact
  consult@stat.berkeley.edu.
- Any compute server should have at most as many jobs (across all users)
  as CPUs on the machine. The number of CPUs on a machine can be seen on
  the [grafana dashboards](../servers/monitoring.md). If you see that all CPUs
  are busy, do not run/start a job on that server until resources become
  available.
- A user should not run so many simultaneous jobs on a compute server
  such that other users are prevented from starting jobs due to lack of
  resources. This policy is intended to ensure that CPU cycles and
  memory are used fairly and effectively. Please contact us if you need
  temporary or long term access to additional computing resources.

Users who do not follow these policies may be restricted from using the
compute servers.
