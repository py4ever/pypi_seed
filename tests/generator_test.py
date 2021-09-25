import os
import unittest

import uuid
import pypi_seed
import pypi_seed.generator as g

MPATH = os.path.dirname(pypi_seed.__file__)
PROJECT_PATH = os.path.dirname(MPATH)


class GeneratorTestCase(unittest.TestCase):
    def test_generate(self):
        dir = os.path.join(PROJECT_PATH, "tests-gen-ignored")
        project = "test" + str(uuid.uuid4())
        author = "levin"
        final_dir = os.path.join(dir, project)
        if os.path.exists(final_dir):
            os.rmdir(final_dir)
        stages = g.generate(dir, project, author)
        self.assertEqual(6, stages, "Must execute all the stages")
        readme = os.path.join(final_dir, "README.md")
        self.assertTrue(os.path.exists(readme), "README file must be generated")
        with open(readme, 'r') as rfile:
            first = rfile.readline().strip()
            headline = "# " + project
            self.assertEqual(headline, first, "Project headline should be " + headline)


if __name__ == '__main__':
    unittest.main()
