# English Detector

[![Downloads](https://static.pepy.tech/personalized-badge/english-detector?period=total&units=none&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/english-detector)

A python package to detect english text.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Installation

Install the package using pip:

```sh
pip install english-detector
```

## Usage

```python
from english-detector import detect_english

text = '''Hansel and Gretel are a brother and sister abandoned in a forest, where they fall into the hands of a witch who lives in a house made of gingerbread, cake, and candy. The cannibalistic witch intends to fatten Hansel before eventually eating him, but Gretel pushes the witch into her own oven and kills her.'''

print(detect_english(text)) # prints True
```

## Support

Please [open an issue](https://github.com/apinanyogaratnam/english-detector/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/apinanyogaratnam/english-detector/compare/).
