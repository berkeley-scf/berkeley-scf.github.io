---
title: "RStudio"
---
SCF account holders can run RStudio through a web browser using our
JupyterHub.

- Visit https://jupyter.stat.berkeley.edu and use your SCF username and
  password to login. By default, your RStudio session will be spawned onto
  the first available standalone Linux server, however you may optionally
  start your session on a cluster node in case you need access to more
  processing power. You can also pass [Slurm job submission options](../servers/cluster/submitting.md) to your server and specify prologue
  commands that will run prior to your RStudio startup.
- Once your Jupyter session is active, click RStudio from the Jupyter
  Lab launcher. If you don't see the launcher, click `File > New
  Launcher`. All R packages installed on the system, as well as packages
  installed by users within their home directories should be available.

In contrast with running RStudio directly on SCF machines and forwarding
the display over X11, this should be much more responsive.
