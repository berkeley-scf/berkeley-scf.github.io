---
title: "How do I copy files to or from my account?"
---
Below we describe a variety of ways of securely transferring files to
and from the SCF using variations on SFTP/SCP.

Other options include:

- You can also have your SCF home directory [represented on your personal computer as a local drive](/faqs/mount-homedir)
- You can use the [Globus data transfer service](/faqs/using-globus-file-transfers).
- You can use [rclone](/faqs/using-rclone) to transfer files to and from bDrive
  (Google Drive), Box, and Dropbox, among other resources.
- And you can of course use [Git](/faqs/git), with
  local copies of your repository on your personal computer and in your
  SCF home directory.

SFTP has replaced FTP as the standard way of copying user files. Since
FTP transmits passwords without encryption, it can only be used for
anonymous uploads and downloads.

### Mac or Windows: Cyberduck

[Cyberduck](http://cyberduck.ch) is a cross-platform application with
SFTP support. When configuring a new connection (on a Mac: File \> Open
Connection):

1.  Specify "SFTP (SSH File Transfer Protocol)" as the protocol.
1.  Enter your favorite SCF machine in "Server".
1.  Enter your SCF credentials under Username/Password.
1.  "Path" is the location on the SCF you want to transfer files
    to/from. This may be your home directory (`/accounts/something/you`),
    your web area (`/accounts/web/public/you`), or another location. If
    you leave this blank it will automatically use your home directory.

### Mac or Linux: SFTP

You can start sftp from a UNIX terminal (on either a Mac or Linux
machine) in much the same way you start ssh, e.g. `sftp
username@remotehost`. Once you are connected, the environment
functions like traditional ftp:

```{code} shell-session
$ sftp scf1@arwen.berkeley.edu
scf1@arwen.berkeley.edu's password:
sftp> cd /tmp
sftp> put paper.txt
Uploading paper.txt to /tmp/paper.txt
sftp> get chart.eps
Fetching /tmp/chart.eps to chart.eps
sftp> quit
```

### Mac or Linux: SCP

SCP is useful for non-interactive file copying, once again from a UNIX
terminal on either a Mac or Linux machine. The following will
copy `file` into the user's home direcory on the remote side:

```{code} shell-session
$ scp file scf1@arwen.berkeley.edu:
scf1@gimli.berkeley.edu's password: 
file                100% |*****************************|   595       00:00
```

The following will copy the remote directory `dir/` to the local
directory `dir2/` via the '-r' (recursive) command-line switch:

```{code} shell-session
$ scp -r scf1@arwen.berkeley.edu:dir dir2/
scf1@arwen.berkeley.edu's password:$ 
ls dir2/ dir
```

### Firefox/Seamonkey

A Firefox and Seamonkey add-on called
[FireFTP](http://fireftp.mozdev.org/) supports SFTP. Follow the
directions to install it and then choose Tools \> Web Developer \>
FireFTP. When creating a new connection, go to Connection \> Security
and select SFTP as the protocol. This should work on Mac OS X, Linux,
and Windows.

### Windows: WinSCP

Windows users can use [WinSCP](http://winscp.net) to transfer files
securely.
