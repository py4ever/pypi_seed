import sys
import unittest
import pypi_seed.argsparser as ap


class ArgsParserTestCase(unittest.TestCase):
    def test_args2dict_with_noargs(self):
        error = None
        sys.argv = [__file__]  # reset argv
        try:
            expect = dict()
            actual = ap.args2dict()
            self.assertTrue(False, "shouldn't run here")
        except Exception as e:
            error = str(e)
        self.assertEqual("Missing project", error, "should raise error")

    def test_args2dict_opt1(self):
        sys.argv = [__file__, "--project=demo", "--author=levin", "--dir=/tmp"]
        print("system args is %s" % sys.argv)
        expect = {'project': 'demo', 'author': 'levin', 'dir': '/tmp', 'verbose': False}
        actual = ap.args2dict()
        self.assertDictEqual(expect, actual, "Invalid ")

    def test_args2dict_opt2(self):
        sys.argv = [__file__, "--project", "demo", "--author", "levin", "--dir", "/tmp"]
        print("system args is %s" % sys.argv)
        expect = {'project': 'demo', 'author': 'levin', 'dir': '/tmp', 'verbose': False}
        actual = ap.args2dict()
        self.assertDictEqual(expect, actual, "Invalid ")

    def test_args2dict_short_opt1(self):
        sys.argv = [__file__, "-p", "demo", "-a", "levin", "-d", "/tmp"]
        print("system args is %s" % sys.argv)
        expect = {'project': 'demo', 'author': 'levin', 'dir': '/tmp', 'verbose': False}
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
