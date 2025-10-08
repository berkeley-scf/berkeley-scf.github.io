---
title: "Manipulating PostScript files in Linux"
---
<div class="titlepage">

<div>

<div>

## Converting to PDF

Run '**ps2pdf file.ps file.pdf**'. This will create `file.pdf`.

## Resizing PostScript files

The command, **psresize**, can rescale a PostScript file. This is most
useful when the original document was created for A4 paper, the standard
in Europe, and the file needs to be sent to printers expecting U.S.
Letter documents. The output is usually cropped unless the document is
resized. Run '**psresize -PA4 -pletter file.ps newfile.ps**'.

If you open your file in gv, a button label at the top will be set to a
your document's current size, such as '**A4**' or '**BBox**'. Click the
button to change the setting to '**Letter**'. Then try printing from
within gv.

## Simplifying a PostScript file

The command '**ps2ps**' is Ghostscript's PostScript distiller that can
convert input files to simpler PostScript. Run '**ps2ps file.ps
newfile.ps**'.

## Changing the PostScript level

The command '**ps2ps**' can change the PostScript level of a document.
For example:

``` programlisting
ps2ps -dLanguageLevel=1 file.ps
```

</div>

</div>

</div>

 
