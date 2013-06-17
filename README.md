CHAOS API Documentation
=======================
The documentation is made with [Sphinx](http://sphinx-doc.org).
To get Sphinx, make sure you have Python installed (with Distribute)
and install it via `pip`

    > pip install sphinx

#### Build
Once you have install Sphinx, you can build the documentation with

    > make html

The docs will then be in `build/html`.

Guide
-----
Sphinx uses reStructuredText (`.rst`) as markup language for its pages. A quick
guide to reStructuredText can be found [here](http://docutils.sourceforge.net/docs/user/rst/quickref.html).

PHP Portal Client documentation
----------------------------

Install the PHP domain for Sphinx

    > pip install sphinxcontrib-phpdomain

Install the 
http://mark-story.com/posts/view/sphinx-phpdomain-released
https://github.com/avalanche123/doxphp

    > pear channel-discover pear.avalanche123.com
    > pear install avalanche123/doxphp-beta

Autogenerate the API documentation

    > cd src/CHAOS/Portal/Client/
    > mkdir docs
    > for f in $(find . -iname '*.php' -print0); do bf="$(basename $f)"; doxphp < $f | doxphp2sphinx > docs/$bf.rst; done

Caveats
-------

 - restructuredText (`.rst`) does not support nested markup ([link](http://docutils.sourceforge.net/FAQ.html#is-nested-inline-markup-possible))
 - To have a non-paragraph linebreak (single instead of double) use |br| ([link](http://docutils.sourceforge.net/FAQ.html#how-to-indicate-a-line-break-or-a-significant-newline))

Credits
-------
Inspired by:
 - [MongoDB Manual](http://docs.mongodb.org/manual/contents/)

