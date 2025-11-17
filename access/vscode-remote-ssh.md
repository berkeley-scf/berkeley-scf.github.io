---
title: VS Code Remote SSH
---

## Connect to an SCF login node


To connect to the SCF using VS Code,  you'll need to have installed the
[Remote Development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) (which includes the [Remote SSH extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)) for your local VS Code.  Then to
connect to the SCF, click on the green Remote "Quick Access" status bar button
labelled `><` in the lower left corner:

```{image} ../images/vscode-brackets.png
:alt: VS Code remote quick access button
```

and choose "Host", providing one of the [SCF login nodes](../servers/login-servers.md). You can then access your SCF files from within your local VS Code instance.

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
            # This must be the cluster node that `salloc` gave you.
            HostName scf-sm20.berkeley.edu
            # This must be the login server on which you ran `salloc`.
            ProxyJump gandalf.berkeley.edu
      :::

  1.  Now in VS Code on your personal machine, use the remote SSH
      extension to connect to the host `scf-slurm` by clicking on the
      blue icon labelled '\>\<' in the lower left corner and setting
      "Host" to `scf-slurm`.

### scf-run script

We have prepared a [shell
script](https://www.stat.berkeley.edu/~paciorek/share/scf-srun) that you could
run on your Mac or Linux machine that will carry out Steps 1 and 2 above for
you. You can run `scf-srun`, followed by your Slurm job syntax. For example:

:::{code} shell
scf-srun -c 4 -t 1:00:00
:::

::: {note}
The script will modify the configuration in your `~/.ssh` directory (slightly
modifying `~/.ssh/config` and adding a new file `~/.ssh/config.d/scf-slurm`).
:::

## Port forwarding (e.g., for web services such as dashboards)

VS Code can forward ports to your local machine. This is particularly helpful if software you are using has started a web service on the SCF machine you are accessing. One example is that the Python Dask.distributed package will start a dashboard on (by default) port 8787. You can view that service in the browser **on your own machine** as follows.

1. Determine the port being used by the web service (e.g., port 8787).
2. If not already open, open the Panel toolbar. You can do this via `Ctrl-backtick` or by opening a Terminal.
3. Click on the `PORTS` tab in the toolbar (it will be next to the `TERMINAL` tab).
4. Enter the port from #1 above as the port to forward. 
5. You should see a URL in the `Forwarded Address` column, which will be something like `localhost:8787`. Go to that URL in the browser on your machine (or click on the browser icon in that column). 

