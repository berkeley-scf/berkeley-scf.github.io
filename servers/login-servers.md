---
title: "Login Servers"
---
We run a variety of stand-alone Linux servers that you can login to. All
machines provide access to your home directory (and other areas of the SCF
filesystem), allow you to submit jobs to our Linux cluster, and provide
the same suite of [SCF-maintained software](../software.md). You can also
run jobs on these machines (see below).

## Available machines

The stand-alone servers include arwen (16 cores), gandalf (8), ghan (4),
gollum (4), hermione (6), quidditch (8), radagast (8), shelob (8).

To connect to machines, please use [SSH](../access/ssh.md), [remote
desktop](../access/remote-desktop.md), or our
[JupyterHub](../access/jupyterhub.md) (which includes a Terminal
application). When ssh'ing, you would enter their fully qualified names,
e.g., `gandalf.berkeley.edu`.

Their names can be listed on any SCF machine by typing `sitehosts
compute`.

You can browse the list of the SCF computers on our [Grafana
dashboards](monitoring.md) (SCF login required), including a [general
overview](https://grafana.stat.berkeley.edu/d/overview/1-overview?orgId=1)
of most machines.

## Running jobs on the stand-alone servers

You can run jobs on the stand-alone servers, but in most cases you are
better off submitting jobs to the cluster. To run jobs on these machines,
you do not need to use Slurm. Also, please read [the
policies](../faqs/policies-using-compute-servers.md) on running jobs on
the compute servers. Of the machines, gollum, hermione, quidditch, and
shelob have the fastest CPUs, while gandalf and radagast have the most
memory (132 GB).
