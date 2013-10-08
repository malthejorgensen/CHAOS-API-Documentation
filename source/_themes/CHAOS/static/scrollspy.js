// Heavily inspired by: http://jsfiddle.net/mekwall/up4nu/
//
// The menu on the `API` page is populated after document load, and triggers the
// 'menu-ready' event.
$(document).on('ready menu-ready', function() {
  // Cache selectors
  var last;

  // All list items
  var menuItems = $("div.sphinxsidebar a");

  // Anchors corresponding to menu items
  var scrollAnchors = $("a.headerlink");

  // Bind click handler to menu items
  // so we can get a fancy scroll animation
  // menuItems.click(function(e){
  //   var href = $(this).attr("href"),
  //       offsetTop = href === "#" ? 0 : $(href).offset().top-topMenuHeight+1;
  //   $('html, body').stop().animate({
  //       scrollTop: offsetTop
  //   }, 300);
  //   e.preventDefault();
  // });

  // if handler has already been bound -- remove it
  $(window).off('scroll.scrollspyHandler');

  // Bind to scroll
  $(window).on('scroll.scrollspyHandler', function() {

    // Get container scroll position
    var scrollPos = $(this).scrollTop(); //+topMenuHeight;

    // Get headers above current scroll position
    var cur = scrollAnchors.filter(function() { return $(this).offset().top < scrollPos; });
    cur = cur[cur.length - 1];

    // If current section changed
    if (last !== cur) {
      last = cur;

      // Remove existing "current"
      // menuItems.parent().removeClass("current");
      menuItems.removeClass("current");

      // Add new "current"
      if ($(cur).length) {
        var href = $(cur).attr("href");
        var anchorName = href.substring(href.lastIndexOf("#"));
        // menuItems.filter("[href~='" + anchorName + "]").addClass("current");
        menuItems.filter(function() { return $(this).attr('href') === anchorName; }).addClass("current");
      }
    }
  });
});

