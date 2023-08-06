import pathlib

from setuptools import find_packages, setup

CURRENT_PATH = pathlib.Path(__file__).parent
README = (CURRENT_PATH / "README.md").read_text()

setup(
    name="gym-PBN",
    version="1.1.0",
    description="A Gymnasium environment modelling Probabilistic Boolean Networks and Probabilistic Boolean Control Networks.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/UoS-PLCCN/gym-PBN/",
    author="Evangelos Chatzaroulas",
    author_email="e.chatzaroulas@surrey.ac.uk",
    license="MIT",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    packages=find_packages(),
    package_data={"gym_PBN.envs.bittner": ["data/*.xls", "data/*.pkl"]},
    install_requires=[
        "gymnasium==0.27.0",
        "networkx",
        "numpy",
        "pandas",
        "xlrd",
        "scipy",
        "sklearn",
        "numba",
        "tqdm",
        "psutil",
    ],
    extras_require={
        "dev": ["pytest", "black", "rope", "wandb"],
        "vis": ["plotly_express==0.4.1", "kaleido"],
    },
    python_requires=">3.9",
)
