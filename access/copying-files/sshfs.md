---
title: SSH as a filesystem
---

## macOS with sshfs

> [sshfs](https://github.com/libfuse/sshfs) allows you to mount a remote
filesystem using SFTP on macOS.

:::{warning}
sshfs is no longer under development, and may not work on newer systems.
:::

[Download](https://github.com/libfuse/sshfs/releases) and install the
sshfs package.

Here is an example terminal session to mount your SCF home directory:

```{code} shell-session
mkdir ~/scf
sshfs username@SOME_SCF_HOST.berkeley.edu: ~/scf

# to detach later ; umount is /sbin/umount on macOS
umount ~/scf
```

## Linux with Desktop File Managers

Linux desktop file managers all support file transfer over SSH natively.

In Nautilus, go to 'File > Connect to Server', select 'SSH' under type and
your favorite SCF machine as the 'Server'. Then fill in the folder you
want to open (generally your home directory on the SCF as a full path,
such as `/accounts/grad/username`. This will allow you to move files by
drag-and-drop.
