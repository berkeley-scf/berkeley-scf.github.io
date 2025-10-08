---
title: "Background Processes"
---
## bash

Unix has the ability to run your program in the background. This means
that instead of waiting for the program to finish execution, the UNIX
shell prompts you again and you can run other commands at the same time
that the background process is running. To run the program `myprog` in
background, type:

    myprog &

The shell will respond with a number, its process identification number
(or PID) and then return to the prompt.

More generally, you can use `nohup` to leave a big job running in the
background even after you logout. For example, to keep the program
`myprog` running in background, type:

    nohup myprog &

For example, to run your R job in the background:

    nohup R CMD BATCH --no-save code.R code.log &

<span style="letter-spacing: 0px;">With a Matlab job, where we redirect
the output to outfile.txt and the error messages to error.txt:</span>

    nohup matlab -nodesktop -nodisplay < infile.m > outfile.txt 2> error.txt &

## screen

You may alternatively choose to use **GNU screen** to run your jobs so
that you can leave them running when you logout. Just invoke `screen`
from your shell, type a space or carriage return to dismiss the startup
message, then start your job. When you want to detach, type Control-a
followed by Control-d. You can then exit from your terminal session.
When you want to access your job again, connect to the same machine your
job is running on and type `screen -r`. Note that `screen` is likely to
be more robust than `nohup` in terms of ensuring your job is not killed
by ending a remote login session abruptly (e.g., closing your laptop,
losing your wireless connection, etc.).

A few more details on `screen`. To see a list of available sessions, do
`screen -ls`. To start a session with a specific name, you can do
`screen -S sessionName`. Then to resume a named session, do
`screen -r SessionName`. Or to resume a particular unnamed session, use
the name reported by `screen -ls`, e.g., it might look something like
4763.pts-2.beren. If a session is in use, you can forcibly detach it
from the other location and attach to it by doing
`screen -d -R sessionName`. To close a session, you can use `exit` from
within the session.
