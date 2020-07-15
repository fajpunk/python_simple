# Simple Python Project template

This is a [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/)
template that gives you a simple python project with all the fixins (testing,
linting, formatting, typing, etc).

# Prerequisites

* [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) is installed
  and on your `PATH`

# Usage

```

$ cookiecutter <this repo's git clone uri>
name [yournamehere]: whatevs
python_version [3.8.1]: 3.8.1
$ cd whatevs/
$ make
python -m venv env
env/bin/pip install -U -r requirements/base.txt
...
...
env/bin/black --check whatevs tests
All done! ✨ 🍰 ✨
4 files would be left unchanged.
env/bin/mypy .
Success: no issues found in 4 source files
env/bin/python -m unittest discover -s tests
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
env/bin/pylint whatevs tests

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```
