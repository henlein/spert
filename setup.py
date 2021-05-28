# Copy-Pasted from AllenNLP (https://github.com/allenai/allennlp/blob/main/setup.py)

from setuptools import find_packages, setup


setup(
    name="spert",
    version="1.0",
    description="Span-based Entity and Relation Transformer",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="spert NLP deep learning machine reading",
    url="https://github.com/henlein/spert",
    packages=find_packages(
        exclude=[
            "*.tests",
            "*.tests.*",
            "tests.*",
            "tests",
            "test_fixtures",
            "test_fixtures.*",
            "benchmarks",
            "benchmarks.*",
        ]
    ),
    install_requires=[
        "Jinja2>=2.10.3",
        "numpy>=1.17.4",
        "tensorboardX>=1.6",
        "torch",
        "tqdm>=4.55.1",
        "transformers[sentencepiece]>=4.1.1",
        "scikit-learn>=0.24.0",
        "spacy>=3.0.1",
    ],
    include_package_data=True,
    python_requires=">=3.5",
    zip_safe=False,
)
