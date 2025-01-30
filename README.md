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
python -m unittest discover -s tests -p '*_test.py'
```

## Usage

To execute DECIDE please run:

```python
python decide.py
```

Ensure that the input data, i.e radar tracking points and necessary parameters, is correctly set within `decide.py` file before execution.

## Way of working & Essence checklist

Our team's way of working has just reached the "In Use" state according to the Essence framework. We have established clear principles for collaboration including standardized commit message and PR formats, code review processes, and GitHub Actions for running the tests on each commit. Our practices and tools are actively being used for real work, with regular inspections through pull requests and code reviews. The team has adapted practices to fit our context, such as using GitHub issues, PRs and maintaining clear documentation. Communication and collaboration are done through WhatsApp, Discord and issue comments.

## Contribution Style

Contributions to the repository should follow the structure outlined below.

### **Prefixes**

Use one of the following prefixes to categorize the changes:

- `feat` – Adding a new feature
- `fix` – Fixing a bug
- `doc` – Writing documentation
- `refactor` – Improving existing code

### **Commit Messages**  

Commit messages should follow the format:  

```  
[prefix] Commit message (#PR)  
```  

Relevant issue numbers should be included in the squashed commit description.  

### **Pull Requests**

Pull request titles should follow the prefix structure:

```
[prefix] PR title
```

All relevant issues should be linked in the description of the PR.

### **Merge Strategy**

Use **Squash and Merge** policy and ensure the final commit message follows the correct format before merging.

### Code Review

Reviever of the Pull Request is responsible for the merger.

## License

This project is licensed under MIT License. See `LICENSE` for details.

## Statement of Contributions

#### [@AlessandroColi](https://github.com/AlessandroColi) - Alessandro Coli

- [feat] Automated testing with GitHub actions.
- [feat] Add `LIC13` and `LIC14`.
- [feat] Add unit tests for `LIC13` and `LIC14`.
- [doc] Create GitHub issues for the project.

#### [@eliasfloreteng](https://github.com/eliasfloreteng) - Elias Floreteng

- [feat] Add `LIC7`, `LIC8` and `LIC9`.
- [feat] Add unit tests for `LIC7`, `LIC8` and `LIC9`.
- [feat] VSCode settings for Python testing options.
- [doc] Create basic `README.md`.
- [refactor] Format files with `ruff`.

#### [@laykos0](https://github.com/laykos0) - Jakub Rybak

- [feat] Add `.gitignore` file.
- [feat] Add `LIC10`, `LIC11` and `LIC12`.
- [feat] Add unit tests for `LIC10`, `LIC11` and `LIC12`.
- [doc] Create `UnitTest` blueprint for the project.
- [doc] Document project and contributions in `README.md`

#### [@RuriThomas](https://github.com/RuriThomas) - Ruri Osmon

- [feat] Add `LIC4`, `LIC5` and `LIC6`.
- [feat] Add unit tests for `LIC4`, `LIC5` and `LIC6`.
- [doc] Create GitHub issues for the project.

#### [@YusufDemir1210](https://github.com/YusufDemir1210) - Yusuf Demir

- [feat] Translate `decide.py` to Python.
- [feat] Add `LIC0`, `LIC1`, `LIC2` and `LIC3`.
- [feat] Add unit tests for `LIC0`, `LIC1`, `LIC2` and `LIC3`.
