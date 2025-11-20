---
title: "Python"
---

We provide Python including a variety of packages (including `numpy`,
`scipy`, `pandas`, `scikit-learn`, `pytorch`, `jax`, and other computational packages) through
the Miniforge installer and the community-driven `conda-forge` channel.

## Python versions

On our Linux servers, we provide Python 3.13. We can also help you
access older versions of Python if needed, by using a [Conda
environment](conda.md). 

Note that in what follows we use [mamba](conda.md#mamba), a
drop-in replacement for conda.

## Installing packages with pip

To see what Python packages are available, invoke

```{code} bash
mamba list
```

To install packages locally in your home directory (in `~/.local`) use the `--user`
flag to `pip`:

```{code} bash
pip install --user package_to_install
```

It is possible to use `conda install` to install packages outside of a
Conda environment, but we don't recommend it as it can cause confusing
interference between dependencies.

If you are using Conda environments you will generally want to [install packages using conda/mamba](./conda.md#conda-python-installer).

### Virtual environments (Conda environments and virtualenv)

Environments provide a way to manage Python packages (and with Conda
environments even the version(s) of Python and other software) in a
context that can be isolated and controlled. This allows one to more
easily manage dependencies and provide for reproducibility.

#### Conda environments

Conda is a very popular tool for installing software, particularly
widely used for creating Python environments and installing Python packages.

We provide [extensive information on using Conda (or our preferred alternative, Mamba)
on the SCF and elsewhere](conda.md).

#### virtualenvs

[virtualenv](https://virtualenv.pypa.io/en/stable/) is an older approach to setting up Python environments. 

To create a virtual env:

```{code} bash
virtualenv --system-site-packages ~/path/for/your/env
source ~/path/for/your/env/bin/activate
```

At this point you can `pip install` packages (without `--user`):

```{code} bash
pip install numpy
```

or do something more involved, such as:

```{code} bash
git clone https://github.com/somerepo/somelibrary.git
cd somepackage
python setup.py install
# optionally, to delete source files
cd .. && rm -rf somepackage
```

When you want to escape out of this environment, run `deactivate`. To
re-enter, run the `source` line as above.

