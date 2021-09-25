import unittest

import pypi_seed.template_loader as tl


class TemplateLoaderTestCase(unittest.TestCase):
    def test_resolve(self):
        expect = "/pypi_seed/template/cli.setup.py.template"
        actual = tl.resolve("cli.setup.py")
        self.assertTrue(actual.endswith(expect), "Path not match: %s " % actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
