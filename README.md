# flake8-kotoha

[**K**o**T**o**H**a](https://millionlive-theaterdays.idolmaster-official.jp/idol/kotoha/): **K**aizen **T**ype **H**int

## Install

pipx

```sh
$ pipx install flake8
$ pipx inject flake8 flake8-kotoha
$ flake8 -h
...
Installed plugins: flake8-kotoha: 0.1.0, ...
```

venv + pip

```sh
$ python -m venv .venv --upgrade-deps
$ .venv/bin/python -m pip install flake8-kotoha
$ .venv/bin/flake8 -h
...
Installed plugins: flake8-kotoha: 0.1.0, ...
```

uv

```sh
$ uv tool install flake8 --with flake8-kotoha
$ flake8 -h
...
Installed plugins: flake8-kotoha: 0.1.0, ...
```

## Usage

```python
def plus_one(numbers: list[int]) -> list[int]:
    return [n + 1 for n in numbers]
```

```sh
$ flake8 example.py
example.py:1:14: KTH101 Type hint with abstract type `collections.abc.Iterable` or `collections.abc.Sequence`, instead of concrete type `list`
```

## Error codes

Type hints in function **parameters**

Use abstract types instead of concrete ones

| error code | description |
|:----:|:------------|
| KTH101 | Use `Iterable` or `Sequence` instead of `list` |
| KTH102 | Use `Iterable` or `Sequence` instead of `tuple` |
| KTH103 | Use `Iterable` instead of `set` |
| KTH104 | Use `Iterable` instead of `dict` |

## Rationale

https://docs.python.org/ja/3/library/typing.html#typing.List

>Note that to annotate arguments, it is preferred to use an abstract collection type such as `Sequence` or `Iterable` rather than to use `list` or `typing.List`.

https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html#standard-duck-types

>Use Iterable for generic iterables (anything usable in "`for`"), and Sequence where a sequence (supporting "`len`" and "`__getitem__`") is required

https://typing.readthedocs.io/en/latest/reference/best_practices.html#arguments-and-return-types

>For arguments, prefer protocols and abstract types (`Mapping`, `Sequence`, `Iterable`, etc.).
