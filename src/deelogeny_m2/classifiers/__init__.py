"""
Classifiers for phylogenetic simulation analysis (deep learning, ML, etc.)
"""

from .train import main as train_classifier_main
from .pipeline import main as pipeline_main

__all__ = [
    "train_classifier_main",
    "pipeline_main"
] 