$(document).ready(function() {
  $menu_links = $('dl.function dt').map(function() {
    var $li = $('<li />');
    var $a = $('<a />');

    $a.attr('href', '#' + this.id);
    var content = $.trim( $(this).text() );
    $a.text( content.substring(0, content.length-3) );

    $li.append($a);
    return $li;
  });

  $api_menu_element = $('div.sphinxsidebar ul.current li.current').first();
  $ul = $('<ul />');
  $menu_links.each(function() { $ul.append(this); });
  $api_menu_element.append($ul);

  // Activate `scrollspy.js` which depends on the menu items (which have just
  // been populated)
  $(document).trigger('menu-ready');
});
