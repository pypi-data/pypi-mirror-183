## minimal_code

[![PyPI](https://img.shields.io/pypi/v/minimal-code.svg)](https://pypi.org/project/minimal-code/) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-brightgreen.svg)](https://www.gnu.org/licenses/gpl-3.0) [![](https://img.shields.io/badge/-Documentation-yellow)](https://kenf1.github.io/Rendered/minimal_code%20Documentation/)

`minimal_code` is a Python package containing a collection of functions (grouped by modules) intended to simplify and automate specific tasks.

This package requires Python >= 3.8 because of reliance on the `pandas` package.

### Install

To install, open the terminal and type in the following.

For Windows and Linux:

```{python}
pip install minimal_code
```

For macOS:

```{python}
python3 -m pip install minimal_code
```

### Dependencies

The table below lists the dependencies for each module within this package:

|Module|Packages|
|---|---|
|converter|os, pandas, docx2pdf|
|copy|os, shutil, pandas|
|create|os, shutil|
|rename|os, re|
|tts|pyttsx3, pandas|