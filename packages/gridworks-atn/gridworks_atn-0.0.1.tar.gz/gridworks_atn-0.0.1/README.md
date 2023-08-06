# Gridworks Atn Spaceheat

[![PyPI](https://img.shields.io/pypi/v/gridworks-atn.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/gridworks-atn.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/gridworks-atn)][python version]
[![License](https://img.shields.io/pypi/l/gridworks-atn)][license]

[![Read the documentation at https://gridworks-atn.readthedocs.io/](https://img.shields.io/readthedocs/gridworks/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/thegridelectric/gridworks-atn/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/thegridelectric/gridworks-atn/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/gridworks-atn/
[status]: https://pypi.org/project/gridworks-atn/
[python version]: https://pypi.org/project/gridworks-atn
[read the docs]: https://gridworks-atn.readthedocs.io/
[tests]: https://github.com/thegridelectric/gridworks-atn/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/thegridelectric/gridworks-atn
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

Repo for AtomicTNodes

## Local Demo Setup

1. Set up python envirnment

   ```
   poetry install

   poetry shell
   ```

2. Install [docker](https://docs.docker.com/get-docker/)

3. Start docker containers

- **X86 CPU**:

  ```
  docker compose -f world-rabbit-x86.yml up -d
  ```

- **arm CPU**:

  ```
  docker compose -f world-rabbit-arm.yml up -d
  ```

4. Check rabbit on its console at [http://0.0.0.0:15672/#/](http://0.0.0.0:15672/#/)

   - username/password are both

     ```
     smqPublic
     ```

5. Run demo:

   ```
   python demo.py
   ```

## Usage

Please see the [Command-line Reference] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Gridworks Atn Spaceheat_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/thegridelectric/gridworks-atn/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/thegridelectric/gridworks-atn/blob/main/LICENSE
[contributor guide]: https://github.com/thegridelectric/gridworks-atn/blob/main/CONTRIBUTING.md
[command-line reference]: https://gridworks-atn.readthedocs.io/en/latest/usage.html
