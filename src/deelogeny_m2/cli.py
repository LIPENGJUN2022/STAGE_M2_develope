#!/usr/bin/env python3
"""
Command Line Interface for Deelogeny M2

This module provides command-line tools for the main functionalities of the package.
"""

import argparse
import sys
from pathlib import Path

from .preprocess import Preprocess
from .computing_trees import Computing_trees
from .alignment_descriptor import Descriptor
from .simulators import Bppsimulator, ESMsimulator
from .mpd import create_group_folders, process_alignments_main, plot_distance_distribution_cli, plot_results_folder_cli, plot_groups_main
from .classifiers import train_classifier_main
from .twodim import twodim_app_main


def preprocess_cmd(args):
    """Command for preprocessing alignments"""
    pr = Preprocess(
        input=args.input,
        output=args.output,
        minseq=args.minseq,
        maxsites=args.maxsites,
        minsites=args.minsites,
        type=args.type
    )
    
    print("Starting preprocessing...")
    pr.preprocessing()
    print("Removing gaps...")
    pr.remove_gaps()
    print("Removing ambiguous sites from gap-less data...")
    pr.remove_ambig_sites('gapless')
    print("Removing ambiguous sites from clean data...")
    pr.remove_ambig_sites('clean')
    print("Preprocessing completed!")


def compute_trees_cmd(args):
    """Command for computing phylogenetic trees"""
    computer = Computing_trees(
        inputdir=args.input,
        outputdir=args.output,
        alphabet=args.alphabet,
        only=args.only
    )
    
    print("Computing phylogenetic trees...")
    computer.compute_all_trees()
    print("Tree computation completed!")


def describe_alignments_cmd(args):
    """Command for analyzing alignment descriptors"""
    descriptor = Descriptor(
        input=args.input,
        output=args.output
    )
    
    print("Computing alignment descriptors...")
    descriptor.calculate()
    print("Alignment analysis completed!")


def simulate_bpp_cmd(args):
    """Command for BPP simulations"""
    simulator = Bppsimulator(
        align=args.align,
        tree=args.tree,
        config=args.config,
        output=args.output,
        tools=args.tools,
        ext_length=args.ext_length,
        root_length=args.root_length,
        gaps=args.gaps,
        mapping=args.mapping
    )
    
    print("Starting BPP simulations...")
    simulator.simulate()
    print("BPP simulations completed!")


def simulate_esm_cmd(args):
    """Command for ESM simulations"""
    simulator = ESMsimulator(
        align=args.align,
        tree=args.tree,
        output=args.output,
        tools=args.tools
    )
    
    print("Starting ESM simulations...")
    simulator.simulate(gap=args.gaps)
    print("ESM simulations completed!")


