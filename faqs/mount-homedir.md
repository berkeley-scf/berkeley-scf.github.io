---
title: How can I mount my home directory remotely?
---

There are a number of options for seamlessly accessing your SCF home directory from your personal computer. In the instructions below, username will be your SCF user name and the password will be this samba password.

Note: when accessing your Samba share from an off-campus network, you will need to use the campus VPN.

## Setting up a Samba Account

At present, we must manually setup a separate login credentials for you to
access your files. Please contact manager@stat.berkeley.edu to facilitate
setting your samba password.

|                | Mac                             | Windows |
|----------------|---------------------------------|---------|
| Home Directory | smb://scf.berkeley.edu/username | \\scf.berkeley.edu\username |
| Web Directory  | smb://scf.berkeley.edu/www      |\\scf.berkeley.edu\www |


## Microsoft Windows

In any Windows Explorer window, select *Tools* \> *Map Network Drive*. Pick any drive letter that is helpful for you and set the Folder to be one of the paths above. Choose to connect using a different user name and set the user to be your SCF login and the password to be that of your samba account.
macOS Finder

To mount your home directory, choose *Go* \> *Connect to Server...* from within the Finder. Enter one of the paths above. In the connection window, enter *SCF* for Workgroup or Domain, your SCF username and your samba password.

## sshfs for Mac OS X and Linux

If you're on a Mac, download and install both "FUSE for macOS" and SSHFS from the FUSE for macOS website

. If you're on Linux, install sshfs. Here is an example terminal session to mount your SCF home directory:

```{code} shell-session
mkdir ~/scf
sshfs username@SOME_SCF_HOST.berkeley.edu: ~/scf

# to detach later ; umount is /sbin/umount on macOS
umount ~/scf
```

Feel free to contact us if you need help.

## Linux File Managers

The GNOME, KDE, and Xfce file managers all support navigating SSH. For nautilus, type 'nautilus' at the command prompt. A graphical file manager will open. You can then go to 'File > Connect to Server', select 'SSH' under type and your favorite SCF machine as the 'Server'. Then fill in the folder you want to open (generally your home directory on the SCF as a full path, such as /accounts/grad/username. This will allow you to move files by drag-and-drop.
