---
title: "Use git On a Shared Project"
---
## Background

If you would like to use git to manage a shared project but do not want
to host it on a world-readable service such as github, we can create a
project account for you to contain one or more git repositories. You and
your colleagues can read and write to the repositories once your access
has been established through SSH in one of two ways:

- By depositing your public SSH key into the shared account
- By establishing your own SCF account

The first method allows you to use your preferred software on your
personal machine, but also requires that you have git and ssh software
installed on your computer. The second method does not require that you
have any software other than SSH, but does require that you use the UNIX
tools available at the SCF.

## Creating the repository

Statistics faculty should send an email to <manager@stat.berkeley.edu>
requesting the creation of a new project account along with some
information about it so that we can name it (in the examples below it is
named *PROJECT_NAME*). SSH to the account when it is available and run
the following command:

```{code} shell-session
PROJECT_NAME:~$ mkdir REPO_NAME
PROJECT_NAME:~$ git init --bare --shared REPO_NAME
```

where *REPO_NAME* is the name of the repository.

## Accessing the repository using SSH keypairs

Collaborators should see [our instructions](./kb/ssh-keys.md)
on creating SSH keypairs</a>. Once you send your public key to
<manager@stat.berkeley.edu> , we can deposit it into the project
account. You will then be able to begin working with the data by cloning
the repository:

```{code} shell-session
user@laptop:~$ git clone ssh://PROJECT_NAME@gandalf.berkeley.edu/accounts/projects/FAC_NAME/PROJECT_NAME/REPO_NAME
```

## Accessing the repository using an SCF account

Collaborators may also fill out our [guest account
form](https://docs.google.com/a/berkeley.edu/forms/d/1O-mHchu1bGXRE_HguMntlmiN0DhPC-mW6zHO4KYcuKo/viewform) if
you would like for them to have an SCF account. Once it has has been
created, they will have direct read access to the repository for
cloning:

```{code} shell-session
git clone ~PROJECT_NAME/REPO_NAME
```

## Using git

The SCF has prepared some [documentation on using git](git.md). A
basic workflow, after you have cloned the repository, is:

```{code} shell-session
# Create a new file
vi doc1.tex

# Add it to the repository
git add doc.tex

# Record your changes. You will be prompted to describe your changes.
git commit

# Write your changes to the repository. You only need to set the origin once.
# All other pushes can omit the --set-upstream action.
git push --set-upstream origin master

# Edit an existing document
vi doc2.tex

# Record and write your changes
git commit
git push

# Pull the most current version with changes from others
git pull
```

If the cloned repository is on your personal computer rather than in
your SCF account, you will be able to use your preferred text editor to
create and/or edit files.
