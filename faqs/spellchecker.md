---
title: "How do I use the spellchecker in UNIX?"
---

This article contains information about how to spellcheck your files.

## General Information

There are several ways to spell check a text files. Most of the time,
you can just launch **'ispell'** on the file that you want to check. In
other cases, you may open the file using your favorite editor. Most
editors have a hook for ispell that you can use within the program.

## Using ispell

To spellcheck a file, just run it through ispell. For example, if the
file that you want to be spellchecked is named `'mispel.txt'`, then you
can simply run **'ispell `mispel.txt'`**. If ispell returns immediately,
that means it did not catch any spelling errors in your file. Otherwise,
it will highlight each misspelled word and wait for your command.

ispell attempts to provide a list of words that it thinks are the
correct spelling for the misspelled word. You can type the number next
to the suggestions to replace the current highlighted word with the one
you choose. Or you can use one of the following commands.

Common commands are:

- R: Replace the misspelled word with one that you provide

- Space: Accept this word this time

- A: Accept this word for this sessio

- I: Accept this word, and put it in the dictionary so that it won't be
  flagged as misspell next time

- ?: Show help

## Launch spellcheck within an editor

### EMACS

**M-x ispell** will run ispell against the current buffer. **M-x
ispell\<tab\>** to see more commands related to ispell

### vi

**:!ispell \<`filename`\>**, then **:e!** after you are done

### nano

**^T** will launch the built-in spellchecker
