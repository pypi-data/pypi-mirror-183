#!/usr/bin/python3
# -*- coding: utf-8 -*-

import locale

from dialog import Dialog
from slpkg.configs import Configs
from slpkg.views.version import Version

locale.setlocale(locale.LC_ALL, '')


class DialogBox:

    def __init__(self):
        self.configs = Configs()
        self.d = Dialog(dialog="dialog")
        self.d.set_background_title(f'{self.configs.prog_name} {Version().version} - Software Package Manager')

    def checklist(self, text, title, height, width, list_height, choices, packages):
        """ Display a checklist box. """

        if self.configs.dialog:
            code, tags = self.d.checklist(text, title=title, height=height,  width=width,
                                          list_height=list_height, choices=choices)
        else:
            code = False
            tags = packages

        return code, tags
