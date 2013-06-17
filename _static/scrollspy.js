// Heavily inspired by: http://jsfiddle.net/mekwall/up4nu/
$(function() {
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

  // Bind to scroll
  $(window).scroll(function(){

    // Get container scroll position
    var scrollPos = $(this).scrollTop(); //+topMenuHeight;

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
        href = $(cur).attr("href");
        anchorName = href.substring(href.lastIndexOf("#"));
        menuItems.filter("[href~=" + anchorName + "]").addClass("current");
      }
    }
  });
});

