from setuptools import setup, find_packages

setup(
    name='nxbinaryen',
    version='1.111.0',
    url='https://github.com/nxpub/nxbinaryen',
    author='NX Maintainer',
    author_email='support@nx.pub',
    description='Python Bindings for Binaryen',
    license='MIT License',
    license_files=('LICENSE',),
    zip_safe=False,
    include_package_data=True,
    packages=[
        'nxbinaryen', 'nxbinaryen.capi', 'nxbinaryen.enums', 'tests'
    ],
    # use_scm_version={
    #     'root': './binaryen',
    #     'tag_regex': r'^version_(?P<version>\d{3})$',
    #     'relative_to': __file__,
    #     'write_to': '../nxbinaryen/__init__.py',
    #     'write_to_template': '__version__ = \'{version}\'\n',
    #     'local_scheme': 'node-and-date',
    # },
    setup_requires=['cffi>=1.13.2'],  # 'setuptools_scm'],
    install_requires=['cffi>=1.13.2'],
    cffi_modules=['scripts/build_ffi.py:ffi'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
    ]
)
