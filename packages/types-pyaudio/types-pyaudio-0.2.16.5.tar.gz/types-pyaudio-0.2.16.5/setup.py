from setuptools import setup

name = "types-pyaudio"
description = "Typing stubs for pyaudio"
long_description = '''
## Typing stubs for pyaudio

This is a PEP 561 type stub package for the `pyaudio` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `pyaudio`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/pyaudio. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `2704a8d916d9d222a7f9f2812511323e07af5673`.
'''.lstrip()

setup(name=name,
      version="0.2.16.5",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/pyaudio.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['pyaudio-stubs'],
      package_data={'pyaudio-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
