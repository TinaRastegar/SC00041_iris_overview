# SC00041 iris overview

### Purpose
This project creates a pairwise visualization of the relationships among the numeric vaiables in the classic Iris dataset 

## What the script does

The script:
- Loads the built-in Iris dataset
- Creates a `PairGrid` grouped by species
- Draws scatterplots on the off-diagonal panels
- Adds a legend for species
- Saves the figure 

## script

# python read iris dataset and do stuff
# import seaborn package 
import seaborn as sns

# import datetime package
from datetime import datetime

# load the iris dataset
iris = sns.load_dataset("iris")

# create timestamp for plot file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# create plot
g = sns.PairGrid(iris, hue="species")
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()

# create output folder
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

# save plot without hardcoding full path
g.figure.savefig(output_dir / "iris_plot.png")


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
