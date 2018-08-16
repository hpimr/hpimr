# -*- coding: UTF-8 -*-
#
#

import unittest
import re
import testsdata

# треба просто дописувати типові помилки сюди:
genitives = [
        'поясу',
        'гуртожитка',
        # 'стола',  # ok, ok, just kidding .)
    ]


class SomeMisspelledCases_Test(testsdata.TestsData, unittest.TestCase):
    def setUp(self):
        self.genitives = [
                re.compile(r'\s{}\s'.format(g), re.M|re.X)
                    for g in genitives
            ]

    def test_CommonMisspellings(self):
        """===> Перевірка деяких типових помилок"""
        for f in self.ascfiles:
            for gpatt in self.genitives:
                self.assertFalse(gpatt.search(f.text),
                    '{} містить "{}".'.format(f.name, gpatt.pattern))


if __name__ == '__main__':
    unittest.main()

