#!/usr/bin/env python3
"""
Basic usage example for Deelogeny M2

This script demonstrates how to use the main functionalities of the package.
"""

import os
from pathlib import Path
from deelogeny_m2 import Preprocess, Computing_trees, Descriptor, Bppsimulator

def main():
    """Example workflow"""
    
    # Set up paths
    base_dir = Path("example_data")
    input_dir = base_dir / "alignments"
    output_dir = base_dir / "results"
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("=== Deelogeny M2 Basic Usage Example ===\n")
    
    # Step 1: Preprocessing
    print("1. Preprocessing alignments...")
    preprocess_output = output_dir / "preprocessed"
    
    preprocessor = Preprocess(
        input=input_dir,
        output=preprocess_output,
        minseq=5,
        maxsites=10000,
        minsites=10,
        type="aa"
    )
    
    preprocessor.preprocessing()
    preprocessor.remove_gaps()
    preprocessor.remove_ambig_sites('gapless')
    preprocessor.remove_ambig_sites('clean')
    
    print("   ✓ Preprocessing completed")
    
    # Step 2: Compute phylogenetic trees
    print("\n2. Computing phylogenetic trees...")
    trees_output = output_dir / "trees"
    
    tree_computer = Computing_trees(
        inputdir=preprocess_output / "gap_and_ambigless",
        outputdir=trees_output,
        alphabet="aa"
    )
    
    tree_computer.compute_all_trees()
    print("   ✓ Tree computation completed")
    
    # Step 3: Analyze alignment descriptors
    print("\n3. Analyzing alignment descriptors...")
    descriptors_output = output_dir / "descriptors"
    
    descriptor = Descriptor(
        input=input_dir,
        output=descriptors_output
    )
    
    descriptor.calculate()
    print("   ✓ Alignment analysis completed")
    
    # Step 4: Run BPP simulations (if config file exists)
    config_file = Path("config/bpp/WAG_frequencies.bpp")
    if config_file.exists():
        print("\n4. Running BPP simulations...")
        simulations_output = output_dir / "simulations"
        
        simulator = Bppsimulator(
            align=preprocess_output / "gap_and_ambigless",
            tree=trees_output,
            config=config_file,
            output=simulations_output,
            tools=Path("tools")
        )
        
        simulator.simulate()
        print("   ✓ BPP simulations completed")
    else:
        print("\n4. Skipping BPP simulations (config file not found)")
    
    print(f"\n=== Results saved in: {output_dir} ===")
    print("\nAvailable output directories:")
    for subdir in output_dir.iterdir():
        if subdir.is_dir():
            print(f"  - {subdir.name}/")


if __name__ == "__main__":
    main() 