# flake8-kotoha

**K**o**T**o**H**a: **K**aizen **T**ype **H**int

## Install

pipx

```sh
$ pipx install flake8
$ pipx inject flake8 flake8-kotoha
$ flake8 -h
...
Installed plugins: flake8-kotoha: 0.0.1, ...
```

venv + pip

```sh
$ python -m venv .venv --upgrade-deps
$ .venv/bin/python -m pip install flake8-kotoha
$ .venv/bin/flake8 -h
...
Installed plugins: flake8-kotoha: 0.0.1, ...
```

## Usage

```python
def plus_one(numbers: list[int]) -> list[int]:
    return [n + 1 for n in numbers]
```

```sh
$ flake8 example.py
example.py:1:14: KTH000 concrete type (`list`, `dict`, `set`, `tuple`) in function parameters, use abstract type (`Iterable`, `Sequence` or `Mapping` from `collections.abc`)
```

## Error codes

TODO
