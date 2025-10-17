---
title: sshfs
---


If you're on a Mac, download and install both "FUSE for macOS" and SSHFS from the FUSE for macOS website

. If you're on Linux, install sshfs. Here is an example terminal session to mount your SCF home directory:

```{code} shell-session
mkdir ~/scf
sshfs username@SOME_SCF_HOST.berkeley.edu: ~/scf

# to detach later ; umount is /sbin/umount on macOS
umount ~/scf
```

## Linux File Managers

Linux desktop file managers all support file transfer over SSH natively. (strictly speaking, not with sshfs)

In Nautilus, go to 'File > Connect to Server', select 'SSH' under type and your favorite SCF machine as the 'Server'. Then fill in the folder you want to open (generally your home directory on the SCF as a full path, such as `/accounts/grad/username`. This will allow you to move files by drag-and-drop.
