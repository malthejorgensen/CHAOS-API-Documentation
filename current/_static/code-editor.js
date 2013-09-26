// Requires Javascript
var setup_code = "";

$(document).ready(function(event) {

  // Calculate line numbers
  var line_count = 0;
  $('pre code#setup.language-javascript').each(function() {
    line_count = $(this).text().split("\n").length + 1
    setup_code = $(this).text();
  });


  if (setup_code == "") {
    setup_code = ['// Setup settings',
                  'var ChaosSettings = {',
                  '  "servicePath":"http://api.chaos-systems.com/",',
                  '  //"clientGUID":"9f62060c-64ff-e14f-a8d5-d85a1e2e21b8",',
                  '  "accessPointGUID":"7A06C4FF-D15A-48D9-A908-088F9796AF28",',
                  '};',
                  '// Instantiate client',
                  'var client = new PortalClient(',
                  '                   ChaosSettings.servicePath,',
                  '                   ChaosSettings.clientGUID',
                  ');'].join('\n');
    line_count = setup_code.split("\n").length + 1;
  }

  $('pre code').each(function() {
    var $pre = $(this).parent();
    var code = $(this).html();

    // id
    // var id_attr = $parent.attr('id', codeElem.attr('id'));
    var id_attr = $pre.attr('id');

    // Wrap code in a <div>
    $pre.wrap('<div class="highlight" />');
    var $parent = $pre.parent();

    // If <pre> has an ID attribute
    if (typeof id_attr !== 'undefined' && id_attr !== false) {
      $parent.attr('id', id_attr);
    }

    // http://codemirror.net/doc/manual.html#api_configuration
    var CodeMirrorSettings = {
      value: code,
      lineNumbers: true,
      tabSize: 2,

      // Autoresize
      // http://codemirror.net/demo/resize.html
      viewportMargin: Infinity,
    };

    // Save the <code> element
    codeElem = $(this).clone();

    // Make CodeMirror
    var textarea = $('<textarea>' + code + '</textarea>');
    $pre.replaceWith(textarea);
    // var textarea = aside.children('textarea').get(0);
    var codeMirror = CodeMirror.fromTextArea(textarea.get(0), CodeMirrorSettings);
    $parent.data('codeMirror', codeMirror);

    // Setup CodeMirror
    if (codeElem.hasClass('language-html')) {
      codeMirror.setOption('mode', 'htmlmixed');
    } else if (codeElem.hasClass('language-json')) {
      codeMirror.setOption('mode', { 'name': 'javascript', 'json': true });
    } else if (codeElem.hasClass('language-javascript')) {
      codeMirror.setOption('mode', 'javascript');

      if (codeElem.hasClass("eval")) {
        codeMirror.setOption('firstLineNumber', line_count);

        // Add Javascript evaluate button
        var codeButton = $('<div class="try-code"><button>Try!<\/button><\/div>');
        codeButton.children('button').click(codeEval(codeMirror, setup_code));
        $parent.after(codeButton);
      }
    }
  });
});

function codeEval(codeMirror, setup_code) {
  return function(event) {
    var code = codeMirror.getValue();

    // http://aaronrussell.co.uk/legacy/check-if-an-element-exists-using-jquery/
    if ($('#setup-code').length > 0) {
      setup_code = $('#setup-code').data('codeMirror').getValue();
    }

    // console.log(setup_code + code);
    eval(setup_code + code);
  };
}
