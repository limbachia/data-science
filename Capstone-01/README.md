### House Price Prediction

This project uses Ames, Iowa housing dataset compiled by Dean De Cook. Dataset is available on [Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

Following notebooks include step-by-step data analysis; from data wrangling to building a machine learning model that predicts house prices as accurately as possible.  


[00-data-wrangling.ipynb](https://github.com/limbachia/data-science/blob/master/Capstone-01/00-data-wrangling.ipynb): outlier removal, missing value imputation, tranformations.  
[01-data-storytelling.ipynb](https://github.com/limbachia/data-science/blob/master/Capstone-01/01-data-storytelling.ipynb): exploratory data analysis, data visualization.  
[02-feature-engineering](https://github.com/limbachia/data-science/blob/master/Capstone-01/02-feature-engineering.ipynb): creation of new features, encoding of qualitative features.  
[03-model-building.ipynb](https://github.com/limbachia/data-science/blob/master/Capstone-01/03-model-building.ipynb): building several models, model-tuning, selection of the best model/parameters.  


Lasso regression performed the best. The model was finally tested on the test dataset (also provided by kaggle). 
The test __Root-Mean-Squared-Error was 0.11840__ which placed the submission in the top 5% of the [kaggle's leaderboard](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/leaderboard#score).

