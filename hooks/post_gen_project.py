import re
import sys
import os
from argparse import ArgumentParser

from venv import EnvBuilder

EnvBuilder().create(os.path.join(os.getcwd(), '.venv'))
