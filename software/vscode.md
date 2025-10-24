---
title: "VS Code"
---

Follow these instructions to use VS Code on the SCF. You can either run
VS Code on a login node or on one of the compute nodes in the SCF
cluster. In either case VS Code will access files (including your home
directory) on the SCF.

## Using the remote SSH extension to connect to an SCF machine

You can [use the Remote SSH extension](../access/vscode-remote-ssh.md#connect-to-an-scf-login-node) to connect to one of the 
[SCF login nodes](../servers/login-servers.md).

## Accessing cluster nodes via VS Code

If you want to access the cluster nodes (including GPUs available on
some cluster nodes), you'll need to do one of the following.

- Use VS Code through [JupyterHub](../access/jupyterhub.md),
  selecting the cluster partition when you start your Jupyter server.
  This uses `code-server` to run VS Code in a web browser. A downside
  is that the extensions available are not exactly as with VS Code
  itself. In particular GitHub Copilot may not work as well.
- Alternatively, and likely better, you can [use some ssh tricks to run VS Code on a cluster node via the remote SSH extension](../access/vscode-remote-ssh.md#connect-to-an-scf-cluster-node).

