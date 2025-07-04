"""
Deelogeny M2 - Learning-based analysis of the realism of phylogenetic simulation methods

This package provides tools for:
- Preprocessing phylogenetic alignments
- Computing phylogenetic trees
- Running simulations with various models (BPP, ESM)
- Analyzing alignment descriptors
- Training and evaluating classifiers
- Visualizing results

Author: LI PENGJUN
Supervision: M. GUEGUEN LAURENT, LBBE, Lyon 1
"""

# Core preprocessing functionality
from .preprocess import Preprocess

# Tree computation
from .computing_trees import Computing_trees

# Simulation capabilities
from .simulators import Bppsimulator, ESMsimulator, AddGap

# Alignment analysis
from .alignment_descriptor import Descriptor

# Model mapping utilities
from .mapping2model import GTR, HKY, estim_seq

# mpD module
from . import mpd

# classifiers
from . import classifiers

# twodim module
from . import twodim

# Version information
__version__ = "0.1.0"
__author__ = "LI PENGJUN"
__email__ = "PENGJUNLI2022@163.COM"

# Main classes for easy access
__all__ = [
    "Preprocess",
    "Computing_trees", 
    "Bppsimulator",
    "ESMsimulator",
    "AddGap",
    "Descriptor",
    "GTR",
    "HKY", 
    "estim_seq"
]
