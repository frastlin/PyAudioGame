import unittest2
from platform_utils import paths


class TestModulePath(unittest2.TestCase):

 def test_module_path(self):
  print paths.module_path()
  self.assertTrue(paths.module_path().endswith('tests'))
