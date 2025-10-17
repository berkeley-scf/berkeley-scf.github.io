---
title: "Accessing Machines and Resources"
---
## Access methods

There are a variety of ways you can access the SCF computers.

- Using SSH: The most basic access to SCF computers is
  [via SSH](/access/ssh) to get to a [command line](/faqs/unix)
  on the machine of your choosing.
  - Example: to SSH to the SCF Linux server named arwen, you'll need to
    connect to arwen.berkeley.edu. From there you can see your home
    directory, connect to other SCF machines without using a password,
    and start jobs on the SCF Linux cluster. 
- Using your web browser: You can use our [JupyterHub](/access/jupyterhub)
  to access
  - Jupyter notebooks (IPython, R, and Julia notebooks as well as
    others)
  - Terminal sessions (similar to SSH command-line sessions, but from
    within your browser)
  - [RStudio](/software/rstudio)
  - [VS (Visual Studio) Code](/software/vscode) sessions
  - Linux desktop sessions
- Using [Remote Desktop](/access/remote-desktop) to get a graphical Linux desktop
- Running [VS (Visual Studio) Code](/software/vscode), an integrated development environment (IDE) on your
  personal machine, with VS Code connecting to an SCF machine to do
  remote development.
- You can [copy files to and from the SCF filesystem](/access/copying-files) in a variety of ways.

## What machines can I use?

You can browse the list of the SCF computers on our
[Grafana dashboards](/servers/monitoring) (SCF login required), including a
[general
overview](https://grafana.stat.berkeley.edu/d/overview/1-overview?orgId=1)
of most machines. Once you are on an SCF machine (e.g., you can
initially SSH to arwen.berkeley.edu), run \`sitehosts compute\` to list
machines you can remotely connect to and run jobs on.

## Running graphical programs from an SCF machine

You can remotely run GUI-based programs on the SCF machines, displaying
the GUI on your local machine. This works for all graphical programs on
our Linux machines and for X-windows based programs on our Macs but not
for Cocoa-based programs on the Macs.
[These instructions](/access/X11) will tell you how to view such programs on your own
Windows or Mac machine.

Note that our JupyterHub provides more responsive access to RStudio and
VS Code sessions, and [Remote Desktop](/access/remote-desktop) may be a better option for displaying GUIs.

## Other ways to access the SCF filesystem

Copying files using tools such as SFTP, SCP, rsync and Globus can be
tedious and requires you to have to deal with the possibility of
different file versions on your personal computer and on the SCF
filesystem.

- You can [mount your SCF home directory as a directory on your personal machine](/access/remote-files) (available
  for any of Windows, MacOS, or Linux).
- If you have a Mac or Linux desktop that you keep in your office in
  Evans, the SCF can maintain that computer for you as an
  SCF-administered machine. In this case, you will have direct access to
  your home directory, mounted via NFS, as for all SCF machines. Please
  [email us](mailto:manager@stat.berkeley.edu) if you are interested in
  this.
