# AdjectiveAnimalNumber

This is a port in Python of the [adjectiveadjectiveanimal](https://github.com/nii236/adjectiveadjectiveanimal)

## Installation

```bash 
pip install adjectiveanimalnumber
```

## Usage

### CLI
    usage: adjectiveanimalnumber [-h] [-a ADJS] [-s SEP] [-n NUM] [-i INF] [-u SUP]                                                                                                                                                                                     
    
    Generate a random adjective with an animal name and a random integer.
    
    optional arguments:
      -h, --help            show this help message and exit
      -a ADJS, --adjs ADJS  Number of adjectives to generate
      -s SEP, --sep SEP     Separator between adjectives and animal name
      -n NUM, --num NUM     Add a random integer to the end of the string
      -i INF, --inf INF     Inferior limit for random integer
      -u SUP, --sup SUP     Superior limit for random integer

Examples:
    
```bash
adjectiveanimalnumber -a 2 -n 1 -i 0 -u 100
```

```bash
adjectiveanimalnumber -a 3 -s "_" -i 0 -u 1024
```

### Python

```python
from adjectiveanimalnumber import generate
generate()
```
