# SC00041 iris overview

### Objective
This script analyzes the Iris dataset, a classic dataset widely used for data analysis and machine learning tasks. The dataset contains measurements from 150 iris flowers belonging to three species:

* Iris setosa
* Iris versicolor
* Iris virginica


## What the script does

The script:
- Loads the built-in Iris dataset
- Creates a `PairGrid` grouped by species
- Draws scatterplots on the off-diagonal panels

## Iris dataset 
First 5 rows

| sepal length (cm) | sepal width (cm) | petal length (cm) | petal width (cm) | target | species |
|-------------------|------------------|-------------------|------------------|--------|---------|
| 5.1 | 3.5 | 1.4 | 0.2 | 0 | setosa |
| 4.9 | 3.0 | 1.4 | 0.2 | 0 | setosa |
| 4.7 | 3.2 | 1.3 | 0.2 | 0 | setosa |
| 4.6 | 3.1 | 1.5 | 0.2 | 0 | setosa |
| 5.0 | 3.6 | 1.4 | 0.2 | 0 | setosa |

### Description of Variables

- **sepal length (cm):** Length of the sepal in centimeters.
- **sepal width (cm):** Width of the sepal in centimeters.
- **petal length (cm):** Length of the petal in centimeters.
- **petal width (cm):** Width of the petal in centimeters.
- **target:** Numeric class label.
  - 0 = setosa
  - 1 = versicolor
  - 2 = virginica
- **species:** Species name corresponding to the target label.




## Requirements

Install the required packages with:

```bash
pip install seaborn matplotlib pandas
```

## How to run

Save the script as `iris_overview.py` and run:

```bash
python iris_overview.py
```

If your system uses Python 3 explicitly:

```bash
python3 iris_overview.py
```

## Output

The script generates a PNG image in the `output` folder:

```text
output/iris_plot.png
```

## Notes

- Using a timestamp in the filename helps avoid overwriting previous plots.
- `PairGrid` gives more control than `sns.pairplot()` when customizing the figure.
- The Iris dataset is bundled with Seaborn, so no separate dataset download is needed.
