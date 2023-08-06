# read version from installed package
from importlib.metadata import version

__version__ = version("pycounts_k108")

# populate package namespace
from pycounts_k108.pycounts import count_words
from pycounts_k108.plotting import plot_words
