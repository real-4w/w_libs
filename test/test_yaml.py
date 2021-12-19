import os, sys, pathlib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))  #needed to import libs from project directory
import w_yaml as w_y
import unittest

class test_w_yaml(unittest.TestCase):
    debug, yaml_data = w_y.ProcessYAML('portfolio.yaml') 
    def test_processyaml(self):
        self.assertFalse(self.debug, "Debug is expected to be False")
                
    def test_keys(self):
        api_key = self.yaml_data['api_key']
        api_key_dev = self.yaml_data['api_key_dev']
        self.assertIn(api_key, "8C7LNHUO0MZEPUTC")
        self.assertIn(api_key_dev, "4OYY6AT2N9B0WB5X")

    def test_currency(self):
        to_cur = self.yaml_data['to_currency']    
        self.assertIn(to_cur, "USD NZD EUR GBP AUD")

    def test_crypto(self):
        pass

    def test_property(self):
        try: 
            properties = self.yaml_data['property']
            for prop in properties:
                price = prop['price']
                mortgage = prop['mortgage']
                address = prop['address']
        except: 
            self.fail("test_property failed. Please check yaml file for a property section.")

#https://stackoverflow.com/questions/6181555/pass-a-python-unittest-if-an-exception-isnt-raised
#def test_does_not_error(self):
#    try:
#        code_under_test()
#    except ThatException:
#        self.fail("code_under_test raised ThatException")


if __name__ == "__main__":
    unittest.main()
    