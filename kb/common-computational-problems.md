---
title: "Common computational problems"
---
Here are some computational problems commonly encountered on the compute
servers and cluster and some solutions or workarounds.

## Cluster and Job Submission Issues

- **Your cluster job won't start**
  - Your account may not have been given access to the cluster. Please
    email <trouble@stat.berkeley.edu>.
  
- **Your cluster job is stuck at the top of the queue and other jobs
  start before it**
  - Jobs requesting multiple cores may not start because not enough
    cores become available at once. The Slurm scheduler will try to
    accumulate sufficient cores for your job to start, but other smaller
    jobs may start before yours if the scheduler determines that doing
    so will not delay the start of your job. Unfortunately, because we
    don't require time limits, Slurm has limited information with which
    to make this determination. So particularly for jobs requesting many
    cores, this may happen.

- **Job immediately fails or doesn't produce output**
  - Check that your job script is executable and has the correct shebang line (`#!/bin/bash`).
  - Verify your working directory is not in `/tmp` or `/var/tmp` when submitting.
  - Check the slurm output file (e.g., `slurm-12345.out`) for error messages.
  - Ensure any paths in your script are absolute or correctly relative to where the job runs.

- **Job killed or shows "Out of Memory" (OOM)**
  - Your job exceeded available memory. Check memory usage with `sacct -j JOBID --format=JobID,MaxRSS,ReqMem`.
  - Request more memory using `#SBATCH --mem=16G` (adjust as needed).
  - Consider if your code has a memory leak or loads too much data at once.
  - For R, use memory-efficient packages (e.g., `data.table` instead of base R for large datasets).

- **Job stuck in state CG (completing)**
  - This usually means the job is finishing up and writing output. Give it a few minutes.
  - If it persists for more than 30 minutes, contact <trouble@stat.berkeley.edu>.

## Memory and Disk Space Issues

- **"Disk quota exceeded" error**
  - Check your quota with the `quota` command.
  - See what's using space: `du -h ~ | sort -h | tail -20`.
  - Find large files: `bigfiles ~` or `find ~ -type f -size +100M -ls`.
  - Clean up temporary files, old output, or compress data files.
  - See [Managing Your Data](./manage-your-data.md) for more details.
  - If you need more space, email manager@stat.berkeley.edu.

- **"/tmp is full" or programs behave erratically**
  - Check available space: `df -h /tmp`.
  - Remove your old temporary files: `rm -rf /tmp/myfiles*`.
  - If less than 30% free, avoid using `/tmp` until space is cleared.
  - Consider using your home directory or scratch space instead.

- **"Cannot allocate memory" errors**
  - Your process is trying to use more memory than available.
  - For cluster jobs, request more memory with `--mem`.
  - For interactive sessions, close other applications or use a less memory-intensive approach.
  - Consider processing data in chunks rather than loading everything at once.

- **Core dumps filling up disk space**
  - Disable core dumps: add `ulimit -c 0` to your `~/.bashrc`.
  - Remove existing core dumps: `find ~ -name "core.*" -delete`.
  - See [Managing Your Data](./manage-your-data.md) for more information.

## Performance Issues

- **Job running much slower than expected**
  - Check if you're unintentionally using multiple threads for linear algebra. Set `export OMP_NUM_THREADS=1` to use single-threaded computation.
  - Use `top` or `htop` to see if your job is CPU-bound or I/O-bound.
  - Verify you're not competing for resources on a login node; submit batch jobs to the cluster instead.
  - Check if your code is actually parallelized when you requested multiple cores.

- **R/Python using too many cores and slowing down other users**
  - Threaded BLAS libraries may use all available cores by default.
  - Limit threads: `export OMP_NUM_THREADS=1` (or another appropriate number).
  - See [Linear Algebra using BLAS](./linear-algebra-using-blas.md) for details.

- **Linear algebra slower than expected**
  - Ensure you're using a threaded BLAS (OpenBLAS or MKL).
  - In R: check with `sessionInfo()` to see which BLAS is in use.
  - Set appropriate thread count: `export OMP_NUM_THREADS=4` (adjust to number of cores).

