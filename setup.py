from setuptools import setup, find_packages
import os

# Read requirements.txt
install_requires = []
if os.path.exists("requirements.txt"):
    with open("requirements.txt") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("@"):
                install_requires.append(line)

# Additional dependencies for classifiers
classifier_requires = [
    "torch>=2.0.0",
    "scikit-learn>=1.3.0",
    "tensorboard>=2.13.0",
    "wandb>=0.15.0",
]

# Development dependencies
dev_requires = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "black>=23.0.0",
    "flake8>=6.0.0",
    "mypy>=1.0.0",
]

setup(
    name="deelogeny_m2",
    version="0.1.0",
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=install_requires,
    extras_require={
        "classifiers": classifier_requires,
        "dev": dev_requires,
        "all": install_requires + classifier_requires + dev_requires,
    },
    python_requires=">=3.10",
    author="LI PENGJUN",
    author_email="PENGJUNLI2022@163.COM",
    description="Learning-based analysis of the realism of phylogenetic simulation methods",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LIPENGJUN2022/deelogeny-m2",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="phylogenetics, simulation, machine learning, bioinformatics",
    project_urls={
        "Bug Reports": "https://github.com/LIPENGJUN2022/deelogeny-m2/issues",
        "Source": "https://github.com/LIPENGJUN2022/deelogeny-m2",
        "Documentation": "https://github.com/LIPENGJUN2022/deelogeny-m2#readme",
    },
    entry_points={
        "console_scripts": [
            "deelogeny=deelogeny_m2.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "deelogeny_m2": ["*.md", "*.txt", "*.json"],
    },
    zip_safe=False,
)
