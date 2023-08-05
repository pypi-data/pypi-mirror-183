from setuptools import setup,find_packages

setup(
    name='pysepm-evo',
    version='0.1.0',
    description='Computes Objective Quality measures',
    author='Aadhitya A',
    author_email='aadhitya864@gmail.com',
    url='https://github.com/alphaX86/pysepm-evo',
    license='GPL',
    install_requires=[
	    'numpy',
		'scipy',
        'numba',
		'pystoi',
	],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages()
)
