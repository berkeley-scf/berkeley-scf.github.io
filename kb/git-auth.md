---
title: "Authenticating to Remote Git Repositories"
---
This documentation outlines how to connect to remote Git repositories,
in particular how to avoid entering a password or authentication token
each time.

Git provides multiple protocols for authenticating to and interacting
with remote Git repositories. This documentation focuses on GitHub but
the ideas are relevant for other platforms.

There are two main approaches you can take:

1.   Using a personal authentication token (PAT) over HTTPS
2.   Using an SSH key

:::{note}
As of August 2021, GitHub no longer accepts passwords for Git operations.
You must use either a personal access token or SSH key.
:::

With either approach you can avoid entering credentials each time you 
interact with the remote repository, as discussed below.

Before going into details, note that you can run the
following (generally run from a directory within a repository) to see
how things are configured:

:::{code} bash
git config -l
:::

In what follows, I'll refer to the account or organization the
repository exists in as ACCOUNT and the repository as REPO.

## Using HTTPS with a personal authentication token

The standard way to interact with a repository is via HTTPS. You can
clone a repository using HTTPS like this:

:::{code} bash
git clone https://github.com/ACCOUNT/REPO
:::

You'll be asked to enter your username and password. The password must
be a personal authentication token (PAT), not your GitHub account password.

You can create a token using [these
instructions](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) or
simply go [to the GitHub tokens page](https://github.com/settings/tokens). If you're just
interacting with repositories, you probably want to simply select 'repo'
as the "scope".

(git-save-auth)=
### Saving your password or token to avoid entering it

You can [save, or cache, your
credentials](https://docs.github.com/en/github/using-git/caching-your-github-credentials-in-git) so
that you don't have to reenter them each time you interact with the
remote repository.

Your credentials can be stored in the keychain of your operating system
or cached in memory or in a file.

To cache in memory, in the MacOS keychain, or in the Windows credential manager,
choose the relevant one of these three invocations:

:::{code} bash
# in memory:
git config --global credential.helper cache
# MacOS
git config --global credential.helper osxkeychain
# Windows (modern Git for Windows)
git config --global credential.helper manager-core
:::

To set the cache in memory to last for a particular amount of time, here
3600 seconds (i.e., 1 hour):

:::{code} bash
git config --global credential.helper 'cache --timeout=3600'
:::

If you prefer to set the credential helper on a repository-specific
basis, you can omit the '--global' flag.

To check if the credential helper is set up:

:::{code} bash
git config --get credential.helper
:::

## SSH keys

To use SSH, you need to put [your SSH public key](/kb/ssh-keys) in your GitHub account.
Your public key file is found in the `~/.ssh` directory on a Mac or Linux
machine (or Windows via Git bash or the Windows Subsystem for Linux) and will generally be a file ending in `.pub`. Go to
<https://github.com/settings/keys> and copy/paste your public key from
the public key file.

:::{tip}
SSH is generally preferred over HTTPS for developers who frequently push to repositories,
as it's more convenient once set up and doesn't require managing tokens.
:::

You can then clone a repository using syntax of either of the following
types:

:::{code} bash
git clone git@github.com:ACCOUNT/REPO.git
git clone ssh://github.com/ACCOUNT/REPO
:::

To confirm you are using ssh, run

:::{code} bash
git config --get remote.origin.url
:::

If you see either of the following, you know you're using SSH to
interact with the repository.

:::{code} shell-session
git@github.com:paciorek/test-auth.git
ssh://github.com/paciorek/test-auth
:::

### Avoiding having to enter your SSH passphrase

Note that you may be asked to enter your SSH passphrase when interacting
with a repository. To avoid having to keep doing this, you can add your
passphrase to your running SSH authentication agent, like this (assuming
here your key is called 'id_rsa'):

:::{code} bash
ssh-add ~/.ssh/id_rsa
:::

Note that you might need to start your SSH agent with:

:::{code} bash
eval `ssh-agent -s`
:::

More details on using the SSH agent can be found
[here](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

If you have a repository that is using HTTPS and you want to switch to
SSH, you can run either of these invocations from within a directory
within your repository:

:::{code} bash
git config remote.origin.url git@github.com:ACCOUNT/REPO.git
git remote set-url origin git@github.com:ACCOUNT/REPO.git
:::

## Using GitHub CLI

Another option is to use the [GitHub CLI](https://cli.github.com/) (`gh`),
which can handle authentication for you. After installing `gh`, run:

:::{code} bash
gh auth login
:::

Follow the prompts to authenticate. The CLI will configure Git to use its
built-in credential helper, so you won't need to enter credentials for
Git operations.
