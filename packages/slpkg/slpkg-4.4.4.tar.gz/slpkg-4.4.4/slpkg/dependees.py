#!/usr/bin/python3
# -*- coding: utf-8 -*-

from slpkg.configs import Configs
from slpkg.queries import SBoQueries


class Dependees:
    """ Show which packages depend. """

    def __init__(self, packages: list, flags: list):
        self.packages = packages
        self.flags = flags
        self.configs = Configs
        self.colors = self.configs.colour

    def slackbuilds(self):
        """ Collecting the dependees. """
        color = self.colors()
        cyan = color['cyan']
        grey = color['grey']
        yellow = color['yellow']
        endc = color['endc']

        print(f"The list below shows the "
              f"packages that dependees on '{', '.join([p for p in self.packages])}':\n")

        print(end='\rCollecting the data... ')

        dependees = {}
        for package in self.packages:
            found = []  # Reset list every package
            sbos = SBoQueries('').sbos()

            for sbo in sbos:
                requires = SBoQueries(sbo).requires()

                if package in requires:
                    found.append(sbo)
                    dependees[package] = found

        last = ' └─'
        print('\n')
        if dependees:
            for key, value in dependees.items():
                print(f'{yellow}{key}{endc}')
                print(end=f'\r{last}')
                char = ' ├─'

                for i, v in enumerate(value, start=1):
                    if i == len(value):
                        char = last

                    if i == 1:
                        print(f'{cyan}{v}{endc}')
                    else:
                        print(f'{" " * 3}{cyan}{v}{endc}')

                    if '--full-reverse' in self.flags:
                        print(f'{" " * 4}{char} {" ".join([req for req in SBoQueries(v).requires()])}')

                print(f'\n{grey}{len(value)} dependees for {key}{endc}\n')
        else:
            print('No dependees found.\n')
