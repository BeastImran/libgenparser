from setuptools import setup, find_packages

with open('README.md', "r", encoding="utf8") as desc:
    long_description = desc.read()

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Operating System :: OS Independent",
]

setup(
    name='libgenparser',
    description="Easy and advanced Libgen site parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/BeastImran/libgenparser',
    author='BeastImran',
    author_email='imsalmanran789@gmail.com',
    install_requires=["lxml", "beautifulsoup4", "requests", "async-cache"],
    classifiers=classifiers,
    python_requires='>=3.6',
    platforms='any',
)
