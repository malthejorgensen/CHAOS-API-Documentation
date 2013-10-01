import json
import os
import argparse
from datetime import datetime
from shutil import rmtree, move
import sphinx

from sh import git

parser = argparse.ArgumentParser()
parser.add_argument('--stash', action='store_true', help='Stash before changing to gh-pages')
parser.add_argument('--commit', action='store_true', help='Whether the auto-generated docs should be committed')
parser.add_argument('--push-gh-pages', help='Specify a repository on which to create Github Pages')
args = parser.parse_args()

versions = json.load(open('versions.json'))

dir_names = []

try:
    rmtree('tmp')
except:
    pass

os.makedirs('tmp')

# builddir = 'current'
# sphinx.main(['sphinx-build', '-b', 'html', '-a', '-E', 'source', 'tmp/' + builddir])
# exit()

if args.stash:
    git.stash()

for name, options in versions.items():
    print 'Generating docs for version ' + name

    try:
        git.checkout(options['branch_name'])
        print 'Checked out "' + options['branch_name'] + '"'
        # Print latest commit
        print git('--no-pager', 'log', '-1')

        os.environ['CHAOS_DOC_VERSION'] = name
        sphinx.main(['sphinx-build', '-b', 'html', '-a', '-E', 'source', 'tmp/' + options['directory_name']])
        del os.environ['CHAOS_DOC_VERSION']
        # sphinx.main(['sphinx-build', '-b', 'html', '-a', '-E', 'source', 'tmp/current'])
        dir_names.append(options['directory_name'])
    except:
        raise
        print 'Could not check out branch "' + options['branch_name'] + '".'
        exit()

time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S %z')

try:
    git.checkout('gh-pages')

    for dir_name in dir_names:
        # Remove the current documentation folders (v4, v5, current)
        try:
            rmtree(dir_name)
        except:
            pass
        # Move generated folders (in 'tmp/') into the root folder
        move('tmp/' + dir_name, '.')

    # Remove 'tmp/'
    rmtree('tmp')
except:
    raise
    # print 'Could not checkout gh-pages'
    # exit()

if args.commit or args.push_gh_pages:
    # Commit new version
    git.add(dir_names)
    git.commit(m='Auto-generated docs %s' % time_str)

if args.push_gh_pages:
    # Commit new version
    # git.push(['origin', 'gh-pages'])
    print 'Pushing to "%s"' % args.push_gh_pages
    git.push([args.push_gh_pages, 'gh-pages'])

# git.checkout('master')
