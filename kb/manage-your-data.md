---
title: Manage Your Data
---

## Determining Usage

Each user is assigned a disk space quota, or allotment, when their account is created to insure that there will be sufficient disk space for all our users' needs. If you need additional space, please submit your request to manager@stat.berkeley.edu.

The commands below can show you how disk space you are consuming. For additional information, consult the respective man pages.

:::{table}
:label: Disk space commands

| Command      | Description |
|--------------|------------------------------------------------------------|
| `ls -l`      | Lists size of all files in the current directory.          |
| `bigfiles`   | Recursively searches a directory for big files.            |
| `quota`      | Reports your disk quota and current disk use.              |
| `du -h .`    | Recursive summary of disk use for the current directory.   |
| `dust`       | Similar to `du`, but faster and more visual.               |
| `find . -ls` | Recursively lists all file sizes in the current directory. |

:::

## Temporary Disk Space

There are several places where users can temporarily store data. These
areas are often larger than home directories, but they are not backed up
and may be removed without notice.

### /tmp

Files put in the `/tmp` directory are only accessible on the machine on
which they were created and are automatically wiped everytime the computer
is rebooted. Files may also be deleted with little or no warning if
resources become scarce. However, if you need a large amount of disk space
for a short amount of time, `/tmp` provides a solution which does not need
any staff intervention. Remember that there is no guarantee that files
stored in `/tmp` are safe. Do not use `/tmp` for data that that is difficult
or expensive to re-create. No special permissions are required to use
/tmp. To reference your files using `/tmp`, use `/tmp` as the prefix to the
name of the file, for example `/tmp/myfile`.

The limit to the amount of storage a user can take up is the physical
limitation of the partition. However, if `/tmp` is full, editors, compilers,
and many other programs will not work or behave erratically. To find out
how much space is available in `/tmp` on your system, type `df -k /tmp`. Do
not use `/tmp` if less than 30% of the space is available. Remove files when
they are no longer needed.

### /var/tmp

The `/var/tmp` directory functions similarly to `/tmp`, however, files are
not automatically removed after the machine is rebooted. This directory
does get erased, however, whenever the workstation needs to be reinstalled
or reconfigured. Otherwise, the same policies that apply to `/tmp` apply
to `/var/tmp`.

### /data

The `/data` directory exists on some systems that have secondary disks.
This directory functions similarly to `/var/tmp`, however, it does not get
erased when the computer is reinstalled or reconfigured.

### /scratch

Directories under `/scratch` exist on the file server and can be accessed
from every machine. Unlike users' home directories, they are not backed
up, but can usually accommodate larger data files. If space becomes
limited we may automatically compress files or (if time permitting) ask
users to either remove or archive files that are no longer needed in order
to make room for other users. Files that are not actively being used
should be compressed if possible.

## Compression

Infrequently accessed files may be compressed to save disk space.

:::{table}
:label: File compression commands

| Command                                | Description |
|----------------------------------------|------------------------------------------------------------|
| `gunzip file.gz`                       | Uncompresses file.gz to file
| `gzip file`                            | Compresses file to file.gz
| `tar xzf file.tar.gz`                  | Extract the contents of file.tar.gz
| `tar czf file.tar.gz file1 [file2...]` | Compresses files into file.tar.gz
| `unzip file.zip`                       | Uncompresses file.zip
| `zip file.zip file1 [file2...]`        | Compresses one or more files to file.zip
| `zcat x.Z y.Z ...`                     | Prints the compressed file(s) to the terminal

:::

See the UNIX manual pages for the above programs by using the 'man', for example 'man gzip'.

## Deleting Files

To remove files and directories type:

:::{table}
:label: File deletion commands

| Command         | Description |
|-----------------|------------------------------------------------------------|
| `rm file`       | Removes 'file' if you have write permission on it.
| `rm -f file`    | Removes 'file' if you have write permission in the directory containing it.
| `rmdir dir`     | Removes the empty directory 'dir'.
| `rm -rf dir`    | Recursively remove dir including every file and subdirectory. Use with caution.

:::

Some applications leave behind files that may be removed without adversely
affecting the program.

Web browser cache files can be removed. You can clear your browser disk
cache, as well as instruct the browser to set aside less disk space to use
for its cache, in the program's Preference window, usually under
'Advanced'.

PostScript, .aux, and .log files produced by LaTeX can be recreated as
necessary from the corresponding .tex file.

Compiled object files, often with the suffix .o, produced by C, C++, or
Fortran compilers, can usually be deleted. If need be, they can be
recreated from the original programs that produced them.

Compilers tend to create lots of big binary files such as '.o' and '.out'
files. '.out' files in particular can be quite large. If you have such
files which have been unused for several days and which you don't intend
to use for several more days, they should be removed. (They can easily be
recreated if you need them.) The size of '.out' files which you do need
can be reduced somewhat by stripping them. Type:

    strip a.out     Strips an already existing 'a.out'.
    f77 -s ...      Creates a pre-stripped '.out' file when using f77.
    cc -s ...       Similarly for cc.

When programs crash, they sometimes report 'Core dumped' indicating that a
large file called 'core' has been created in the program's current working
directory. A user may disable core dumps by adding "ulimit -c 0" to
~/.bashrc.

## Best Practices

The Library and Research IT have a Research Data Management (RDM) program
that, "helps researchers navigate the complex landscape of managing data
before, during, and after their research."
