---
title: "AI-assisted Coding"
---
AI coding assistants/agents and AI-based (or AI-augmented) integrated
development environments (IDEs) are now widely-used. This page documents
some ways you can use such tools for your work, in particular when using
the SCF. 

## Overview of tools 

Many tools are now available as **all** of a VS Code extension, a desktop app,
and a command-line interface (CLI). These include Claude Code (Anthropic), Codex (OpenAI),
and Antigravity (Google).

Other tools include Cursor (an AI-based IDE built on top of VS Code)
and the GitHub Copilot extension for VS Code. 

They use a variety of back-end large
language models, generally hosted in the cloud, and allow you
to choose amongst a set of models. 

This space is moving really fast, so new tools and improved existing
tools are likely to change the landscape frequently, and some of the
information here may be outdated (please contact us with suggestions!). 


Some tools have free access tiers, and one can of course pay
out-of-pocket for more intensive use or access to premium back-end
models.

The tools have generally transitioned from focusing on inline code completion and code suggestions
to operating as agents that accomplish entire tasks by writing or changing
code across one or more files and running code on your behalf. 

## Ways to use AI assistants with the SCF 

There are a wide variety of ways to run AI coding assistants on the SCF, with 
access to your files on the SCF and the ability to run commands on an SCF machine.

If you're using a GUI (including VS Code or an AI coding assistant desktop app)
it's often best to run the GUI on your laptop and have it connect to the SCF to execute
on an SCF machine with access to your files on the SCF.

Here are some good options:

- 1. The Claude Code desktop app allows you to select an "SSH environment" in order to run
on a remote machine (e.g., an SCF login node). Make sure you are in the Claude Code interface rather than the 
Claude Cowork interface.
     - You can do something similar in the ChatGPT desktop app in the Codex interface. 
     It takes a couple more steps to setup (going to `Settings -> Connections` and also
     installing the Codex CLI on the SCF machine).
- 2. Run VS Code and access the AI coding assistant as a VS Code extension. To use on the SCF, connect to an SCF login node using the 
        [VS Code remote SSH extension](../access/vscode-remote-ssh). 
     - With some additional configuration, you can connect to one of the SCF cluster machines from your local VS Code application. 
- 3. Any tool built on top of VS Code (such as Cursor or Positron) should also allow you to set up a remote SSH extension to the SCF.
- 4. You can ssh to an SCF login node and then run a CLI such as Claude Code CLI or Codex CLI in the terminal.

## GitHub Copilot

GitHub Copilot is available in several contexts,
including: 

- One can use GitHub Copilot in VS Code. 
- Some limited features are also available in RStudio. 
- Positron Assistant (a preview feature in Positron as of summer 2025)
  provides chat-based assistance using Claude (requiring a paid API key)
  and code completion using GitHub Copilot. In the future, one will
  likely be able to use GitHub Copilot for chat-based assistance with
  Positron. 
- One can configure Open Code to use GitHub Copilot for LLM access.

The free version of GitHub Copilot has various limits on requests. You
can use the GitHub Copilot Pro version (which has no limits on the use
of selected back-end large language models but limits on requests to
premium models) through GitHub Education if you are a student or a
teacher. (Note that it’s not clear if one can get access if you are a
researcher and your ID card does not say “student” or “faculty”.) You’ll
need to go through an application process that includes uploading a
photo of your Cal 1 Card. This should work even though there is no date
on your Card, so long as you have set up multi-factor authentication
with GitHub and your name on your Card matches the name associated with
your GitHub account. 

### Enabling GitHub Copilot in VS Code

To enable Copilot in your VS Code app with your GitHub for Education access, you'll need to login in to your GitHub account. As shown in the screenshot below, you should be able to login by going to one of the areas marked in the red ovals. 

```{image} ../images/vscode-gh-copilot.png
:alt: VS Code GUI with GitHub copilot icons
```

Once you are logged in, you should see the GitHub Copilot icon in the top toolbar (see the green oval in the screenshot). Clicking there should allow you to open the Chat window (or do `Cmd+Alt+I` on MacOs or `Ctrl+Alt+I` on Windows). You can also start inline chat in a code file with `Cmd+I` on MacOS or `Ctrl+I` on Windows.


