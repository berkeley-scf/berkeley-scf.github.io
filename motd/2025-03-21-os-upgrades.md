---
title: "Downtime notice: Cluster node OS upgrade"
description: "We are upgrading the operating system on most systems."
thumbnail: ../images/logo.svg
author: "Dan Ackerman"
date: "2025-03-21"
keywords:
  - Ubuntu
  - Maintenance
---

We will be performing operating system upgrades on all of our compute servers during the upcoming spring break. The upgrades will occur in batches from Monday, March 24, through Thursday, March 27, starting each morning at approximately 8:30am. We will begin with the least active nodes.

Your home and scratch directories will not be affected, however /tmp and /var/tmp on each machine will be wiped. /data partitions, which exist on a small number of systems, will not be impacted.

We will place reservations on the systems to be upgraded about 72 hours in advance. If you currently have or plan to start jobs that you expect to run into next week, please ensure that your code can resume from where it left off if interrupted. For jobs starting before the upgrade, we recommend setting a time limit of no more than 72 hours.

Self-Installed Packages
If you have installed your own R packages, you will need to reinstall them after the upgrade or request that we install them system-wide. Check your packages in ~/R/x86_64-pc-linux-gnu-library in versioned subdirectories. Although these directories will remain after the upgrade, R on the new system will look in ~/R/x86_64-pc-linux-gnu-library-ubuntu-24.04/. This is necessary because compiled R packages link against system libraries from the old OS, which may not exist or have different versions on the new OS. To request system-wide installation, please contact us at consult@stat.berkeley.edu.

Python packages installed via conda are not affected. If you have installed Python packages using pip and the setup involves compiling shared objects, these libraries will need to be reinstalled. Compiling shared objects typically means that the package installation involves building components that link to system libraries. If you're unsure which packages need reinstallation, you can check the package documentation or contact us for assistance.
