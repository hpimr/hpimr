# -*- coding: UTF-8 -*-
#
#

import unittest
import re
import testsdata


class GreatHallCase_Test(testsdata.TestsData, unittest.TestCase):
    def setUp(self):
        self.patt = re.compile(r'Велик\S+ \s+ За', re.M|re.X)

    def test_thereIsNoHall(self):
        """===> Перевірка регістру у «Велика зала» та відмінюваннях"""
        for f in self.ascfiles:
            self.assertFalse(self.patt.search(f.text),
                    '{} містить «Велика Зала» замість «Велика зала».'.format(f.name))


if __name__ == '__main__':
    unittest.main()
