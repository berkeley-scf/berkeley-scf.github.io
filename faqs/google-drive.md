---
title: "Using Google Drive (aka bDrive)
---

## What is Google Drive (aka bDrive)?

According to a [knowledgebase
article](https://berkeley.service-now.com/kb?id=kb_article_view&sys_kb_id=c71222486f7339005aa3cbbbbb3ee411),
this service provides:

- Long term support from campus
- Easy to set up and use
- Strong collaborative editing features (multiple people can edit
  simultaneously)
- Fully integrated with other Google Apps, including bMail, bCal and
  Contacts
- Convenient built-in poll/survey tool - Google Forms
- Strong search capabilities
- Data is encrypted in transit and at rest
- Collaborate with colleagues outside of UC Berkeley using free Google
  accounts
- Mobile apps for
  [Apple](https://support.google.com/drive/answer/2424384?co=GENIE.Platform%3DiOS&hl=en)
  or [Android](http://www.google.com/mobile/)

## Connecting to Google Drive from Mac and Windows

See [here](https://www.google.com/drive/download) to download the Google
Drive application that will automatically sync between your computer
(Mac or Windows), phone, or tablet and your Google Drive account.

The Google Drive application is also installed on the SCF Macs, so you
can use it to sync between your SCF account and your Google Drive
account. Here are some instructions (similar to what you would do on
your own machine but without the business of having to use a directory
outside of your home directory).

1.  Prepare the local directory on the SCF machine by creating a folder
    `/var/tmp/your_username/gdrive` (you can choose a different
    location/folder name, but it's best to put it within
    /var/tmp/your_username.
2.  Open the Finder and navigate 'Go -\> Go to Folder'. Find
    `/var/tmp/your_username/gdrive` and drag it to the Favorites area in
    the left panel
3.  Now open the Google Drive application and click on the triangular
    Google Drive logo icon in bar on the upper right of your Mac desktop
4.  Click on Sign In and login to the Google account (e.g., your
    \@berkeley.edu account) for which you want to access your Google
    Drive content
5.  Click through some information windows. You will arrive a window
    that says "Whooops we ran into a problem" related to not being able
    to sync to a folder in your home directory because your home
    directory is on the network.
6.  Choose to change the folder, selecting
    `/var/tmp/your_username/gdrive` from the Favorites area.
7.  Select 'Start Sync'

Note that you can always disconnect the local machine from Google
Drive - this keeps the files on the local machine but does not keep them
synced. Just choose 'Preferences -\> Account -\> Disconnect Account'
after clicking on the Google Drive menu icon.

## Automating access to Google Drive on the SCF Linux machines

You can programmatically copy files to and from your Google Drive
account from the command line. This allows you to avoid having to
point-and-click via a web browser to upload and download files, which is
particularly a pain when dealing with many files.

First, create a directory on an SCF machine to use to sync your Drive
files, e.g.:

:::{code} shell
arwen$ mkdir ~/gdrive
arwen$ cd ~/gdrive
:::

Second, initialize the Google drive tool and authenticate to Google:

:::{code} shell
drive init
:::

This will print out a URL. Go to that URL via a browser on which you are
logged into your \@berkeley.edu account. Copy the magic token and paste
it at the terminal prompt.

You're now set up to push and pull files between Google Drive and your
local directory. Simply typing 'drive' in the terminal will bring up
some help information about potential commands you can use.

We'll illustrate basic usage of the push and pull commands. The
following will copy all files from Google Drive to the current directory
on the SCF machine.

:::{code} shell
drive pull
:::

Now suppose you want to copy files to Google Drive. Simply move or copy
them into the current directory, and then use the push command. Here's
an illustration with a simple test file. When you've completed the
following, you should be able to see the newly-added files via a web
browser pointing to your Google Drive directory.

:::{code} shell
echo "some text" > testfile
drive push
:::
