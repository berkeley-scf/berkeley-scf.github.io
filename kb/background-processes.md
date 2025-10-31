---
title: "Background Processes"
---

:::{important}
For computationally intensive or long-running jobs, you should use the
cluster rather than running background processes on the login servers.
See [Cluster Documentation](../servers/cluster.md) for details on submitting
jobs to the cluster.
:::

## Basic Background Execution

Unix has the ability to run your program in the background. This means
that instead of waiting for the program to finish execution, the UNIX
shell prompts you again and you can run other commands at the same time
that the background process is running. To run the program `myprog` in
background, type:

:::{code} bash
myprog &
:::

The shell will respond with a number, its process identification number
(or PID) and then return to the prompt.

## Job Control Commands

You can manage background and foreground jobs with these commands:

- `jobs` - List all background jobs
- `fg %1` - Bring job 1 to the foreground
- `bg %1` - Resume job 1 in the background (if it was stopped)
- `Ctrl-Z` - Suspend the current foreground job
- `disown %1` - Remove job 1 from the shell's job table (it continues running)

For example, if you start a job in the foreground and want to move it to
the background:

:::{code} bash
# Start a long-running job (oops, forgot the &)
myprog
# Press Ctrl-Z to suspend it
# [1]+  Stopped    myprog
# Resume it in the background
bg %1
# Detach it from the shell so it continues even if you logout
disown %1
:::

## Using nohup

More generally, you can use `nohup` to leave a big job running in the
background even after you logout. For example, to keep the program
`myprog` running in background, type:

:::{code} bash
nohup myprog &
:::

The output will be written to `nohup.out` by default. You can redirect it:

:::{code} bash
nohup myprog > output.log 2>&1 &
:::

For example, to run your R job in the background:

:::{code} bash
nohup R CMD BATCH --no-save code.R code.log &
:::

With a Matlab job, where we redirect
the output to outfile.txt and the error messages to error.txt:

:::{code} bash
nohup matlab -nodesktop -nodisplay < infile.m > outfile.txt 2> error.txt &
:::

For a Python script:

:::{code} bash
nohup python script.py > output.log 2>&1 &
:::

## Using screen

You may alternatively choose to use **GNU screen** to run your jobs so
that you can leave them running when you logout. Just invoke `screen`
from your shell, type a space or carriage return to dismiss the startup
message, then start your job. When you want to detach, type `Ctrl-a`
then `d` (press Control and 'a' together, release, then press 'd'). You can then exit from your terminal session.
When you want to access your job again, connect to the same machine your
job is running on and type `screen -r`. Note that `screen` is likely to
be more robust than `nohup` in terms of ensuring your job is not killed
by ending a remote login session abruptly (e.g., closing your laptop,
losing your wireless connection, etc.).

### Common screen Commands

A few more details on `screen`. To see a list of available sessions, do
`screen -ls`. To start a session with a specific name, you can do
`screen -S sessionName`. Then to resume a named session, do
`screen -r sessionName`. Or to resume a particular unnamed session, use
the name reported by `screen -ls`, e.g., it might look something like
4763.pts-2.beren. If a session is in use, you can forcibly detach it
from the other location and attach to it by doing
`screen -d -R sessionName`. To close a session, you can use `exit` from
within the session.

Useful commands while in a screen session:
- `Ctrl-a d` - Detach from the session
- `Ctrl-a c` - Create a new window within the session
- `Ctrl-a n` - Switch to the next window
- `Ctrl-a p` - Switch to the previous window
- `Ctrl-a "` - List all windows
- `Ctrl-a k` - Kill the current window
- `Ctrl-a ?` - Show help

## Using tmux

`tmux` is a modern alternative to `screen` with similar functionality
but a more powerful feature set. If available, you can use it as follows:

Start a new session:

:::{code} bash
tmux
:::

Or start a named session:

:::{code} bash
tmux new -s mysession
:::

Detach from a session: Press `Ctrl-b` then `d`.

List sessions:

:::{code} bash
tmux ls
:::

Reattach to a session:

:::{code} bash
tmux attach -t mysession
:::

Common tmux commands (press `Ctrl-b` first, then the key):
- `d` - Detach from session
- `c` - Create a new window
- `n` - Switch to next window
- `p` - Switch to previous window
- `w` - List all windows
- `&` - Kill current window
- `%` - Split pane vertically
- `"` - Split pane horizontally
- `?` - Show help

## Monitoring Background Processes

To check on your background processes:

:::{code} bash
# See jobs started from current shell
jobs

# See all your processes
ps -u $USER

# See detailed information about a specific process
ps -p PID -o pid,cmd,%cpu,%mem,etime

# Monitor process resource usage in real-time
top -u $USER
:::

## Best Practices

1. **Use the cluster for heavy computations** - Don't run intensive jobs
   on login servers even with `nohup` or `screen`.
2. **Redirect output** - Always redirect stdout and stderr to files to
   capture results and errors.
3. **Check on jobs periodically** - Use `ps` or `top` to ensure your job
   is still running and not consuming excessive resources.
4. **Clean up** - Kill finished or unnecessary processes and remove old
   screen/tmux sessions.
5. **Use screen/tmux for interactive work** - They're better than `nohup`
   for interactive sessions you want to preserve.
