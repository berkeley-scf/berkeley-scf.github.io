---
title: "How do I copy files to or from my account?"
---
Below we describe a variety of ways of securely transferring files to
and from the SCF using variations on SFTP/SCP.

Other options include:

- You can also have your SCF home directory
  <a href="/node/4183" data-entity-substitution="canonical"
  data-entity-type="node"
  data-entity-uuid="380916b5-c828-4fc5-b7b8-0f260225b118">represented on
  your personal computer as a local drive</a>.
- You can use the
  <a href="/node/5261" data-entity-substitution="canonical"
  data-entity-type="node"
  data-entity-uuid="77eba9df-89ab-4b67-a5ff-f68a5ff5e3d7">Globus data
  transfer service</a>.
- You can use <a href="/node/7392" data-entity-substitution="canonical"
  data-entity-type="node"
  data-entity-uuid="a07d448c-8969-475e-8f5c-e3c7090477ec">rclone</a> to
  transfer files to and from bDrive (Google Drive), Box, and Dropbox,
  among other resources.
- And you can of course use
  <a href="/node/4243" data-entity-substitution="canonical"
  data-entity-type="node"
  data-entity-uuid="1ac8e2e5-b616-4552-8317-b31af0de2344">Git</a>, with
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
2.  Enter your favorite SCF machine in "Server".
3.  Enter your SCF credentials under Username/Password.
4.  "Path" is the location on the SCF you want to transfer files
    to/from. This may be your home directory (/accounts/something/you),
    your web area (/accounts/web/public/you), or another location. If
    you leave this blank it will automatically use your home directory.

### Mac or Linux: SFTP

You can start sftp from a UNIX terminal (on either a Mac or Linux
machine) in much the same way you start ssh, e.g. '**sftp
username@remotehost**'. Once you are connected, the environment
functions like traditional ftp:

    $ sftp scf1@arwen.berkeley.edu
    scf1@arwen.berkeley.edu's password:
    sftp> cd /tmp
    sftp> put paper.txt
    Uploading paper.txt to /tmp/paper.txt
    sftp> get chart.eps
    Fetching /tmp/chart.eps to chart.eps
    sftp> quit

### Mac or Linux: SCP

SCP is useful for non-interactive file copying, once again from a UNIX
terminal on either a Mac or Linux machine. The following will
copy `file` into the user's home direcory on the remote side:

    $ scp file scf1@arwen.berkeley.edu:
    scf1@gimli.berkeley.edu's password: 
    file                100% |*****************************|   595       00:00

The following will copy the remote directory `dir/` to the local
directory `dir2/` via the '-r' (recursive) command-line switch:

    $ scp -r scf1@arwen.berkeley.edu:dir dir2/
    scf1@arwen.berkeley.edu's password:$ 
    ls dir2/ dir

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
