---
title: "GPU Servers"
---

## Hardware

The SCF can help with access to several GPU resources:

The SCF operates one GPU available to all SCF users. You need to [use
the SLURM scheduling software](/servers/cluster/gpus) to run
any job making use of the GPU. You may want to use an interactive
session to develop and test your GPU code. That same link also has
information on monitoring GPU usage of your job.

### General Access

#### *GPU* partition

We have one Titan Xp with 12 GB memory on one of our Linux servers
(roo), available through the *gpu* partition. The GPUs formerly
available in the *high* partition have been retired as of March 2023.

#### Savio

Access to GPUs on Savio is available through the [Savio faculty
computing
allowance](http://research-it.berkeley.edu/services/high-performance-computing/faculty-computing-allowance).
Please contact SCF staff for more information.

### Research Groups

The SCF also operates the following GPUs. These GPUs are owned by
individual faculty members, but anyone can run jobs on them. Note that
if you are not a member of the lab group, your jobs will run on a
preemptible basis, which means they can be cancelled at any time by a
higher-priority jobs. These servers can be accessed by submitting to the
*jsteinhardt*, *yugroup*, *yss,* or *songmei* partitions (details below)
using the <a href="/node/4805" data-entity-substitution="canonical"
data-entity-type="node"
data-entity-uuid="ddfd25a8-44e8-4d4b-8ba1-463ead55b47b">SLURM scheduling
software</a>.

#### Steinhardt lab group (*jsteinhardt* partition)

- 8 GeForce RTX 2080 Ti, each with 11 GB memory (shadowfax).
- 2 Quadro RTX 8000, each with 48 GB memory (smaug).
- 8 A100, each with 40 GB memory (balrog).
- 10 A100, each with 80 GB memory (saruman).
- 8 A4000, each with 16 GB memory (sunstone and smokyquartz).
- 8 A5000, each with 24 GB memory (rainbowquartz).

#### Steinhardt lab group remote cluster (lambda partition)

- 8 A100, each with 80 GB memory (five machines at a remote co-location
  facility in Texas)

To use these machines, one must specifically [connect to the remote
cluster](/servers/cluster/gpus#jump%5Baccordion%5D%5B1%5D%5B5%5D),
which is accessed separately from the other SCF resources.

#### Yu lab group (*yugroup* partition)

- 1 A100 with 40 GB memory (treebeard).
- 1 GeForce GTX TITAN X with 12 GB memory (merry).
- 1 Titan Xp with 12 GB memory (morgoth).
- 1 Titan X (Pascal) with 12 GB memory (morgoth).

#### Yun Song lab group (*yss* partition)

- 4 A100, each with 80 GB memory (luthien).
- 8 A100, each with 80 GB memory (beren).

#### Song Mei lab group (*songmei* partition)

- 8 H200, each with 144 GB memory (feanor.stat.berkeley.edu).

#### BerkeleyNLP lab group (*berkeleynlp* partition)

- 8 H200, each with 144 GB memory (lorax.stat.berkeley.edu).

## <span id="software">Software</span>

We provide the following software that will help you in making use of
the GPU:

- CUDA (version 12.8; other versions can be made available)
- cuDNN (cuDNN 9.8.0 for CUDA 12.8; other versions can be made
  available)
- PyTorch (version 2.6.0 for Python 3.13 and version 2.2.1 for Python
  3.12)
- Jax (version 0.5.2 for Python 3.13 and 0.4.25 for Python 3.12)
- Tensorflow is not currently available for Python 3.13, but version
  2.16.1 is available for Python 3.12. Note that Tensorflow may not work
  on some of our old machines, but it should work on the cluster nodes
  as well as on gandalf and radagast among others.
- We can install additional or upgrade current software as needed. 

We use Linux environment
<a href="/node/5458" data-entity-substitution="canonical"
data-entity-type="node"
data-entity-uuid="6cf4643f-ad87-4040-bf87-8eb6e08ff379">modules</a> to
manage the use of GPU-based software, as discussed next. Note that you
could insert any of these commands in your .bashrc (after the stanza
involving ~skel/std.bashrc) so they are always in effect or invoke them
as needed in a script (including a cluster submission script) or in a
terminal session.

For use Python packages that use the GPU for back-end computations,
simply import the package in Python.

<span style="line-height: 1.69231em;">To program with CUDA and related
packages directly, y</span><span style="line-height: 22px;">ou'll need
to load CUDA as follows in order to be able to compile and run your
code:</span>

- CUDA: to use CUDA directly in C or another language, invoke "module
  load cuda".
- cuDNN: cuDNN is available on the GPU servers without needing to load
  any modules.

<span style="line-height: 1.69231em;">If you have questions or would
like additional GPU-related software installed, please contact
</span><a href="mailto:consult@stat.berkeley.edu"
style="line-height: 1.69231em;">consult@stat.berkeley.edu</a><span style="line-height: 1.69231em;">.</span>
