---
title: "Secure Shell (SSH)"
---

## Introduction

SSH provides a secure means to access a UNIX command-line shell on a
remote computer. It also provides a way of transfering files and
securing otherwise unsafe protocols.

The term 'SSH' may be used to name the secure connection protocol and
the name of the primary program that implements the protocol.

## Getting SSH software on your personal machine

- macOS comes with SSH preinstalled. Just open Terminal.app in
  `/Applications/Utilities/`.
- Windows users have several options:
  - Newer versions of Windows have ssh built-in. You can access it in a
    Command Prompt (cmd.exe) window.
  - The old standby for many years is a free program called **putty**
    available at http://www.chiark.greenend.org.uk/%7Esgtatham/putty/.
    You may choose to download putty as a single executable file which
    can be stored wherever you find it convenient, or as an installer
    which provides several other programs such as scp and sftp.
  - A newer option that many people like is
    [MobaXterm](https://mobaxterm.mobatek.net/download.html). The free
    version has a number of features, including tabbed SSH terminals,
    built-in X11 forwarding of graphical windows from the remote Linux
    server, and RDP service.
  - An alternative for Windows is [Ubuntu on
    WSL](https://ubuntu.com/wsl), a complete Ubuntu terminal environment
    on Windows 10.
- Linux distributions usually install SSH by default. If not, you will
  need to use your distribution's software management program to install
  SSH. You can open any terminal window such as `gnome-terminal`,
  `konsole`, or `xterm` to run SSH.
- You can also interact with the SCF machines using the remote SSH
  functionality of the [code editor
  VSCode](https://code.visualstudio.com/docs/remote/ssh).

## Basic usage

The most common way of logging into a remote site from the command-line
is with '**ssh username@remotehost**'. An alternative is '**ssh -l
username remotehost**'. If your local username is the same as your
remote username, you needn't specify it on the command line, e.g. '**ssh
remotehost**'. **putty** uses a graphical user interface to set the
username and remotehost.

We have a [variety of servers](../servers/login-servers.md) that you can login to,
one of which is called `arwen.berkeley.edu`. Here's an example command-line
login to arwen:

    me@my-laptop$ ssh myusername@arwen.berkeley.edu
    The authenticity of host 'arwen.berkeley.edu (128.32.135.115)' can't be established.
    RSA key fingerprint is 5e:c2:af:be:bc:15:09:6f:5a:74:b1:e9:3a:45:bf:f6.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added 'arwen.berkeley.edu,128.32.135.115' (RSA) to the list of known hosts.
    myusername@arwen.berkeley.edu's password: 
    You have mail.
    ...
    arwen:~$ 

Whenever SSH connects to another computer, it receives a digital
fingerprint of that computer. If you are connecting to a computer for
the first time, it asks whether you want to continue, and then saves the
fingerprint for the next time you want to connect. If you have connected
to that computer before, it checks to make sure that the fingerprint is
the same as it was the first time you connected to that machine. If the
fingerprints are different, it will warn you that someone might have
installed nefarious ssh software on the remote host. This is useful
because bad people to break into computer seldom know the passphrase
that the remote administrator used to generate the fingerprint with.

## Authentication Failures

If there are too many unsuccessful SSH connection attempts from your IP
address, the computer you are trying to connect to will temporarily
block you. It interprets this behavior as a brute force ssh attempt. The
block applies to attempts from outside the SCF network and not inside,
so if this happens, so you can connect to a blocked SCF machine from an
unblocked one. This might be useful if you have some local data stored
on the blocked machine. You can also just connect to any other SCF
machine where you are not blocked.

You can reduce the number of unsuccessful SSH attempts by setting up
[public key authentication with SSH keys](./ssh/ssh-keys.md).
