---
title: "Request file restoration from backups"
---
The weekly backups are performed at 10pm. In order for a file to be
restored, the file must be present in your home directory at 10pm to be
copied to tape. We back up account directories, but do not backup
temporary filesystems such as /scratch, /tmp, or /var/tmp.

## Requesting File Restoration

Please fill out [our form](http://goo.gl/5xYPbY) if you need to have
files restored from backup tapes. Please be prepared to supply the
following information:

1.  The absolute pathnames of each file/directory you want restored,
    e.g. `/accounts/projects/joe`, or just `~joe/pathname` if you are
    user joe and the pathname is in your home directory.
2.  The date and time they were created
3.  The date and time they were deleted
4.  The date and time the files were last modified (very important)

Usually the restorations can be done within 24 hours of the request. The
files can usually be reconstructed to their state prior to the last
backup which was done before they were destroyed.

## Backup Schedule

1.  Weekly back-ups are performed on Sunday night at 10:00 pm. A weekly
    backup reflects the content of the files prior to the time of the
    creation of the previous monthly backup tape. Incremental changes to
    files can be recovered on a weekly basis from subsequent weekly
    backup tapes for up to five weeks.
2.  Monthly back-ups are performed on the first Sunday night of each
    month between the hours of 5:00pm and 12:00 midnight. Monthly backup
    tapes are retained for 6 months before being rotated on a new cycle.
    A monthly backup tape reflects the content of the files prior to the
    time of the creation of the previous monthly backup tape.

## Disaster Recovery

The SCF backs up data off-site monthly for recovery in
the event of a catastrophic disaster, for example, damage to Evans Hall
resulting from either an earthquake, fire, or bomb.
