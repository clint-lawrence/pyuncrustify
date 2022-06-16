from skbuild import setup

setup(
    name='pyuncrustify',

    version="0.75.1",

    author='Clint Lawrence',
    author_email='clint.lawrence+pyuncrustify@gmail.com',

    package_dir={'': 'src'},
    packages=['pyuncrustify'],

    cmake_install_dir='src/pyuncrustify',

    entry_points={
        'console_scripts': [
            'uncrustify=pyuncrustify:main'
        ]
    },

    # url='https://cmake.org/',
    # download_url='https://cmake.org/download',
    # project_urls={
    #     "Documentation": "https://cmake-python-distributions.readthedocs.io/",
    #     "Source Code": "https://github.com/scikit-build/cmake-python-distributions",
    #     "Mailing list": "https://groups.google.com/forum/#!forum/scikit-build",
    #     "Bug Tracker": "https://github.com/scikit-build/cmake-python-distributions/issues",
    # },


    # description='CMake is an open-source, cross-platform family of '
    #             'tools designed to build, test and package software',

    # long_description=readme + '\n\n' + history,
    # long_description_content_type='text/x-rst',

    # classifiers=[
    #     'License :: OSI Approved :: Apache Software License',
    #     'License :: OSI Approved :: BSD License',
    #     'Programming Language :: C',
    #     'Programming Language :: C++',
    #     'Programming Language :: Fortran',
    #     'Programming Language :: Python',
    #     'Operating System :: OS Independent',
    #     'Development Status :: 5 - Production/Stable',
    #     'Intended Audience :: Developers',
    #     'Topic :: Software Development :: Build Tools'
    #     ],

    # license='Apache 2.0',

    # keywords='CMake build c++ fortran cross-platform cross-compilation',

    # extras_require={"test": test_requirements},
    cmake_source_dir = "uncrustify",
    cmake_args=['-DCMAKE_BUILD_TYPE=Release'],
)
