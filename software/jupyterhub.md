---
title: "JupyterHub"
---
We have deployed JupyterHub at <https://jupyter.stat.berkeley.edu> so
that you may remotely run the following on SCF machines through your
browser:

- [Jupyter notebooks](http://jupyter.org/) (including Python, R, Julia,
  and MATLAB notebooks).
- Terminals
- RStudio
- VS Code
- Linux desktops

Any of those can use the standalone/login SCF servers or nodes on the
SCF Linux cluster, including nodes with GPUs.

By default, your server will be spawned onto the first available
standalone Linux machine, however you may optionally start your server
on a cluster node in case you need access to more processing power. You
can also pass [SBATCH options](/servers/cluster) to your
server, and specify prologue commands that will run prior to your server
startup. Please [let us
know](mailto:consult@stat.berkeley.edu?subject=JupyterHub%20feedback) if
you have any difficulties or if you need us to add features to it.

## Long Running Code

Interactive programs like Jupyter Lab, RStudio, or VS Code might not
respond well if you launch long running jobs interactively from their
UIs, and then close your device, reconnect to another network, and
re-open your browser. They will often work just fine, but there can be
problems. If you need to run code that you expect to take a long time to
complete, it would be best to run it as a batch job
[on the cluster](/servers/cluster/submitting). You can submit the job from your Jupyter session or by
connecting with SSH to a login node.

## Stopping Your Server

To stop your server (and free up resources for other users), please
visit the [control panel](https://jupyter.stat.berkeley.edu/hub/home) by
selecting File \> Hub Control Panel from within Jupyter Lab. Then click
"Stop My Server". Note that selecting "Logout" does not free up
resources for other users as it keeps your server running.

## Named Servers

It is possible to start up multiple servers on the cluster, analogously
to how you might start up more than one job on the cluster. This is
useful if you want to provide your jupyter server with different
hardware resources or cluster options, or if you are sharing a research
account and want to let each user run a different jupyter server.

After you login, do not click Start on the Server Options page. Instead,
visit the control panel at <https://jupyter.stat.berkeley.edu/hub/home>.
You can get there by clicking the Home button at the top-left. Specify
an arbitrary name in the "Name your server" field, then click "Add New
Server". You will then be prompted to specify spawning options.

If you have multiple named servers running, just navigate to the hub
control panel by clicking the Home button at the top left, clicking File
\> Hub Control Panel from within Lab, or by visiting
https://jupyter.stat.berkeley.edu/hub/home directly. There is no hub
control panel button from within RStudio. You can access, modify, or
stop the servers there. Note that your default server will be available
at
`https://jupyter.stat.berkeley.edu/user/username`
while your named servers will be available at
`https://jupyter.stat.berkeley.edu/user/username/servername/`.

## Shared Project Accounts

Some non-personal accounts are shared amongst multiple people to ease
the management burden of large datasets and/or code development. While
SSH access to such accounts is managed through SSH keys, our JupyterHub
has a different method. If you have been authorized to use a shared
account, when you login you can specify a username of
`your_username@shared_username`, and then your own password, e.g.
`jane_doe@big_research`. You can request access to shared accounts
through the faculty who manages the account or through
manager@stat.berkeley.edu.

Users of shared accounts are encouraged to create independent named
servers within JupyterHub, as documented above. For example for user
*user3* accessing account *project1*, we recommend accessing JupyterHub
via `https://jupyter.stat.berkeley.edu/user/*project1*/*user3*`. This way
all of user3's session including Jupyter Kernels and RStudio environment
are properly separated from others users of the account.

In this example, user3 could still create multiple servers within the
project account, e.g.

  - `https://jupyter.stat.berkeley.edu/user/project1/user3_experiment1`
  - `https://jupyter.stat.berkeley.edu/user/project1/user3_try2`

We just recommend that the name of the server describes who created it
in some way.

## Packages Available

All Python 3 and R packages installed on the system, as well as packages
installed by users within their home directories, should be available.

## Using a Custom Conda Environment<span id="#custom-kernel"></span>

If you would like your jupyter notebook to leverage your own conda
environment, you must prepare a custom Jupyter kernel (here we use
*mamba* as a drop-in replacement for *conda* that provides faster
dependency resolution):

```{code} bash
# Switch to your conda environment
source activate /path/to/your/custom/conda/env

# Install the ipykernel package for python
mamba install ipykernel

# Create a new jupyter kernel
python -m ipykernel install --user --name=mycondakernel
```

Once you have created the kernel, you can access it from the JupyterLab
launcher.

You can also prepare an R-based kernel:

```{code} bash
# Activate your environment
source activate ~/.conda/envs/myr

# Install R and the IRkernel
mamba install -c conda-forge r r-irkernel

# Create a new jupyter kernel named "My R"
r -e "IRkernel::installspec(displayname='My R')"
```

## Using SSH in a Jupyter session terminal 

To use ssh to connect to another machine while in a terminal in a
Jupyter session, you'll need to use the following flag:

```{code} shell
ssh -F none arwen
```
