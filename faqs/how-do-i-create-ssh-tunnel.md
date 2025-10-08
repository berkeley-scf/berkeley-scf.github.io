---
title: "How do I create an SSH tunnel?"
---
An SSH tunnel establishes a connection between your local machine and
the remote machine via a TCP port. When you configure your local
application to use an SSH tunnel you tell it to connect to your local
machine at a specified port, rather than the remote machine. The tunnel
then carries your traffic securely to the remote machine.

## Example Configurations

Here is a list of application-specific tunnel settings:

**Table 1. Tunnel Settings**

| Application | Type | Listen Port |
|-------------|------|-------------|
| SMB         | TCP  | 139         |
| RDP         | TCP  | 3389        |
| MySQL       | TCP  | 3306        |
| VNC         | TCP  | 5901        |
| JSTOR       | TCP  | 8000        |

## In Windows - putty

1.  Click the plus sign by the `SSH` menu choice in the left pane of the
    main window.
2.  Click on **Tunnels**.
3.  Set `Source port` to the value of the `listen port` and
    `Destination` to `DESTINATION_HOST:DESTINATION_PORT` given your
    specific tunneling options. (see table above)
4.  Once the information is in place, click the **Add** button to create
    the tunnel.
5.  Click on the **Session** menu choice at the top of the left hand
    pane and enter any valid SCF host in the `Host Name` window. Click
    on **Open**, and log in with your SCF username and password.

## In Mac OS X and Linux

Type (on your local machine) in a terminal window:

    ssh -l username -L LISTEN_PORT:stat.berkeley.edu:DESTINATION_PORT SCF_HOSTNAME

where LISTEN_PORT is the Listen Port, DESTINATION_PORT is the
Destination Port, and SCF_HOSTNAME is any SCF computer. See the
<a href="https://scf.berkeley.edu/ingrid" target="_top">computer
grid</a> for a list of SCF computers.

You may included more than one tunnel on the command-line, for example:

    ssh -l username -L 25:DESTINATION_HOST:25 -L 110:DESTINATION_HOST:110 SCF_HOSTNAME

If you receive a message that the port is in use, this means that there
is currently a service running on your local machine listening on the
local port. You will need to either disable it (change /etc/inetd.conf)
or choose a different port number for the local port:

    ssh -l username -L 5025:DESTINATION_HOST:25 -L 5110:DESTINATION_HOST:110 SCF_HOSTNAME

For example, to read JSTOR from off campus, execute:

    ssh -L 8000:www.jstor.org:80 username@SCF_HOSTNAME

and then connect your web browser to http://localhost:8000.
