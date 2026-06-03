# Import packages
from pathlib import Path
from datetime import datetime

import seaborn as sns

# Load the iris dataset from seaborn
iris = sns.load_dataset("iris")

# Create timestamp for plot file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Create plot
g = sns.PairGrid(iris, hue="species")
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()

# Create output folder
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

# Save plot with timestamp
g.figure.savefig(output_dir / f"iris_plot_{timestamp}.png")

