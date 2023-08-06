# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sanpo']

package_data = \
{'': ['*']}

install_requires = \
['chardet>=5,<6', 'pygments>=2,<3']

entry_points = \
{'console_scripts': ['sanpo = sanpo.command:main']}

setup_kwargs = {
    'name': 'sanpo',
    'version': '0.2.0',
    'description': 'Sanitize PO files from gettext for version control',
    'long_description': '# sanpo\n\n`sanpo` is a command line tool to sanitize PO files from gettext for version\ncontrol.\n\n## The problem\n\nThe [gettext](https://www.gnu.org/software/gettext/) collects text to be\ntranslated from source code in PO files that can be sent to translators. These\nfiles contain metadata about the project that can be helpful when using an\nemail based workflow.\n\nWhen creating a PO file the first time, these metadata look like this:\n\n```\n"Project-Id-Version: PACKAGE VERSION\\n"\n"Report-Msgid-Bugs-To: \\n"\n"POT-Creation-Date: 2021-09-06 16:16+0200\\n"\n"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"\n"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"\n"Language-Team: LANGUAGE <LL@li.org>\\n"\n"Language: \\n"\n"MIME-Version: 1.0\\n"\n"Content-Type: text/plain; charset=UTF-8\\n"\n"Content-Transfer-Encoding: 8bit\\n"\n"Plural-Forms: nplurals=2; plural=(n != 1);\\n"\n```\n\nHowever, when having the PO file under version control, these metadata get in\nthe way. Most of them are available from the commit history. And when\nrunning `gettext` automatically as part of the build process, the\n`PO-Revision-Date` get updated every time even if none of the messages\nchanged, resulting in spuriously modified PO files without any actual\nchanges worth committing.\n\n## The solution\n\nYour localized software does not use the PO files directly but the MO files\ncompiled from them, they unhelpful metadata can be removed. Which is exactly\nwhat `sanpo` does.\n\nA typical build chain would look like this:\n\n1. gettext - collect PO file\n2. msgfmt - compile into MO file\n3. sanpo - remove unhelpful metadata from PO\n4. commit possible changes in PO file\n\n`sanpo` simple takes one or more PO files as argument, for example:\n\n```bash\nsanpo locale/de/LC_MESSAGES/django.po locale/en/LC_MESSAGES/django.po locale/hu/LC_MESSAGES/django.po\n```\n\nAfter this, the remaining metadata are:\n\n```\n"Language: \\n"\n"MIME-Version: 1.0\\n"\n"Content-Type: text/plain; charset=UTF-8\\n"\n"Content-Transfer-Encoding: 8bit\\n"\n"Plural-Forms: nplurals=2; plural=(n != 1);\\n"\n```\n\nUsing the special pattern `**` folders can be scanned recursively.\n\nTo sanitize PO files for all languages in a certain folder, use for example:\n\n```bash\nsanpo locale/**/django.po\n```\n\n## Django\n\nFor [Django](https://www.djangoproject.com/) projects, the typical workflow\nis:\n\n1. django-admin makemessages\n2. django-admin compilemessages\n3. sanpo\n4. commit possible changes in PO file\n',
    'author': 'Thomas Aglassinger',
    'author_email': 'roskakori@users.sourceforge.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/roskakori/sanpo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.9,<4.0.0',
}


setup(**setup_kwargs)
