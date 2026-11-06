# Tennis Career Analysis

## Project Overview

This Python package retrieves tennis players' career match data from Tennis Abstract and creates a scatter plot comparing player age with the age difference between the player and their opponents.

The project builds on the Serena Williams analysis from HW2 and extends it to other ATP and WTA players.

## Installation

Install the package directly from GitHub:

```bash
pip install git+https://github.com/UCB-stat159-f26/hw03-3-hxxstxr.git
```

Note: Access to the private course repository may require GitHub authentication.

## Usage

```python
import matplotlib.pyplot as plt
from tennis_analysis import get_player_matches, plot_age_difference

serena = get_player_matches("Serena Williams")
print(serena.head())

fig = plot_age_difference(serena)
plt.show()

rafa = get_player_matches("Rafael Nadal")
fig = plot_age_difference(rafa)
plt.show()
```

The package accepts player names with or without spaces and is not case-sensitive.

If a player cannot be found, the function returns a descriptive error.

## Package Structure

- `tennis_analysis/data.py` — Data retrieval and cleaning
- `tennis_analysis/plot.py` — Career match visualization
- `tennis_analysis/__init__.py` — Public functions
- `tests/test_data.py` — Offline unit tests
- `pyproject.toml` — Package configuration and dependencies

## Data Sources

Career match records are retrieved from [Tennis Abstract](https://www.tennisabstract.com/).

Player names and birth dates are obtained from the [Jeff Sackmann tennis data archive](https://github.com/Aneeshers/tennis-sackmann-archive).

The package processes the different age formats used by female and male player career files.

## Testing

Tests use sample data without contacting live servers.

Run the tests with:

```bash
python -m unittest discover -s tests -v
```

The package has been tested using Serena Williams and Rafael Nadal, and seven offline unit tests have passed.

## Personal Reflections

One thing I learned from this assignment was how to turn code from a single analysis into functions that can be reused for different players. In HW2, I mainly focused on Serena Williams, but this time I had to think about differences in the data formats for male and female players.

I also learned more about organizing a Python package and writing tests without relying on a live website. Finding a reliable way to retrieve players' birth dates was more challenging than I expected, but it helped me understand why data sources and error handling matter when building reusable software.