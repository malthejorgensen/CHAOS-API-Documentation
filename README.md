CHAOS API Documentation
=======================
The documentation is made with [Sphinx](http://sphinx-doc.org).

#### Build
Build the documentation with

    > make html

The docs will then be in `build/html`.

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

Credits
-------
Inspired by:
 - [MongoDB Manual](http://docs.mongodb.org/manual/contents/)
