---
title: "Manipulating PDF documents"
---

You can use GNU Ghostscript, `gs`, to manipulate PDF files. Other tools
like `qpdf`, `pdftk`, and `pdfunite` are also available and may be easier
to use for some tasks. These can be installed via conda-forge if not
already available.

## Merge

You can merge multiple PDFs using `gs`:

:::{code} shell-session
gs -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=output.pdf -dBATCH \
    input1.pdf input2.pdf input3.pdf
:::

The backslash (`\`) allows the command to continue on the next line.

Alternatively, using `pdfunite` (simpler syntax):

:::{code} shell-session
pdfunite input1.pdf input2.pdf input3.pdf output.pdf
:::

Or using `qpdf`:

:::{code} shell-session
qpdf --empty --pages input1.pdf input2.pdf input3.pdf -- output.pdf
:::

## Subsetting

You can create a new PDF from a subset of the pages in an original
PDF using `gs`, where m and n are the first and last page numbers to extract:

:::{code} shell-session
gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dFirstPage=m -dLastPage=n \
    -sOutputFile=output.pdf input.pdf
:::

For example, to extract pages 5-10:

:::{code} shell-session
gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dFirstPage=5 -dLastPage=10 \
    -sOutputFile=output.pdf input.pdf
:::

Or using `qpdf` (e.g., pages 5-10):

:::{code} shell-session
qpdf input.pdf --pages . 5-10 -- output.pdf
:::

## Compress / Reduce File Size

You can reduce the file size of a PDF by reprocessing it with compression
settings. The `-dPDFSETTINGS` option controls the quality/size tradeoff:

:::{code} shell-session
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
    -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
:::

Quality options (from lowest to highest quality, smallest to largest file):
- `/screen` - low quality, smallest file (72 dpi)
- `/ebook` - moderate quality (150 dpi)
- `/printer` - high quality (300 dpi)
- `/prepress` - highest quality, largest file (300 dpi, preserves color)

Or using `qpdf` for compression/optimization:

:::{code} shell-session
qpdf --compress-streams=y --recompress-flate input.pdf output.pdf
:::

## Convert to Grayscale

To convert a color PDF to grayscale:

:::{code} shell-session
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dQUIET \
    -sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray \
    -sOutputFile=output.pdf input.pdf
:::

## Rotate Pages

To rotate all pages 90 degrees clockwise (Orientation values: 0=0°, 1=90°,
2=180°, 3=270°):

:::{code} shell-session
gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dQUIET \
    -sOutputFile=output.pdf -c "<</Orientation 1>> setpagedevice" \
    -f input.pdf
:::

## Convert PDF to PostScript

You can convert PDF files to PostScript format using either Poppler's
`pdftops` or Ghostscript's `pdf2ps`:

:::{code} shell-session
pdftops input.pdf output.ps
:::

or

:::{code} shell-session
pdf2ps input.pdf output.ps
:::

Both commands will create a PostScript file from the PDF input.

## Installing Tools

Most tools mentioned above are available on SCF Linux systems. If you need
to install them locally, you can use conda-forge:

:::{code} shell-session
conda install -c conda-forge qpdf poppler
:::
