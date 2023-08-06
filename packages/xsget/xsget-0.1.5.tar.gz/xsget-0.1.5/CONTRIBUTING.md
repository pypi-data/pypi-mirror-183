# Contributing

Setting up development environment:

```bash
python -m pip install --upgrade pip flit tox tox-pyenv pylint pre-commit
flit install --symlink
playwright install
```

Show all available tox tasks:

```bash
$ tox -av
...
py37     -> testing against python3.7
py38     -> testing against python3.8
py39     -> testing against python3.9
py310    -> testing against python3.10
py311    -> testing against python3.11
cover    -> generate code coverage report in html
doc      -> generate sphinx documentation in html
```

To run all tox tasks, we need to install all supported Python version using
[pyenv](https://github.com/pyenv/pyenv):

```bash
pyenv install 3.7.16
pyenv install 3.8.16
pyenv install 3.9.16
pyenv install 3.10.9
pyenv install 3.11.1
```

For code linting, we're using `pre-commit`:

```bash
pre-commit install
pre-commit clean
pre-commit run --all-files
```
