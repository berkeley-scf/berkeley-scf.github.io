---
title: "AI-assisted Coding"
---
AI coding assistants and AI-based (or AI-augmented) integrated
development environments (IDEs) are now widely-used. This page documents
some ways you can use such tools for your work, in particular when using
the SCF. 

## Overview of tools 

The available tools include a wide variety of AI-based IDEs (such as
Cursor), AI-enhanced IDEs (such as VS Code extensions for GitHub Copilot
and Gemini Code Assist), and command-line interface (CLI) tools such as
Claude Code and Gemini Code Assist. They use a variety of back-end large
language models, generally hosted in the cloud, with some tools allowing
one to choose amongst a set of models. 

This space is moving really fast, so new tools and improved existing
tools are likely to change the landscape frequently, and some of the
information here may be outdated (please contact us with suggestions!). 

Since many of the tools are available either as VS Code extensions or
are built on top of VS Code, if you are familiar with VS Code, the
interface will look familiar. 

Some tools have free access tiers, and one can of course pay
out-of-pocket for more intensive use or access to premium back-end
models, which some of our graduate students are doing. 

The tools generally provide some or all of the following kinds of
interactivity: 

- Inline code completion and code suggestions. 
- In-editor interactivity for modifying and generating code. 
- Chat sidebars for asking questions and controlling the AI assistant,
  including full agent mode in which the AI can carry out complicated
  workflows. 

### GitHub Copilot

GitHub Copilot is widely used and is available in several contexts,
including: 

- One can use GitHub Copilot in VS Code. 
- Some limited features are also available in RStudio. 
- Positron Assistant (a preview feature in Positron as of summer 2025)
  provides chat-based assistance using Claude (requiring a paid API key)
  and code completion using GitHub Copilot. In the future, one will
  likely be able to use GitHub Copilot for chat-based assistance with
  Positron. 
- One can configure Opencode to use GitHub Copilot for LLM access.

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

## Ways to use AI assistants with the SCF 

- Run VS Code with GitHub Copilot (or other VS Code extensions providing
  AI assistants such as Cursor, Windsurf, Gemini Code Assist or Continue) on your personal
  machine and connect to the SCF standalone servers using the remote SSH extension. 
  - With some additional configuration, you can connect to one of the
    SCF cluster machines from your local VS Code application. 
- We expect to support the use of Jupyter AI on the SCF JupyterHub (in
  particular the forthcoming version 3 with various improvements) in the
  near future. 
- One can use AI-assisted code completions in RStudio on the SCF
  JupyterHub. This can be helpful, as it allows you to do a variety of
  things all couched as code completions, but it doesn’t have the full
  AI assistance of other tools. 
- There are various AI assistants available through a command line
  interface (CLI), including OpenAI CLI, Claude CLI, or Gemini CLI with
  which one can chat with AI models, generate code, or get explanations
  in the terminal. If you’re interested in using these on the SCF,
  please let us know.
