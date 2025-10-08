---
title: "Maintenance reminder: Slurm scheduler software update"
description: "We are performing a minor update to the SLURM scheduler."
thumbnail: ../assets/img/logo.svg
author: "Dan Ackerman"
date: "2025-03-03"
options:
    date-modified: "2025-03-04"
keywords:
  - Ubuntu
  - Maintenance
---

::: {.callout-note}
This is a reminder for the upgrade announcement originally sent on February 19.
:::

## Announcement

We are planning to do a minor software update on the SCF SLURM scheduler, which manages batch and JupyterHub jobs on the cluster, on Tuesday, March 4 at 1:00pm.

We anticipate that jobs that are currently running or queued on the cluster will experience no interruption. However, the ability to run or queue new jobs will be impacted for up to 60 minutes.

There is a very small possibility that currently-running jobs may be interrupted. We will be taking every possible precaution to ensure this does not happen, and we will send an announcement immediately if this does occur.

Please email trouble@stat.berkeley.edu if you have any questions or concerns regarding this announcement.

## Update

The SCF Slurm scheduler software update is now complete. The cluster is back online and accepting jobs. So far we have seen no indication that any of the already running jobs were impacted.

If you notice any new issues with Slurm, please contact trouble@stat.berkeley.edu with a description of the problem.
