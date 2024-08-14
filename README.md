# Normalizing Streets

## Motivation

When working with addresses, there are many different ways to represent a street.
Using the [USPS](https://pe.usps.com/text/pub28/28c1_001.htm) for a method of normalizing, we can use this Python module to normalize an address, which can be useful when trying to compare addresses.

## How it works:

```python
from street_normalizer import *
example_street = "123 54th Ave apt 1115"
cleaned_street = cleaner(example_street)
print(cleaned_street)
# 123 54TH AVE APT 1115
```

## Building Locally

As there are no dependencies required to run this tool you can install using pip with the below:

```bash
pip install --upgrade git+https://github.com/avgra3/Street_Normalizer.git
```

