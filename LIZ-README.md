# commands to setup this lab

git clone https://github.com/lmarkscp/pandas-workshop.git
cd pandas-workshop/
sudo apt-get install python3.9-venv
python3.9 -m venv pandas_workshop
source pandas_workshop/bin/activate
pip install "jupyterlab>=3" "ipywidgets>=7.6"
pip install plotly==5.11.0
pip install -U kaleido
pip install -r requirements.txt
jupyter lab


# once lab is running
double click on notebooks
double click on 0-check_your_env.ipynb
click the >> button
verify all the packages are loaded


# the notebooks I have created from the workshop
playground - started as the workbook going through the assignments, then branched off to run stuff against our csv files
altair-examples - tried to use altair's library for visualization
Scans-stacked-hist - uses seaborn and api_scans.csv to  renames columns, modifies data, sorts, and display various histograms
AssetsRiskScore - uses seaborn and assets.csv, adds column based on values in other column (uses function in lambda), displays, and saves pie charts using matplotlib
Plotly - uses plotly to display a simple histogram
