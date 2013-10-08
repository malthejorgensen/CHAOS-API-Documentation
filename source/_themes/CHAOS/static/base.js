$(document).ready(function() {
  // CHAOS uses '/' as a separator between classes (Extensions in CHAOS) and
  // their methods (Actions in CHAOS), because it uses an HTTP-interface
  $('dl.function dt > tt:first-child').each(function() {
    var new_text = $(this).text().replace('.', '/');
    $(this).text(new_text);
  });
  $('a.reference tt.xref.py-func >:first-child').each(function() {
    var new_text = $(this).text().replace('.', '/');
    new_text = new_text.replace('()', '');
    $(this).text(new_text);
  });
});
