# Deepcomparer

![](https://img.shields.io/badge/PRs-welcome-green.svg)
[![GitHub](https://img.shields.io/github/license/jparadadev/deepcomparer.py)](https://github.com/jparadadev/deepcomparer.py/blob/main/LICENSE)
[![Pypi](https://img.shields.io/pypi/v/deepcomparer)](https://pypi.org/project/deepcomparer/)
[![Downloads](https://pepy.tech/badge/deepcomparer)](https://pepy.tech/project/deepcomparer)
[![GA](https://github.com/jparadadev/deepcomparer.py/workflows/Tests/badge.svg)](https://github.com/jparadadev/deepcomparer.py/actions/workflows/test.yml)

Deep compare python objects and structures like dictionaries, lists and iterables.

## Getting Started

### Installation

```Shell
  pip install deepcomparer
```

### Usage

```python
from deepcomparer import deep_compare

class Pokemon:
    def __init__(self, name):
        self.name = name

user: dict = {
    'name': 'ash',
    'links': {
        'pokehub': '@ash'
    },
    'pokemons': [Pokemon('pikachu')]
}

user2: dict = {
    'name': 'ash',
    'links': {
        'pokehub': '@ash'
    },
    'pokemons': [Pokemon('geodude')]
}
print(deep_compare(user, user2))
# output: False

user2['pokemons'] = [Pokemon('pikachu')]
print(deep_compare(user, user2))
# output: True

```


```python
from deepcomparer import deep_compare

ash_data: dict = {
    'name': 'ash',
    'links': {
        'pokehub': '@ash'
    }
}

brock_data: dict = {
    'name': 'brock',
    'links': {
        'pokehub': '@brock'
    }
}

# Over iterable structures
print(deep_compare([ash_data, brock_data], [ash_data, brock_data]))
# output: True

# Over iterable structures
print(deep_compare([ash_data, brock_data], [brock_data, ash_data]))
# output: False

# Over unsorted iterable structures
print(deep_compare([ash_data, brock_data], [brock_data, ash_data], ignore_order=True))
# output: True
```
