from setuptools import setup, find_packages

setup(
    name = "EmotionDetection",
    version = "1.0.0",
    description = "A package for emotion detection using Watson NLP",
    packages = find_packages(),
    install_requires = [ "requests" ],
    python_requires = ">=3.10"
)