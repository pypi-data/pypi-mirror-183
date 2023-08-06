from setuptools import setup
import setuptools

setup(
    name='heartt',
    version='1.0.0',
    packages=setuptools.find_packages(),
    url='https://github.com/Liu-from-the-production-team/Heart-Toolkit',
    license='GUN 3.0',
    author='LiuZhenming',
    author_email='2124619132@qq.com',
    description='This is a Python algorithm for generating text summaries.',
    long_description_content_type="text/markdown",
    install_requires=['nltk', 'jieba'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10.9',
)
