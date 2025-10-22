---
title: "Using the Hadoop cluster and Rhipe"
---

::: {warning}
The SCF's test Hadoop cluster is now offline due to limited use.
Please see our [page on Spark](spark.md) or [contact
us](mailto:consult@stat.berkeley.edu?subject=Hadoop%2FSpark%20interest)
if you would like to try out Hadoop or Spark in cluster computing. The
material below is now out of date, but preserved at the moment for
historical purposes.
:::

### SCF Hadoop Cluster Information

The SCF has a small Hadoop test cluster that all SCF users can use to
run Hadoop jobs, including R jobs that use the
<a href="http://www.datadr.org" title="Rhipe">Rhipe
package</a> as a front end to Hadoop.

The Hadoop cluster has eight nodes, each with two cores, and a total of
about 1 Tb of disk space set up with the Hadoop distributed file system.
Note that the nodes are a set of our outdated compute servers and the
amount of disk space is limited. The goal of the Hadoop cluster at this
point is to serve as a testbed rather than for doing real analyses of
large data. If you have need for more resources please [contact
us](../getting-started/contact-us.md) and we can discuss how you might
use cloud resources such as Amazon's EC2.

Below is more detailed information about using the Hadoop cluster.

### Basic Configuration So You Can Run Jobs

First, you must [email us](mailto:consult@stat.berkeley.edu) and let us
know that you would like to use the cluster. We will create a directory
on the Hadoop distributed file system (HDFS) for you to store your
files. The directory will be /user/username, where username is your SCF
username. Note that /user/username is on the HDFS and is not directly
accessible on the Linux filesystem of the Hadoop nodes.

Second, add the line 'hadoop=1' to your .bashrc file in your SCF home
directory. It should be added before the following lines, which should
already exist in your .bashrc file:

``` {code} bash
if [ -f ~skel/std.bashrc ]; then
    source ~skel/std.bashrc
fi
```

This sets up some environment variables that you need in order to use
Hadoop.

### Running Hadoop and Rhipe Jobs

All jobs must be run from one of the following compute servers:

    badger, crow, dorothy, heffal, mole, rabbit, toad, witch

You can also find this list of servers by typing the following on any
SCF machine:

    sitehosts broadcomm

To check on the status of the cluster, go to the following URL using a
browser running on any SCF machine (this could be a browser on an SCF
machine that is ssh-tunneled to your local machine):

    http://witch:50070 

If you know how to interact with the HDFS directly or how to use Hadoop,
you can do so from the command line of any of these machines.

To use Rhipe, start R, and load and initialize the Rhipe package:

    library(Rhipe)
    rhinit(TRUE, TRUE) # the TRUEs are not necessary but give debugging information

### How Interact with the HDFS

You can use UNIX-like syntax to interact with the HDFS.

To look at directories and files:

    hadoop fs -ls /  # to see the root directory
    hadoop fs -ls /user/username # to see the home directory of the user username

To see your disk usage on the HDFS:

    hadoop fs -du /user/username

To get a list of various Hadoop filesystem commands:

    hadoop fs

### Some Tips on Using Rhipe

Any data that you want to write to the HDFS should be written to
/user/username. It's also possible to write to /tmp but we ask that you
not do this.

In some cases, to fully exploit all 16 cores on the cluster, you may
need to explicitly specify the number of map tasks and reduce tasks for
your MapReduce job. These can be specified in the mapred argument passed
into the rhmr() function. Hadoop documentation suggests that the number
of map tasks be 10 times the number of slaves and the number of reduce
tasks be two times the number of slaves, so in R, you would specify

    z <- rhmr(..., mapred = list(mapred.map.tasks = 10*8, mapred.reduce.tasks = 2.8), ...)

where the ... indicate the various other arguments you are passing in.
These can also be set via rhoptions().

The [Rhipe package website](http://www.datadr.org) has some example code.
Per the above comment, you'll need to change any HDFS file paths to point
to your user directory on the HDFS. Also, note that the code has some bugs
in it and the syntax is not fully up to date with Rhipe v. 0.71, which is
the version we are currently using. Please email consult@stat.berkeley.edu
for more information and updated code.

After you have created the MapReduce job using rhmr(), you can run it
and monitor its status as follows:

    r <- rhwatch(z)

You can also see some information about the Hadoop processes by going to
the URL printed out by rhwatch(). As above, you need to enter that URL
in a browser running on an SCF machine.

Note that debugging may be difficult because the R code is run across
multiple nodes, the data are distributed across multiple nodes, and
Hadoop jobs are based on Java, so you may get error messages from Java.
You can email consult@stat.berkeley.edu for assistance.
