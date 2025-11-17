---
title: "Python"
---

We provide Python including a variety of packages (including numpy,
scipy, pandas, scikit-learn, and other computational packages) through
the Miniforge installer and the community-driven `conda-forge` channel.

## Python versions

On our Linux servers, we provide Python 3.13. We can also help you
access older versions of Python if needed, by using a [Conda
environment](conda.md). 

Note that in what follows we use [mamba](install.md), a
drop-in replacement for conda.

## Packages

To see what Python packages are available, invoke

    mamba list

To install packages locally in your home directory use the `--user`
flag to `pip`:

    pip install --user package_to_install

It is possible to use `conda install` to install packages outside of a
Conda environment, but we don't recommend it as it can cause confusing
interference between dependencies.

### virtualenv and Conda environments

Environments provide a way to manage Python packages (and with Conda
environments even the version(s) of Python and other software) in a
context that can be isolated and controlled. This allows one to more
easily manage dependencies and provide for reproducibility.

#### virtualenvs

If you would like to override system-installed libraries, for example if
you want to use a newer or older version, try
[virtualenv](https://virtualenv.pypa.io/en/stable/), "a tool to create
isolated Python environments".

    virtualenv --system-site-packages ~/path/for/your/env
    source ~/path/for/your/env/bin/activate

At this point you can `pip install` your library or do something more
involved:

    git clone https://github.com/somerepo/somelibrary.git
    cd somelibrary
    python setup.py install
    # optionally, to delete source files
    cd .. && rm -rf somelibrary

When you want to escape out of this environment, run `deactivate`. To
re-enter, run the `source` line as above.

#### Conda environments

Alternatively you can use mamba to create Conda environments:

    mamba create --name myenv
    source activate myenv

To escape out of this environment, run `source deactivate`.

Note that use of `source` in `source activate` and `source
deactivate` is deprecated, but you should be able to use these without
problems.  

You can also use `mamba activate` and `mamba deactivate`, but there
are some issues to be aware of. When you first try to use `mamba
activate`, Mamba/Conda will prompt you to run `mamba init` to
initialize mamba for the shell you are using. You can do this, but note
that it will modify your `.bashrc` so that Mamba commands are
available whenever you log in. As part of this, Mamba will put you in
the base Conda/Mamba environment automatically when a new shell starts,
which will prevent you from accessing the Python version and related
packages that the SCF provides. To avoid this, we recommend running
`mamba config --set auto_activate_base False` after running `mamba
init`. The same discussion holds for the use of `conda` rather than
`mamba` above.
