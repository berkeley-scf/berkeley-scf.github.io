---
title: Encrypt a file or folder
---
You can use PGP encryption to do this with the command-line tool
`gpg`.

## Choosing an Encryption Method

GPG supports two types of encryption:

1. **Symmetric encryption**: Uses a passphrase only. Simpler and recommended
   for encrypting your own files.
2. **Public-key encryption**: Uses a key pair. Useful for sharing encrypted
   files with others or encrypting to yourself using your GPG identity.

This guide covers both methods.

## Encrypting Directories

If you want to encrypt a directory, you will need to convert it to a
file first. Run the command:

:::{code} shell-session
tar czf myfiles.tar.gz mydirectory/
:::

This gives you a new file 'myfiles.tar.gz' which you can then
encrypt/decrypt.

Alternatively, you can combine tar and encryption in one step, which saves
disk space:

:::{code} shell-session
tar czf - mydirectory/ | gpg -c -o myfiles.tar.gz.gpg
:::

To decrypt and extract in one step:

:::{code} shell-session
gpg -d myfiles.tar.gz.gpg | tar xzf -
:::

To turn a tarball back into a directory manually:

:::{code} shell-session
tar xzf myfiles.tar.gz
:::

## Symmetric Encryption (Recommended for Personal Use)

This method uses only a passphrase - no key generation required.

### Encrypt a file

:::{code} shell-session
gpg --symmetric filename
:::

or using the short form:

:::{code} shell-session
gpg -c filename
:::

You will be prompted to enter a passphrase. This creates *filename.gpg*.
**Important**: If you lose this passphrase, your data is permanently
unrecoverable.

### Decrypt a file

:::{code} shell-session
gpg --decrypt filename.gpg
:::

or to save to a specific output file:

:::{code} shell-session
gpg --decrypt --output decrypted filename.gpg
:::

You will be prompted to enter the passphrase you used when encrypting.

## Public-Key Encryption

This method uses a key pair and is useful for encrypting to your GPG
identity or sharing encrypted files with others.

### Check for existing keys

Before creating a new key, check if you already have one:

:::{code} shell-session
gpg --list-keys
:::

### Generate a key pair

If you need to create a key pair (public and private keys), type:

:::{code} shell-session
gpg --gen-key
:::

You will be prompted to enter some security information. Use the
defaults when available, otherwise enter your name and email address.
You will also be prompted for a passphrase. Remember this passphrase,
as you will need it to decrypt files later. **If you lose this passphrase,
your encrypted data is permanently unrecoverable.**

### Encrypt a file

To encrypt a file, type

:::{code} shell-session
gpg --encrypt --recipient YOUR_EMAIL filename
:::

or using short form:

:::{code} shell-session
gpg -e -r YOUR_EMAIL filename
:::

where `filename` is the name of the file you want to encrypt and
`YOUR_EMAIL` is the email address you used when creating your GPG key.
This command will create *filename.gpg*.

### Decrypt a file

To decrypt the file, type

:::{code} shell-session
gpg --decrypt --output decrypted filename.gpg
:::

or using short form:

:::{code} shell-session
gpg -d -o decrypted filename.gpg
:::

You will be prompted to enter your passphrase. This will create the new
file *decrypted* containing the unencrypted contents.

## Verifying Encryption

To verify that a file is encrypted and see encryption information:

:::{code} shell-session
gpg --list-packets filename.gpg
:::

## Security Considerations

### Securely delete original files

After encrypting a file, simply deleting the original with `rm` may leave
recoverable data on disk. For sensitive data, use secure deletion:

:::{code} shell-session
shred -u filename
:::

The `shred` command overwrites the file multiple times before deleting it,
making recovery much more difficult.

### Backup your keys and remember passphrases

- **Lost passphrases mean lost data**: There is no password recovery for GPG.
  Your encrypted files are permanently unrecoverable without the correct
  passphrase.
- **Backup your private keys**: If using public-key encryption, back up your
  private key in a secure location. You can export it with:
  
  :::{code} shell-session
  gpg --export-secret-keys --armor YOUR_EMAIL > private-key-backup.asc
  :::

  Store this file securely (preferably encrypted with a different method or
  in a password manager).
