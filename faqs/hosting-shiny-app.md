---
title: "Hosting a Shiny App"
---
[Shiny](http://shiny.rstudio.com) is a web application framework
developed by RStudio. It allows you to create interactive graphics that
users access through the web. The graphics are supported by R
computation and graphing behind the scenes using R code that you write.

If you are affiliated with the department, following these steps to host
your Shiny app on the SCF.

1.  Email
    [consult@stat.berkeley.edu](mailto:consult@stat.berkeley.edu?subject=set%20up%20my%20account%20for%20Shiny%20hosting)
    to let us know you'd like to use this service, as we need to set up
    your account to do this.
2.  Once you hear back from us, create a directory in your web area,
    /mirror/data/pub/shiny/{username}/{appname}, where '{username}' is
    your SCF username and '{appname}' is the name you choose for your
    app. You can create multiple apps.
3.  Put your server.R and ui.R in the app directory. Note that when a
    user uses the app, the server starts an R process running in your
    SCF account, so your app should have access to any R packages you
    have installed locally in your account (in addition to the
    system-installed packages). Your app will also have access to data
    stored in your SCF account.
4.  Point your users to
    https://scf.berkeley.edu/shiny/{username}/{appname} to use the app.
    As an example, see <https://scf.berkeley.edu/shiny/paciorek/faith/>
    for a basic histogram/density app with the faithful dataset from R.
    You can see the underlying code in server.R and ui.R in
    /mirror/data/pub/shiny/paciorek/faith.

## Troubleshooting

You must be on the campus network to view shiny applications --
CalVisitor does not work. If on wireless, connect to *eduroam* after
[setting up your wireless passphrase](https://idc.berkeley.edu/mmk). For
the username, eduroam uses your CalNet login while eduroam uses your
CalNet login followed by "@berkeley.edu".

The [eduroam homepage](https://technology.berkeley.edu/wi-fi) contains
information on how to connect to eduroam, links to general CSS IT
support, and instructions on connecting various operating systems and
mobile devices.
