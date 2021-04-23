from setuptools import setup

with open('README.md', "r") as desc:
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
    version='0.1.0',
    packages=['libgenparser', 'libgenparser.__future__'],
    url='https://github.com/BeastImran/libgenparser',
    author='BeastImran',
    author_email='imsalmanran789@gmail.com',
    install_requires=["lxml", "beautifulsoup4", "requests", "async-cache"],
    classifiers=classifiers,
    python_requires='>=3.6',
    platforms='any',
)