- **R hangs when using profiling**
  - This is likely a conflict between Rprof() and the threaded BLAS
    used by R for linear algebra. Solutions include [disabling
    threading](./linear-algebra-using-blas.md) and (2) not
    using profiling.

## File and Permission Issues

- **"Permission denied" when accessing files**
  - Check file permissions and verify ownership: `ls -l filename`.
  - If it's a directory, ensure it has execute permission: `chmod u+x dirname`.
  - For group-shared files, check that group permissions are set correctly.
  - See [File Permissions](./file-access.md) for more details.

- **"Permission denied" when running a script**
  - Make the script executable: `chmod u+x script.sh`.
  - Alternatively, run with `bash script.sh` instead of `./script.sh`.

- **Cannot access files in someone else's directory**
  - The file owner needs to grant you permission.
  - They may need to set permissions on the directory: `chmod g+rx dirname` (for group access).
  - All parent directories in the path need execute permission.

- **"Text file busy" error**
  - The file is currently being executed. Wait for it to finish or kill the process.
  - If modifying a script, copy it to a new name, edit, then replace the original.

## Software and Module Issues

- **"Command not found" for installed software**
  - Load the appropriate environment module: `module load software-name`.
  - See available modules: `module avail`.
  - Check if software is in your PATH: `which command-name`.
  - For Python/R packages, ensure you're in the correct environment (conda, virtualenv).

- **Module conflicts or incompatible versions**
  - Unload conflicting modules: `module purge` then reload only what you need.
  - Use `module list` to see currently loaded modules.
  - Some modules automatically load dependencies; check with `module show module-name`.

- **Python/R package installation fails**
  - For Python: ensure you're using a virtual environment or conda environment.
  - For R: check you have write permission to the library directory.
  - Install locally: in R use `install.packages("pkg", lib="~/R_libs")`.
  - See [Installing Software](./install.md) for detailed instructions.

- **Segmentation fault or core dump**
  - Often caused by memory access errors in compiled code (C/C++/Fortran).
  - Update to the latest version of the software.
  - Check for known bugs in the software documentation.
  - Try running with different compiler optimizations or debug builds.
  - If using R/Python with compiled extensions, try reinstalling the package.

- **Library version conflicts (e.g., "undefined symbol" errors)**
  - Unload all modules and reload only what's needed: `module purge; module load module-name`.
  - Check which libraries are being loaded: `ldd executable-name`.
  - Ensure compatible versions of dependencies (check module show output).

## Connection and Access Issues

- **SSH connection times out or is very slow**
  - Check your network connection.
  - Too many failed password attempts will cause you to be blocked. Try a different login server (e.g., arwen vs. gandalf).
  - See [SSH](../access/ssh.md) for connection tips.
  - If using X11 forwarding, try without it: `ssh -X` can be slow.

- **X11 forwarding not working**
  - Ensure you used `ssh -X` or `ssh -Y` when connecting.
  - Check that X11 is installed on your local machine.
  - Try `echo $DISPLAY` to verify it's set.
  - See [X11 Forwarding](../access/X11.md) for troubleshooting.

## Data and File Transfer Issues

- **File transfer is very slow**
  - For large transfers, use Globus rather than scp/sftp.
  - Compress files before transferring: `tar -czf archive.tar.gz directory/`.
  - Transfer during off-peak hours if possible.
  - See [Copying Files](../access/copying-files.md) for efficient transfer methods.

- **Transferred files are corrupted**
  - Verify checksums: `md5sum filename` on both source and destination.
  - Ensure binary files are transferred in binary mode (not an issue with scp/rsync).
  - For text files, check for line ending issues (Windows vs. Unix).

## Getting Help

If you encounter a problem not listed here or the suggested solutions don't work:

- Check the Slurm output file for error messages
- Email <trouble@stat.berkeley.edu> with:
  - Description of the problem
  - Any error messages (exact text)
  - What you've already tried
  - For cluster jobs: the job ID
  - For software issues: the software name and version
