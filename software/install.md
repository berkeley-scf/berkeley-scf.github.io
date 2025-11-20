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

### Using the Conda (or Mamba) package installer

Conda is a general package manager. While it is best known for 
[installing Python packages](conda.md#conda-python-installer), you can also use it to 
[install other software](conda.md#conda-general-installer), including executables with
complicated dependencies that would otherwise need to be installed using admin privileges.

