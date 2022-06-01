<div id="top"></div>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/aravind9722">
    <img src="https://img.icons8.com/external-flat-wichaiwi/64/undefined/external-bush-fire-climate-change-flat-wichaiwi.png" alt="Logo" width="80" height="80"/> 
  </a>

<h3 align="center">Forest Fire Predictor</h3>

  <p align="center">
    Machine Learning Project
    <br />
    <a href="https://github.com/aravind9722/Forest-fire_Prediction"><strong>Explore the Repo »</strong></a>
    <br />
    <br />
    <a href="https://github.com/aravind9722/Forest-fire_Prediction/blob/main/app.py">View Flask app code</a>
    ·
    <a href="https://github.com/aravind9722/Forest-fire_Prediction/blob/main/Forest%20Fire%20Part-2%20Model.ipynb"> Model Building</a>
    ·
    <a href="https://github.com/aravind9722/Forest-fire_Prediction/blob/main/Forest%20Fire%20Part-1%20EDA.ipynb">EDA on Forest Fires dataset</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project
* Using Data Science and Machine learning, we can build a model that takes in the detected fires dataset learns and detects future fires based on certain Weather report.
* Storing the Sourced dataset to MongoDB.
* Building a **Flask App** hosted on **Heroku**.
* **Sklearn** for pre-processing and Model Building
* Pandas, Numpy, Matplotlib for csv reading, Data Processing, Data Cleaning, Visualization etc.

## Deployed app
[![Screenshot (10)](https://user-images.githubusercontent.com/97881558/171418344-52e4b748-069c-4731-a37f-7788a3db02db.png)
](https://forest-fire-predictionv1.herokuapp.com/)

[LINK TO HEROKU APP](https://forest-fire-predictionv1.herokuapp.com/)

<!-- GETTING STARTED -->
## Introduction
*  I used a dataset on **Algerian Forest Fires from UCI**. The dataset contains a culmination of forest fire observations and data in two regions of Algeria: the Bejaia region and the Sidi Bel-Abbes region. 
* The timeline of this dataset is from June 2012 to September 2012. In this project, we focused on whether certain weather features could predict forest fires in these regions using few Machine Learning algorithms. 

<!-- USAGE EXAMPLES -->
## Steps

* Installing Python, PyCharm, Monogodb, Git to Computer.
* Creating Flask app by importing `Flask` module.
* Download the source dataset from [UCI Repository](https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset++#).
* For Classification algorithm decided to predict the features `Classes` from the dataset which is Binary classification `(fire, not fire)`.
* For Regression Problem algorithm decided to predict the feature `FWI` (Fire weather Index) which is 90%+ correlated to Classes Feature.

### Loading CSV and Inserting to DB
* The Downloaded CSV file is loaded as pandas Dataframe using Pandas Library.
* Pandas Dataframe is converted to Dict .
* Mongodb Altas is used as DB here, with `pymongo library` mongodb is connected to python.
* Database and collections created via python and the list of dictionaries is uploaded using `collection.insert_many` method.

<p align="right">(<a href="#top">back to top</a>)</p> 

### EDA
* In this step, we will apply Exploratory Data Analysis (EDA) to extract insights from the data set to know which features have contributed more in predicting Forest fire by performing Data Analysis using Pandas and Data visualization using Matplotlib & Seaborn. 
* It is always a good practice to understand the data first and try to gather as many insights from it.

### Model Building 
* For Regression Problem algorithm decided to predict the feature `FWI` (Fire weather Index) which is 90%+ correlated to Classes Feature.
* Models used : **Linear regression, Lasso Regression, Ridge Regression, Random forest, Decision tree, K-Nearest Neighbour regressor, Support Vector Regressor.**
* For Classification algorithm decided to predict the features `Classes` from the dataset which is Binary classification `(fire, not fire)`.
* Models used : **Logistic Regression, Decision Tree, Random Forest, XGboost, K-Nearest Neighbour.**

### Model Selection
* HyperParameter Tuning Randomized Gridsearch CV is done for top 2 models for both Regression and Classification.
* For Classification `Stratified Kfold Cross-Validation metrics` is used based best Mean CV Accuracy Model is used for Model Deployment.
* For Regression `R2 score metrics` is used to select best model The R2 score is one of the performance evaluation measures for regression-based machine learning models.

### Flask
* Importing the Flask module and creating a Flask web server from the Flask module.
* Create an object **app** in flask class with `__name__` which represents current app.py file.
* Create `/` route to render default page html.
* `/predict_api` route for api testing using `Postman`
* Create a route `/predict` `/predictR` to get user input for Classification and Regression respectively. 
* Run the flask app with `app.run()` code.

### Heroku Deployment
* Create new repo in Github and push all the data using `Git`.
* Install Heroku CLI and login using `heroku login` and setup the app in Heroku Web.
* Connect with app `heroku git:remote -a appname`
* Push to Heroku using `git push heroku main`

<p align="right">(<a href="#top">back to top</a>)</p>

### **Technologies used**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)


### **Tools used**
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
[![Tools used | Postman](https://img.shields.io/badge/Postman-eeeeee?style=for-the-badge&logo=postman&logoColor=FF6C37&labelColor=fefefe)][postman]
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)



<!-- CONTACT -->
## Contact
[![Aravind Selvam | LinkedIn](https://img.shields.io/badge/Aravind_Selvam-eeeeee?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=0A66C2)][reach_linkedin]
[![Aravind Selvam | G Mail](https://img.shields.io/badge/aravind9722-eeeeee?style=for-the-badge&logo=gmail&logoColor=ffffff&labelColor=EA4335)][reach_gmail]
[![GodWin1100 | GitHub](https://img.shields.io/badge/aravind-eeeeee?style=for-the-badge&logo=microsoft-outlook&logoColor=ffffff&labelColor=blue)][reach_outlook]


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS  -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://linkedin.com/in/linkedin_username

<!-- Tools Used -->
[PyCharm]: https://code.visualstudio.com/
[postman]: https://www.postman.com/
[git]: https://git-scm.com/
[github]: https://github.com/
[heroku]: https://www.heroku.com/
[microsoft_azure]: https://azure.microsoft.com/en-in/features/azure-portal/
[python]: https://www.python.org/
[mongodb]: https://www.mongodb.com/
[flask]: https://flask.palletsprojects.com/en/2.1.x/
[sklearn]: https://scikit-learn.org/stable/

<!--contact-->
[reach_linkedin]: https://www.linkedin.com/in/aravind-selvam/
[reach_gmail]: mailto:aravind9722@gmail.com?subject=Github
[reach_outlook]: mailto:aravind_selvam@outlook.com
