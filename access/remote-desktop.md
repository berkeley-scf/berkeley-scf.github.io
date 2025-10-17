---
title: "Remote Desktop"
---
Remote desktop software enables you to connect to a graphical Linux
desktop running on SCF servers. You can start a desktop session,
disconnect, then resume later on with all of your applications still
running. You can connect to any of our Linux machines that are not part
of the cluster.

## VPN

You are now required to first login to the campus VPN before accessing a
remote desktop from off-campus. Note that if you are already connected
to the VPN and change your wifi network, you will need to disconnect and
reconnect to the VPN.

## Remote Desktop (RDP)

### Client Software

- macOS: [Microsoft Remote
  Desktop](https://apps.apple.com/us/app/microsoft-remote-desktop/id1295203466)
- Linux: rdesktop (command-line), remmina, vinagre
- Windows: Microsoft Remote Desktop Connection (search applications for
  "remote")

Collaborators on project accounts that do not have access to the campus
VPN and use the Remote Desktop Application to access the SCF can create
an [SSH tunnel](/access/ssh/ssh-tunnel.md).

### Configuration

Choose an [SCF server](/computing/servers), and specify your username in your
RDP program. You may want to also change the defaults for sound output
and whether you want the application to run in fullscreen.

## X2go

X2go is a similar remote desktop application, but has an open
development model. There are clients for both
<a href="http://code.x2go.org/releases/X2GoClient_latest_macosx.dmg"
target="_blank">Mac</a> and
[Windows](http://code.x2go.org/releases/X2GoClient_latest_mswin32-setup.exe).

### Settings

Launch the application and create a new session. The following settings
are where I overrode the default values:

- Session
  - Session name: *Your Favorite Machine*
  - Host: *machine-name.berkeley.edu*
  - Login: *YOUR SCF LOGIN*
  - Enable "*Try auto login (ssh-agent or default ssh key)*" if you use
    ssh-agent to connect to the SCF [without your password](/faqs/ssh-keys).
    If you do not enable this you will be prompted to enter your SCF
    password when connecting.
  - Session type: *XFCE*
- Input/Output
  - Custom: 1024x768 (or whatever you desire)
  - Set display DPI: 100
- Media
  - Disable "*Enable sound support*"
  - Disable "*Client side printing support*"
