---
title: "Project Accounts"
---

It is theoretically possible to enable one account to read and write to
a directory or file located in another account. This can be done through
filesystem permissions and access control lists. However, it is
inevitable that despite the initial configuration, files created through
such a configuration will eventually become owned by the authoring
account without permitting others to modify them. Additionally, if the
authoring account that created the files in the shared space is deleted,
the files are not automatically accounted for. Deleting the home or
scratch directories alone is not sufficient to clear out that account's
files from the system.

To facilitate shared workspaces without introducing such problems, we
create project accounts. They are shared accounts that multiple people
may access. All files in the account are owned by it and not by others.
Typically access is configured through [SSH keys](/faqs/ssh-keys). You
cannot transfer files directly from your own account via `cp` -- you will
need to use `scp` or some other network transfer program.

We can also enable users to access these shared account
through [JupyterHub](/software/jupyterhub). 

Please contact manager@stat.berkeley.edu if you would like to create a project account. Let us know:

- which local accounts need access
- is the project is related to a course or faculty research
- what is the suggested account name (something 12 characters or less,
  or so)
