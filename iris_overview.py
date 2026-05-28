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

# save plot
g.figure.savefig("/home/xaemmo/teaching/reproducible_code/assignment_repos/output.png")
