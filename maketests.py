# -*- coding: UTF-8 -*-
#
#

import unittest

suite = unittest.TestLoader().discover('tests', pattern='*_test.py',)

unittest.TextTestRunner().run(suite)
