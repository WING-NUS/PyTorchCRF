from setuptools import setup, find_packages

setup(
    name="PyTorchCRF",
    version="0.1",
    packages=find_packages(),

    scripts=['say_hello.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['torch>=0.4.1'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    author="WING NUS",
    author_email="wing.nus@gmail.com",
    description="A stand-alone lightweight CRF layer based on PyTorch.",
    license="Apache",
    keywords="pytorch, crf, probabilistic modelling",
    url="https://github.com/WING-NUS/PyTorchCRF",
    project_urls={
        "Bug Tracker": "https://github.com/WING-NUS/PyTorchCRF",
        "Documentation": "https://github.com/WING-NUS/PyTorchCRF",
        "Source Code": "https://github.com/WING-NUS/PyTorchCRF",
    }
)
