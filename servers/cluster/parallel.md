---
title: "Submitting Parallel Jobs"
---
One can use Slurm to submit a variety of types of parallel code. Here is
a set of potentially useful templates that we expect will account for
most user needs. If you have a situation that does not fall into these
categories or have questions about parallel programming, submitting jobs
to use more than one core, or are not sure how to follow these rules,
please email <consult@stat.berkeley.edu>.

For additional details, please see [our tutorial on the basics of
parallel programming in Python, R, Julia, MATLAB and
C/C++](https://computing.stat.berkeley.edu/tutorial-parallelization) or [our tutorial on the Dask package in Python and the future package in R](https://computing.stat.berkeley.edu/tutorial-dask-future). If you're making use of
the [threaded BLAS](/blas), it's worth doing some testing to
make sure that threading is giving an non-negligible speedup; see the
notes above for more information.

## Threaded jobs
Here's an example job script to use multiple threads (4 in this case) in
R (or with your own openMP-based program):

```{code} bash
#!/bin/bash
#SBATCH --cpus-per-task 4
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
R CMD BATCH --no-save simulate.R simulate.Rout
```

This will allow your R code to use the system's threaded BLAS and LAPACK
routines. Note that in R you can instead use the `omp_set_num_threads()`
function in the `RhpcBLASctl` package, again making use of the
`SLURM_CPUS_PER_TASK` environment variable. The same syntax in your job
script will work if you've compiled a C/C++/Fortran program that makes
use of openMP for threading. Just replace the `R CMD BATCH` line with the
line calling your program.

Here's an example job script to use multiple threads (4 in this case) in
MATLAB:

```{code} bash
#!/bin/bash
#SBATCH --cpus-per-task 4
matlab -nodesktop -nodisplay < simulate.m > simulate.out
```

## Multi-core (one node) jobs
The following example job script files pertain to jobs that need to use
multiple cores on a single node that do not fall under the
threading/openMP context. This is includes most packages for parallelization in Python and R, as well as `parfor` in MATLAB.

Note that because we have enabled hyperthreading on the machines, each
core is actually a virtual core (hardware thread), and so code may not
run as quickly as if each core were a physical core. If you'd like to
avoid using hyperthreading, get in contact with us for work-arounds.

Here's an example script that uses multiple cores (4 in this case):

```{code} bash
#!/bin/bash
#SBATCH --cpus-per-task 4
R CMD BATCH --no-save simulate.R simulate.Rout
```

In general, in your R, Python, or any other code, you wouldn't want to
have more worker processes than the number of total cores requested (4
in this case). You can use the `SLURM_CPUS_PER_TASK` environment variable
to programmatically control this.

Note that in R, you should not use the `detectCores()` function (from
the parallel package) as this detects the number of cores physically on
the node, not the number available via Slurm for your job. You will end
up starting too many processes (more than the number of cores
available), which may slow down your computation.

The same syntax for your job script pertains to MATLAB.

Note that by default the maximum number of workers in MATLAB is 12. To
use more, run the following before invoking parpool.

```{code} R
c = parcluster('local');
c.NumWorkers = str2num(getenv('SLURM_CPUS_PER_TASK'));
```

By default MATLAB will use one core per worker (i.e., the parallel tasks
will not be threaded). To use multiple threads per worker, here's an
example job script (this is for four workers and two threads per
worker):

```{code} bash
#!/bin/bash
#SBATCH --nodes 1
#SBATCH --ntasks 4
#SBATCH --cpus-per-task 2
matlab -nodesktop -nodisplay < simulate.m > simulate.out
```

and here's example MATLAB code for starting up your parallel pool of
(threaded) workers:

```{code} R
c = parcluster('local');
c.NumThreads = str2num(getenv('SLURM_CPUS_PER_TASK'));
c.parpool(str2num(getenv('SLURM_NTASKS')));
```

## Multi-node (distributed memory) jobs

There are ways to run software such as Python and R across multiple nodes (in particular using the Dask and future packages, respectively), as well as Julia and MATLAB. One can also use MPI to run a job across multiple nodes. This is useful in two ways. First, it allows you to use more cores for a
single job than are available on a single node. Second, if you need
fewer cores but the free cores are scattered across the nodes and there
are not sufficient cores on any one node, this allows you to make use of
those scattered cores.

Note that because we have enabled hyperthreading on the machines, each
core discussed below is actually a virtual core (hardware thread), and
so code may not run as quickly as if each core were a physical core. If
you'd like to avoid using hyperthreading, get in contact with us for
work-arounds.

A standard approach for such jobs is to request the number of cores (one
core per parallel worker) using the "-n" flag. Here we request 36 cores.

```{code} bash
#!/bin/bash
#SBATCH -n 36
< insert your call(s) to executables that can parallelize across nodes here >
```

In the remainder of this section, we show how to run MPI-based code. For
information on using software such as R and Python across multiple
nodes, see [our tutorial on
parallelization](https://berkeley-scf.github.io/tutorial-parallelization).

Here's an example script that uses multiple processors via MPI (36 in
this case):

```{code} bash
#!/bin/bash
#SBATCH -n 36
mpirun myMPIexecutable
```

`myMPIexecutable` could be C/C++/Fortran code you've written that uses
MPI, or R or Python code that makes use of MPI. More details are
available [here](/parallel).

To run an MPI job with each process threaded, your job script would look
like the following (here with 18 processes and two threads per process):

```{code} bash
#!/bin/bash
#SBATCH -n 18 -c 2
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
mpirun -x OMP_NUM_THREADS myMPIexecutable
```

### Running MATLAB across Multiple Nodes

You can run MATLAB across unlimited workers (except as constrained by
the number of cores available on the system not used by other jobs) on
one or more nodes. There are two ways you can do this. Please see [these
instructions](https://eml.berkeley.edu/cluster#parallel-server) for how
this is done on the EML (Economics) cluster, also run by SCF. The same
instructions will work on the SCF, but for 'Option 2', of course you
should be running MATLAB on an SCF stand-alone server. 

## Parallelizing independent computations or jobs

There are various ways to collect multiple computations or jobs and run
them in parallel as one or more Slurm jobs. See the subsections below for more details on each of these options.

- Slurm job arrays allow you to submit multiple jobs at once.
- GNU parallel allows you to run multiple tasks in parallel within a
  job.
- Slurm allows you to start multiple tasks in parallel in a job via
  srun.
- Finally, you can use shell scripting to 'manually' automate job
  submission.

(slurm-job-arrays)=
### Slurm job arrays

Job array submissions are a nice way to submit multiple jobs in which
you vary a parameter across the different jobs.

Here's what your job script would look like, in this case to run a total
of 5 jobs with parameter values of 0, 1, 2, 5, 7:

```{code} bash
#!/bin/bash
#SBATCH -a 0-2,5,7
myExecutable
```

Your program should then make use of the SLURM_ARRAY_TASK_ID environment
variable, which for a given job will contain one of the values from the
set given with the `-a` flag (in this case from {0,1,2,5,7}). You could,
for example, read `SLURM_ARRAY_TASK_ID` into your R, Python, etc. code.

Here's a concrete example where it's sufficient to use
SLURM_ARRAY_TASK_ID to distinguish different input files if you need to
run the same command (the bioinformatics program tophat in this case) on
multiple input files (in this case, trans0.fq, trans1.fq, ...):

```{code} bash
#!/bin/bash
#SBATCH -a 0-2,5,7
tophat BowtieIndex trans$SLURM_ARRAY_TASK_ID.fq
```

(gnu-parallel)=
### GNU parallel 

GNU Parallel is a shell tool for executing jobs in parallel on one or
multiple computers. It’s a helpful tool for automating the
parallelization of multiple (often serial) jobs, in particular allowing
one to group jobs into a single Slurm submission to take advantage of
the multiple cores on a given node of the cluster.

For details, please see the Berkeley [Savio cluster documentation on
using GNU
parallel](https://docs-research-it.berkeley.edu/services/high-performance-computing/user-guide/running-your-jobs/gnu-parallel).

(srun)=
### Slurm tasks in parallel

Here's how you would set up your job script if you want to run multiple
instances (18 in this case) of the same code as part of a single job.

```{code} bash
#!/bin/bash
#SBATCH --ntasks 18
srun myExecutable
```

To have each instance behave differently, you can make use of the
`SLURM_PROCID` environment variable, which will be distinct (and have
values 0, 1, 2, ...) between the different instances.

(automating-submission)=
### Automating job submission

The above approaches are more elegant, but you can also use UNIX shell
tools to submit multiple Slurm jobs. Here are some approaches and
example syntax. We've tested these a bit but email us if you have
problems or find a better way to do this. (Of course you can also
manually create lots of individual job submission scripts, each of which
calls a different script.)

First, remember that each individual job must be submitted through
sbatch. I.e., no job submission script should execute jobs in parallel,
except via the mechanisms discussed earlier in this document.

Here is some example bash shell code (which could be placed in a shell
script file) that loops over two variables (one numeric and the other a
string):

:::{code} bash
for ((it = 1; it <= 10; it++)); do
  for mode in short long; do
    sbatch job.sh $it $mode
  done
done
:::

You now have a couple options in terms of how `job.sh` is specified. This
illustrates things for MATLAB jobs, but it shouldn't be too hard to
modify for other types of jobs.

#### Option 1

In this case `myMATLABCode.m` would use the variables `it` and `mode` but
not define them.
:::{code} bash
# contents of job.sh
echo "it = $1; mode = '$2'; myMATLABCode" > tmp-$1-$2.m
matlab -nodesktop -nodisplay -singleCompThread < tmp-$1-$2.m > tmp-$1-$2.out 2> tmp-$1-$2.err
:::


#### Option 2

In this case you need to insert the following MATLAB code at the start
of myMATLABCode.m so that MATLAB correctly reads the values of `it` and
`mode` from the UNIX environment variables:

:::{code} bash
# contents of job.sh
export it=$1; export mode=$2;
matlab -nodesktop -nodisplay -singleCompThread < myMATLABCode.m > tmp-$1-$2.out 2> tmp-$1-$2.err
:::

:::{code} matlab
it = str2num(getenv('it'));
mode = getenv('mode');
:::
