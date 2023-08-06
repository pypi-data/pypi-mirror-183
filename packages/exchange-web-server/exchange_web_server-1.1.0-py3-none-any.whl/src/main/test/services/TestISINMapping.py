import unittest.mock


class TestISINMapping(unittest.TestCase):

    def test_a_zipped_files(self):
        list_a = [1, 2, 3]
        list_b = ['a', 'b', 'c']
        list_c = ['1a', '2b', '3c']

        zipped_list = zip(list_a, list_b, list_c)

        for k, v, c in zipped_list:
            self.assertEqual(k, 1)
            self.assertEqual(v, 'a')
            self.assertEqual(c, '1a')
            break
