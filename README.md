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


## How to run

Clone the repository:

```bash
git clone https://github.com/TinaRastegar/SC00041_iris_overview.git
cd SC00041_iris_overview
```
Create the environmenet:

```bash
conda env create -f environment.yml
```
Activate the environment

```bash
conda activate sc00041-iris-overview
```

Run the script:

```bash
python iris_overview.py
```

Expected output: 

```text
output/iris_plot_20260603_110230.png
```

The plot visualizes relationships between Iris flower measurements. Points are colored by species.


## License

This project is licensed under the GPL-3.0 license. See the `LICENSE` file for details.


