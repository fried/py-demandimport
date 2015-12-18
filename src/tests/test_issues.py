import unittest
import textwrap
import os.path

import demandimport
from demandimport.tests import TestModule

# Test-cases for bugs we encountered

class TestIssues(unittest.TestCase):
    def test_issue1(self):
        with TestModule() as m:
            with demandimport.enabled():
                with open(os.path.join(m.path, 'a.py'), 'w') as f:
                    f.write(textwrap.dedent("""
                            import {0}.b
                            {0}.b.__name__
                            """).format(m.name))
                with open(os.path.join(m.path, 'b.py'), 'w') as f:
                    pass
                __import__(m.name+'.a', locals={'foo': 'bar'}).a.__name__

if __name__ == '__main__':
    def log(msg, *args):
        print(msg % args)
    demandimport.set_logfunc(log)
    unittest.main()
