---
title: "VS Code"
---

Follow these instructions to use VS Code on the SCF. You can either run
VS Code on a login node or on one of the compute nodes in the SCF
cluster. In either case VS Code will access files (including your home
directory) on the SCF.

To connect to the SCF using VS Code,  you'll need to have installed the
'Remote Development' extension pack on your local VS Code.  Then to
connect to the SCF, click on the blue icon labelled `\>\<` in the lower
left corner and choose "Host", providing one of the
[SCF login nodes](/servers/login-servers).

If you want to access the cluster nodes (including GPUs available on
some cluster nodes), you'll need to do one of the following.

- Use VS Code through [JupyterHub](/access/jupyterhub),
  selecting the cluster partition when you start your Jupyter server.
  This uses `code-server` to run VS Code in a web browser. A downside
  is that the extensions available are not exactly as with VS Code
  itself. In particular GitHub Copilot may not work as well.
- You can use some ssh tricks to run VS Code on a cluster node with
  these steps:
  1.  On [one of the SCF login servers](/servers/login-servers), request a
      Slurm "allocation" using with `salloc`, e.g., `salloc -c 4 -t 1:00:00`
      for one hour on four cores on the high (default) partition. The flags are
      the same flags one uses with `srun` and `sbatch`.

  1.  Modify your  `~/.ssh/config` file on your local computer to
      include this new stanza:

      :::{code} ini
      :caption: ProxyJump ssh configuration
          Host scf-slurm
            HostName scf-sm20.berkeley.edu # This must be the cluster node that `salloc` gave you.
            ProxyJump gandalf.berkeley.edu # This must be the login server on which you ran `salloc`.
      :::

  1.  Now in VS Code on your personal machine, use the remote SSH
      extension to connect to the host `scf-slurm` by clicking on the
      blue icon labelled '\>\<' in the lower left corner and setting
      "Host" to `scf-slurm`.
- We have prepared a [shell
  script](https://www.stat.berkeley.edu/~paciorek/share/scf-srun) that
  you could run on your Mac or Linux machine that will carry out Steps 1
  and 2 above for you. You can run it like this: `scf-srun \<insert
  Slurm job syntax here\>`, e.g., `scf-srun -c 4 -t 1:00:00`. Note
  that the script will modify the configuration in your ~/.ssh directory
  (slightly modifying `~/.ssh/config` and adding a new file
  `~/.ssh/config.d/scf-slurm`.
