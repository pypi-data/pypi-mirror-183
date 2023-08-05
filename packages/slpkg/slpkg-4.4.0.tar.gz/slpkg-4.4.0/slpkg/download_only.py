#!/usr/bin/python3
# -*- coding: utf-8 -*-


from slpkg.downloader import Wget
from slpkg.configs import Configs
from slpkg.queries import SBoQueries
from slpkg.views.views import ViewMessage
from slpkg.models.models import session as Session


class Download:
    """ Download the slackbuilds with the sources only. """

    def __init__(self, flags: list):
        self.flags: list = flags
        self.configs = Configs
        self.session = Session

    def packages(self, slackbuilds: list):
        """ Download the package only. """
        view = ViewMessage(self.flags)
        view.download_packages(slackbuilds)
        view.question()
        wget = Wget()

        for sbo in slackbuilds:
            file = f'{sbo}{self.configs.sbo_tar_suffix}'
            location = SBoQueries(sbo).location()
            url = f'{self.configs.sbo_repo_url}/{location}/{file}'

            wget.download(self.configs.download_only, url)

            sources = SBoQueries(sbo).sources()
            for source in sources:
                wget.download(self.configs.download_only, source)
