import unittest

import pytest
import json

from fotocasa.application.Mapper import Mapper


class TestMapper(unittest.TestCase):
    def testRawFlatToObject(self):
        #Given
        with open('tests/data/flat_fotocasa.json') as json_file:
            data = json.load(json_file)

        result = Mapper().rawFlatToObject(data)

        self.assertIsNotNone(result)


