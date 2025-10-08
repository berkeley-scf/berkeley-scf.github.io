---
title: "Using rclone"
---
*rclone* is a command-line tool that can connect to Dropbox, Box, Google
Drive, sftp servers, and a many other file services.

## Initial Configuration

The instructions here assume you are in a terminal on an SCF machine,
but also that you can install rclone on your local machine where you can
open a browser window for the graphical authentication process.  If you
run into problems, please ask us. Note that in the examples below for
Dropbox and Google, the service order may change. For example Dropbox
may not be entry \#7 depending on the version of rclone available.

### Dropbox

You only need to configure rclone for Dropbox once. These instructions
assume you are in a terminal session on an SCF Linux machine, and that
you can open a browser on that machine. In a terminal window:

    scf:~$ rclone config
    n) New remote
    s) Set configuration password
    q) Quit config
    n/s/q> n
    name> dropbox
    Type of storage to configure.
    Choose a number from below, or type in your own value
    ...
     7 / Dropbox
       \ "dropbox"
    ...
    Storage> 7
    Dropbox App Client Id - leave blank normally.
    client_id>
    Dropbox App Client Secret - leave blank normally.
    client_secret>
    Remote config
    Use auto config?
     * Say Y if not sure
     * Say N if you are working on a remote or headless machine
    y) Yes
    n) No
    y/n> n
    For this to work, you will need rclone available on a machine that has a web browser available.
    Execute the following on your machine:
        rclone authorize "dropbox"

At this point you would run \`rclone authorize dropbox\` in a second
terminal. This will open a web browser where you log into Dropbox and
permit rclone to access files. rclone will paste a long string into the
second terminal. Copy that string and pasted it into the first terminal.

<span style="font-family: &quot;Courier New&quot;, &quot;DejaVu Sans Mono&quot;, monospace, sans-serif; font-size: 1em; white-space: pre-wrap;">result\>
**{"access_token":"abc1234...","token_type":"bearer","expiry":"0001-01-01T00:00:00Z"}**</span>

    --------------------
    [dropbox]
    type = dropbox
    client_id =
    client_secret =
    token = {"access_token":"abc1234...","token_type":"bearer","expiry":"0001-01-01T00:00:00Z"}
    --------------------
    y) Yes this is OK
    e) Edit this remote
    d) Delete this remote
    y/e/d> y
    Current remotes:
    Name                 Type
    ====                 ====
    dropbox              dropbox
    e) Edit existing remote
    n) New remote
    d) Delete remote
    r) Rename remote
    c) Copy remote
    s) Set configuration password
    q) Quit config
    e/n/d/r/c/s/q> q

### Google Drive

    scf:~$ rclone config
    ...
    e/n/d/r/c/s/q> n
    name> drive
    Type of storage to configure.
    Enter a string value. Press Enter for the default ("").
    Choose a number from below, or type in your own value
    ...
    12 / Google Drive
       \ "drive"
    ...
    Storage> 12
    client_id>
    client_secret>
    scope> 1
    service_account_file>
    Edit advanced config? (y/n)
    y/n> n
    Remote config
    Use auto config?
    y/n> n
    If your browser doesn't open automatically go to the following link: https://accounts.google.com/o/oauth2/auth?access_type=offline&client_id=...longstring...
    Log in and authorize rclone for access
    Enter verification code> {{ enter code from browser }}

The documentation for the campus cluster, Savio, describes [how to
configure rclone for
bDrive](https://docs-research-it.berkeley.edu/services/high-performance-computing/user-guide/data/transferring-data/rclone-box-bdrive/) and
may also be helpful.

### Box

The documentation for the campus cluster, Savio, describes [how to
configure rclone for
Box](https://docs-research-it.berkeley.edu/services/high-performance-computing/user-guide/data/transferring-data/rclone-box-bdrive/),
and following those instructions should work. Let us know if they don't.

## Using rclone

Test your configuration by listing the files in your Dropbox:

    scf:~$ rclone ls dropbox:
    ... lists your Dropbox files...

    scf:~$ rclone ls drive:
    ... lists your Drive files...

Sync a file/directory to/from dropbox:

    scf:~$ rclone sync dropbox:path-to-file-or-folder ~/place/i/want/to/sync/to/
    scf:~$ rclone sync some/dir/on/scf dropbox:

Since *rclone sync* can drastically change the contents of the
destination location, you may want to append the --dry-run option to
rclone at first, just to see what it would do before it does it. Then
repeat without it to actually make changes.

### Dropbox Limitations

There are some limitations mentioned on <https://rclone.org/dropbox/>:

> Note that Dropbox is case insensitive so you can’t have a file called
> “Hello.doc” and one called “hello.doc”. There are some file names such
> as thumbs.db which Dropbox can’t store. There is a full list of them
> in the “Ignored Files” section of this document. Rclone will issue an
> error message File name disallowed - not uploading if it attempts to
> upload one of those file names, but the sync won’t fail. If you have
> more than 10,000 files in a directory then rclone purge dropbox:dir
> will return the error Failed to purge: There are too many files
> involved in this operation. As a work-around do an rclone delete
> dropbox:dir followed by an rclone rmdir dropbox:dir.
