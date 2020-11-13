# [Deploying Python Models to Production](https://www.youtube.com/watch?v=f3I0izerPvc)
Video only

# [Production Data Science using Git](https://github.com/FilippoBovo/production-data-science)


### Installation packages to create virtual env
(make sure `virtualenv` is already installed)

<pre><code>pip install virtualenvwrapper
export WORKON_HOME=~/Envs
source ~/anaconda3/bin/virtualenvwrapper.sh</code></pre>

### Source .bashrc
<pre><code>. /home/climbach/.bashrc</code></pre>

### Environment Creation
<pre><code>mkvirtualenv --python=python3 titanic_datascience</code></pre>

### Activate the environment
<pre><code>workon titanic_datascience</code></pre>

### Check which python is being used after activating the environment
<pre><code>echo "Python=`which python`</code></pre>

### Following package is needed to run setup.py. Install it
<pre><code>pip install pypandoc==1.4</code></pre>

### Put the titanic package in developmental mode 
<pre><code>pip install -e .</code></pre>
`.` to indicate the directory in which setup.py is located.

### Reproducibility 
<pre><code>pip freeze | grep -v titanic > requirements.txt</code></pre>

The `grep -v titanic` command omits the local package titanic to avoid errors
when installing packages from the requirement file

### For exploratory analysis start a new branch
<pre><code>git checkout -b explore_passenger_survival</code></pre>

### Install jupyter lab and link current environment to jupyter
<pre><code>pip install jupyter
python -m ipykernel install --user --name=titanic_datascience  # Install the Jupyter kernel
</code></pre>

### Install some useful data science pacakges
<pre><code>
pip install watermark==1.8.1 pandas==0.24.2 scikit-learn==0.20.3 scipy==1.2.1 matplotlib==3.0.3
pip freeze | grep -v titanic > requirements.txt
</code></pre>

### Perform exploratory analysis in the exploratory branch
Check the following  notebook:

`exploration/predict_survival_using_logistic_regression_with_sex_age_title/analysis.ipynb`

### Commit the exploration

After the analysis in the notebook is completed, we commit our changes to the `explore_passenger_survival` branch, merge the branch to the master branch and push to GitHub.

<pre><code>git add .
git commit -m "Predict passenger survival using ridge logistic regression"
git checkout master
git merge explore_passenger_survival
git push
</code></pre>

### Refactoring the Notebook
Start a  refactoring branch
<pre><code>git checkout -b refactor_passanger_survival</code></pre>

Go thru the exploratory notebooks, refactor function are used repeatedly into the `titanic` module.  