from setuptools import setup

setup(
    name = "coretex",
    version = "0.0.1",
    author="Coretex LLC (Igor Peric)",
    author_email="igor@coretex.ai",
    description="A package for AI experiment tracking, infrastructure and dataset management using Coretex.ai platform.",
    install_requires = [
        "requests",
        "inflection",
        "pillow",
        "numpy",
        "scikit-image",
        "shapely",
        "opencv-python",
        "tensorflow==2.8",
        "tensorflowjs",
        "torch",
        "protobuf~=3.19.0",
        "typed-argument-parser",
        "termcolor"
    ],
    package_data = {
        "coretex": ["**/py.typed"]
    }
)
