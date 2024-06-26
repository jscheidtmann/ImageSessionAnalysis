"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['ImagingSessionAnalysis.py']
DATA_FILES = []
OPTIONS = { 'argv_emulation': True,
            'iconfile': 'Icons/Icon.icns',
            'packages': ['PIL', 'PyQt6', 'PyQt6-Charts', 'PyQt6-Charts-Qt6',
                        'PyQt6-Qt6', 'PyQt6-sip', 'QDarkStyle', 'astropy', 'certifi', 'numpy', 'pandas', 'photutils',
                        'scikit-image', 'scipy']
           }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
