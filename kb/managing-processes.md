---
title: Managing UNIX processes
---

## Display Process Information

### The 'ps' command

The output of `ps` will indicate the name of the program, its
process I.D., and the amount of CPU time it has consumed so far.

1.  To display information about a specific user's processes:

    :::{code} shell-session
    ps -U USERNAME
    :::

    where USERNAME is your username

1.  To display information about a specific running program:

    :::{code} shell-session
    ps -ef | grep PROGRAM
    :::

    where PROGRAM is the program's name

See `man ps` for additional information.

## Killing Processes

To kill a running program, type:

:::{code} shell-session
kill PID
:::

where PID is the process I.D. obtained by running `ps`.

If the first form does not kill your process, try

:::{code} shell-session
kill -9 PID
:::

To kill all your background processes, execute:

:::{code} shell-session
kill 0
:::

## Input and Output

Most programs initially inherit the current terminal or pseudo-terminal
for doing input and output. This means that these programs have a
'controlling terminal'. The controlling terminal', and therefore all
output, is lost if you logout before your background job completes. To
avoid this loss, you should either code your program to read all input
and write all output to specific files, or your should redirect input
and output for the program by using the shell operators: \<, \>, \>\>,
and \>&.

It is recommended that you redirect standard output and standard error
to a log file for all programs run in the background. For example:

:::{code} shell-session
myprog >& logfile &
:::

will run `myprog` in the background, redirecting all output to the file
`logfile` in the current directory. See `man bash` for details on shell
redirection operators.

### Hints to Improve Efficiency

Some people run 2-hour CPU-time jobs only to discover afterwords that
the program didn't even do what they wanted. Avoid this. Debug your
program using small test cases until you're sure you've got it right.
Only then should you run the big monster.

### Timing Jobs

Two common questions when running big jobs are: How do I find out the
running time? and How do I capture the program output which would
normally go to the screen?. Here is one simple way to do both (as:

:::{code} shell-session
% nice -n 19 /usr/bin/time program-name >& ouput-filename
:::

Where program-name is the name of your program and ouput-filename is the
name of the file in which you want to capture output. The running time
will be the last line of the output file, formatted like this:

:::{code} shell-session
60.0 real        10.0 user         0.5 sys
:::

In this example, the cpu time used was 10.5 seconds (10.0 user + 0.5
sys) and the elapsed (wall-clock) time was 60.0 seconds. By division,
your program used 10.5/60 or just over 1/6th of the available cpu time
while it ran.

### Running sequential jobs

If your programs are 'prog1', 'prog2' and 'prog3', you can run them in
background via the shell command:

:::{code} shell-session
(prog1 ; prog2 ; prog3) >& log &
:::

Another way is to use a semicolon:

:::{code} shell-session
run1 >& run1.log ; run2 >& run2.log
:::

where run1 and run2 are the programs you wish to run and run1.log and
run2.log are the logfiles.

Yet annother way is to set up a shell script file, for example
'`run_all`', containing:

:::{code} shell-session
#!/bin/sh run1 >& run1.log run2 >& run2.log
:::

By specifying the \> sign, you save the output from run1 into file
run1.log. By also including the & sign, it also saves any error message
output into run1.log.

Then from the unix prompt:

:::{code} shell-session
% chmod +x run_all
:::

to allow the script to be executable, and then type:

:::{code} shell-session
./run_all
:::

to run the script. You could also type:

:::{code} shell-session
./run_all &
:::

to have it run in the background.

## Scheduling Jobs

The `at` and `batch` commands allow the system to queue up big
jobs and run them at a later time. `at` allows you to specify when
the commands should be executed, while jobs queued with `batch` will
execute as soon as the system load level permits. These commands provide
a mechanism for big jobs to run without slowing down interactive
response and interfering with other people trying to use the computer.

### Queue Execution

To use `at` or `batch`, create a script file which contains the
unix commands you want to run. Suppose your script file is called
'filename'. To run it in batch, type the command:

:::{code} shell-session
batch filename
:::

To run the script at a specific time, use:

:::{code} shell-session
at time date filename
:::

where time is in the form `0815`, `0815am`, `8:15am`, `now`, and `5 pm`;
and date is in the form `Jan 24`, `Friday`, `tomorrow`, and `today`.

If you leave out the date field, the date will default to `today`.

The computer will respond:

:::{code} shell-session
job N at <full date>
:::

where 'N' is the job number it creates. When the job finishes, it will
mail you the output of the script, unless output was redirected. (see
below)

### Shell Features

By default, /bin/bash is used as the shell interpreter for the commands
in your script.

If the commands in your script file need any input, create separate
input files which contain the necessary input and use the '\<' shell
feature in the script file. To redirect the output of a particular
command in your script, use the '\>' shell feature. For example, your
script file might contain the line:

:::{code} shell
proga < inputa > outputa
:::

This would cause the program 'proga' to take its input from the file
'inputa' and send output to 'outputa'.

### Controlling jobs

To find out the status of your jobs, type the command:

:::{code} shell
at -l
:::

This will report both 'batch' and 'at' jobs. If 'N' is the job number
reported by 'at -l' then the command:

:::{code} shell
at -r N
:::

will remove that job from the queue (whether or not it is already
running) and interrupt it (if it is already running).
