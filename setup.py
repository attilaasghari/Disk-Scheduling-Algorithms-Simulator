"""
Setup script for Disk Scheduling Simulator.
"""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="disk-scheduling-simulator",
    version="2.0.0",
    author="Attila Asghari",
    author_email="attilaasghari@gmail.com",
    description="An educational tool for demonstrating disk scheduling algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/attilaasghari/Disk-Scheduling-Algorithms-Simulator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Education",
        "Topic :: System :: Operating System",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "disk-scheduler=disk_scheduling_simulator.gui:run_simulator",  # Removed 'src.' prefix
        ],
    },
    include_package_data=True,
    zip_safe=False,
)