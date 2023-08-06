import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from parser.generator import Generator

def return_generate_dags_by_file(file):
    return Generator(file).generate_dags()