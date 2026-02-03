---
title: Personal Website
---

We support department members in creating personal websites to share
information about their own activities at UC Berkeley, such as their research
groups, publications, courses, and other academic work.

We can support two models for hosting personal websites: GitHub Pages-based
sites and traditional HTML hosting.

Modern alternatives not directly supported by SCF include [Netlify](https://netlify.com) and [bCourses sites](https://bcourses.berkeley.edu/courses/1336779/pages/2-dot-3-create-your-course-site).

Some platforms like [Google Sites](https://bconnected.berkeley.edu/collaboration-services/google/sites) have been deprecated for accessibility considerations since cannot adjust the underlying HTML,

## GitHub Pages-Based Sites

For faculty and students who want to use [GitHub Pages](https://pages.github.com/) to publish their personal websites, we provide support for hosting and domain management. This approach can be particularly advantageous for:

- **Reproducibility**: Use automation tools and workflows to keep your site content up-to-date.
- **Collaboration**: Delegate authoring and content management to collaborators, students, or research group members
- **Version control**: Track changes to your website over time using Git
- **Modern tooling**: Use static site generators, markdown-based tools, and continuous deployment

### How It Works

We create repositories under the [berkeley-stat organization](https://github.com/berkeley-stat/) on GitHub for your website, and facilitate the creation of departmental subdomains such as these examples:

::::{grid} 1 2 2 2

:::{card}
:header: Bin Yu
 - [binyu-site](https://github.com/berkeley-stat/binyu-site)
 - [https://binyu.stat.berkeley.edu](https://binyu.stat.berkeley.edu)
:::

:::{card}
:header: Elizabeth Purdom
 - [purdom-site](https://github.com/berkeley-stat/purdom-site)
 - [https://purdom.stat.berkeley.edu](https://purdom.stat.berkeley.edu)
:::

::::


These subdomains point to your GitHub Pages site, providing a professional departmental URL while maintaining all the benefits of GitHub-based hosting.

### Getting Started

Contact <consult@stat.berkeley.edu> to request a GitHub Pages-based personal website. We will:

1. Create a repository under the berkeley-stat organization
2. Set up the departmental subdomain for your site
3. Provide you with access to manage your repository

You'll then be able to use GitHub Pages with your choice of static site generator (Quarto, MyST, etc.) or plain HTML/CSS/JavaScript.

:::{note}
If you choose to host your site on an external provider (not GitHub Pages through our organization), we can still create a domain name alias for you in the `.stat.berkeley.edu` subdomain, e.g., `yourname.stat.berkeley.edu`.
:::

## Traditional HTML Hosting

Department members can publish documents and data on the web by uploading
files to their [computing
accounts](../getting-started/computing-accounts.md).

:::{note}
Your personal website will be available at `https://www.stat.berkeley.edu`,
and not the departmental site, `https://statistics.berkeley.edu`.
:::

### Guidelines

Only individuals who are associated with either the Statistics or
Biostatistics departments are eligible to use this resource to
distribute information. Participants must observe all departmental and
UC campus rules and regulations, and all copyright laws. The SCF
reserves the right not to post submitted material.

Graduate students may maintain their own homepage using the following
guidelines:

- Posted material at the top level home page is limited to information
  related to the individual's academic interests. Listed below are
  examples of the type of information that is appropriate for the top
  level home page:
  1.  Biographical information (including the student's photograph).
  1.  Dissertation abstract.
  1.  Technical reports (with the signed approval of faculty advisor).
  1.  Data sets (with the signed approval of faculty advisor).
  1.  Links to other professionally relevant sites.
- Personal information can be included in a sub-level home page that is
  clearly identified as containing personal information. This area can
  include links to sites that are not related to to the individual's
  academic work.
- The posting or advertising of personal items for sale and the posting
  of any published material (including articles authored by the student)
  is forbidden.

### Creating HTML

Many applications can generate HTML files and you can probably export to
HTML from your favorite application suite. LaTeX, Google Docs, Microsoft
Word, TextEdit, and [Mozilla
SeaMonkey](http://www.seamonkey-project.org/) are good places to start.

Other approaches to creating HTML include:

1.  Modern markdown-based tools such as [MyST](https://mystmd.org) and [Quarto](https://quarto.org).
1.  latex2html will convert a LaTeX document to HTML. Here is a
    [template tex
    file](https://www.stat.berkeley.edu/~scf/latex2htmlExample.tex) and
    here is the [accompanying jpeg
    figure](https://www.stat.berkeley.edu/~scf/escher-stars.jpg) that is
    used in the tex file. To create the HTML, run `latex2html
    latex2htmlExample` on any SCF machine. If you want to have all the
    LaTeX section in a single HTML rather than separate HTML files for
    each section, do `latex2html -split 0 latex2htmlExample`.
1.  You can use the knitr package in R to convert from R Markdown (.Rmd)
    and Sweave (.Rnw/.Rtex) files with embedded R code to HTML. Load the
    knitr package in R and then run "knit2html file.Rmd", replacing
    "Rmd" with the appropriate extension, as necessary. Contact
    <consult@stat.berkeley.edu> if you have questions.

### Setting up the web area

You will need to [deposit your HTML files](../access/copying-files.md) into a
user-specific directory, `/accounts/web/public/username/`, on the SCF.
View your site at the address `https://www.stat.berkeley.edu/~username/`.
Your files will be available immediately on the website, though you may
need to reload your browser to see the changes. Make sure that your files
are readable, e.g. `chmod go+r filename.html`, otherwise the public will
not be able to view them. You can make use of this to hide content as
well, e.g. `chmod go-r filename.html`.

### Redirecting to Another Web Page

If you want to migrate your website to another provider and redirect
people to the new site, you can create an index.html file of the form
below, replacing the example URL with your own:

:::{code} html
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="refresh" content="0; url='https://example.com'" />
  </head>
</html>
:::

## Password protected web areas

Use [Google Drive](http://drive.google.com/a/berkeley.edu) to share
material if you need to have collaborators access restricted content
over the web.
