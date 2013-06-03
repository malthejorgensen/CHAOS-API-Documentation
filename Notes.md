
The way you make the hierarchy of documentation pages is via the command
`toctree::`.
(`toctree::` in the [Sphinx docs](http://sphinx-doc.org/markup/toctree.html#toctree-directive)).

`toctree::` refers to other pages by their path relative to the current
document. Multi-level hierarchies (nesting) is done by having `toctree::`
commands in the documents referred to by this `toctree::`.

If you want a page to have children pages, but not show them, you can use the
`toctree::` command with the option `:hidden:`.

