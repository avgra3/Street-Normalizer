# Normalizing Streets

## Motivation

When working with addresses, there are many different ways to represent a street.
Using the [USPS](https://pe.usps.com/text/pub28/28c1_001.htm) for a method of normalizing, we can use this Python module to normalize an address, which can be useful when trying to compare addresses.

## How it works:

```python
from package import cleaner

example_street = "123 12th Avenue Apt 1234"

cleaned_street = cleaner(example_street)

print(cleaned_street)
# 123 12TH AVE APT 1234
```
