#
#
#

import os


class AscFile:
    def __init__(self, fname):
        self.name = fname
        self.text = ''.join(open(fname).readlines())


class TestsData:
    @property
    def ascfiles(self):
        return [ AscFile(f)
                 for f in os.listdir('.')
                    if os.path.isfile(os.path.join('.', f))
                    and f[-4:]=='.asc' ]