def default_group_def():
    return {
        "group1_four_model_F": [
            "DSO78_frequencies",
            "JTT92_frequencies",
            "LG08_frequencies",
            "WAG_frequencies"
        ],
        "group2_WAG_posterior_extra_length": {
            "with_data2": [
                "WAG_frequencies_posterior_extra_length_data2_ext_0",
                "WAG_frequencies_posterior_extra_length_data2_ext_0.05",
                "WAG_frequencies_posterior_extra_length_data2_ext_0.1",
                "WAG_frequencies_posterior_extra_length_data2_ext_0.2",
                "WAG_frequencies_posterior_extra_length_data2_ext_0.5"
            ],
            "without_data2": [
                "WAG_frequencies_posterior_extra_length_ext_0",
                "WAG_frequencies_posterior_extra_length_ext_0.05",
                "WAG_frequencies_posterior_extra_length_ext_0.1",
                "WAG_frequencies_posterior_extra_length_ext_0.2",
                "WAG_frequencies_posterior_extra_length_ext_0.5"
            ]
        },
        "group3_WAG_sampling_seq_root": {
            "with_data2": [
                "WAG_sampling_seq_data2_root_0",
                "WAG_sampling_seq_data2_root_0.05",
                "WAG_sampling_seq_data2_root_0.1",
                "WAG_sampling_seq_data2_root_0.2",
                "WAG_sampling_seq_data2_root_0.5"
            ],
            "without_data2": [
                "WAG_sampling_seq_root_0",
                "WAG_sampling_seq_root_0.05",
                "WAG_sampling_seq_root_0.1",
                "WAG_sampling_seq_root_0.2",
                "WAG_sampling_seq_root_0.5"
            ]
        },
        "group4_WAG_basic_comparison": {
            "with_data2": [
                "WAG_frequencies_posterior_extra_length_data2_ext_0",
                "WAG_sampling_seq_data2_root_0",
                "WAG_frequencies_sampling_seq_data2"
            ],
            "without_data2": [
                "WAG_frequencies",
                "WAG_frequencies_posterior_extra_length_ext_0",
                "WAG_sampling_seq_root_0",
                "WAG_frequencies_sampling_seq"
            ]
        }
    }


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Deelogeny M2 - Learning-based analysis of phylogenetic simulation methods",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  deelogeny preprocess --input data/alignments --output results/preprocessed --minseq 5 --maxsites 10000 --minsites 10 --type aa
  deelogeny compute-trees --input results/preprocessed/gap_and_ambigless --output results/trees --alphabet aa
  deelogeny describe --input data/alignments --output results/descriptors
  deelogeny simulate-bpp --align data/alignments --tree results/trees --config config/bpp/WAG_frequencies.bpp --output results/simulations --tools tools/
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Preprocess command
    preprocess_parser = subparsers.add_parser('preprocess', help='Preprocess alignments')
    preprocess_parser.add_argument('--input', '-i', required=True, help='Input directory with alignments')
    preprocess_parser.add_argument('--output', '-o', required=True, help='Output directory for results')
    preprocess_parser.add_argument('--minseq', '-s', type=int, required=True, help='Minimum number of sequences')
    preprocess_parser.add_argument('--maxsites', type=int, required=True, help='Maximum number of sites')
    preprocess_parser.add_argument('--minsites', type=int, required=True, help='Minimum number of sites')
    preprocess_parser.add_argument('--type', required=True, choices=['aa', 'dna'], help='Sequence type')
    preprocess_parser.set_defaults(func=preprocess_cmd)
    
    # Compute trees command
    trees_parser = subparsers.add_parser('compute-trees', help='Compute phylogenetic trees')
    trees_parser.add_argument('--input', '-i', required=True, help='Input directory with alignments')
    trees_parser.add_argument('--output', '-o', required=True, help='Output directory for trees')
    trees_parser.add_argument('--alphabet', required=True, choices=['aa', 'nt'], help='Sequence alphabet')
    trees_parser.add_argument('--only', help='File listing specific alignments to process')
    trees_parser.set_defaults(func=compute_trees_cmd)
    
    # Describe alignments command
    describe_parser = subparsers.add_parser('describe', help='Analyze alignment descriptors')
    describe_parser.add_argument('--input', '-i', required=True, help='Input directory with alignments')
    describe_parser.add_argument('--output', '-o', required=True, help='Output directory for results')
    describe_parser.set_defaults(func=describe_alignments_cmd)
    
    # BPP simulation command
    bpp_parser = subparsers.add_parser('simulate-bpp', help='Run BPP simulations')
    bpp_parser.add_argument('--align', required=True, help='Input directory with alignments')
    bpp_parser.add_argument('--tree', required=True, help='Input directory with trees')
    bpp_parser.add_argument('--config', required=True, help='BPP configuration file')
    bpp_parser.add_argument('--output', required=True, help='Output directory for simulations')
    bpp_parser.add_argument('--tools', required=True, help='Tools directory')
    bpp_parser.add_argument('--ext-length', type=float, help='External branch length')
    bpp_parser.add_argument('--root-length', type=float, help='Root branch length')
    bpp_parser.add_argument('--gaps', action='store_true', help='Add gaps to simulations')
    bpp_parser.add_argument('--mapping', help='Mapping file')
    bpp_parser.set_defaults(func=simulate_bpp_cmd)
    
    # ESM simulation command
    esm_parser = subparsers.add_parser('simulate-esm', help='Run ESM simulations')
    esm_parser.add_argument('--align', required=True, help='Input directory with alignments')
    esm_parser.add_argument('--tree', required=True, help='Input directory with trees')
    esm_parser.add_argument('--output', required=True, help='Output directory for simulations')
    esm_parser.add_argument('--tools', required=True, help='Tools directory')
    esm_parser.add_argument('--gaps', action='store_true', help='Add gaps to simulations')
    esm_parser.set_defaults(func=simulate_esm_cmd)
    
    # MPD: create group folders
    mpd_create_parser = subparsers.add_parser('mpd-create-folders', help='Create MPD group folders')
    mpd_create_parser.add_argument('--base-dir', required=True, help='Base directory for group results')
    mpd_create_parser.set_defaults(func=lambda args: create_group_folders(args.base_dir, default_group_def()))

    # MPD: process alignments
    mpd_process_parser = subparsers.add_parser('mpd-process-alignments', help='Process alignments and calculate MPD')
    mpd_process_parser.add_argument('args', nargs=argparse.REMAINDER)
    mpd_process_parser.set_defaults(func=lambda args: process_alignments_main())

    # MPD: plot groups
    mpd_plot_parser = subparsers.add_parser('mpd-plot-groups', help='Plot MPD group results')
    mpd_plot_parser.set_defaults(func=lambda args: plot_groups_main())
    
    # Classifier: train
    classifier_train_parser = subparsers.add_parser('train-classifier', help='Train a classifier (deep learning/ML)')
    classifier_train_parser.add_argument('args', nargs=argparse.REMAINDER)
    classifier_train_parser.set_defaults(func=lambda args: train_classifier_main())
    
    # Two-dimensional visualization app
    twodim_app_parser = subparsers.add_parser('twodim-app', help='Run 2D visualization app')
    twodim_app_parser.add_argument('args', nargs=argparse.REMAINDER)
    twodim_app_parser.set_defaults(func=lambda args: twodim_app_main())
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        args.func(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main() 