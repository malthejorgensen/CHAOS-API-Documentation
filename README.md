CHAOS API Documentation
=======================
The documentation can be viewed at <http://chaos-community.github.io/CHAOS-API-Documentation/>.

Build
-----
The documentation is made with [Sphinx](http://sphinx-doc.org).
To get Sphinx, make sure you have Python installed (with Distribute)
and install it via `pip`

    > pip install sphinx

You can install all dependencies automatically with

    > pip install -r requirements.txt

**Note:** Please do not add `distribute` to requirements.txt, as this
breaks our _drone.io_ continous integration for the documentation.

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


Continuous deployment
--------------------
[drone.io] is setup to monitor the Github repository for
changes. A push or commit to any of the version branches (`master`, `v4` etc.)
will automatically build the documentation of all versions and put them in
the `gh-pages` branch. [drone.io] is set to run the following commands:

    git checkout master
    pip install -r requirements.txt --use-mirrors
    python create_docs.py --commit
    git push https://$TOKEN:@github.com/malthejorgensen/CHAOS-API-Documentation.git gh-pages

This of course assumes that the master branch has a `create_docs.py` script and
a `requirements.txt` file. Furthermore a [Github token login] is set up and the
token should be put in the `TOKEN` environment variable on [drone.io]:

    TOKEN=b5836fa...

[drone.io]: http://drone.io
[Github token login]: https://help.github.com/articles/creating-an-oauth-token-for-command-line-use

Credits
-------
Inspired by:
 - [MongoDB Manual](http://docs.mongodb.org/manual/contents/)

