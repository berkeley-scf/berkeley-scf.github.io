---
title: "Saving Plots in R"
---
<div>

Originally for Statistics 133, by
<a href="http://www.stat.berkeley.edu/~spector" rel="author"
title="Phil Spector">Phil Spector</a>

</div>

Since R runs on so many different operating systems, and supports so
many different graphics formats, it's not surprising that there are a
variety of ways of saving your plots, depending on what operating system
you are using, what you plan to do with the graph, and whether you're
connecting locally or remotely.

The first step in deciding how to save plots is to decide on the output
format that you want to use. The following table lists some of the
available formats, along with guidance as to when they may be useful.

|            |                |                                                          |
|------------|----------------|----------------------------------------------------------|
| Format     | Driver         | Notes                                                    |
| JPG        | `jpeg`         | Can be used anywhere, but doesn't resize                 |
| PNG        | `png`          | Can be used anywhere, but doesn't resize                 |
| WMF        | `win.metafile` | Windows only; best choice with Word; easily resizable    |
| PDF        | `pdf`          | Best choice with pdflatex; easily resizable              |
| Postscript | `postscript`   | Best choice with latex and Open Office; easily resizable |

## A General Method

First, here's a general method that will work on any computer with R,
regardless of operating system or the way that you are connecting.

1.  Choose the format that you want to use. In this example, I'll save a
    plot as a JPG file, so I'll use the `jpeg` driver.
2.  The only argument that the device drivers need is the name of the
    file that you will use to save your graph. Remember that your plot
    will be stored relative to the current directory. You can find the
    current directory by typing `getwd()` at the R prompt.
3.  You may want to make adjustments to the size of the plot before
    saving it. Consult the help file for your selected driver to learn
    how.
4.  Now enter your plotting commands as you normally would. You
    will **not** actually see the plot - the commands are being saved to
    a file instead.
5.  When you're done with your plotting commands, enter
    the `dev.off()` command. This is very important - without it you'll
    get a partial plot or nothing at all.

So if I wanted to save a jpg file called "`rplot.jpg`" containing a plot
of `x` and `y`, I would type the following commands:

    > jpeg('rplot.jpg')
    > plot(x,y)
    > dev.off()

## Another Approach

If you follow the process in the previous section, you'll first have to
make a plot to the screen, then re-enter the commands to save your plot
to a file. R also provides the `dev.copy` command, to copy the contents
of the graph window to a file without having to re-enter the commands.
For most plots, things will be fine, but sometimes translating what was
on the screen into a different format doesn't look as nice as it should.

To use this approach, first produce your graph in the usual way. When
you're happy with the way it looks, call `dev.copy`, passing it the
driver you want to use, the file name to store it in, and any other
arguments appropriate to the driver.

For example, to create a png file called `myplot.png` from a graph that
is displayed by R, type

    > dev.copy(png,'myplot.png')
    > dev.off()

Remember that when you save plots this way, the plot isn't actually
written to the file until you call `dev.off`.

## Local Sessions with Windows or OS X

If you're actually sitting in front of a Windows or Mac computer (i.e.
not using ssh to connect), the graphical user interface makes it easy to
save files. Under Windows, right click inside the graph window, and
choose either "`Save as metafile ...`" or "`Save as postscript ...`" If
using Word, make sure to save as a metafile.

On a Mac, click on the graphics window to make sure it's the active one,
then go to `File -> Save` in the menubar, and choose a location to save
the file. It will be saved as a pdf file, which you can double click to
open in Preview, and then use the `File -> Save As` menu choice to
convert to another format.
