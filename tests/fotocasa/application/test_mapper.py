import unittest

import pytest
import json

@pytest.mark.current
class TestMapper(unittest.TestCase):
    def testRawFlatToObject(self):
        #Given
        raw_flat = json.load("test/data/flat_fotocasa.json")



        self.assertEqual(True, False)


