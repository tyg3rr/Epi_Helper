# Development

## Packaging

This project uses [setuptools](https://setuptools.pypa.io/en/latest/userguide) for packaging and [setuptools-scm](https://pypi.org/project/setuptools-scm/) for version management. It uses `release-branch-semver` as its version scheme and reads the most recent git tag for the base number.

To test the package locally install it as an editable package `pip install --editable .` to enable local execution e.g. `python -m epi_helper`

### Project Structure

To learn about simple project structures see [Python - Packaging Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) for a brief overview of how packaging works in python. Any new modules should be added under their own package inside the root src folder.

```ascii
/--...
  |-pyproject.toml
  |-src/-...
        |-__main__.py
        |-__init__.py
        |-package1/-
                  |-__init__.py
                  |-module1.py
                  |--...
```

## Dependencies

This project depends on tkinter which is a srclib. Thus it is expected the user will include it in their base python install. You may need to do this if you are doing local development. Future Binary Distributions of this package should include python srclibs and not run into any missing dependency issues.

## Linting

This project is using [flake8](https://flake8.pycqa.org/) for linting. [Here](https://www.flake8rules.com/) is a link to the master list of rules. Project specific config is stored in `pyproject.toml` thanks to `https://pypi.org/project/Flake8-pyproject/`
