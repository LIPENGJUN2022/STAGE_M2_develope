# Installation Guide for Deelogeny M2

This guide will help you install and set up Deelogeny M2 for phylogenetic analysis and simulation.

## Prerequisites

### System Requirements
- Linux operating system (Ubuntu/Debian recommended)
- Python 3.10 or higher
- Git
- CMake
- C++ compiler (g++)
- Eigen3 library (version >= 3.8)

### Install System Dependencies

On Ubuntu/Debian:
```bash
sudo apt update
sudo apt install git cmake g++ libeigen3-dev python3-pip python3-venv
```

On CentOS/RHEL:
```bash
sudo yum install git cmake gcc-c++ eigen3-devel python3-pip
```

## Installation Options

### Option 1: Install from Source (Recommended)

1. **Clone the repository:**
```bash
git clone https://github.com/LIPENGJUN2022/deelogeny-m2.git
cd deelogeny-m2
```

2. **Create a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install the package:**
```bash
# Install basic version
pip install -e .

# Install with classifier support
pip install -e .[classifiers]

# Install with all dependencies (including development tools)
pip install -e .[all]
```

### Option 2: Install via pip (when available on PyPI)

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install basic version
pip install deelogeny_m2

# Install with classifier support
pip install deelogeny_m2[classifiers]
```

## Bio++ Installation

Deelogeny M2 requires Bio++ libraries for phylogenetic simulations. Follow these steps:

### Step 1: Set up Bio++ source directory
```bash
PROJECTDIR=$HOME/devel/bpp/
mkdir -p $PROJECTDIR
cd $PROJECTDIR
```

### Step 2: Clone Bio++ repositories
```bash
git clone https://github.com/BioPP/bpp-core
git clone https://github.com/BioPP/bpp-seq
git clone https://github.com/BioPP/bpp-popgen
git clone https://github.com/BioPP/bpp-phyl
git clone https://github.com/BioPP/bppsuite
```

### Step 3: Compile and install each component
```bash
# Install bpp-core
cd $PROJECTDIR/bpp-core
mkdir build && cd build
cmake -B . -S .. -DCMAKE_INSTALL_PREFIX=$HOME/.local
make
make install

# Install bpp-seq
cd $PROJECTDIR/bpp-seq
mkdir build && cd build
cmake -B . -S .. -DCMAKE_INSTALL_PREFIX=$HOME/.local
make
make install

# Install bpp-popgen
cd $PROJECTDIR/bpp-popgen
mkdir build && cd build
cmake -B . -S .. -DCMAKE_INSTALL_PREFIX=$HOME/.local
make
make install

# Install bpp-phyl
cd $PROJECTDIR/bpp-phyl
mkdir build && cd build
cmake -B . -S .. -DCMAKE_INSTALL_PREFIX=$HOME/.local
make
make install

# Install bppsuite
cd $PROJECTDIR/bppsuite
mkdir build && cd build
cmake -B . -S .. -DCMAKE_INSTALL_PREFIX=$HOME/.local
make
make install
```

### Step 4: Set environment variables
Add these lines to your `~/.bashrc`:
```bash
export CPATH=$CPATH:$HOME/.local/include
export LIBRARY_PATH=$LIBRARY_PATH:$HOME/.local/lib
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.local/lib
export PATH=$PATH:$HOME/.local/bin
```

Then reload your shell:
```bash
source ~/.bashrc
```

## Verify Installation

### Test Python package
```bash
python -c "import deelogeny_m2; print('Deelogeny M2 installed successfully!')"
```

### Test command-line interface
```bash
deelogeny --help
```

### Test Bio++ installation
```bash
which bppseqgen
bppseqgen --help
```

## Data Setup

### Extract required data files
```bash
# Extract data archives
tar -xzf data.tar.gz
tar -xzf Original_Data.tar.gz
tar -xzf results.tar.gz
```

### Verify data structure
```bash
ls -la data/
ls -la Original_Data/
ls -la results/
```

## Quick Start

### Using the command-line interface
```bash
# Preprocess alignments
deelogeny preprocess --input data/alignments --output results/preprocessed --minseq 5 --maxsites 10000 --minsites 10 --type aa

# Compute phylogenetic trees
deelogeny compute-trees --input results/preprocessed/gap_and_ambigless --output results/trees --alphabet aa

# Analyze alignment descriptors
deelogeny describe --input data/alignments --output results/descriptors
```

### Using Python API
```python
from deelogeny_m2 import Preprocess, Computing_trees, Descriptor

# Preprocess alignments
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
```

## Troubleshooting

### Common Issues

1. **Bio++ not found:**
   - Ensure environment variables are set correctly
   - Check that Bio++ is installed in the expected location
   - Verify PATH includes Bio++ binaries

2. **Python import errors:**
   - Ensure virtual environment is activated
   - Check that package is installed: `pip list | grep deelogeny`
   - Try reinstalling: `pip install -e . --force-reinstall`

3. **Permission errors:**
   - Use `sudo` for system-wide installation
   - Or install in user space with `--user` flag

4. **Missing dependencies:**
   - Install missing packages: `pip install package_name`
   - Check requirements.txt for complete list

### Getting Help

- Check the [README.md](README.md) for detailed usage instructions
- Review example scripts in the `examples/` directory
- Open an issue on GitHub for bugs or feature requests

## Development Installation

For developers who want to contribute:

```bash
# Clone repository
git clone https://github.com/LIPENGJUN2022/deelogeny-m2.git
cd deelogeny-m2

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install with development dependencies
pip install -e .[dev]

# Install pre-commit hooks (optional)
pre-commit install
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 