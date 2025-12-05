---
title: "Conda and Mamba"
---
Conda is a package management system that can be used to 
install software and create Python (and R) development environments on many different platforms. You can
install it on your own device, and it is available at many High
Performance Computing centers.

`conda` (and `mamba`) are command-line tools run from the terminal (shell).

## Mamba

It's common that installing packages using Conda is slow or fails
because Conda is unable to resolve dependencies. To get around this,
**we suggest the use of Mamba**.

[Mamba](https://mamba.readthedocs.io/en/latest/) is a drop-in
replacement for Conda that is generally faster and better at resolving
dependencies.

In the examples below, we show the syntax for Mamba, but you can simply
replace `mamba` with `conda` if for some reason you prefer that
(e.g., if you haven't installed `mamba` on your own machine).


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

```{code} bash
mamba create --name myproject2
```

You can also create new environments with an entirely different version
of python:

```{code} bash
mamba create --name myproject2 python=3.12
```

Note that under some situations your environment might
make use of the Python executable or some Python packages from outside the environment.
We have [details and tips](#conda-isolate) on when this happens and how to create
a completely isolated environment.

### Activating

To enter into (activate) your newly created environment, you can use
`source activate` or `mamba activate`.  

Here we illustrate using `source` as that is recommended on the SCF as discussed below.

```{code} shell-sessionbash
gandalf:~$ source activate myproject2
```

The shell prompt will be updated to reflect the active environment name.

```{code} shell-session
(myproject2) gandalf:~$ 
```

To deactivate the environment:

```{code} shell-session
(myproject2) gandalf:~$ source deactivate
gandalf:~$ 
```

In some cases you may default to the `base` environment so you might see:

```{code} shell-session
(myproject2) gandalf:~$ source deactivate
(base) gandalf:~$ 
```

#### mamba/conda activate versus source activate

You can also use `mamba activate` and `mamba deactivate`, but there
are some issues to be aware of.

When you first try to use `mamba activate`, Mamba will prompt you to
run `mamba init` to initialize Mamba for the shell you are using. You
can do this, but note that it will modify your `.bashrc` so that Mamba
commands are available whenever you log in. As part of this, Mamba will
put you in the `base` Mamba environment automatically when a new shell
starts. On the SCF, this will prevent you from accessing the
Python version and related packages that the SCF provides. To avoid
this, we recommend running `mamba config --set auto_activate_base
False` if you run `mamba init` on the SCF.

Using `source activate` (and `source deactivate`) instead of `conda
activate` (and `conda deactivate`) are deprecated but still work, and
you may wish to use them in some situations (such as on the SCF) to
avoid the behavior discussed above.


(conda-python-installer)=
### Installing packages

In general, you'll need to install all the packages you need in 
your environment, though in [some cases your environment might
make use of packages from outside the environment](#conda-isolate).

You can search for available packages.

```{code} shell-session
(myproject2) gandalf:~> mamba search jax
Getting repodata from channels...

conda-forge/linux-64                                        Using cache
conda-forge/noarch                                          Using cache
 Name Version Build                     Channel     Subdir
───────────────────────────────────────────────────────────
 jax  0.7.2   pyhd8ed1ab_0              conda-forge noarch
 jax  0.7.1   pyhd8ed1ab_0              conda-forge noarch
 jax  0.7.0   pyhd8ed1ab_0              conda-forge noarch
 jax  0.6.2   pyhd8ed1ab_0              conda-forge noarch
 jax  0.6.0   pyhd8ed1ab_0              conda-forge noarch
<snip>
```

Here we have searched for `jax` and mamba found several
versions of it. 

You can now install packages you need, including specific versions if desired.

If we ask mamba to install version 0.6.2,
it will check to make sure that it can proceed, and will tell you what
it will do:

```{code} shell-session
(myproject) gandalf:~$ mamba install jax=0.6.2
Pinned packages:

  - python=3.13


Transaction

  Prefix: /scratch/users/paciorek/conda/envs/myproject2

  Updating specs:

   - jax=0.6.2


  Package                  Version  Build                Channel          Size
────────────────────────────────────────────────────────────────────────────────
  Install:
────────────────────────────────────────────────────────────────────────────────

  + c-ares                  1.34.5  hb9d3cd8_0           conda-forge     207kB
  + importlib-metadata       8.7.0  pyhe01879c_1         conda-forge      35kB
  + jax                      0.6.2  pyhd8ed1ab_0         conda-forge       2MB
  + jaxlib                   0.6.2  cpu_py313h9430eff_1  conda-forge      67MB
  + libabseil           20250127.1  cxx17_hbbce691_0     conda-forge       1MB
  + libblas                 3.11.0  1_h4a7cf45_openblas  conda-forge      18kB
  + libcblas                3.11.0  1_h0358290_openblas  conda-forge      18kB
  + libgfortran             15.2.0  h69a702a_7           conda-forge      29kB
  + libgfortran5            15.2.0  hcd61629_7           conda-forge       2MB
  + libgrpc                 1.71.0  h8e591d7_1           conda-forge       8MB
  + liblapack               3.11.0  1_h47877c9_openblas  conda-forge      18kB
  + libopenblas             0.3.30  pthreads_h94d23a6_4  conda-forge       6MB
  + libprotobuf             5.29.3  h7460b1f_2           conda-forge       3MB
  + libre2-11           2025.06.26  hba17884_0           conda-forge     212kB
  + ml_dtypes                0.5.1  py313h08cd8bf_1      conda-forge     294kB
  + numpy                    2.3.5  py313hf6604e3_0      conda-forge       9MB
  + opt_einsum               3.4.0  pyhd8ed1ab_1         conda-forge      62kB
  + re2                 2025.06.26  h9925aae_0           conda-forge      27kB
  + scipy                   1.16.3  py313h11c21cd_1      conda-forge      17MB
  + zipp                    3.23.0  pyhd8ed1ab_0         conda-forge      23kB

  Summary:

  Install: 20 packages

  Total download: 115MB

────────────────────────────────────────────────────────────────────────────────


Confirm changes: [Y/n] 
```

Typing `Y` will let mamba proceed.

You could also avoid the interactivity and let mamba proceed without asking by
including `-y` in your `mamba install` invocation.

You can list installed packages like this:

```{code} shell-session
(myproject2) gandalf:~> mamba list jax
List of packages in environment: "/scratch/users/paciorek/conda/envs/myproject2"

  Name    Version  Build                Channel    
─────────────────────────────────────────────────────
  jax     0.6.2    pyhd8ed1ab_0         conda-forge
  jaxlib  0.6.2    cpu_py313h9430eff_1  conda-forge
```

:::{tip} Using pip within an environment is tricky

You can use pip within a Conda environment, but this can cause issues because conda doesn't consider pip-installed packages when installing additional packages, so proceed with caution as follows:

 - Use pip only after conda.
 - If Conda changes are needed after using pip, create a new environment.
 - Don't use `--user` when calling `pip install`.
 - Always run pip with `--upgrade-strategy only-if-needed` (the default).

:::

### Environment locations

If you have a scratch directory on the SCF, your Conda environments by
default will be stored in `/scratch/users/<username>/conda/envs`. If
you don't have a scratch directory, they will be in the usual
`~/.conda/envs` directory. The purpose of this is to reduce backup
sizes, as scratch it not backed up and Conda environments can be
reproduced based on saving an environment recipe using `mamba env
export`.

Source packages that Conda caches for later use will be stored in
`/tmp/pkgs` on each machine.


### Reproducing an environment

You can create a snapshot of your current environment that can then be
reproduced by collaborators, or even just yourself if you want to setup
the same environment on another device. To export an environment:

```{code} bash
source activate myproject2
mamba env export --from-history > environment.yml
```

Transmit the `environment.yml` file to the other person or device. One
can then create a new environment from that file:

```{code} bash
mamba env create -f environment.yml
```

Note that installing on a different operating system can easily fail because the requirements file includes build-specific versioning that only works on the specific operating system, so using on a different OS can require one to pass additional flags, such as the `--from-history` flag above.

(conda-isolate)=
### Isolating your environment from the SCF Python installation

When creating a Conda environment, if you do not specify the version of
Python, your environment will use our default Python version via the SCF
default Python executable, and with all the SCF-installed Python packages
available to you. That has the advantage that you may not need to
install a bunch of packages. 

```{code} shell-session
gandalf:~$ mamba create -y -n myenv
gandalf:~$source activate myenv
(myenv) gandalf:~$ type python
python is /usr/local/linux/miniforge-3.13/bin/python
(myenv) gandalf:~$ python -c "import numpy; print(numpy.__version__)"
2.1.3
```

The downside is that your environment is tied to our defaults and is
harder to reproduce. Also, in many cases, when you install a package in
the environment, updated versions of dependencies (potentially including
Python itself) may be installed.

To isolate your environment, be sure to specify the Python version you
want, even if it is the same as the SCF's default Python version. Of course
as a result you'll need to install all the packages you need.

```{code} shell-session
gandalf:~$ mamba create -y -n myenv python=3.13
gandalf:~$ source activate myenv
gandalf:~$ type python
python is /accounts/vis/paciorek/.conda/envs/myenv/bin/python
gandalf:~$ python -c "import numpy; print(numpy.__version__)"
ModuleNotFoundError: No module named 'numpy'
```

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

### Jupyter kernels

You can [create a Jupyter kernel associated with your environment](/access/jupyterhub#custom-kernel) for use with Jupyter notebooks.


(conda-general-installer)=
## Using Mamba/Conda as a general installer

Conda is a general package manager. Many users use it just to install
Python packages, but it can be used to install software more generally,
including packages that would otherwise require installation from source
(e.g., using `make` or `cmake`) and potentially have complicated additional
dependencies. A good option for installing a piece of software is to check if there is
a Conda package for it, before you try to install from source code.
Executables installed when you install a Conda package will be placed in
the `bin` subdirectory of the active Conda environment.

### R and Conda

Conda can actually be used to install R and R packages inside a Conda
environment. You're welcome to do this, but most SCF users make use of the R
installation (and a wide range of R packages) that we provide at the
system level and [install additional packages](R.md) for use
with the system R.


## Installing Mamba/Conda on your own computer

(install-miniforge)=
### Using Miniforge (recommended)

For your own computer, we recommend using the [Miniforge
distribution](https://github.com/conda-forge/miniforge) as your Python
installation rather than Anaconda. Miniforge by default uses the
`conda-forge` channel, a popular channel providing a wide variety of
up-to-date packages. You can optionally have it use Mamba rather than
Conda. 



### Using Anaconda/Miniconda

While we recommend [installing Miniforge](#install-miniforge), you can also install Anaconda
or a minimal installation called Miniconda. 

To install Miniconda:

1. Download
   [Miniconda](https://docs.conda.io/en/latest/miniconda.html). There
   are installers for Linux, macOS, and Windows. Miniconda is a much
   smaller version of Anaconda that includes more packages out of the
   box as well as a graphical user interface to the installer.
   Miniconda is better if you don't want to install too many
   unnecessary packages right at the start.

1. Run the installer. This will prompt you a couple of times, and it is
   usually sensible to accept the defaults. Conda alters your shell
   initialization, and updates your executable path to find the base
   installation. For example, Miniconda will be installed into
   `~/miniconda3/` by default, so `~/miniconda3/bin/` will be added to your
   `PATH` variable. Conda may update your shell prompt as well with
   status information.

1. Open a new terminal window. This will start up a new shell that
   will be aware of the new Conda tools. For example, on a Mac:

   ```{code} shell-session
   (base) mylaptop:~$ type -a python
   python is /Users/me/miniconda3/bin/python
   python is /usr/bin/python
   ```



