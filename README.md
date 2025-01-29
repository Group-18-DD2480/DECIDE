# DECIDE

DECIDE is a Launch Interceptor Program that determines whether to launch an interceptor based on radar tracking information. 

> This repository if is part of assignment 1 in the [Software Engineering Fundamentals](https://www.kth.se/student/kurser/kurs/DD2480?l=en) course at the KTH Royal Institute of Technology.

## API Overview
### `DECIDE()`
The main function responsible for evaluating radar tracking data and deciding whether to launch the interceptor. Decision (`YES` or `NO`) is determined based on predefined 15 Launch Interceptor Conditions (LICs) using logical matrices and vectors.

### Conditions Met Vector `(CMV)`
A boolean array containing the outcome of each of the Launch Interceptor Conditions (LICs).

### Logical Connector Matrix (`LCM`)
Symmetric matrix of size 15x15 defining relationships between different LICs using `ANDD`, `ORR` and `NOTUSED` values.

### Preliminary Unlocking Matrix `(PUM)`
A 15x15 boolean matrix derived from `CMV` and `LCM`, representing the preliminary evaluation of launch conditions. 

### Preliminary Unlocking Vector `(PUV)`
Boolean array of size 15 indicating, which of the LICs should be considered in the launch decision.

### Final Unlocking Vector `(FUV)`
Boolean array computed based on `PUM` and `PUV`. Given that all entries are `true`, the interceptor is set to be launched.

## Requirements

- Python 3.13
- No additional dependencies required

## Setup

1. Clone the repository
2. Ensure Python 3.13 is installed
3. Run tests with:
```sh
python -m unittest discover -s . -p '*_test.py'
```

## Usage
```python
python decide.py
```
Ensure that the input data, i.e radar tracking points and necessary parameters, is correctly set within `decide.py` file before execution.

## Essence Checklist
...

## License
...

## Contributors
- [@AlessandroColi](https://github.com/AlessandroColi) - Alessandro Coli
- [@eliasfloreteng](https://github.com/eliasfloreteng) - Elias Floreteng
- [@laykos0](https://github.com/laykos0) - Jakub Rybak
- [@RuriThomas](https://github.com/RuriThomas) - Ruri Osmon
- [@YusufDemir1210](https://github.com/YusufDemir1210) - Yusuf Demir


## 