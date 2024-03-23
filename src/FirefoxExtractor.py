from os import path
from itertools import chain
from glob import glob

from Extractor import Extractor


class FirefoxExtractor(Extractor):
    def __init__(self):
        self.basedir = self._get_base_dir()

    @staticmethod
    def _get_base_dir():
        return '/home/rhys/.mozilla/firefox/'

    def _profiles(self):
        return (
                path.join(self.basedir, 'default'),
                *glob(path.join(self.basedir, '*.default'))
            )

    def history(self):
        out = []
        for p in self._profiles():
            file = path.join(p, 'places.sqlite')

            out.append(map(
                    lambda x: (x[1], x[8]//10**6),
                    filter(
                        lambda x: x[8],
                        self._sqlite3_load_table(file, 'moz_places')
                    )
                )
            )

        return chain(*out)
