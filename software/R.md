---
title: R
---

We provide R, including a variety of popular libraries. You can request that
we install additional libraries for you, or you can install them yourself in
your own account.

## Installation by SCF staff

First, note that in general, SCF staff will install an R package on the
system on [request](mailto:consult@stat.berkeley.edu).

## User installation

However, you can also install packages locally within your home
directory. So if you need a package quickly or on a one-time basis, or
if the package is particularly specialized, you might install it
locally.

By default, user-installed packages are installed in the \`R\`
subdirectory in your home directory, in
`~/R/x86_64-pc-linux-gnu-library/4.5`. However, if that directory does
not exist, you may get an error message like this:

``` programlisting
mkdir: cannot create directory  '/server/linux/lib/R/site-library/00LOCK': Permission denied ERROR: failed to lock directory  '/server/linux/lib/R/site-library' for modifying
```

The simplest solution is to create the directory:

    mkdir -p ~/R/x86_64-pc-linux-gnu/4.5

You can use `.libPaths()` to check that the user-level directory is the
default location (it should be the first result printed, as seen below)
where R will install packages.

    > .libPaths()
    [1] "/accounts/grad/username/R/x86_64-pc-linux-gnu-library-ubuntu-24.04/4.5"
    [2] "/system/linux/lib/R-24.04/4.5.0/x86_64/site-library"                  
    [3] "/usr/lib/R/site-library"                                              
    [4] "/usr/lib/R/library"                                                   

### Library path management

If you need more control over the library path, R provides a number of
methods for controlling the library path to accommodate just about any
user's need.

#### Temporarily changing the library path

You can modify R's notion of your library path on a one-time basis by
specifying the `lib=` argument to `install.packages`. Suppose there is a
directory called `MyRlibs` in your home directory. The command:

    install.packages('caTools',lib='~/MyRlibs')

will install the specified package in your local directory. To access
it, the `lib.loc=` argument of `library` must be used:

    library('caTools',lib='~/MyRlibs')

One problem with this scheme is that if a local library invokes the
`library()` function, it won't know to also search the local library

#### Changing the library path for a session

The `.libPaths()` function accepts a character vector naming the
libraries which are to be used as a search path. Note that it does not
automatically retain directories which are already on the search path.
Since the `.libPaths()` function returns the current search path when
called with no arguments, a call like

    .libPaths(c('~/MyRlibs',.libPaths()))

will put your local directory at the beginning of the search path. This
means that `install.packages()` will automatically put packages there,
and the `library()` function will find libraries in your local directory
without additional arguments.

#### Permanently changing the library path

The environmental variable `R_LIBS` is set by the script that invokes R,
and can be overridden (in a shell startup file, for example) to
customize your library path. This variable should be set to a
colon-separated string of directories to search. Since it's always set
inside of an R session, the easiest way to get a starting point for it
is to use `Sys.getenv()`:

``` programlisting
> Sys.getenv('R_LIBS')                          
[1] "/usr/local/linux/lib/R/site-library:/usr/local/lib/R/site-library:/usr/lib/R/site-library:/usr/lib/R/library"
```

You could then make a copy of this path, modify it, and set the `R_LIBS`
environmental variable to that value in the shell or a startup script.
