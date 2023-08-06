import os.path

import setuptools


def get_readme() -> str:
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
        return f.read()


setuptools.setup(
    name='pytest-yc-bugtracker',
    version='0.0.1',
    author='Matveev K.A.',
    author_email='matveevkirill@internet.ru',
    url="https://github.com/PlagerX-Group/pytest-yc-tracker",
    description='Yandex Bug Tracker plugin for pytest',
    packages=setuptools.find_packages(),
    license="Apache 2.0",
    keywords="pytest-yc-bugtracker",
    long_description=get_readme(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Quality Assurance',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.9',
    setup_requires=["pytest"],
    install_requires=["pytest>=7.1.2"],
    entry_points={"pytest11": ["bugtracker = bugtracker.plugin"]},
    package_dir={"pytest_yc_bugtracker": "bugtracker"},
)
