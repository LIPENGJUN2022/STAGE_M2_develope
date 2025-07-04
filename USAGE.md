# Deelogeny M2 - Usage Guide

This document provides comprehensive usage instructions for the deelogeny_m2 package, which integrates phylogenetic analysis, simulation, and machine learning tools.

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Core Functionality](#core-functionality)
4. [MPD Analysis](#mpd-analysis)
5. [Classifiers](#classifiers)
6. [Two-Dimensional Visualization](#two-dimensional-visualization)
7. [Python API Reference](#python-api-reference)
8. [Command Line Interface](#command-line-interface)
9. [Examples](#examples)
10. [Troubleshooting](#troubleshooting)

## Installation

### Prerequisites

- Python 3.10 or higher
- Linux operating system (Ubuntu/Debian recommended)
- Bio++ libraries (for simulations)
- FastTree (for tree computation)

### Install the Package

```bash
# Clone the repository
git clone https://github.com/LIPENGJUN2022/deelogeny-m2.git
cd deelogeny-m2

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install basic version
pip install -e .

# Install with classifier support
pip install -e .[classifiers]

# Install with all dependencies
pip install -e .[all]
```

### Install System Dependencies

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install git cmake g++ libeigen3-dev python3-pip python3-venv

# Install Bio++ (required for simulations)
# Follow instructions in INSTALL.md
```

## Quick Start

### Basic Workflow

```python
from deelogeny_m2 import Preprocess, Computing_trees, Descriptor, Bppsimulator

# 1. Preprocess alignments
preprocessor = Preprocess(
    input="data/alignments",
    output="results/preprocessed",
    minseq=5,
    maxsites=10000,
    minsites=10,
    type="aa"
)
preprocessor.preprocessing()
preprocessor.remove_gaps()
preprocessor.remove_ambig_sites('gapless')

# 2. Compute phylogenetic trees
tree_computer = Computing_trees(
    inputdir="results/preprocessed/gap_and_ambigless",
    outputdir="results/trees",
    alphabet="aa"
)
tree_computer.compute_all_trees()

# 3. Analyze alignment descriptors
descriptor = Descriptor(
    input="data/alignments",
    output="results/descriptors"
)
descriptor.calculate()
```

### Command Line Workflow

```bash
# 1. Preprocess alignments
deelogeny preprocess --input data/alignments --output results/preprocessed --minseq 5 --maxsites 10000 --minsites 10 --type aa

# 2. Compute phylogenetic trees
deelogeny compute-trees --input results/preprocessed/gap_and_ambigless --output results/trees --alphabet aa

# 3. Analyze alignment descriptors
deelogeny describe --input data/alignments --output results/descriptors
```

## Core Functionality

### Preprocessing Alignments

The preprocessing module filters and cleans multiple sequence alignments.

**Python API:**
```python
from deelogeny_m2 import Preprocess

preprocessor = Preprocess(
    input="data/alignments",      # Input directory with .fasta/.aln files
    output="results/preprocessed", # Output directory
    minseq=5,                     # Minimum number of sequences
    maxsites=10000,               # Maximum number of sites
    minsites=10,                  # Minimum number of sites
    type="aa"                     # Sequence type: "aa" or "dna"
)

# Run preprocessing steps
preprocessor.preprocessing()           # Remove outliers
preprocessor.remove_gaps()             # Remove gap columns
preprocessor.remove_ambig_sites('gapless')  # Remove ambiguous sites
```

**Command Line:**
```bash
deelogeny preprocess --input data/alignments --output results/preprocessed --minseq 5 --maxsites 10000 --minsites 10 --type aa
```

### Computing Phylogenetic Trees

Generate phylogenetic trees using FastTree.

**Python API:**
```python
from deelogeny_m2 import Computing_trees

tree_computer = Computing_trees(
    inputdir="results/preprocessed/gap_and_ambigless",  # Input directory
    outputdir="results/trees",                          # Output directory
    alphabet="aa",                                      # "aa" or "nt"
    only="specific_files.txt"                          # Optional: process only listed files
)

tree_computer.compute_all_trees()
```

**Command Line:**
```bash
deelogeny compute-trees --input results/preprocessed/gap_and_ambigless --output results/trees --alphabet aa
```

### Alignment Descriptors

Analyze alignment characteristics and generate visualizations.

**Python API:**
```python
from deelogeny_m2 import Descriptor

descriptor = Descriptor(
    input="data/alignments",    # Input directory
    output="results/descriptors" # Output directory
)

descriptor.calculate()  # Generates plots and data.tsv
```

**Command Line:**
```bash
deelogeny describe --input data/alignments --output results/descriptors
```

### Simulations

Run phylogenetic simulations using BPP or ESM models.

**BPP Simulations:**
```python
from deelogeny_m2 import Bppsimulator

simulator = Bppsimulator(
    align="data/alignments",                    # Input alignments
    tree="results/trees",                       # Input trees
    config="config/bpp/WAG_frequencies.bpp",    # BPP configuration
    output="results/simulations",               # Output directory
    tools="tools/",                             # Tools directory
    ext_length=0.1,                             # Optional: external branch length
    root_length=0.05,                           # Optional: root branch length
    gaps=True,                                  # Optional: add gaps
    mapping="config/mapping/mapnh.bpp"          # Optional: mapping file
)

simulator.simulate()
```

**ESM Simulations:**
```python
from deelogeny_m2 import ESMsimulator

simulator = ESMsimulator(
    align="data/alignments",
    tree="results/trees",
    output="results/simulations",
    tools="tools/"
)

simulator.simulate(gap=True)  # Optional: add gaps
```

**Command Line:**
```bash
# BPP simulations
deelogeny simulate-bpp --align data/alignments --tree results/trees --config config/bpp/WAG_frequencies.bpp --output results/simulations --tools tools/

# ESM simulations
deelogeny simulate-esm --align data/alignments --tree results/trees --output results/simulations --tools tools/ --gaps
```

## MPD Analysis

Mean Phylogenetic Distance (MPD) analysis tools for comparing empirical and simulated sequences.

### Creating Group Folders

**Python API:**
```python
from deelogeny_m2.mpd import create_group_folders

# Define group structure
group_def = {
    "group1_four_model_F": [
        "DSO78_frequencies",
        "JTT92_frequencies",
        "LG08_frequencies",
        "WAG_frequencies"
    ],
    "group2_WAG_posterior_extra_length": {
        "with_data2": [
            "WAG_frequencies_posterior_extra_length_data2_ext_0",
            "WAG_frequencies_posterior_extra_length_data2_ext_0.05"
        ],
        "without_data2": [
            "WAG_frequencies_posterior_extra_length_ext_0",
            "WAG_frequencies_posterior_extra_length_ext_0.05"
        ]
    }
}

create_group_folders("results/MPD/viridiplantae_group_results", group_def)
```

**Command Line:**
```bash
deelogeny mpd-create-folders --base-dir results/MPD/viridiplantae_group_results
```

### Processing Alignments and Calculating Distances

**Command Line:**
```bash
deelogeny mpd-process-alignments --empirical data/empirical --simulation results/simulations/BPP/WAG_frequencies --output results/MPD --plot --threads 4
```

### Plotting Group Results

**Command Line:**
```bash
deelogeny mpd-plot-groups
```

## Classifiers

Train and evaluate machine learning classifiers for phylogenetic simulation analysis.

### Training Classifiers

**Python API:**
```python
from deelogeny_m2.classifiers import train_classifier_main

# Train classifier (parameters depend on the specific implementation)
train_classifier_main()
```

**Command Line:**
```bash
deelogeny train-classifier --config config/classifier_config.yaml --data data/ --output results/classifiers
```

## Two-Dimensional Visualization

Interactive 2D visualization tools for exploring phylogenetic data.

### Running the 2D App

**Python API:**
```python
from deelogeny_m2.twodim import twodim_app_main

# Start 2D visualization app
twodim_app_main()
```

**Command Line:**
```bash
deelogeny twodim-app --port 8080 --host 0.0.0.0
```

## Python API Reference

### Main Classes

```python
from deelogeny_m2 import (
    Preprocess,           # Alignment preprocessing
    Computing_trees,      # Tree computation
    Descriptor,           # Alignment analysis
    Bppsimulator,         # BPP simulations
    ESMsimulator,         # ESM simulations
    AddGap,              # Gap addition utility
    GTR, HKY, estim_seq  # Model mapping utilities
)
```

### Submodules

```python
# MPD analysis
from deelogeny_m2.mpd import (
    create_group_folders,
    process_alignments_main,
    plot_distance_distribution_cli,
    plot_results_folder_cli,
    plot_groups_main
)

# Classifiers
from deelogeny_m2.classifiers import (
    train_classifier_main,
    pipeline_main
)

# 2D visualization
from deelogeny_m2.twodim import (
    twodim_app_main
)
```

## Command Line Interface

### Available Commands

```bash
# Core functionality
deelogeny preprocess      # Preprocess alignments
deelogeny compute-trees   # Compute phylogenetic trees
deelogeny describe        # Analyze alignment descriptors
deelogeny simulate-bpp    # Run BPP simulations
deelogeny simulate-esm    # Run ESM simulations

# MPD analysis
deelogeny mpd-create-folders      # Create MPD group folders
deelogeny mpd-process-alignments  # Process alignments and calculate MPD
deelogeny mpd-plot-groups         # Plot MPD group results

# Classifiers
deelogeny train-classifier        # Train a classifier

# Visualization
deelogeny twodim-app             # Run 2D visualization app
```

### Help and Examples

```bash
# Get help for a specific command
deelogeny preprocess --help

# See all available commands
deelogeny --help
```

## Examples

### Complete Workflow Example

```python
#!/usr/bin/env python3
"""
Complete workflow example for phylogenetic analysis
"""

from deelogeny_m2 import Preprocess, Computing_trees, Descriptor, Bppsimulator
from deelogeny_m2.mpd import create_group_folders, plot_groups_main

def main():
    # 1. Preprocess alignments
    print("Step 1: Preprocessing alignments...")
    preprocessor = Preprocess(
        input="data/alignments",
        output="results/preprocessed",
        minseq=5,
        maxsites=10000,
        minsites=10,
        type="aa"
    )
    preprocessor.preprocessing()
    preprocessor.remove_gaps()
    preprocessor.remove_ambig_sites('gapless')
    
    # 2. Compute trees
    print("Step 2: Computing phylogenetic trees...")
    tree_computer = Computing_trees(
        inputdir="results/preprocessed/gap_and_ambigless",
        outputdir="results/trees",
        alphabet="aa"
    )
    tree_computer.compute_all_trees()
    
    # 3. Analyze descriptors
    print("Step 3: Analyzing alignment descriptors...")
    descriptor = Descriptor(
        input="data/alignments",
        output="results/descriptors"
    )
    descriptor.calculate()
    
    # 4. Run simulations
    print("Step 4: Running BPP simulations...")
    simulator = Bppsimulator(
        align="results/preprocessed/gap_and_ambigless",
        tree="results/trees",
        config="config/bpp/WAG_frequencies.bpp",
        output="results/simulations",
        tools="tools/"
    )
    simulator.simulate()
    
    # 5. MPD analysis
    print("Step 5: Creating MPD group folders...")
    create_group_folders("results/MPD/group_results", default_group_def())
    
    print("Step 6: Plotting MPD results...")
    plot_groups_main()
    
    print("Workflow completed!")

if __name__ == "__main__":
    main()
```

### Command Line Workflow Example

```bash
#!/bin/bash
# Complete workflow using command line interface

echo "Step 1: Preprocessing alignments..."
deelogeny preprocess --input data/alignments --output results/preprocessed --minseq 5 --maxsites 10000 --minsites 10 --type aa

echo "Step 2: Computing phylogenetic trees..."
deelogeny compute-trees --input results/preprocessed/gap_and_ambigless --output results/trees --alphabet aa

echo "Step 3: Analyzing alignment descriptors..."
deelogeny describe --input data/alignments --output results/descriptors

echo "Step 4: Running BPP simulations..."
deelogeny simulate-bpp --align results/preprocessed/gap_and_ambigless --tree results/trees --config config/bpp/WAG_frequencies.bpp --output results/simulations --tools tools/

echo "Step 5: Creating MPD group folders..."
deelogeny mpd-create-folders --base-dir results/MPD/group_results

echo "Step 6: Processing alignments for MPD..."
deelogeny mpd-process-alignments --empirical data/empirical --simulation results/simulations/BPP/WAG_frequencies --output results/MPD --plot --threads 4

echo "Step 7: Plotting MPD results..."
deelogeny mpd-plot-groups

echo "Workflow completed!"
```

## Troubleshooting

### Common Issues

1. **Bio++ not found:**
   - Ensure Bio++ is installed and environment variables are set
   - Check PATH includes Bio++ binaries
   - Verify LD_LIBRARY_PATH includes Bio++ libraries

2. **FastTree not found:**
   - Install FastTree: `sudo apt install fasttree` (Ubuntu/Debian)
   - Or download from: http://www.microbesonline.org/fasttree/

3. **Import errors:**
   - Ensure virtual environment is activated
   - Check package installation: `pip list | grep deelogeny`
   - Try reinstalling: `pip install -e . --force-reinstall`

4. **Permission errors:**
   - Check file/directory permissions
   - Use `chmod` to set appropriate permissions

### Getting Help

- Check the [README.md](README.md) for detailed project information
- Review the [INSTALL.md](INSTALL.md) for installation instructions
- Open an issue on GitHub for bugs or feature requests
- Check the example scripts in the `examples/` directory

### Logging

Most functions provide detailed logging. Check log files for error details:
- `preprocess.log` - Preprocessing logs
- `process_alignments.log` - MPD analysis logs
- `plot_groups.log` - Plotting logs

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use this software in your research, please cite:

```
LI PENGJUN. (2024). Deelogeny M2: Learning-based analysis of phylogenetic simulation methods. 
GitHub repository: https://github.com/LIPENGJUN2022/deelogeny-m2
``` 