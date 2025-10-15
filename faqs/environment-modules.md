---
title: Environment Modules
---
We use Linux [environment modules](http://modules.sourceforge.net) to
allow users to control what software is available to them on the SCF
Linux machines. At the moment, these are being used to allow one to
choose between Python versions such as 3.13 (the default) and others,
between R, Julia, and MATLAB versions, and to make certain GPU
functionality available.

### Using modules

Modules are designed to change your environment so you can easily switch
between different versions of software and to allow access to software
that might have conflicts with other software on the system. You can use
the load, unload, and switch commands seen below either on a one-time
basis in a terminal session or a cluster submission script or set
defaults in your .bashrc (in general you'd want include any such
commands after the stanza involving `~skel/std.bashrc` so as to have your
modifications override any modules set by default on the system).

To see the software (and versions) available via the modules system:

     module avail

To see what modules are currently loaded:

     module list

To unload a module:

     module unload python/3.13

To load a module:

     module load python/3.12

To switch between different versions:

     module switch python/3.13 python/3.12

### Modules in Slurm sessions

Slurm sessions (either started via srun or sbatch) inherit the modules
loaded when the Slurm session was started.
