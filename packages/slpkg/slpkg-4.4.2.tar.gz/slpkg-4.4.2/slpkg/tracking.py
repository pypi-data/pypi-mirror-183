#!/usr/bin/python3
# -*- coding: utf-8 -*-

from slpkg.configs import Configs
from slpkg.dependencies import Requires


class Tracking:
    """ Tracking of the package dependencies. """

    def __init__(self):
        self.configs = Configs
        self.colors = self.configs.colour

    def packages(self, packages: list):
        """ Prints the packages dependencies. """
        color = self.colors()
        cyan = color['cyan']
        grey = color['grey']
        yellow = color['yellow']
        endc = color['endc']

        print(f"The list below shows the packages with dependencies:\n")

        char = ' └─'
        for i, package in enumerate(packages):
            requires = Requires(package).resolve()
            how_many = len(requires)

            if not requires:
                requires = ['No dependencies']

            print(f'{yellow}{package}{endc}')
            print(f'{char} {cyan}{" ".join([req for req in requires])}{endc}')
            print(f'\n{grey}{how_many} dependencies for {package}{endc}\n')
