---
title: "SSH Keys"
---
SSH key pairs allow users to connect to remote accounts without having
to use the password of the remote account. This is useful if you'd like
to not have to enter the password to an account you own and access
frequently, or if you need to connect to a shared account where you are
not its owner and do not know its password. You create a pair of files
known as "keys", one private and one public, to facilitate this process.
The private key stays on the machine you will connect from which is
usually the machine where it is created (for example, your laptop). The
other key, the public key, is put into the remote account by the owner
of that account (which may be you) or by the server administrator. Think
of this process as leaving a real key (the public key) in a remote door.
The door will only open if you have the associated private key as you
approach. This is why you must keep the private key to yourself,
otherwise people who have a copy of it can pass through all the doors in
which you left your public key.

## On UNIX and macOS

### Generating SSH Keys

You can generate keys with the `ssh-keygen` command:

```{code} shell-session
$ ssh-keygen -t ed25519
Generating public/private ed25519 key pair.
Enter file in which to save the key ($HOME/.ssh/id_ed25519):     
Enter passphrase (empty for no passphrase):  
Enter same passphrase again:  
Your identification has been saved in $HOME/.ssh/id_ed25519.
Your public key has been saved in $HOME/.ssh/id_ed25519.pub.
```

If you already have a keypair with the standard names, you may choose to
create additional keypairs with different names. For security reasons
you should not use empty passphrases.

We recommend that you save the keypair in the suggested location since
ssh will look for them there. If you save the keys elsewhere, you will
need to tell ssh and related programs where to find them when needed.

### Uploading the public key

Once you have generated the key pair, you will need to transfer the
public key, e.g. `~/.ssh/id_ed25519.pub`, to the remote site. You can
transfer the public key in any number of ways, such as by emailing it to
the owner of the remote account or an administrator, or FTP, SCP, or
SFTP if you have access. The public key file is actually just a text
file.

### Installing the public key

Once the key has been transfered to the remote machine, its contents
will need to be appended to `~/.ssh/authorized_keys` within the
remote account. If you are not the owner of the remote account you will
need to have the owner perform this step. Otherwise, on the remote
computer:

```{code} bash
cat id_ed25519.pub >> ~/.ssh/authorized_keys
```

## On Windows

Some modern versions of Windows now ship with the standard OpenSSH
utilities. If your PC has ssh already installed, you can run them from
the Command or PowerShell programs. They will behave as they do on UNIX
and macOS above.

### Putty

The most popular Windows SSH client today is Putty which is available
from <a href="http://www.chiark.greenend.org.uk/%7Esgtatham/putty"
data-_mce_href="http://www.chiark.greenend.org.uk/~sgtatham/putty">http://www.chiark.greenend.org.uk/~sgtatham/putty</a>.
Download the complete Windows installer rather than just the putty.exe
file. You may choose to follow the thorough Putty documentation directly
on how to <a
href="http://the.earth.li/%7Esgtatham/putty/0.60/htmldoc/Chapter8.html#pubkey-puttygen"
data-_mce_href="http://the.earth.li/~sgtatham/putty/0.60/htmldoc/Chapter8.html#pubkey-puttygen">create
an SSH keypair on Windows</a>. Otherwise see the more brief step-by-step
instructions below.

#### Generating SSH Keys

1.  Start the puttygen.exe program included with the Putty installer.
1.  In the *Parameters* section choose SSH2 RSA as the key type and
    press **Generate**. You will need to move your mouse about in the
    small window area in order to generate randomness that the process
    requires.
1.  You may choose to enter a key comment which can be used by you to
    identify the key (useful when you use several SSH keys).
1.  Type in a passphrase and confirm it. The passphrase is used to
    protect your key and you will be asked for it when you connect via
    SSH using public key authentication.
1.  Click **Save private key** to save your private key. A common name
    is **id_rsa**.
1.  Click **Save public key** to save your public key.  A common name
    is **id_rsa.pub**.

#### Uploading and Installing the public key

See the UNIX instructions for these steps above as they are identical.

## Using the SSH Key

### SSH config file

You can explicitly tell your ssh program to use your ssh key and not
your password with `ssh -o preferredauthentications=publickey ...`.
Since you may not want to type that every time, you can configure an ssh
host alias. Create and/or append to the file ~/.ssh/config on your local
computer and enter the following:

```{code} ini
Host somename
HostName your.favorite.machine.berkeley.edu
User theuser
PreferredAuthentications publickey
```

Then you can invoke `ssh somename` and it will pass in all of the
above options.

### SSH Agent

If you do not want to have to type your ssh key's passphrase every time
you run ssh, you can store the key into the program `ssh-agent`. This
program is launched automatically on macOS and most newer Linux systems
when you login to your computer. You would then store the key into your
agent by running `ssh-add`.

ssh-agent can also be set to automatically have access to your SSH keys
each time you login without needing to manually provide the keys with
`ssh-add`. On most newer Linux systems, your ssh keys will be read
into your keychain via programs such as gnome-keychain. On macOS, you
can enable this by running `ssh-add --apple-use-keychain` once. 

If your key is in a non-standard location, you can manually specify it
as a parameter, for example `ssh-add /path/to/the/ssh/key`.

#### One-time Invocation

If your ssh-agent is running but it is not working properly with your
desktop session, you can run the following so that it works in your
current terminal:

```{code}  bash
eval `ssh-agent -s`
```

If your desktop environment has not started ssh-agent for you
automatically, you can launch a per-terminal instance instead:

```{code} shell-session
$ exec ssh-agent $SHELL
$ ssh-add
```
