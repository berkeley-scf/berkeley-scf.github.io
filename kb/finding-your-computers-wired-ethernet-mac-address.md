---
title: "Finding your computer's wired ethernet (MAC) address"
---
## Overview

Every computer's network interface has a unique identifer called a MAC
address. It is a 12 digit hexadecimal number usually delimted by colons,
e.g. ab:01:23:ef:45:dc. Both wired and wireless network interfaces have
these addresses.

## Finding the Ethernet MAC Address

### Microsoft Windows

For PCs running Windows 7 and earlier, Go to Start Menu \> Programs \>
Accessories \> DOS Command Prompt. Type **cmd**. For PCs running Windows
8 and later, launch the "Command" program by searching for it in your
applications list. When the command window appears, type **ipconfig
/all**. The Physical Address value for your ethernet card is your MAC
address. Make sure you're looking at your ethernet interface and not
your wireless interface.

### Apple macOS

#### From the Terminal

Type "**networksetup -listallhardwareports**" in a Terminal window. The
"Ethernet Address" field for the ethernet hardware port is your MAC
address. If there are too many ports listed and you're not sure which is
your active ethernet port, try one of the options below.

#### Recent macOS (System Settings)

1.  Go to the Apple menu \> System Settings \> Network.
2.  Click on the wired network device you plan on using, then click
    Details.
3.  Click on the Hardware label in the left column. The MAC address will
    be on the right.

#### Older macOS (System Preferences)

1.  Go to the Apple menu \> System Preferences \> Network (under
    "Internet and Wireless").
2.  Make sure that the ethernet interfaces is selected on the left side.
3.  Click on the Advanced button on the right, and then the Hardware
    tab. The MAC address is listed there.

### Linux

Type **ip link** in a terminal window. The link/ether field associated
with your ethernet interface is your MAC address.
