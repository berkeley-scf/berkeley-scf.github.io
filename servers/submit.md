---
title: "Submitting cluster jobs"
---
One can use SLURM to submit a variety of types of parallel code. Here is
a set of potentially useful templates that we expect will account for
most user needs. If you have a situation that does not fall into these
categories or have questions about parallel programming, submitting jobs
to use more than one core, or are not sure how to follow these rules,
please email <consult@stat.berkeley.edu>.

For additional details, please see the
<a href="/node/4244" data-entity-substitution="canonical"
data-entity-type="node"
data-entity-uuid="1a0a6b9b-4498-4ed3-843b-83de434deb7a">notes from SCF
workshops</a> on the basics of parallel programming in R, Python, Matlab
and C, with some additional details on using the cluster. If you're
making use of the
<a href="/node/4279" data-entity-substitution="canonical"
data-entity-type="node"
data-entity-uuid="fdb7da38-b279-4357-917a-08c76f112767">threaded
BLAS</a>, it's worth doing some testing to make sure that threading is
giving an non-negligible speedup; see the notes above for more
information.

#### Running MATLAB across Multiple Nodes

\[TO BE MOVED TO OWN PAGE\]

As of June 2019, you can run MATLAB across unlimited workers (except as
constrained by the number of cores available on the system not used by
other jobs) on one or more nodes. There are two ways you can do this.
Please see [these
instructions](http://eml.berkeley.edu/cluster#parallel-server) for how
this is done on the EML (Economics) cluster, also run by SCF. The same
instructions will work on the SCF, but for 'Option 2', of course you
should be running MATLAB on an SCF stand-alone server. 

<div class="tab">

Non-parallel

Threaded

Multi-core

Multi-node

Multiple jobs

GPU

</div>

<div id="single" class="tabcontent">

### Non-parallel (single core, single thread) code

</div>

<div id="threaded" class="tabcontent">

### Threaded (one process, multiple threads) code

Here's an example job script to use multiple threads (4 in this case) in
R (or with your own openMP-based program):

    #!/bin/bash
    #SBATCH --cpus-per-task 4
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    R CMD BATCH --no-save simulate.R simulate.Rout

This will allow your R code to use the system's threaded BLAS and LAPACK
routines. \[Note that in R you can instead use the omp_set_num_threads()
function in the RhpcBLASctl package, again making use of the
SLURM_CPUS_PER_TASK environment variable.\] The same syntax in your job
script will work if you've compiled a C/C++/Fortran program that makes
use of openMP for threading. Just replace the R CMD BATCH line with the
line calling your program.

Here's an example job script to use multiple threads (4 in this case) in
Matlab:

    #!/bin/bash
    #SBATCH --cpus-per-task 4
    matlab -nodesktop -nodisplay < simulate.m > simulate.out

IMPORTANT: At the start of your Matlab code file you should include this
line:

    maxNumCompThreads(str2num(getenv('SLURM_CPUS_PER_TASK')));

Here's an example job script to use multiple threads (4 in this case) in
SAS:

    #!/bin/bash
    #SBATCH --cpus-per-task 4
    sas -threads -cpucount $SLURM_CPUS_PER_TASK

</div>

<div id="multicore" class="tabcontent">

### Multi-core (multiple process) code

The following example job script files pertain to jobs that need to use
multiple cores on a single node that do not fall under the
threading/openMP context. This is relevant for parallel code in R that
starts multiple R process (e.g., foreach, mclapply, parLapply), for
parfor in Matlab, and for Pool.map and pp.Server in Python.

Here's an example script that uses multiple cores (4 in this case):

    #!/bin/bash
    #SBATCH --cpus-per-task 4
    R CMD BATCH --no-save simulate.R simulate.Rout

IMPORTANT: Your R, Python, or any other code should use no more than the
number of total cores requested (4 in this case). You can use the
SLURM_CPUS_PER_TASK environment variable to programmatically control
this.

The same syntax for your job script pertains to Matlab. IMPORTANT: when
using parpool in Matlab, you should do the following:

    parpool(str2num(getenv('SLURM_CPUS_PER_TASK')))

Note that by default the maximum number of workers is 12. To use more,
run the following before invoking parpool.

    c = parcluster('local');
    c.NumWorkers = str2num(getenv('SLURM_CPUS_PER_TASK'));

By default MATLAB will use one core per worker (i.e., the parallel tasks
will not be threaded). To use multiple threads per worker, here's an
example job script (this is for four workers and two threads per
worker):

    #!/bin/bash
    #SBATCH --nodes 1
    #SBATCH --ntasks 4
    #SBATCH --cpus-per-task 2
    matlab -nodesktop -nodisplay < simulate.m > simulate.out

and here's example MATLAB code for starting up your parallel pool of
(threaded) workers:

    c = parcluster('local');
    c.NumThreads = str2num(getenv('SLURM_CPUS_PER_TASK'));
    c.parpool(str2num(getenv('SLURM_NTASKS')));

</div>

<div id="multinode" class="tabcontent">

### Multi-node (multiple machine) code

You can use MPI to run jobs across multiple nodes. Alternatively, there
are ways to run software such as Python and R across multiple nodes.
This is useful in two ways. First, it allows you to use more than 24 or
32 cores (depending on the partition) for a single job. Second, if you
need fewer cores but the free cores are scattered across the nodes and
there are not sufficient cores on any one node, this allows you to make
use of those scattered cores.

A standard approach for such jobs is to request the number of cores (one
core per parallel worker) using the "-n" flag. Here we request 36 cores.

\#!/bin/bash  
\#SBATCH -n 36  
\< insert your call(s) to executables that can parallelize across nodes
here \>

Here's an example script that uses multiple processors via MPI (36 in
this case):

    #!/bin/bash
    #SBATCH -n 36
    mpirun -np $SLURM_NTASKS myMPIexecutable

