---
title: VS Code Remote SSH
---

## Connect to an SCF login node


To connect to the SCF using VS Code,  you'll need to have installed the
[Remote Development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) (which includes the [Remote SSH extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) for your local VS Code.  Then to
connect to the SCF, click on the blue icon labelled `><` in the lower
left corner and choose "Host", providing one of the
[SCF login nodes](../servers/login-servers.md). You can then access your SCF files from within your local VS Code instance. 

[Remote Development using SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) describes this workflow in more detail.

## Connect to an SCF cluster node


  1.  On [one of the SCF login servers](../servers/login-servers.md), request a
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
