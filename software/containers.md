---
title: "Running Docker containers via enroot"
---
You can't run Docker containers directly via `docker` on the SCF
because of security considerations. However you can import a Docker
container and run it using software called `enroot`. One can also use
`udocker`, however we haven't documented that.

Here's an example using the Docker container for R/RStudio available
from the Rocker project.

First we download the image from DockerHub and create the enroot image.

```{code} shell-session
# Download Docker image:
$ enroot import docker://rocker/r-ver:latest
# Create container from image:
$ enroot create --name=myRimage rocker-r.sqsh
```

The image, in this case `rocker-r.sqsh`, is saved as a single file (in
SquashFS format) in your working directory.

We can run the default application in the container (R in this case)
like this. By default the user inside the container is the same as the
user outside the container.

```{code} shell
enroot start myRimage 
```

We can install additional software in the container as follows. Here we
need to be the root user once we are inside the container and we need
the container to be writeable (`-w`):

```{code} shell-session
$ enroot start --root -w myRimage bash
# run some admin-level commands in the container as the root user in the container, then exit
root@arwen:/# apt update && apt install <some packages>; exit 
```

### Mounting your directories inside the container

You can access your SCF directories (both for reading and writing)
inside the container by mounting a directory using `--mount`,
specifying where in the container filesystem to make it available.

If you're mounting your home directory, one option is to mount it at the
same location inside the container as its location outside the
container. This allows applications inside the container to work with
your home directory seamlessly. This also allows the applications to
modify files in your home directory. For example you could end up
installing R or Python packages from inside the container that are then
available in the future either from inside the container or not. Of
course that might or might not be what you want.

```{code} shell-session
$ enroot start -w --mount ${HOME}:${HOME} myRimage bash
username@arwen:/> cd  # change to home directory
username@arwen:~> pwd
/accounts/grad/username
```

Alternatively you might not want to mount your home directory to the
same path, to avoid modifying your home directory outside the container.
But you might still want to mount the home directory somewhere else
inside the container to provide access to files. Here we mount the home
directory at `/home`.

```{code} shell-session
$ enroot start -w --mount ${HOME}:/home myRimage bash
username@arwen:/$ cd   # go to home directory
username@arwen:~$ pwd
/accounts/grad/username
username@arwen:~$ ls
username@arwen:~$ touch test
username@arwen:~$ ls
test
username@arwen:~$ cd /home
username@arwen:/home$ ls     # files in SCF home directory, mounted at /home
analysis.py do_runs.sh output.txt
```
