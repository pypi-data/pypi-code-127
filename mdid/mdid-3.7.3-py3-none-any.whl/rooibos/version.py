# -*- coding: utf-8 -*-

"""Calculates the current version number.

If possible, uses output of “git describe” modified to conform to the
visioning scheme that setuptools uses (see PEP 386).  Releases must be
labelled with annotated tags (signed tags are annotated) of the following
format:

   v<num>(.<num>)+ [ {a|b|c|rc} <num> (.<num>)* ]

If “git describe” returns an error (likely because we're in an unpacked copy
of a release tarball, rather than a git working copy), or returns a tag that
does not match the above format, version is read from RELEASE-VERSION file.

To use this script, simply import it your setup.py file, and use the results
of getVersion() as your package version:

    import version
    setup(
        version=version.getVersion(),
        .
        .
        .
    )

This will automatically update the RELEASE-VERSION file.  The RELEASE-VERSION
file should *not* be checked into git but it *should* be included in sdist
tarballs (as should version.py file).  To do this, run:

    echo include RELEASE-VERSION version.py >>MANIFEST.in
    echo RELEASE-VERSION >>.gitignore

With that setup, a new release can be labelled by simply invoking:

    git tag -s v1.0
"""

__author__ = ('Douglas Creager <dcreager@dcreager.net>',
              'Michal Nazarewicz <mina86@mina86.com>')
__license__ = 'This file is placed into the public domain.'
__maintainer__ = 'Michal Nazarewicz'
__email__ = 'mina86@mina86.com'

__all__ = ('getVersion')

import os
import os.path
import re
import subprocess
import sys


RELEASE_VERSION_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'RELEASE-VERSION'
)

# http://www.python.org/dev/peps/pep-0386/
_PEP386_SHORT_VERSION_RE = r'\d+(?:\.\d+)+(?:(?:[abc]|rc)\d+(?:\.\d+)*)?'
_PEP386_VERSION_RE = r'^%s(?:\.post\d+)?(?:\.dev\d+)?$' % (
    _PEP386_SHORT_VERSION_RE)
_GIT_DESCRIPTION_RE = r'^v(?P<ver>%s)-(?P<commits>\d+)-g(?P<sha>[\da-f]+)$' % (
    _PEP386_SHORT_VERSION_RE)


def read_git_version():
    try:
        proc = subprocess.Popen(('git', 'describe', '--long',
                                 '--match', 'v[0-9]*.*'),
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        data, _ = proc.communicate()
        if proc.returncode:
            return None
        ver = data.splitlines()[0].strip()
    except IOError:
        return None

    if not ver:
        return None
    m = re.search(_GIT_DESCRIPTION_RE, ver.decode('utf8'))
    if not m:
        sys.stderr.write('version: git description (%s) is invalid, '
                         'ignoring\n' % ver)
        return None

    commits = int(m.group('commits'))
    if not commits:
        return m.group('ver')
    else:
        suffix = os.environ.get('GIT_VERSION_SUFFIX')
        if suffix is None:
            suffix = 'post%d.dev%d' % (commits, int(m.group('sha'), 16))
        return '%s.%s' % (m.group('ver'), suffix)


def read_release_version():
    try:
        fd = open(RELEASE_VERSION_FILE)
        try:
            ver = fd.readline().strip()
        finally:
            fd.close()
        if not re.search(_PEP386_VERSION_RE, ver):
            sys.stderr.write('version: release version (%s) is invalid, '
                             'will use it anyway\n' % ver)
        return ver
    except IOError:
        return None


def write_release_version(version):
    fd = open(RELEASE_VERSION_FILE, 'w')
    fd.write('%s\n' % version)
    fd.close()


def get_version():
    release_version = read_release_version()
    version = read_git_version() or release_version
    if not version:
        version = '0.0.0'
    elif version != release_version:
        write_release_version(version)
    return version


if __name__ == '__main__':
    print(get_version())
