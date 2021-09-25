import sys
import unittest
import pypi_seed.argsparser as ap


class ArgsParserTestCase(unittest.TestCase):
    def test_args2dict_with_noargs(self):
        error = None
        sys.argv = [__file__]  # reset argv
        actual = ap.args2dict()
        self.assertIsNone(actual, "No output")

    def test_args2dict_opt1(self):
        sys.argv = [__file__, "--project=demo", "--author=levin", "--dir=/tmp"]
        print("system args is %s" % sys.argv)
        expect = {'name': 'demo', 'author': 'levin', 'dir': '/tmp', 'verbose': False, 'cli': False}
        actual = ap.args2dict()
        self.assertDictEqual(expect, actual, "Invalid ")

    def test_args2dict_opt2(self):
        sys.argv = [__file__, "--project", "demo", "--author", "levin", "--dir", "/tmp"]
        print("system args is %s" % sys.argv)
        expect = {'name': 'demo', 'author': 'levin', 'dir': '/tmp', 'verbose': False, 'cli': False}
        actual = ap.args2dict()
        self.assertDictEqual(expect, actual, "Invalid ")

    def test_args2dict_short_opt1(self):
        sys.argv = [__file__, "-p", "demo", "-a", "levin", "-d", "/tmp"]
        print("system args is %s" % sys.argv)
        expect = {'name': 'demo', 'author': 'levin', 'dir': '/tmp', 'verbose': False, 'cli': False}
        actual = ap.args2dict()
        self.assertDictEqual(expect, actual, "Invalid ")

    def test_args2dict_short_opt2(self):
        sys.argv = [__file__, "-h"]
        print("system args is %s" % sys.argv)
        actual = ap.args2dict()
        self.assertIsNone(actual, "Invalid ")

    def test_args2dict_short_opt3(self):
        sys.argv = [__file__, "-v"]
        print("system args is %s" % sys.argv)
        actual = ap.args2dict()
        self.assertIsNone(actual, "Invalid ")


if __name__ == '__main__':
    unittest.main()
