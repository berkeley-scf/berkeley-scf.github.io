---
title: "Manipulating PDF documents"
---
On the SCF Linux machines, you can merge multiple PDFs as follows:

    $ gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=output.pdf -dBATCH input1.pdf input2.pdf input3.pdf

You can also create a new PDF from a subset of the pages in an original
PDF:

    $ gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dFirstPage=m -dLastPage=n -sOutputFile=output.pdf input.pdf

gs is ghostscript, which can also do a number of other manipulations of
postscript and PDF files.
