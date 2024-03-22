# imcvtP

## Table of Contents
  * [Installation](#installation)
  * [Quick start](#quick-start)
  * [Features](#features)
  
## Installation

Download using pip via pypi.

```bash
$ pip install 'imcvtP' --upgrade
  or
$ pip install git+https://github.com/kanon39/imcvtP.git
```
(Mac/homebrew users may need to use ``pip3``)


## Quick start
```python
 >>> from imcvtP.converter import GifConverter
 >>> c = GifConverter("your original images path", 'your gif output path', (320,240))
 >>> c.convert_gif()
```

## Features
  * Python library to convert single order multiple frame gif images
  * OpenCV does not support gif images.