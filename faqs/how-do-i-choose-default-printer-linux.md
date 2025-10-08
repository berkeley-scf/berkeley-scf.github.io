---
title: "How do I choose a default printer in Linux?"
---
<div class="toc">

## Environment Variables

</div>

<div class="section" lang="en">

If you wish to change your default printer, you can put the name of the
preferred printer in the environment variables PRINTER and LPDEST. For
instance, if you want printer 365 to be your default printer, type the
commands:

tcsh:

``` programlisting
setenv PRINTER 365 setenv LPDEST 365
```

bash:

``` programlisting
export PRINTER=365 export LPDEST=365
```

This will enforce the printer choice for every program started from the
shell that you typed the commands in. If you want to always use a
particular printer, put the setenv commands at the end of your
`~/.cshrc` file or the export commands at the end of your `~/.bashrc`
file. Note that users with printers in their offices usually get the
correct PRINTER and LPDEST settings without needing to edit their dot
files.

</div>

<div class="titlepage">

<div>

<div>

## Related Information

</div>

</div>

</div>

<a href="/node/4274" data-_mce_href="/836"
data-entity-substitution="canonical" data-entity-type="node"
data-entity-uuid="ce27fa38-9da8-47b7-82b4-6255f8091f78">What are the
names and locations of all the printers?</a>
