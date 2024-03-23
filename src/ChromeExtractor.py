from os import path
from itertools import chain

from Extractor import Extractor


class ChromeExtractor(Extractor):
    def __init__(self):
        self.basedir = self._get_base_dir()

    @staticmethod
    def _get_base_dir():
        return '/home/rhys/.config/chromium'

    def _profiles(self):
        return (path.join(self.basedir, 'Default'), )

    def history(self):
        out = []
        for p in self._profiles():
            file = path.join(p, 'History')

            out.append(map(
                    lambda x: (x[1], (x[5]//1000000)-11644473600),
                    self._sqlite3_load_table(file, 'urls')
                )
            )

        return chain(*out)
