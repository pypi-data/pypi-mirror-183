from setuptools import setup

name = "types-ExifRead"
description = "Typing stubs for ExifRead"
long_description = '''
## Typing stubs for ExifRead

This is a PEP 561 type stub package for the `ExifRead` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `ExifRead`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/ExifRead. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `0cf685cc17b9d71e1be6d60241f80c210c6dade2`.
'''.lstrip()

setup(name=name,
      version="3.0.0.1",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/ExifRead.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['exifread-stubs'],
      package_data={'exifread-stubs': ['__init__.pyi', '_types.pyi', 'classes.pyi', 'exceptions.pyi', 'exif_log.pyi', 'heic.pyi', 'jpeg.pyi', 'tags/__init__.pyi', 'tags/exif.pyi', 'tags/makernote/__init__.pyi', 'tags/makernote/apple.pyi', 'tags/makernote/canon.pyi', 'tags/makernote/casio.pyi', 'tags/makernote/fujifilm.pyi', 'tags/makernote/nikon.pyi', 'tags/makernote/olympus.pyi', 'utils.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
