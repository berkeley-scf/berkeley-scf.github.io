---
title: "Using AWS for Instructional Computing"
---
## Amazon Web Services

Amazon Web Services (AWS) provides a number of cloud-based services. In
particular, instructors may be interested in using virtual machines and
virtual computing clusters through Amazon's EC2 or MapReduce (EMR)
services. SCF staff will provide individualized support to instructors
wishing to use AWS in their classes.

Some potential instructional uses for AWS include:

1.  Working with cloud-based virtual machines
1.  Running parallelized computational tasks that scale to many cores
    using cloud-based virtual clusters
1.  Using [Spark](/faqs/spark) to
    carry out distributed computation, including MapReduce computations
1.  Using Amazon's MapReduce service for distributed computation

We note that SCF supports the use of virtual machines on student laptops
and SCF servers, as well as provides access to parallel computing
resources on our multi-core servers and our Linux multi-node clusters.
So uses \#1 and \#2 above could be achieved either through AWS or
through existing SCF resources. Doing it through AWS provides students
with experience in cloud-based computing that may be useful in their
careers. Doing it using SCF resources may be logistically easier.

## Getting Started

Amazon's handling of credits for classes is currently in flux. **The
instructions below are out of date as the educational grants program
does not formally exist any more.** However, it may be possible to get a
set of credits for a class via direct contact with Berkeley's campus AWS
representative and follow steps 6-8 below. SCF can help with this --
please just email us.

To make use of AWS for your class, these are the steps you'll need to
follow.

1.  Let us know of your plans and needs by emailing
    <consult@stat.berkeley.edu>.

2.  The cost of using AWS resources, in particular computing cycles with
    EC2 or EMR, can add up fairly quickly. To cover the cost of the
    class usage, please apply for an Amazon educational grant by going
    to <http://aws.amazon.com/grants>, clicking on the "*Educators*" tab
    and filling out the form. Amazon will generally provide a credit of
    \$100 per student. Ideally, you would do this a couple weeks before
    you wish to use AWS in class as it can take a few days for Amazon to
    approve the grant.

3.  After 1-4 days, you'll receive an email from Amazon that should
    begin as follows. "Thank you for your AWS course grant application,
    your submission was successful. Would you like the credits set up
    for your AWS account and for you to manage access for students, or
    would your students be setting up their own AWS accounts
    separately?" Respond to the email and ask that credits be set up for
    your AWS account with access managed centrally. SCF will manage this
    access for your class.

4.  Wait another few days. You should get an email titled "*AWS In
    Education Grant - Congratulations!*" which will contain a credit
    code resembling "*PC1IJ749GVDDG09*".

5.  Send email to <consult@stat.berkeley.edu> containing:

    1.  the credit code
    2.  a plain text file containing the @berkeley.edu email addresses
        of your students (obtained from BearFacts)
    3.  a separate plain text file containing the @berkeley.edu email
        addresses of any instructors (including GSIs) who should have
        administrative access

     

6.  SCF staff will then apply the credit to the overall SCF AWS account
    and will make accounts for the students and instructors/GSIs. Each
    individual will receive an automated email containing a URL to login
    to, their user name, and a one-time password to use the first time
    they login. Once the individual logs in, they will be prompted to
    create a new password to access the AWS website and will be able to
    download the AWS credentials (an AWS_ACCESS_KEY_ID and
    AWS_SECRET_ACCESS_KEY) that can be used to start EC2/EMR virtual
    machines/clusters.

7.  Instructors will be able to monitor activity in EC2 or EMR by
    logging into the AWS Management Console. Go to
    <http://aws.amazon.com> and click on "*AWS Management Console*"
    under the "*My Account*" pulldown. Login using your username and
    your password. Then click on the orange cube in the upper left
    corner and select the service you'd like to access (e.g., EC2).

8.  Users can start up virtual machines/clusters in a variety of ways:
    by using the AWS web interface, using scripts provided by Spark,
    using the StarCluster command line tools, the Python boto package
    and many others.

SCF staff can provide technical assistance with actually using AWS in
your class as well as general feedback on how you might use AWS for
instruction. Please email <consult@stat.berkeley.edu> with questions.
