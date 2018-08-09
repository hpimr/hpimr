# -*- coding: UTF-8 -*-
#
#

import unittest
import re
import testsdata

# треба просто дописувати неправильні закінчення сюди:
genitives = [
        'поясу',
        # 'стола',  # ok, ok, just kidding .)
    ]


class SomeGenitiveCases_Test(testsdata.TestsData, unittest.TestCase):
    def setUp(self):
        self.genitives = [
                re.compile(r'\s{}\s'.format(g), re.M|re.X)
                    for g in genitives
            ]

    def test_CommonGenitives(self):
        """===> Перевірка закінчень деяких слів у родовому"""
        for f in self.ascfiles:
            for gpatt in self.genitives:
                self.assertFalse(gpatt.search(f.text),
                    '{} містить "{}".'.format(f.name, gpatt.pattern))


if __name__ == '__main__':
    unittest.main()

