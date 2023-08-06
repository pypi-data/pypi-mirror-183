#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import hashlib

from slpkg.views.views import ViewMessage


class Md5sum:
    """ Checksum the sources. """

    def __init__(self, flags: list):
        self.flags = flags

    def check(self, path: str, source: str, checksum: str, name: str):
        """ Checksum the source. """
        source_file = os.path.join(path, source.split('/')[-1])

        md5 = self.read_file(source_file)

        file_check = hashlib.md5(md5).hexdigest()

        if file_check not in checksum:
            print('\nExpected:', ''.join(checksum))
            print('Found:', file_check)
            print(f'\nMD5SUM check for {name} FAILED.')

            view = ViewMessage(self.flags)
            view.question()

    @staticmethod
    def read_file(filename: str) -> bytes:
        """ Reads the text file. """
        with open(filename, 'rb') as f:
            return f.read()
