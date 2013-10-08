CHAOS Sphinx theme
==================
This is the theme for the CHAOS API documentation.

### Python Domain display modifications (a hack)
Right now we're using the Sphinx Python Domain to document the CHAOS Portal HTTP
API. The Python Domain displays module function as `Object.Get()` but we need it
to display as `Object/Get`.

This has nothing to do with the theme so really it should be in the
documentation config - not in the theme. But Sphinx does not have a good way to
add Javascript to the HTML pages right now. See [issue #964 on Bitbucket].

**Hacks**

 * `static/base.js` replaces `.` with `/` in references and function names
 * `static/style.css_t` hides `()` in function names

[issue #964 on Bitbucket]: https://bitbucket.org/birkenfeld/sphinx/issue/964/make-it-possible-to-add-script_files-from

