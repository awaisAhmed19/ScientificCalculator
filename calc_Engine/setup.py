from setuptools import setup, find_packages

setup(
    name="Scientific Calculator",
    version="0.1.0",
    description="This project is a Python-based scientific calculator that includes a parsing algorithm called a tokenizer and a postfix evaluator. These algorithms are fundamental for processing mathematical expressions and are the foundation for the calculator's functionality.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Awais Ahmed",
    author_email="awaisahmedoffi@gmail.com",
    packages=find_packages(),
    install_requires=[
        "pygame>=2.5.0",
        "re",
    ],
    # Entry points for command-line scripts, if any
    entry_points={
        "console_scripts": [
            "your_script_name=your_module:main_function",
        ],
    },
    python_requires=">=3.13.0",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_data={
        "": ["*.txt", "*.md"],  # include all *.txt and *.md files
    },
    # Build options
    options={
        "build": {
            "build_base": "build/lib",  # Build directory
        },
    },
    # Additional build commands
    cmdclass={
        "build": "build",  # Override default build command if needed
    },
)
