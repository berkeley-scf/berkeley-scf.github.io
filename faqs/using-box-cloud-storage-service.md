---
title: "Using the Box cloud storage service"
---
## What is Box?

Campus has an agreement with Box to provide storage for Berkeley
faculty, staff, and students. This enables to freely upload your
documents and data sets to Box and share those files with collaborators.
According to the [bConnected project
page](http://bconnected-project.berkeley.edu/collaboration-tools/box/),
this service provides:

- Unlimited (as of August 2015) free, secured, and encrypted content
  storage of files with a maximum file size of 15 Gb (However other
  information provided by campus indicates a maximum upload size of 5 GB
  using the Web and 200 MB when using smart phones)
- Encrypted storage of all files
- File preview for many formats (i.e., PDF, Word, Excel, etc.)
- Access to content via desktop and laptop browsers, and through mobile
  devices running iOS and Android
- Secure synchronization of files between desktops and laptops
- Collaboration and file sharing with anyone who has an email address —
  inside or outside the University
- File and folder access control with a range of user/group permissions
  from preview-only to full editing and collaboration rights
- Permissions control for access, preview, editing, download, and
  sharing
- Capacity to password-protect confidential documents and set expiration
  dates for file access
- Ability to edit MS Office documents online
- Ability to create simple workflows, task assignments, and comment on
  files

## Connecting to Box

To access this service via your CalNet credentials, please visit the [UC
Berkeley Box landing page](https://berkeley.box.com).

You can [download software](https://berkeley.box.com/settings/sync) for
your personal computers so that you do not need to transfer files
exclusively through the web interface. This software has been installed
on SCF managed Macs and can be accessed through System Preferences \>
Box Sync.

You can transfer files between SCF Linux machines (or Savio) and Box
using rsync from the UNIX command line. See the [Savio instructions on
how to do
this](https://docs-research-it.berkeley.edu/services/high-performance-computing/user-guide/data/transferring-data/rclone-box-bdrive/).
Simply replace dtn.brc.berkeley.edu with the name of an SCF Linux
machine.

## Collaborator Uploads

In addition to being able to share large datasets with your
collaborators over this service, you can also enable them to upload data
to your Box storage.

- Once logged in to [http://berkeley.box.com](http://berkeley.box.com/),
  click the New... button and choose to create a new folder.
- When prompted, invite your collaborators to upload files to that
  folder. Their access type should be set to "Uploader".
- Your collaborators will receive an email letting them know that they
  can upload files to your Box storage. If they do not already have a
  Box account, Box will prompt them to establish one before they can
  upload.

## Storage and your SCF Home Directory

If you have or plan to have a lot of files in your Box account and you
would like to keep a Box-synced folder on SCF machines, you may wish to
locate this folder outside of your home directory. For example, you
might consider running:

    mkdir /var/tmp/$USERNAME
    chmod 700 /var/tmp/$USERNAME

(where \$USERNAME is your SCF user name) on whichever SCF machine you
use most often and specify that directory as the one to sync with. This
would prevent your Box storage from overflowing your SCF home directory.
You would also benefit from increased access to local disk without
having to worry about backups or the machine getting reinstalled.

This is only a suggestion however, not a requirement.
