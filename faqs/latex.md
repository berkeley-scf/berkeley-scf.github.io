---
title: "How do I use LaTeX?"
---
This is the local guide to using Tex or LaTeX and should not serve as a
substitute for the appropriate User's Guides, referenced below.

<div class="article" lang="en">

<div class="section" lang="en">

<div class="titlepage">

<div>

<div>

## The Basics

</div>

</div>

</div>

The basic command for running TeX or LaTeX is **'tex filename'**,
**'latex filename'**, or **'pdflatex filename'**.

There should be a file in your current directory called `filename.tex`,
containing the TeX or LaTeX commands. Upon successful completion of
processing, a file called `filename.dvi` is created and `filename.pdf`
if you used **pdflatex**. (LaTeX also produces a file called
`filename.aux` with information for tables of content and indices; don't
be alarmed if it tells you it doesn't exist. However, if you wish to
produce a table of contents, index or document with references, you will
need the .aux file. Since the .aux file is produced if it is not
present, this simply means that you may have to run TeX or LaTeX twice
in order to get these features.) It is the .dvi file which you will
eventually print to get your final copy.

</div>

<div class="section" lang="en">

<div class="titlepage">

<div>

<div>

## Previewing

</div>

</div>

</div>

You can preview your file on the screen before you print it. Use the
command **'xdvi'**, with the dvi file given as an argument, as in
`xdvi filename.dvi`. If you make a change to your dvi file (by
reinvoking tex or latex), xdvi will refresh itself as soon as the cursor
is returned to it's window -- that is, it is not necessary to quit and
restart xdvi every time you reprocess your input file.

</div>

<div class="section" lang="en">

<div class="titlepage">

<div>

<div>

## Printing

</div>

</div>

</div>

To print a dvi file called `filename.dvi` use the command **'dvips
filename'**. Dvips automatically routes the output to your default
printer (as set by the PRINTER environment variable). You can override
the destination printer by adding a **`-Pprinter`** to the dvips command
line. For example, **'dvips `-Ppr1 filename`'** will print
`filename.dvi` on printer `pr1`.

If you wish to print only part of a .dvi file (or you are having trouble
printing a large .dvi file), you can print part of the file using the
command **dviselect**. Type **man dviselect** for information on using
the dviselect command.

In order to view a LaTeX document which uses PostScript fonts (like
Helvetica), you should first convert the document to PostScript, and use
ghostview to view it.

Suppose your document is called `sem.tex`, then the command **'latex2e
sem'** creates the file `sem.dvi`, and the command **'dvips -f -t
landscape sem.dvi \> sem.ps'** creates the PostScript file `sem.ps`.
This file can be viewed with the command **'ghostview sem.ps'** and can
be printed with the command **'lpr sem.ps'**

</div>

<div class="section" lang="en">

<div class="titlepage">

<div>

<div>

## Additional Documentation

</div>

</div>

</div>

The appropriate User's Guides are:

<div class="itemizedlist">

- The LaTeX WikiBook, <a href="http://en.wikibooks.org/wiki/LaTeX"
  target="_top">http://en.wikibooks.org/wiki/LaTeX</a>

- The TeXbook, by Donald E. Knuth, Addison-Wesley, 1984

- LaTeX User's Guide & Reference Manual, by Leslie Lamport,
  Addison-Wesley, 1986

</div>

For help in getting PostScript output into your TeX or LaTeX document,
see `help psfig`.

For infomation on the style file `ucthesis` (e.g.
documentclass{ucthesis} ) refer to [ucthesis](computing/ucthesis-latex).

</div>

</div>

 
