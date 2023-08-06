import unittest

from python.services.functions.mounted_directory import construct_file_path


class TestMountDirectory(unittest.TestCase):

    def test_a_construct_file_path_steubing(self):
        self.assertTrue(construct_file_path('Steubing').endswith("Steubing"), True)

    def test_b_construct_file_path_caceis(self):
        self.assertTrue(construct_file_path('Caceis').endswith("Caceis"), True)

    def test_c_construct_file_path_konvertierer(self):
        self.assertTrue(construct_file_path('1 Konvertierer').endswith("1 Konvertierer"), True)
