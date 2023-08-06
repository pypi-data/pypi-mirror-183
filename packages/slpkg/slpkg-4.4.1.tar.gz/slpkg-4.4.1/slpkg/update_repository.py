#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

from os import path

from slpkg.downloader import Wget
from slpkg.configs import Configs
from slpkg.create_data import CreateData
from slpkg.models.models import SBoTable
from slpkg.views.views import ViewMessage
from slpkg.check_updates import CheckUpdates
from slpkg.models.models import session as Session


class UpdateRepository:
    """ Deletes and install the data. """

    def __init__(self, flags: list):
        self.flags = flags
        self.configs = Configs
        self.session = Session

    def sbo(self):
        """ Updated the sbo repository. """
        view = ViewMessage(self.flags)
        check_updates = CheckUpdates()

        if not check_updates.check():
            print('\n\nNo changes in ChangeLog.txt between your last update and now.')
        else:
            print('\n\nThere are new updates available!')

        view.question()

        print('Updating the package list...\n')
        self.delete_file(self.configs.sbo_repo_path, self.configs.sbo_txt)
        self.delete_file(self.configs.sbo_repo_path, self.configs.sbo_chglog_txt)
        self.delete_sbo_data()

        slackbuilds_txt = f'{self.configs.sbo_repo_url}/{self.configs.sbo_txt}'
        changelog_txt = f'{self.configs.sbo_repo_url}/{self.configs.sbo_chglog_txt}'

        wget = Wget()
        wget.download(self.configs.sbo_repo_path, slackbuilds_txt)
        wget.download(self.configs.sbo_repo_path, changelog_txt)

        data = CreateData()
        data.insert_sbo_table()

    @staticmethod
    def delete_file(folder: str, txt_file: str):
        """ Delete the file. """
        file = f'{folder}/{txt_file}'
        if path.exists(file):
            os.remove(file)

    def delete_sbo_data(self):
        """ Delete the table from the database. """
        self.session.query(SBoTable).delete()
        self.session.commit()
