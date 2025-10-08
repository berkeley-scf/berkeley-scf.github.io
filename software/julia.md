---
title: "Using Julia on the SCF"
---


We provide Julia, including a variety of packages. To use the current
version, do

```{code} shell
module load julia
```

Once you've loaded Julia, the version number will be available in the
`JULIA_VERSION` environment variable.

## Packages

### Julia packages provided by the system

To see what Julia packages are installed on the system, you can run

```{code} shell
ls /usr/local/linux/julia-${JULIA_VERSION}/share/julia/packages
```

To see what Julia packages are directly available for loading (via
`using` or `import`) through our system project, you can run

```{code} shell
cat /usr/local/linux/julia-1.10.4/share/julia/environments/v1.10/Project.toml
```

(modifying the version numbers as need for other Julia versions). We're
happy to install additional packages system-wide, particularly if they
seem like they would be useful to multiple people. Just email us.

For packages not available through the system project (see above), you
need to add the packages to your Julia project (which might simply be
the default project in `~/.julia/environments/v1.10`) using
`Pkg.add` as described below. Packages installed on the system won't
be reinstalled (unless there is a newer version available than the one
we installed); they'll simply be associated with your project.

### Install Julia packages into your account

You can also install additional packages into your own account. Packages
are associated with Julia projects. You can view your current project
with `Base.active_project()` and activate a project using
`Pkg.activate()`.

Here is an example of installing the `GaussianMixtures` package for
your current project:

```{code} julia
using Pkg
Pkg.add("GaussianMixtures")
using GaussianMixtures
```

By running the 'using' command immediately, Julia will precompile the
package.

Note that if the current version of GaussianMixtures were already
installed at the system level, Julia won't reinstall it, but will simply
make the system-installed package available in your current project.

## Versions

You can use Linux [environment
modules](/faqs/using-environment-modules-scf) to switch between
different Julia versions. This can be done on a one-time basis in a
given terminal session or cluster submission script, or can be done in
your .bashrc (after the stanza involving ~skel/std.bashrc) to set a
default different than the system default. 

To switch from Julia 1.10.4 (the default) to Julia 1.8:

```{code} shell
module switch julia/1.10.4 julia/1.8
```

To see what Julia is being used:

```{code} shell
module list
```
