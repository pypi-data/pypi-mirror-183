#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import urllib3

from slpkg.configs import Configs


class CheckUpdates:
    """ Check for changes in the ChangeLog file. """

    def __init__(self):
        self.configs = Configs

    def check(self) -> bool:
        """ Checks the ChangeLogs and returns True or False. """
        print(end='\rChecking for news in the Changelog.txt file... ')
        local_date = 0

        local_chg_txt = os.path.join(self.configs.sbo_repo_path,
                                     self.configs.sbo_chglog_txt)

        http = urllib3.PoolManager()
        repo = http.request(
            'GET', f'{self.configs.sbo_repo_url}/{self.configs.sbo_chglog_txt}')

        if os.path.isfile(local_chg_txt):
            local_date = int(os.stat(local_chg_txt).st_size)

        repo_date = int(repo.headers['Content-Length'])

        return repo_date != local_date

    def updates(self):
        if self.check():
            print('\n\nThere are new updates available!\n')
        else:
            print('\n\nNo updated packages since the last check.\n')
