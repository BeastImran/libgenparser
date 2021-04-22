from setuptools import setup

with open('README.md', "r") as desc:
    long_description = desc.read()

setup(
    name='libgenparser',
    description="Easy and advanced Libgen site parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='0.1.0',
    packages=['libgenparser', 'libgenparser.__future__'],
    url='',
    license='',
    author='Beast',
    author_email='imsalmanran789@gmail.com',
    install_requires=["lxml", "beautifulsoup4", "requests"],
)
