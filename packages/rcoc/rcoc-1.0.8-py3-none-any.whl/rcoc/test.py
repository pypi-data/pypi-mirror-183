import rcoc, unittest

class TestRcoc(unittest.TestCase):

    def test_specific_country(self):
        '''Passing non existent country should return empty string'''
        self.assertEqual(rcoc.get_random_city_by_country("Non existent country"), "")


if __name__ == '__main__':
    unittest.main()

