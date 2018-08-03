# -*- coding: UTF-8 -*-
#
#

import os
import re
import unittest

class GreatHallCase_Test(unittest.TestCase):
    def setUp(self):
        self.patt = re.compile(r'Велик\S+ \s+ За', re.M|re.X)

        self.files = [ f for f in os.listdir('.')
                if os.path.isfile(os.path.join('.', f))
                and f[-4:]=='.asc' ]

    def test_thereIsNoHall(self):
        for f in self.files:
            lines = '\n'.join(open(f).readlines())
            self.assertFalse(self.patt.search(lines),
                    'File {} contains "Great Hall in wrong case."'.format(f))


if __name__ == '__main__':
    unittest.main()
