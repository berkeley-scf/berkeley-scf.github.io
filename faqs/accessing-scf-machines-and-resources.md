---
title: "Accessing SCF machines and resources"
---
## Access methods

There are a variety of ways you can access the SCF computers.

- Using SSH: The most basic access to SCF computers is
  <a href="/node/4180" data-entity-substitution="canonical"
  data-entity-type="node"
  data-entity-uuid="69b1aab6-045e-4b12-bd5d-918504c5f615">via SSH</a> to
  get to a
  <a href="/unix" data-entity-substitution="canonical"
  data-entity-type="node"
  data-entity-uuid="69b1aab6-045e-4b12-bd5d-918504c5f615">command line</a>
  on the machine of your choosing.
  - Example: to SSH to the SCF Linux server named arwen, you'll need to
    connect to arwen.berkeley.edu. From there you can see your home
    directory, connect to other SCF machines without using a password,
    and start jobs on the SCF Linux cluster. 
- Using your web browser: You can use our
  <a href="/node/5501" data-entity-substitution="canonical"
  data-entity-type="node"
  data-entity-uuid="4c053f30-dc8e-4af6-9069-ba72e526b73a">JupyterHub</a>
  to access
  - Jupyter notebooks (IPython, R, and Julia notebooks as well as
    others)
  - Terminal sessions (similar to SSH command-line sessions, but from
    within your browser)
  - <a href="/rstudio" data-entity-substitution="canonical"
    data-entity-type="node"
    data-entity-uuid="a624aada-5afe-4fa5-ac3b-12735bfe688c">RStudio</a> 
  - VS (Visual Studio) Code sessions
  - Linux desktop sessions
- Using <a href="/node/4633" data-entity-substitution="canonical"
  data-entity-type="node"
  data-entity-uuid="bee9562c-9845-4ce4-a22e-050b28b384fe">Remote
  Desktop</a> to get a graphical Linux desktop
- Running <a href="/node/8820" data-entity-substitution="canonical"
  data-entity-type="node"
  data-entity-uuid="248dae8f-2588-4324-8bf1-045e15193f12">VS (Visual
  Studio) Code</a>, an integrated development environment (IDE) on your
  personal machine, with VS Code connecting to an SCF machine to do
  remote development.
- You can <a href="/node/4151" data-entity-substitution="canonical"
  data-entity-type="node"
  data-entity-uuid="dcece840-f0b4-495d-8861-e78303320047">copy files to
  and from the SCF filesystem</a> in a variety of ways.

## What machines can I use?

You can browse the list of the SCF computers on our
<a href="/node/8218" data-entity-substitution="canonical"
data-entity-type="node"
data-entity-uuid="b7ea7503-2a95-4bfa-ac7b-547b2e4ffda7"
target="_top">Grafana dashboards</a> (SCF login required), including a
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
<a href="/node/3869" data-entity-substitution="canonical"
data-entity-type="node"
data-entity-uuid="1af80c69-68a3-4d7c-a989-a8b9794c61cd">These
instructions</a> will tell you how to view such programs on your own
Windows or Mac machine.

Note that our JupyterHub provides more responsive access to RStudio and
VS Code sessions, and
<a href="/node/4633" data-entity-substitution="canonical"
data-entity-type="node"
data-entity-uuid="bee9562c-9845-4ce4-a22e-050b28b384fe">Remote
Desktop</a> may be a better option for displaying GUIs.

## Other ways to access the SCF filesystem

Copying files using tools such as SFTP, SCP, rsync and Globus can be
tedious and requires you to have to deal with the possibility of
different file versions on your personal computer and on the SCF
filesystem.

- You can <a href="/node/4183" data-entity-substitution="canonical"
  data-entity-type="node"
  data-entity-uuid="380916b5-c828-4fc5-b7b8-0f260225b118">mount your SCF
  home directory as a directory on your personal machine</a> (available
  for any of Windows, MacOS, or Linux).
- If you have a Mac or Linux desktop that you keep in your office in
  Evans, the SCF can maintain that computer for you as an
  SCF-administered machine. In this case, you will have direct access to
  your home directory, mounted via NFS, as for all SCF machines. Please
  [email us](mailto:manager@stat.berkeley.edu) if you are interested in
  this.
