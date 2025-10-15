---
title: "Conda and Mamba"
---
Conda is a package management system which can be used to create Python
and R development environments on many different platforms. You can
install it on your own device, and it is often available at many High
Performance Computing centers.

It's common that installing packages using Conda is slow or fails
because Conda is unable to resolve dependencies. To get around this,
**we suggest the use of Mamba**.

[Mamba](https://mamba.readthedocs.io/en/latest/) is a drop-in
replacement for Conda that is generally faster and better at resolving
dependencies.

In the examples below, we show the syntax for Conda, but you can simply
replace "conda" with "mamba" on the SCF (or if you've installed Mamba on
your own machine), e.g., "mamba install pytorch" rather than "conda
install pytorch".

## Installing software using Conda/Mamba

We have information on
[using Conda (and Mamba) to install software](/software/install) on the SCF.

## Using Conda/Mamba

Once conda is installed, you can use it to search for and install other
things.

```{code} shell-session
(base) mylaptop:~$ conda search pytorch
Loading channels: done
# Name                       Version           Build  Channel
pytorch                        1.3.1 cpu_py27h0c87eb2_0  pkgs/main
pytorch                        1.3.1 cpu_py36h0c87eb2_0  pkgs/main
pytorch                        1.3.1 cpu_py37h0c87eb2_0  pkgs/main
pytorch                        1.4.0 cpu_py36hf9bb1df_0  pkgs/main
pytorch                        1.4.0 cpu_py37hf9bb1df_0  pkgs/main
pytorch                        1.4.0 cpu_py38hf9bb1df_0  pkgs/main
pytorch                        1.6.0 cpu_py37hd70000b_0  pkgs/main
pytorch                        1.6.0 cpu_py38hd70000b_0  pkgs/main
```

Here we have searched for `pytorch` and conda has found several
versions of it. There are also multiple build per version. For example
above you can see that the latest version is 1.6.0 and there are builds
for python3.7 and python3.8. If we ask conda to install version 1.6.0,
it will check to make sure that it can proceed, and will tell you what
it will do:

```{code} shell-session
(base) mylaptop:~$ conda install pytorch=1.6.0
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /Users/me/miniconda3

  added / updated specs:
    - pytorch=1.6.0


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    _pytorch_select-0.1        |            cpu_0         169 KB
    blas-1.0                   |              mkl           6 KB
    ca-certificates-2020.6.24  |                0         125 KB
    certifi-2020.6.20          |           py38_0         156 KB
    conda-4.8.4                |           py38_0         2.9 MB
    intel-openmp-2019.4        |              233         887 KB
    libmklml-2019.0.5          |                0        16.2 MB
    llvm-openmp-10.0.0         |       h28b9765_0         236 KB
    mkl-2019.4                 |              233       101.9 MB
    mkl-service-2.3.0          |   py38hfbe908c_0          42 KB
    mkl_fft-1.1.0              |   py38hc64f4ea_0         138 KB
    mkl_random-1.1.1           |   py38h959d312_0         290 KB
    ninja-1.10.0               |   py38h879752b_0         102 KB
    numpy-1.19.1               |   py38h3b9f5b6_0          21 KB
    numpy-base-1.19.1          |   py38hcfb5961_0         4.1 MB
    pytorch-1.6.0              |cpu_py38hd70000b_0        34.0 MB
    ------------------------------------------------------------
                                           Total:       161.2 MB

The following NEW packages will be INSTALLED:

  _pytorch_select    pkgs/main/osx-64::_pytorch_select-0.1-cpu_0
  blas               pkgs/main/osx-64::blas-1.0-mkl
  intel-openmp       pkgs/main/osx-64::intel-openmp-2019.4-233
  libmklml           pkgs/main/osx-64::libmklml-2019.0.5-0
  llvm-openmp        pkgs/main/osx-64::llvm-openmp-10.0.0-h28b9765_0
  mkl                pkgs/main/osx-64::mkl-2019.4-233
  mkl-service        pkgs/main/osx-64::mkl-service-2.3.0-py38hfbe908c_0
  mkl_fft            pkgs/main/osx-64::mkl_fft-1.1.0-py38hc64f4ea_0
  mkl_random         pkgs/main/osx-64::mkl_random-1.1.1-py38h959d312_0
  ninja              pkgs/main/osx-64::ninja-1.10.0-py38h879752b_0
  numpy              pkgs/main/osx-64::numpy-1.19.1-py38h3b9f5b6_0
  numpy-base         pkgs/main/osx-64::numpy-base-1.19.1-py38hcfb5961_0
  pytorch            pkgs/main/osx-64::pytorch-1.6.0-cpu_py38hd70000b_0

The following packages will be UPDATED:

  ca-certificates                                2020.1.1-0 --> 2020.6.24-0
  certifi                                 2020.4.5.1-py38_0 --> 2020.6.20-py38_0
  conda                                        4.8.3-py38_0 --> 4.8.4-py38_0


Proceed ([y]/n)?

Typing `y`, or accepting the default choice (surrounded by brackets
\[\]) of `y` by pressing return, will let conda proceed.

Downloading and Extracting Packages
certifi-2020.6.20    | 156 KB    | ##################################### | 100%
blas-1.0             | 6 KB      | ##################################### | 100%
...
[snip]
...
pytorch-1.6.0        | 34.0 MB   | ##################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done

You can then start using the installed library.

(base) mylaptop:~$ python
Python 3.8.3 (default, May 19 2020, 13:54:14)
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>>
```

## Environments

Conda will install all of your packages into your default environment.
However there are various situations in which you may want to create a
[separate
environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html),
These include (1) if you are working on multiple projects
simultaneously, (2) if you want to be able to eventually share your
environment with a collaborator, and (3) if some package versions
conflict with others in your default environment.

### Creating

To create a new environment:

```{code} shell-session
(base) mylaptop:~$ conda create --name myproject2
```

You can also create new environments with an entirely different version
of python:

```{code} shell-session
(base) mylaptop:~$ conda create --name myproject2 python=3.8
```

Note that under some situations, your environment might still make use
of the default environment for the Python executable or certain packages
already available in the default environment. We have
[details and tips](/software/install#conda-isolate) on creating a completely isolated environment.

To enter into your newly created environment:

```{code} shell-session
(base) mylaptop:~$ source activate myproject2
```

The shell prompt will be updated to reflect the active environment name.

You can also activate an environment with `conda activate myproject2`,
but see below for some cautionary notes before doing that.

```{code} shell-session
(myproject2) mylaptop:~$ 
```

Also, note that your previously installed libraries are not in your new
environment.

```{code} shell-session
(myproject2) mylaptop:~$ python -m torch
/Users/me/miniconda3/envs/myproject2/bin/python: No module named torch
```

We will install a completely different version of pytorch into this
environment.

```{code} shell-session
(myproject2) mylaptop:~$ conda install pytorch=1.4.0
Collecting package metadata (current_repodata.json): done
...
[snip]
...
Downloading and Extracting Packages
pycparser-2.20       | 94 KB     | ##################################### | 100%
six-1.15.0           | 13 KB     | ##################################### | 100%
cffi-1.14.1          | 219 KB    | ##################################### | 100%
pytorch-1.4.0        | 26.3 MB   | ##################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(myproject2) mylaptop:~$ python
Python 3.8.5 (default, Aug  5 2020, 03:39:04)
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.__version__
'1.4.0'
```

You can invoke the `activate` and `deactivate` conda commands to
switch between the environments. The shell prompt is updated to reflect
the activate environment.

```{code} shell-session
(myproject2) mylaptop:~$ conda deactivate
(base) mylaptop:~$ 
```

#### Environment locations

If you have a scratch directory on the SCF, your Conda environments by
default will be stored in `/scratch/users/\<username\>/conda/envs`. If
you don't have a scratch directory, they will be in the usual
`~/.conda/envs` directory. The purpose of this is to reduce backup
sizes, as scratch it not backed up and Conda environments can be
reproduced based on saving an environment recipe using `conda env
export`.

Source packages that Conda caches for later use will be stored in
`/tmp/pkgs` on each machine.

### Conda activate versus source activate

When you first try to use `conda activate`, Conda will prompt you to
run `conda init` to initialize conda for the shell you are using. You
can do this, but note that it will modify your `.bashrc` so that Conda
commands are available whenever you log in. As part of this, Conda will
put you in the base Conda environment automatically when a new shell
starts. Note that on the SCF, this will prevent you from accessing the
Python version and related packages that the SCF provides. To avoid
this, we recommend running `conda config --set auto_activate_base
False` after running `conda init` on the SCF.

Using `source activate` (and `source deactivate`) instead of `conda
activate` (and `conda deactivate`) are deprecated but still work, and
you may wish to use them in some situations (such as on the SCF) to
avoid the behavior discussed above.

### Reproducing an environment

You can create a snapshot of your current environment which can then be
reproduced by collaborators, or even just yourself if you want to setup
the same environment on another device. To export an environment:

```{code} shell-session
(base) mylaptop:~$ source activate myproject2
(myproject2) mylaptop:~$ conda env export --from-history > environment.yml
```

Transmit the `environment.yml` file to the other person or device. One
can then create a new environment from that file:

```{code} shell-session
(base) mylaptop:~$ conda env create -f environment.yml
```

## Installing Mamba/Conda on your own computer

On the SCF, we use Mamba as a drop-in replacement for Conda.

For your own computer, we recommend using the [Miniforge
distribution](https://github.com/conda-forge/miniforge) as your Python
installation rather than Anaconda. Miniforge by default uses the
conda-forge channel, a popular channel providing a wide variety of
up-to-date packages. You can optionally have it use Mamba rather than
Conda. 

#### Mamba for Mac ARM64-based machines (Apple Silicon M1 and M2 Macs)<span id="m1-anaconda"></span>

With the M1 and M2 Macs, Apple is now using its own chips, referred to
as *Apple Silicon*. These have a different architecture, ARM64, than
standard x86-64 chips, such as those produced by Intel and AMD.

To take full advantage of the new chips, you can use Miniforge as it
provides versions for ARM64. 

Non-ARM64 programs, including non-ARM64 Miniforge installations, will
work on the new Apple Silicon-based machines by automatically making use
of Apple's Rosetta2 system to translate machine code from ARM64 to
x86_64, but you can expect some decrease in performance. 

### Using Anaconda/Miniconda

While we recommend installing Miniforge, you can also install Anaconda
or a minimal installation called Miniconda. 

#### Miniconda

1. Download
   [Miniconda](https://docs.conda.io/en/latest/miniconda.html). There
   are installers for Linux, macOS, and Windows. Miniconda is a much
   smaller version of Anaconda which includes more packages out of the
   box as well as a graphical user interfaces to the installer.
   Miniconda is better if you don't want to install too many
   unnecessary packages right at the start.

1. Run the installer. This will prompt you a couple of times, and it is
   usually sensible to accept the defaults. Conda alters your shell
   initialization, and updates your executable path to find the base
   installation. For example, Miniconda will be installed into
   ~/miniconda3/ by default, so ~/miniconda3/bin/ will be added to your
   PATH variable. Conda may update your shell prompt as well with
   status information.

1. Open a new terminal window. This will start up a new shell which
   will be aware of the new Conda tools. For example, on a Mac:

   ```{code} shell-session
   (base) mylaptop:~$ type -a python
   python is /Users/me/miniconda3/bin/python
   python is /usr/bin/python
   ```

#### Anaconda for Mac ARM64-based machines (Apple Silicon M1 and M2 Macs)

With the M1 and M2 Macs, Apple is now using its own chips, referred to
as *Apple Silicon*. These have a different architecture, ARM64, than
standard x86-64 chips, such as those produced by Intel and AMD.

To take full advantage of the new chips, you can use [Anaconda with
ARM64
support](https://www.anaconda.com/blog/new-release-anaconda-distribution-now-supporting-m1).
You can either install Anaconda using the [64 -Bit (M1)
installer](https://www.anaconda.com/products/distribution#Downloads), or
update your existing conda installation:

```{code} bash
conda install anaconda=2022.05
```

Non-ARM64 programs, including standard Miniconda and Anaconda
installations, will work on the new Apple Silicon-based machines by
automatically making use of Apple's Rosetta2 system to translate machine
code from ARM64 to x86_64, but you can expect some decrease in
performance. 
