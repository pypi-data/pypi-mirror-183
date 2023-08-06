import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from parser.generator import Generator

print(Generator('poetry_test_pda_fga/yamls').generate_dags())