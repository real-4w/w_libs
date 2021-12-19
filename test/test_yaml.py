import os, sys, pathlib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))  #needed to import libs from project directory
import w_yaml as w_y
if __name__ == "__main__":
    debug, yaml_data = w_y.ProcessYAML('portfolio.yaml')  