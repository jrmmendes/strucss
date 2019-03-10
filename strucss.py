#! /usr/bin/env python3

import os
import sys


class CssStructure:
    """
    Defines a CSS structure that can be generated with Strucss
    """
    def __init__(self, name, dirs, descs):
        self._name = name
        self._dirs = dirs
        self._descs = descs

    def _get_struct_info(self):
        return zip(self._dirs, self._descs)

    def generate(self):
        """
        Generates the selected structure
        """
        for dir_name, desc in self._get_struct_info():
            os.system('mkdir -p scss/'+dir_name)
            description_file = open('scss/'+dir_name+'/__DESCRIPTION__', 'w')
            description_file.write(desc)


itcss_dirs = [  # TODO: Change this manual config for a *css.toml
        'settings',
        'tools',
        'generic',
        'base',
        'objects',
        'components',
        'trumps',
    ]

itcss_desc = []
itcss_desc.append('Basic configuration of the architecture \
- e.g. colors and spacing units')

itcss_desc.append('Mixins and functions.')

itcss_desc.append('First layer that will generate compiled css directly. Only \
generic styles, like resetes and box-sizing.')

itcss_desc.append('Basic styles for h1-h6, a, blockquotes, buttons, etc. The \
last layer with tag selectors being used')

itcss_desc.append('From here, you should only use classes. Here comes the small \
pieces that will be used to mount interfaces within the app \
- e.g. lists, buttons, panels, etc')

itcss_desc.append('The macro components, mounted with objects.')

itcss_desc.append('Helpers, debug, trash.scss. Here you can make things like \
use !important to make specific things work')

itcssStructure = CssStructure('ITCSS', itcss_dirs, itcss_desc)


if __name__ == "__main__":
    structure = sys.argv[1]

    if structure.upper == 'ITCSS':
        itcssStructure.generate()

    else:
        itcssStructure.generate()