"myMPIexecutable" could be C/C++/Fortran code you've written that uses
MPI, or R or Python code that makes use of MPI. More details are
available [here](/parallel). One simple way to use MPI is to
use the doMPI back-end to foreach in R. In this case you invoke R via
mpirun as:

    mpirun -np $SLURM_NTASKS R CMD BATCH file.R file.out

Note that in this case, unlike some other invocations of R via mpirun,
mpirun starts all of the R processes.

Another use case for R in a distributed computing context is to use
functions such as parSapply and parLapply after using the makeCluster
command with a character vector indicating the nodes allocated by SLURM.
If you run the following as part of your job script before the command
invoking R, the file slurm.hosts will contain a list of the node names
that you can read into R and pass to makeCluster.

    srun hostname -s > slurm.hosts

To run an MPI job with each process threaded, your job script would look
like the following (here with 18 processes and two threads per process):

    #!/bin/bash
    #SBATCH -n 18 -c 2
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    mpirun -np $SLURM_NTASKS -x OMP_NUM_THREADS myMPIexecutable

</div>

<div id="multijob" class="tabcontent">

### Automating multiple jobs

There are a variety of ways to automate the creation of multiple jobs
(or, equivalently, bundling jobs into a master job).

#### **Submitting Data Parallel (SPMD) Code**

Here's how you would set up your job script if you want to run multiple
instances (18 in this case) of the same code.

    #!/bin/bash
    #SBATCH -n 18 
    srun myExecutable

To have each instance behave differently, you can make use of the
SLURM_PROCID environment variable, which will be distinct (and have
values 0, 1, 2, ...) between the different instances.

To have each process be  threaded, see the syntax under the MPI section
above.

#### **Job Arrays: Submitting Multiple jobs in an Automated fashion**

Job array submissions are a nice way to submit multiple jobs in which
you vary a parameter across the different jobs.

Here's what your job script would look like, in this case to run a total
of 5 jobs with parameter values of 0, 1, 2, 5, 7:

    #!/bin/bash
    #SBATCH -a 0-2,5,7
    myExecutable

Your program should then make use of the SLURM_ARRAY_TASK_ID environment
variable, which for a given job will contain one of the values from the
set given with the -a flag (in this case from {0,1,2,5,7}). You could,
for example, read SLURM_ARRAY_TASK_ID into your R, Python, Matlab, or C
code.

Here's a concrete example where it's sufficient to use
SLURM_ARRAY_TASK_ID to distinguish different input files if you need to
run the same command (the bioinformatics program tophat in this case) on
multiple input files (in this case, trans0.fq, trans1.fq, ...):

    #!/bin/bash
    #SBATCH -a 0-2,5,7
    tophat BowtieIndex trans$SLURM_ARRAY_TASK_ID.fq

</div>

<div id="gpu" class="tabcontent">

### GPU jobs

To use the GPUs on the scf-sm20 node or the roo server, you need to
specifically request that your job use the GPU as follows:

    arwen:~/Desktop$ sbatch --partition=gpu --gres=gpu:1 job.sh

Once it starts your job will have exclusive access to the GPU and its
memory. If another user is using the GPU, your job will be queued until
the current job finishes.

Interactive jobs should use that same gres flag with the usual srun
syntax for an interactive job.

    arwen:~/Desktop$ srun --pty --partition=gpu --gres=gpu:1 /bin/bash

Note that the GPU hosted on scf-sm20 is quite a bit older, and likely
slower, than the GPU hosted on roo. If you'd like to specifically
request one of the GPUs, you can add the -w flag, e.g. "-w roo" to
request the GPU on roo. 

scf-sm20-gpu is a virtual node - it is a set of two CPUs on the scf-sm20
node that are partitioned off for GPU use.

If you want to interactively logon to the GPU node to check on compute
or memory use of an sbatch job that uses the GPU, find the job ID of
your job using squeue and insert that job ID in place of '\<jobID\>' in
the following command. This will give you an interactive job running in
the context of your original job:

    arwen:~/Desktop$ srun --pty --partition=gpu --jobid=<jobid> /bin/bash

and then use nvidia-smi commands, e.g.,

    scf-sm20:~$ nvidia-smi -q -d UTILIZATION,MEMORY -l 1

We have [more details](/gpu) on setting up your code to use
the GPU.

</div>
