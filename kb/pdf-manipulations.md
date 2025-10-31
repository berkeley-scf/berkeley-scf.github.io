---
title: "Manipulating PDF documents"
---

You can use GNU Ghostscript, `gs`, to manipulate PDF files. Other tools
like `qpdf`, `pdftk`, and `pdfunite` are also available and may be easier
to use for some tasks. These can be installed via conda-forge if not
already available.

## Merge

You can merge multiple PDFs as follows:

:::{code} shell-session
gs -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=output.pdf -dBATCH \
    input1.pdf input2.pdf input3.pdf
:::

The backslash (`\`) allows the command to continue on the next line.

Alternatively, using `pdfunite` (simpler syntax):

:::{code} shell-session
pdfunite input1.pdf input2.pdf input3.pdf output.pdf
:::

## Subsetting

You can also create a new PDF from a subset of the pages in an original
PDF, where m and n are the first and last page numbers to extract:

:::{code} shell-session
gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dFirstPage=m -dLastPage=n \
    -sOutputFile=output.pdf input.pdf
:::

For example, to extract pages 5-10:

:::{code} shell-session
gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dFirstPage=5 -dLastPage=10 \
    -sOutputFile=output.pdf input.pdf
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

## Merge PDFs

`qpdf` is another powerful tool for PDF manipulation with a more
user-friendly syntax.

:::{code} shell-session
qpdf --empty --pages input1.pdf input2.pdf input3.pdf -- output.pdf
:::

## Extract pages

For example, pages 5-10:

:::{code} shell-session
qpdf input.pdf --pages . 5-10 -- output.pdf
:::

## Compress/optimize:

:::{code} shell-session
qpdf --compress-streams=y --recompress-flate input.pdf output.pdf
:::
