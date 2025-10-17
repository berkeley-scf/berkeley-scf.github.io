---
title: "Samba"
---

The SCF's Samba service enables you to access your files as a network volume
on your computer.

## Configuration

In the instructions below, `username` will be your SCF user name and the password will be this samba password.

::: {note}
When accessing your Samba share from an off-campus network, you will need to
use the campus VPN.
:::

At present, we must manually setup a separate login credentials for you to
access your files. Please contact manager@stat.berkeley.edu to facilitate
setting your samba password.

| Directory | Mac                             | Windows                        |
|-----------|---------------------------------|--------------------------------|
| Home      | smb://scf.berkeley.edu/username | \\\\scf.berkeley.edu\\username |
| Web       | smb://scf.berkeley.edu/www      | \\\\scf.berkeley.edu\\www      |


## Microsoft Windows

In any Windows Explorer window, select *Tools* \> *Map Network Drive*. Pick any drive letter that is helpful for you and set the Folder to be one of the paths above. Choose to connect using a different user name and set the user to be your SCF login and the password to be that of your samba account.
macOS Finder

To mount your home directory, choose *Go* \> *Connect to Server...* from within the Finder. Enter one of the paths above. In the connection window, enter *SCF* for Workgroup or Domain, your SCF username and your samba password.
