---
title: rsync
---

`rsync` is similar to [scp](sftp-scp.md) but is especially useful for keeping
two directories in sync, for example, when you want to copy only the
**differences** between a local and remote directory. This makes it efficient
for repeated transfers or incremental updates. It uses [SSH](../ssh.md) internally, so you would authenticate with your password or [SSH keys](../../kb/ssh-keys.md).

Unlike `scp`, rsync only transfers files that have changed, making it ideal for synchronizing large directories or backups.

To copy a local file or directory to a remote system:

```{code} shell-session
$ rsync -av paper/ scf1@arwen.berkeley.edu:/tmp/paper/
scf1@arwen.berkeley.edu's password:
sending incremental file list
./
draft.txt
figures/
figures/chart.eps

sent 1,234 bytes  received 56 bytes  860.00 bytes/sec
total size is 12,345  speedup is 9.52
```

```{important}
Pay attention to the **trailing slash** on the source directory (`paper/`).  
In `rsync`, this determines *what* is copied:

- `rsync -av paper/ remote:/tmp/paper/` — copies the *contents* of `paper/` into `/tmp/paper/`.
- `rsync -av paper remote:/tmp/paper/` — copies the *directory itself* (creating `/tmp/paper/paper/`).

This subtle difference can save confusion when syncing directories.
```

The options commonly used here are:

- `-a` (archive): preserves file permissions, timestamps, symbolic links, etc.  
- `-v` (verbose): shows progress messages.  

To copy files **from** the remote system back to your local machine:

```{code} shell-session
$ rsync -avz scf1@arwen.berkeley.edu:/tmp/paper/ paper/
scf1@arwen.berkeley.edu's password:
receiving incremental file list
./
notes.txt
new_results.csv
```
