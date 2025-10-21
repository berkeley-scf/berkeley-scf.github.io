---
title: "Globus"
---

[Globus](http://globus.org) is a data management service that allows you
to easily transfer data (including fast transfers of extremely large
datasets) between machines and share data with others. You logon and
specify the transfer to be made, and Globus takes care of it in a robust
manner without you having to monitor the transfer or worry about the
connection between the machines being lost.

The easiest thing you can do is transfer files between machines/systems
that are already registered with Globus as Globus endpoints. Some
endpoints that may be useful for Berkeley affiliates include Berkeley
Research Computing's Savio campus cluster and NERSC:

:::{table}
:label: Globus endpoints

| Endpoint                          | Display Name                      |
|-----------------------------------|-----------------------------------|
| UC Berkeley Statistics Department | UC Berkeley Statistics Department |
| UC Berkeley Economics Department  | UC Berkeley Economics Department  |
| ucb#brc                           |                                   |
| nersc#cori                        | NERSC Cori                        |
| nersc#edison                      | NERSC Edison                      |
| nersc#hpss                        | NERSC HPSS                        |

:::

{button}`Launch Globus Web App <https://app.globus.org/>`

The first time you connect to the endpoint, you will be offered the
option to "Link an identity from UC Berkeley Statistics OIDC Auth".
Selecting this link will take you to a login page where you will be
asked to authenticate using your SCF account credentials. This will link
your identity to your Globus account. You may also create additional
linked identities for any project accounts you want to use.

The first time you establish a new linked identity, you may be asked to
log in twice. The first login request establishes the new linked
identity. The second login request logs you in to the collection. Once
the linked identities have been created, you can choose from a list of
those you have created when you make subsequent connections, and logins
will proceed as expected.

Enter the name of the endpoint and authenticate to the resource by
following the directions given. Once both endpoints are authenticated,
it's straightforward to drag and drop to transfer files. Globus will
email you when the transfer is complete.

You can also transfer to/from your own machine. To do so, first get the
[Globus Connect
Personal](https://www.globus.org/globus-connect-personal) client for
your machine (see the lower right of the webpage to download the client
for your operating system). Your machine will then be registered as one
of your personal endpoints. When selecting an endpoint, you should be
able to click on the box labelled "Endpoint" and select the resource
from the list in "My Endpoints".
