---
title: "Setting up a course website"
---
Starting in the Spring semester 2024, the department, through the SCF,
is helping instructors create discoverable and modern class websites,
with memorable URLs in the berkeley.edu domain.

This page provides an overview and gives details to instructors on
setting up a [class website](/faqs/course-website) using the system.

The department strongly encourages instructors to set up a class
website.

## Advantages

The benefits of having public course websites compared to bCourses or
one-off websites set up by faculty include:

- More visibility/discoverability for potential students and others not
  enrolled in the course.
- More consistent and modern style and branding, including use of the
  berkeley.edu domain.
- Ease of archiving/sharing/transfer to future instructors.
- Consistency with Berkeley Data Science courses and Statistics 20,
  which have course overview pages and per-semester offering pages at
  memorable URLs.
- Integration of course website and content in one place, with the
  ability to manage via version control systems such as Git.


::::{grid} 2

::: {card}
:header: Course Landing Page

![Course Landing Page](https://lh7-us.googleusercontent.com/JwaYSIhThPLIpI-p3qQp_OxlN1WjE2WdOhA64FaSBl-NoOTydIqbn104Dv6dffDouYOOytZ4e_rEbcDhfwNUnN0v3EYM-Q0g_gId4bjZQVXTSeNxm0Kvca0LKXGqFRmfsIFKhOfZTkd31DYbhDcTkqU){width="298px" height="251px"}
:::

::: {card}
:header: Class website

![Class website](https://lh7-us.googleusercontent.com/LqhL2UsVZw3TH6pupIxkpY_KJcOy7n-b5DKL2kAbIvCH5TGX0QSrSVDiUIXvfAgxBNeHQEjXqpn3mG7fkk-wgerJUQevfDp9nMC1jtVdyQnRR-Vqmtwfv1VP3DF8Gjl75f3-U5XWO_CDAQ4QTLZVU9A){width="298px" height="249px"}
:::

::::

## Course Landing Pages

The SCF will create “landing pages” for each course at
statXYZ.berkeley.edu, e.g.,
[stat133.berkeley.edu](https://stat133.berkeley.edu) for Statistics 133.
Each landing page will contain overview information about the course
gathered from the academic guide. Most importantly, it will link to
class websites specific to each semester the course is offered.

As basic pages, the course landing pages use the [Just The
Class](https://kevinl.info/just-the-class/) framework.

## Class Websites

The department strongly encourages instructors to set up a class
website. 

While we encourage instructors to set up [websites with extensive
materials](/faqs/course-website#full-featured-websites), we
ask those who wish to continue to primarily use bCourses to set up a
[minimal site](/faqs/course-website#minimal-websites) with
syllabus information. The minimal site could also include pointers to
external resources (such as Ed, Gradescope, DataHub, etc.) and course
staff. 

With the goal of helping students during course shopping and encouraging
enrollment, ideally at least some syllabus-style information would be
posted by the time classes start or even better before the semester
starts. 

We provide instructions below for setting up both minimal and
full-featured websites using the SCF-developed department course website
templates below. 

**To get started with a website for your class, please email the SCF at
consult@stat.berkeley.edu and let us know whether you'd like to set up a
fully-featured site (and let us know if you'd prefer to use Quarto or
MyST) or if you'd like to set up a minimal site. We'll then set up the
structure of the site and point you to how/where you can start adding
content.**

Course websites will be found at statXYZ.berkeley.edu/{semester-year},
e.g.,
[stat133.berkeley.edu/spring-2024](http://stat133.berkeley.edu/spring-2024). 

To see class websites that used the department template, see the spring
2024 sites for [Statistics 133](http://stat133.berkeley.edu/spring-2024)
and [Statistics 151A](http://stat151a.berkeley.edu/spring-2024).

SCF staff can provide assistance as needed, in person or via
consult@stat.berkeley.edu.

### Full-featured Websites<span id="full-featured-websites"></span>

For instructors wishing to provide a full website and course materials,
the SCF provides both a [Quarto
template](https://github.com/berkeley-cdss/course-site-quarto) and a
[MyST template](https://github.com/berkeley-cdss/course-site-myst). The
README files found when navigating to each of those templates provide
full instructions for setting up the course website.

In both cases, one can edit Markdown-style or notebook-style files as
the source files for pages on the site. We anticipate that course staff
will use Git to manage their materials. 

Some features of the templates include the ability to:

- Create a website by modifying content in a GitHub-based repository.
- Create documents either using Quarto Markdown (qmd), Jupyter notebook
  (ipynb), or Markdown files.
- Include LaTeX (including LaTeX macros) for mathematical notation.
- Include code chunks that are dynamically evaluated and whose output is
  included in the document (qmd or ipynb files only).
- Include external webpages (such as Google calendars) as iframes within
  a page.
- Have documents be rendered to HTML or PDF (the latter for documents
  that students will download).
- Render a course schedule, with links to course materials, from a plain
  text file of information.
- For Quarto-based sites, set up timed release of course content/pages,
  using functionality developed by Andrew Bray for Statistics 20.
- Have the website be searchable.

### Minimal Websites

The SCF provides a [template for a minimal class
website](https://github.com/berkeley-cdss/course-site-quarto-lite) using
a consistent department style, [illustrated with this dummy
site](https://berkeley-cdss.github.io/course-site-quarto-lite/). An
instructor can follow [these directions in the template
README](https://github.com/berkeley-cdss/course-site-quarto-lite?tab=readme-ov-file#instructions-for-course-staff),
editing the pages for the website in a browser window. The content is
managed by GitHub (and you'll need a GitHub account), but knowledge of
Git or GitHub is not required.  
 
