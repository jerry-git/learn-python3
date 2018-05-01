from distutils.core import setup


with open('README.rst') as f:
    long_description = f.read()


setup(
    name='ipython_pytest',
    version='0.0.1.dev',
    author='Antti Kaihola <antti dot kaihola at eniram dot fi>',
    py_modules=['ipython_pytest'],
    url='https://github.com/akaihola/ipython_pytest',
    license='README.rst',
    description='IPython extension to run pytest for the current cell.',
    long_description=long_description,
)
