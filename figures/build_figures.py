# -*- coding: utf-8 -*-

# Dependencies
from Cheetah.Template import Template
from sh import lualatex, convert
#-- `convert` is ImageMagick

# Python built-ins
from shutil import rmtree
from tempfile import mkdtemp
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', action='store_true', help='Print output from Luatex `lualatex` and ImageMagic `convert`.')
args = parser.parse_args()

def print_verbose(msg, newline=True):
    if args.verbose:
        print msg,
        if newline:
            print ''

# configure Cheetah
compiler_settings = u"""
#compiler-settings
cheetahVarStartToken = ¢
#end compiler-settings
"""

tex_files = [
  'chaos_objects.tex',
  'chaos_org_chart.tex',
]

for tex_filename in tex_files:
    filename = tex_filename[:-4]
    print 'Building figure "%s".' % filename
    temp_dir = mkdtemp()
    print_verbose('Made temporary directory "%s".' % temp_dir)
    temp_filename = temp_dir + '/' + filename + '.cheetah'
    img_in_filename = temp_dir + '/' + filename + '.pdf'
    img_out_filename = '../source/static/' + filename + '.png'
    with open(tex_filename) as f_in:
        f_contents = f_in.read().decode('utf-8')
        # fix comments
        f_contents = f_contents.replace('\\','\\\\').replace('\\\\#','\\#')
        # compile template
        compiled = str(Template(compiler_settings + f_contents)).replace('\\\\','\\')
        with open(temp_filename, 'w') as f_temp:
            f_temp.write(compiled)
        print_verbose("STARTING lualatex")
        for line in lualatex('--output-directory', temp_dir, '--shell-escape', '--jobname', filename, temp_filename, _err_to_out=True, _iter=True):
            print_verbose(line, newline=False)
        print_verbose("STOPPED lualatex")
        print_verbose("STARTING convert")
        for line in convert('-trim', '-density', '300x300','-resize', '50%', img_in_filename, img_out_filename, _err_to_out=True, _iter=True):
            print_verbose(line, newline=False)
        print_verbose("STOPPED convert")
    rmtree(temp_dir)
    print_verbose('Removed temporary directory "%s"' % temp_dir)

#lualatex --output-directory tex-temp --shell-escape --jobname %B %B.cheetah.tex';

