import os, sys, pathlib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))  #needed to import libs from project directory
import w_yaml as w_y
import unittest

class Test_W_Yaml(unittest.TestCase):
    def test_ProcessYAML(self):
        debug, yaml_data = w_y.ProcessYAML('portfolio.yaml') 
        assert(debug, False)

if __name__ == "__main__":
    unittest.main()
    #debug, yaml_data = w_y.ProcessYAML('portfolio.yaml') 
    #print(f"Debug: {debug}") 