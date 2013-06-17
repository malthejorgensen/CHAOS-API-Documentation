def setup(app):
    app.add_node(code_editor_node, html=(visit_code_editor_node, depart_code_editor_node))

    app.add_directive('code-editor', CodeEditorDirective)
    # app.connect('doctree-resolved', process_code_editor_nodes)
    # app.connect('env-purge-doc', purge_code_editors)

    app.add_javascript("http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js")

    app.add_stylesheet("http://cdn.jsdelivr.net/codemirror/3.0/codemirror.css")
    app.add_javascript("http://cdn.jsdelivr.net/codemirror/3.0/codemirror.js")
    app.add_javascript("http://cdn.jsdelivr.net/codemirror/3.0/mode/javascript/javascript.js")
    app.add_javascript("http://cdn.jsdelivr.net/codemirror/3.0/mode/css/css.js")
    app.add_javascript("http://cdn.jsdelivr.net/codemirror/3.0/mode/xml/xml.js")
    app.add_javascript("http://cdn.jsdelivr.net/codemirror/3.0/mode/htmlmixed/htmlmixed.js")

    app.add_javascript("CHAOS.Portal.Client.PortalClient.js")
    app.add_javascript("code-editor.js")
    app.add_stylesheet("code-editor.css")

from docutils.parsers.rst import Directive, directives
from docutils import nodes


class code_editor_node(nodes.General, nodes.Element):
    pass


def visit_code_editor_node(self, node):
    linenos = node.rawsource.count('\n') >= \
                self.highlightlinenothreshold - 1
    highlight_args = node.get('highlight_args', {})
    if node.has_key('language'):
        # code-block directives
        lang = node['language']
        highlight_args['force'] = True
    if node.has_key('linenos'):
        linenos = node['linenos']
    # def warner(msg):
    #     self.builder.warn(msg, (self.builder.current_docname, node.line))
    # highlighted = self.highlighter.highlight_block(
    #     node.rawsource, lang, warn=warner, linenos=linenos,
    #     **highlight_args)
    # startpre = self.starttag(node, 'pre')
    # startcode = self.starttag(node, 'code', suffix='', CLASS='language-%s' % lang)
    # self.body.append(startpre + startcode + node.rawsource + '</code></pre>\n')
    class_value = 'language-%s' % lang
    if 'eval' in node and node['eval']:
        class_value += ' eval'

    id_attr = ''
    if 'id' in node and node['id']:
        id_attr = ' id="%s"' % node['id']

    code_content = node.rawsource
    code_content = code_content.replace('<', '&lt;');
    code_content = code_content.replace('>', '&gt;');

    self.body.append('<pre%s><code class="%s">' % (id_attr, class_value) + \
                                            code_content + '</code></pre>\n')
    raise nodes.SkipNode

def depart_code_editor_node(self, node):
    pass

from sphinx.util.nodes import set_source_info

class CodeEditorDirective(Directive):

    # this enables content in the directive
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    option_spec = {
        'linenos': directives.flag,
        'emphasize-lines': directives.unchanged_required,
        'eval': directives.flag,
        'id' : directives.unchanged_required,
    }

    def run(self):
        code = u'\n'.join(self.content)

        linespec = self.options.get('emphasize-lines')
        if linespec:
            try:
                nlines = len(self.content)
                hl_lines = [x+1 for x in parselinenos(linespec, nlines)]
            except ValueError, err:
                document = self.state.document
                return [document.reporter.warning(str(err), line=self.lineno)]
        else:
            hl_lines = None

        # literal = nodes.literal_block(code, code)
        # literal['language'] = self.arguments[0]
        # literal['linenos'] = 'linenos' in self.options
        # if hl_lines is not None:
        #     literal['highlight_args'] = {'hl_lines': hl_lines}
        # set_source_info(self, literal)
        # return [literal]
        code_editor = code_editor_node(code)
        code_editor['language'] = self.arguments[0]
        code_editor['linenos'] = 'linenos' in self.options
        code_editor['eval'] = 'eval' in self.options
        code_editor['id'] = self.options.get('id')
        if hl_lines is not None:
            code_editor['highlight_args'] = {'hl_lines': hl_lines}

        return [code_editor]
