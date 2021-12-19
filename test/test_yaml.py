import os, sys, pathlib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))  #needed to import libs from project directory
import w_yaml as w_y
import unittest

class test_w_yaml(unittest.TestCase):
    debug, yaml_data = w_y.ProcessYAML('portfolio.yaml') 
    def test_processyaml(self):
        self.assertEqual(self.debug, False , "Debug needs to be True or False")
        
    def test_keys(self):
        api_key = self.yaml_data['api_key']
        api_key_dev = self.yaml_data['api_key_dev']
        self.assertIn(api_key, "8C7LNHUO0MZEPUTC")
        self.assertIn(api_key_dev, "4OYY6AT2N9B0WB5X")
        
    def test_crypto(self):
        pass

    def test_property(self):
        pass    


if __name__ == "__main__":
    unittest.main()
    