#!/usr/bin/env python3
"""
Basic import tests for Deelogeny M2
"""

import unittest
import sys
from pathlib import Path

# Add src to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


class TestImports(unittest.TestCase):
    """Test that all main modules can be imported"""
    
    def test_main_package_import(self):
        """Test importing the main package"""
        try:
            import deelogeny_m2
            self.assertIsNotNone(deelogeny_m2)
        except ImportError as e:
            self.fail(f"Failed to import deelogeny_m2: {e}")
    
    def test_core_modules_import(self):
        """Test importing core modules"""
        try:
            from deelogeny_m2 import Preprocess, Computing_trees, Descriptor
            self.assertIsNotNone(Preprocess)
            self.assertIsNotNone(Computing_trees)
            self.assertIsNotNone(Descriptor)
        except ImportError as e:
            self.fail(f"Failed to import core modules: {e}")
    
    def test_simulator_modules_import(self):
        """Test importing simulator modules"""
        try:
            from deelogeny_m2 import Bppsimulator, ESMsimulator, AddGap
            self.assertIsNotNone(Bppsimulator)
            self.assertIsNotNone(ESMsimulator)
            self.assertIsNotNone(AddGap)
        except ImportError as e:
            self.fail(f"Failed to import simulator modules: {e}")
    
    def test_mapping_module_import(self):
        """Test importing mapping module"""
        try:
            from deelogeny_m2 import Mapping2Model
            self.assertIsNotNone(Mapping2Model)
        except ImportError as e:
            self.fail(f"Failed to import mapping module: {e}")
    
    def test_cli_import(self):
        """Test importing CLI module"""
        try:
            from deelogeny_m2 import cli
            self.assertIsNotNone(cli)
        except ImportError as e:
            self.fail(f"Failed to import CLI module: {e}")
    
    def test_version_info(self):
        """Test version information is available"""
        try:
            import deelogeny_m2
            self.assertIsNotNone(deelogeny_m2.__version__)
            self.assertIsNotNone(deelogeny_m2.__author__)
            self.assertIsNotNone(deelogeny_m2.__email__)
        except AttributeError as e:
            self.fail(f"Missing version information: {e}")


class TestClassInstantiation(unittest.TestCase):
    """Test that main classes can be instantiated"""
    
    def test_preprocess_instantiation(self):
        """Test Preprocess class instantiation"""
        try:
            from deelogeny_m2 import Preprocess
            # Test with minimal parameters
            preprocessor = Preprocess(
                input="test_input",
                output="test_output", 
                minseq=5,
                maxsites=1000,
                minsites=10,
                type="aa"
            )
            self.assertIsNotNone(preprocessor)
        except Exception as e:
            self.fail(f"Failed to instantiate Preprocess: {e}")
    
    def test_computing_trees_instantiation(self):
        """Test Computing_trees class instantiation"""
        try:
            from deelogeny_m2 import Computing_trees
            computer = Computing_trees(
                inputdir="test_input",
                outputdir="test_output",
                alphabet="aa"
            )
            self.assertIsNotNone(computer)
        except Exception as e:
            self.fail(f"Failed to instantiate Computing_trees: {e}")
    
    def test_descriptor_instantiation(self):
        """Test Descriptor class instantiation"""
        try:
            from deelogeny_m2 import Descriptor
            descriptor = Descriptor(
                input="test_input",
                output="test_output"
            )
            self.assertIsNotNone(descriptor)
        except Exception as e:
            self.fail(f"Failed to instantiate Descriptor: {e}")


if __name__ == '__main__':
    unittest.main() 