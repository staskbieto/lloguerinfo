import unittest

import django
import pytest
import json

from fotocasa.application.Mapper import Mapper


class TestMapper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        django.setup()


    def testRawFlatToObject(self):
        #Given
        with open('tests/data/flat_fotocasa.json') as json_file:
            data = json.load(json_file)

        result = Mapper().rawFlatToObject(data)

        result = Mapper().rawFlatToObject(data)
        self.assertEqual(result['neighbourhood'], "el fort pienc")
        self.assertEqual(round(result['neighbourhood_meanprice'],2), 14.02)
        self.assertEqual(result['price_m2'], 9.67741935483871)


    def testRawFlatToObject_NoPrice(self):
        #Given
        with open('tests/data/flat_fotocasa.json') as json_file:
            data = json.load(json_file)

        data['rawPrice'] = None
        result = Mapper().rawFlatToObject(data)
        self.assertIsNone(result['price_m2'])
