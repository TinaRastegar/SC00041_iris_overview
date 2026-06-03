# SC00041 iris overview

## Objective

This repository contains a Python script for exploring the Iris dataset. The Iris dataset is a classic dataset widely used for data analysis, visualization, and machine learning examples.

The dataset contains measurements from iris flowers belonging to three species:

- Iris setosa
- Iris versicolor
- Iris virginica

## What the script does

The script:

- Loads the built-in Iris dataset from Seaborn
- Creates a `PairGrid` grouped by species
- Draws histograms on the diagonal panels
- Draws scatterplots on the off-diagonal panels
- Adds a legend showing the species
- Saves the resulting plot as a PNG file in the `output` folder

## Iris dataset

The dataset includes the following variables:

| Variable | Description |
|---|---|
| `sepal_length` | Length of the sepal |
| `sepal_width` | Width of the sepal |
| `petal_length` | Length of the petal |
| `petal_width` | Width of the petal |
| `species` | Iris species name |

The species are:

- `setosa`
- `versicolor`
- `virginica`

Example of the first five rows:

| sepal_length | sepal_width | petal_length | petal_width | species |
|---:|---:|---:|---:|---|
| 5.1 | 3.5 | 1.4 | 0.2 | setosa |
| 4.9 | 3.0 | 1.4 | 0.2 | setosa |
| 4.7 | 3.2 | 1.3 | 0.2 | setosa |
| 4.6 | 3.1 | 1.5 | 0.2 | setosa |
| 5.0 | 3.6 | 1.4 | 0.2 | setosa |

## Requirements

The script requires Python and the following packages:

- `seaborn`
- `matplotlib`

Install the required packages with:

```bash
pip install seaborn matplotlib
```

## How to run

Clone the repository:

```bash
git clone https://github.com/TinaRastegar/SC00041_iris_overview.git
cd SC00041_iris_overview
```

Run the script:

```bash
python iris_overview.py
```

If your system uses Python 3 .

```text
output/iris_plot_20260603_110230.png
```

The plot visualizes relationships between Iris flower measurements. Points are colored by species.

## Notes

- `PairGrid` gives more control than `sns.pairplot()` when customizing figures.
- The Iris dataset is loaded directly from Seaborn, so no separate dataset download is needed.
- Saving the plot in an `output` folder keeps generated files separate from the source code.
- Using a timestamp in the filename helps avoid overwriting previous plots.

## License

This project is licensed under the GPL-3.0 license. See the `LICENSE` file for details.


