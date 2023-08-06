import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from parser.generator import Generator

def funcao_teste():
    print('ok')

def return_yaml_file(file):
    print(Generator(file).generate_dags())