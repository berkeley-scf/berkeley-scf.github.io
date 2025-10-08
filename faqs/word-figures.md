---
title: "How do I put a figure into a Microsoft Word document?"
---
<div class="titlepage">

<div>

<div>

<div class="section" lang="en">

<div class="titlepage">

<div>

<div>

## Vector formats

</div>

</div>

</div>

EPS files will not display properly within Microsoft Word, however if an
EPS graphic is embedded in a Word document, it will print properly on a
PostScript printer. Depending on the way the document is produced, EPS
figures might be usable.

Most likely though, the best way to get a figure from R into Word is to
use the Windows Metafile format (WMF), which unfortunately can only be
produced on Windows operating systems using the win.metafile() R device.

</div>

<div class="section" lang="en">

<div class="titlepage">

<div>

<div>

## Bitmap formats

</div>

</div>

</div>

Bitmap formats such as JPEG, GIF, and PNG can be easily produced and
imported into Word documents. The problem with these formats, however,
is that they will have image artifacts if resized.

</div>

</div>

</div>

</div>

 
