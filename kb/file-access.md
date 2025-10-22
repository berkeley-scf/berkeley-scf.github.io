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
-rwxr-x--x 1 owner      2300 Jul 14 14:38 filename
:::

The string of 10 characters at the left shows the mode. The initial `-`
indicates that the file is a plain file; a `d` would indicate a
directory. Characters 2-4 are, respectively, `r`, `w`, or `x` if the
corresponding permission is turned on for the owner or `-` if the
permission is turned off. Characters 5-7 similarly show the permissions
for the group; characters 8-10 for all others.

To change the mode of a file, use the chmod command. The general form
is:

:::{code} shell
chmod X@Y file1 file2 ...
:::

where X is any combination of the letters `u` (for owner), `g` (for
group), `o` (for others), `a` (for all; that is, for `ugo`); @ is either
`+` to add permissions, `-` to remove permissions, or `=` to assign
permissions absolutely; and Y is any combination of `r`, `w`, `x`.
Examples:

:::{code} shell
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
read permission). To find out the mode of a directory:

:::{code} shell
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

For more information, including octal specification of permissions, see
`man chmod`, `man ls`, `man umask`.
