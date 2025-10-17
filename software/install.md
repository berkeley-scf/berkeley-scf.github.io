---
title: "Installing Software"
---
## Requesting software installation by the SCF

In general, SCF staff are happy to install software at the system level
when that software could be of interest to multiple users. Please [email
your request](mailto:consult@stat.berkeley.edu), including
links/instructions for installing the software.

For specialized software, we can help you install software in your home
directory or a project directory.

## Installing software on the SCF

### Tips for installing software

- Note that any installation instructions that require you to use
  `apt-get` or `sudo` won't work because they require administrative
  privileges.
- However, in many cases, one can install software in your home
  directory by making sure the installation process will only create
  files in your home directory. SCF staff are available to help.
- Since home and scratch directories are accessible from all SCF
  machines, you only need to install the software of interest once while
  on any SCF Linux machine, and it will be available on all the
  machines.

### Using the Conda/Mamba package manager

Conda is a general package manager. Many users use it just to install
Python packages, but it can be used to install software more generally.
A good option for installing a piece of software is to check if there is
a Conda package for it, before you try to install from source code.
Executables installed when you install a Conda package will be placed in
the `bin` subdirectory of the active Conda environment.

(mamba)=
#### Mamba

It's common that installing packages using Conda is slow or fails
because Conda is unable to resolve dependencies. To get around this, we
suggest the use of Mamba.

[Mamba](https://mamba.readthedocs.io/en/latest/) is a drop-in
replacement for Conda that is generally faster and better at resolving
dependencies. Here's an example of creating an environment and
installing package(s) of interest:

:::{code} bash
mamba create --name your_env_name python=3.10
source activate your_env_name
mamba install name_of_python_package
:::

(conda-isolate)=
#### Isolating your environment from the SCF Python installation

When creating a Conda environment, if you do not specify the version of
Python, your environment will use our default Python version via the SCF
Python executable, and with all the SCF-installed Python packages
available to you. That has the advantage that you may not need to
install a bunch of packages. 

::: {code} bash
mamba create -y -n myenv
source activate myenv
type python
# (myenv) paciorek@smeagol:~> type python
python is /usr/local/linux/mambaforge-3.11/bin/python
python -c "import numpy; print(numpy.__version__)"
# 1.23.5
:::

The downside is that your environment is tied to our defaults and is
harder to reproduce. Also, in many cases when you install a package in
the environment, updated versions of dependencies (potentially including
Python itself) may be installed.

To isolate your environment, make sure to specify the Python version you
want, even if it is the same as the SCF's default Python version.

:::{code} bash
mamba create -y -n myenv python=3.8
source activate myenv
type python
# python is /accounts/vis/paciorek/.conda/envs/myenv/bin/python
python -c "import numpy; print(numpy.__version__)"
# NameError: name 'numpy' is not defined
:::

One additional complication is that if you have packages installed via
pip (which will be located in `~/.local` in your home directory), your
environment will try to use those packages, which means your environment
is not fully isolated and can be hard to reproduce. In addition, if you
choose to install packages for your environment via pip, you'll
generally want to install without using the `--user` flag. Omitting
that flag will cause packages to be installed within the environment's
directory, while including the flag will cause them to be installed in
`~/.local` (and risk affecting your use of packages outside the
environment!).

#### R and Conda

Conda can actually be used to install R and R packages inside a Conda
environment. You're welcome to do this, but most users make use of the R
installation (and a wide range of R packages) that we provide at the
system level and [nstall additional packages](/software/R) for use
with the system R.
