---
title: Encrypt a file or folder
---
You can use PGP encryption to do this with the command-line tool
`gpg`.

## Turn a directory into a file

If you want to encrypt a directory, you will need to convert it to a
file first. Run the command:

:::{code} shell-session
tar czf myfiles.tar.gz mydirectory/
:::

This gives you a new file 'myfiles.tar.gz' which you can then
encrypt/decrypt. To turn a tarball back into a directory:

:::{code} shell-session
tar xzf myfiles.tar.gz
:::

## Prepare GPG

You will need to create a key pair (public and private keys) with which
you will encrypt and decrypt your files. Type

:::{code} shell-session
gpg --gen-key
:::

You will be prompted to enter some security information. Use the
defaults when available, otherwise enter your name and email address.
You will also be prompted for a passphrase. Remember this passphrase,
as you will need it to decrypt files later.

## Encrypt

To encrypt a file, type

:::{code} shell-session
gpg -e -r YOUR_EMAIL filename
:::

where `filename` is the name of the file you want to encrypt and
`YOUR_EMAIL` is the email address you used when creating your GPG key.
This command will create *filename.gpg*. At this point you may choose
to remove *filename* in favor of the encrypted file *filename.gpg*.

## Decrypt

To decrypt the file, type

:::{code} shell-session
gpg -d -o decrypted filename.gpg
:::

You will be prompted to enter your passphrase. This will create the new
file *decrypted* containing the unencrypted contents.
