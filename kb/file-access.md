---
title: File Access
---

## Basics

A file may have three types of permission: read (`r`), write (`w`), and
execute (`x`). Each permission may be `on` or `off` for each of three
categories of users: the file's owner; other people in the same group as
the owner; and all others. To find out a file's mode, or permission
settings, use the command `ls -l filename`. The output will be of the
form:

:::{code} shell-session
-rwxr-x--x 1 owner group 2300 Jul 14 14:38 filename
:::

The string of 10 characters at the left shows the mode. The initial `-`
indicates that the file is a plain file; a `d` would indicate a
directory. Characters 2-4 are, respectively, `r`, `w`, or `x` if the
corresponding permission is turned on for the owner or `-` if the
permission is turned off. Characters 5-7 similarly show the permissions
for the group; characters 8-10 for all others.

To change the mode of a file, use the chmod command.

## Symbolic Mode

The general form is:

:::{code} shell-session
chmod X@Y file1 file2 ...
:::

where X is any combination of the letters `u` (for owner), `g` (for
group), `o` (for others), `a` (for all; that is, for `ugo`); @ is either
`+` to add permissions, `-` to remove permissions, or `=` to assign
permissions absolutely; and Y is any combination of `r`, `w`, `x`.
Examples:

:::{code} shell-session
# Give the owner rx permissions, but not w 
chmod u=rx file
 
# Deny rwx permission for group and others 
chmod go-rwx file       

# Give write permission to the group
chmod g+w file

# Give execute permission to everybody
chmod a+x file1 file2

# OK to combine like this with a comma
chmod g+rx,o+x file     
:::

## Octal (Numeric) Mode

Permissions can also be set using octal (base-8) numbers, where each digit
represents the permissions for owner, group, and others respectively. Each
permission has a numeric value:
- `r` (read) = 4
- `w` (write) = 2
- `x` (execute) = 1

Add these values together for each category. For example:

:::{code} shell-session
# rwxr-xr-x (755): owner=rwx(7), group=rx(5), others=rx(5)
chmod 755 file

# rw-r--r-- (644): owner=rw(6), group=r(4), others=r(4)
chmod 644 file

# rwx------ (700): owner=rwx(7), group=none(0), others=none(0)
chmod 700 file

# rw------- (600): owner=rw(6), group=none(0), others=none(0)
chmod 600 file
:::

Common patterns:
- **755** for directories and executable files (owner can do everything, others can read and execute)
- **644** for regular files (owner can read/write, others can only read)
- **700** for private directories (only owner has access)
- **600** for private files (only owner can read/write)

## Recursive Changes

To change permissions for a directory and all its contents, use the `-R` flag:

:::{code} shell-session
# Make all files in a directory readable by group
chmod -R g+r directory/

# Set directory permissions recursively
chmod -R 755 directory/
:::

## Groups

Regular accounts on SCF are generally assigned to the groups `faculty`,
`grad`, or `projects`. To find out what groups you are in, type the
command `groups`.

## Directories

The same permission scheme applies to directories. For a directory, read
permission gives the ability to list files in it via the ls command (and
thus to discover what file names are); write permission gives the
ability to create and delete files in it; execute permission gives the
ability to access a file or subdirectory of known name (even without
read permission).

**Important**: Directories typically need execute permission (`x`) to be
usable. Without it, you cannot `cd` into the directory or access files
within it, even if you have read or write permission.

To find out the mode of a directory:

:::{code} shell-session
# Show permissions for the named directory(ies)
ls -dl dir ...

# Long list of all files in named directory(ies) (including those with names starting in `.`)
ls -al dir ...
:::

If no directories are specified, the listing is for all files in the
current directory. The output will look something like:

:::{code} shell-session
drwx------  12  perito      592 Jul 11 13:46 .
drwxr-xr-x  24  stat       1424 Jul 10 13:07 ..
:::

The initial `d` in the 10-character mode string indicates that the file
is a directory. The file name `.` always refers to the current
directory; the file name `..` always refers to the parent of the current
directory. Thus, this output shows the permissions for the current
directory and its parent.

## Default Permissions with umask

When you create new files and directories, their default permissions are
determined by your `umask` setting. The umask value is subtracted from the
default permissions (666 for files, 777 for directories).

To see your current umask:

:::{code} shell-session
umask
:::

To set a new umask (for the current session):

:::{code} shell-session
# Set umask to 022 (new files: 644, new directories: 755)
umask 022

# Set umask to 077 (new files: 600, new directories: 700 - private)
umask 077
:::

## Special Permissions

In addition to read, write, and execute, there are three special permission
bits:

- **Setuid (4000)**: When set on an executable file, it runs with the
  permissions of the file's owner
- **Setgid (2000)**: When set on an executable, it runs with the group's
  permissions. When set on a directory, new files inherit the directory's
  group
- **Sticky bit (1000)**: When set on a directory, only the file owner can
  delete or rename files within it (useful for shared directories like `/tmp`)

Example:

:::{code} shell-session
# Set the sticky bit on a shared directory
chmod +t shared_directory/

# Set setgid on a directory (new files inherit the group)
chmod g+s shared_directory/
:::

## Access Control Lists (ACLs)

Modern systems support Access Control Lists (ACLs), which provide more
fine-grained control than traditional Unix permissions. ACLs allow you to
set different permissions for multiple users and groups on the same file.

To view ACLs:

:::{code} shell-session
ls -le filename
:::

For more information on ACLs, see `man chmod` and look for the ACL-related
options.

## Further Reading

For more information, see `man chmod`, `man ls`, and `man umask`.
