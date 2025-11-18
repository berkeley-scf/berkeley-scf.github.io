---
title: Environment Modules
---

## Overview

SCF Linux machines use [environment modules](http://modules.sourceforge.net) to help you manage software versions and configurations. This system lets you easily switch between different versions of:

- Python
- R
- Julia
- MATLAB
- GPU-enabled tools

## How Modules Work

Environment modules modify your shell environment to control which software is available. This approach prevents version conflicts and lets you switch between different versions of the same software seamlessly.

## Using Modules

You can load, unload, and switch modules in two ways:

**Temporary (session-only):** Run module commands directly in your terminal or include them in cluster submission scripts.

**Permanent (default configuration):** Add module commands to the end of your `.bashrc` file so your preferences override system defaults.

Slurm sessions (either started via srun or sbatch) inherit the modules loaded when the Slurm session was started.

## Basic Commands

```{code} shell
# List available modules
module avail

# Show currently loaded modules
module list

# Unload a module
module unload python/3.12

# Load a module
module load python/3.12

# Switch between versions
module switch python/3.11
```
