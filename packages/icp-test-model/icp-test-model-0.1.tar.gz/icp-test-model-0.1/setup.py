from setuptools import setup, find_packages


setup(
    name='icp-test-model',
    version='0.1',
    license='MIT',
    author="Syeda Farwa Zaidi",
    author_email='syeda.zaidi@mhp.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://gitlab.com/mhub1/icp-product/icp-model-creation-workflow',
    keywords='icp model creation workflow',
    install_requires=[
        'scikit-learn',
    ],

)