from setuptools import setup, find_packages

setup(
    name='maphis', 
    version='0.1.0', 
    packages=find_packages(),
    install_requires=[
        "numpy~=1.19.5",
        "scikit-image~=0.19.0",
        "PySide6",
        "opencv-python~=4.2.0.34",
        "ExifRead~=2.3.2",
        "Pillow~=8.4.0",
        "imagecodecs",
        "numba~=0.55.1",
        "openpyxl~=3.0.9",
        "scikit-learn~=1.0.2",
        "scipy~=1.8.0",
        "pytesseract~=0.3.9",
        "mouse",
        "pyinstaller",
        "torch",
        "arthseg",
    ])
