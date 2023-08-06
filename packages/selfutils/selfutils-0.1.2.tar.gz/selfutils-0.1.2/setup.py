from setuptools import setup

setup(
    # Needed to silence warnings
    name='selfutils',
    url='https://github.com/ankurk017/pyhurr',
    author='Ankur Kumar',
    author_email='ankurk017@gmail.com',
    # Needed to actually package something
    packages=['self_utils'],
    # Needed for dependencies
    install_requires=["cartopy", "matplotlib", "numpy", "xarray"],
    # *strongly* suggested for sharing
    version='0.1.2',
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.rst').read(),
)
