---
title: "JupyterHub updates"
description: "Updated default python kernel and the remote desktop feature."
thumbnail: ../images/jupyterhub.svg
author: "Ryan Lovett"
date: "2025-04-03"
keywords:
  - JupyterHub
  - Python
  - Remote Desktop
---

I have updated the default python kernel from 3.12 to 3.13 to match the login environment of our recently upgraded systems. The previous kernel is still available as "Python 3.12" in the jupyter lab launcher.

I've also updated the remote desktop feature. The latest version supports copy/paste and desktop resizing, has a link back to the hub, and uses a unix socket for security.
