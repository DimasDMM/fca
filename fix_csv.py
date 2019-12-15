#-*- coding: utf8 -*-

import os
import sys
import pandas as pd
from pathlib import Path

"""
Change semicolons ";" to commas ","
"""

# Receives the filepath as argument
source = sys.argv[1]

df = pd.read_csv(source, sep=';')

dirname = os.path.dirname(os.path.abspath(source))
filename = Path(source).name

result = os.path.join(dirname, "fixed_%s" % (filename))
df.to_csv(result, index=False)

