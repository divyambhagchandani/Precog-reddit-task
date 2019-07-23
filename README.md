# Precog-reddit-task
Reddit Flair Detector
Website:- https://whispering-oasis-57240.herokuapp.com/

A reddit flair dectector classifies a reddit post in given number of flairs. It uses machine learning algorithms like logistic regression, Naive Bayes etc to classify. 

## Structure

Data and Model - it includes data collection and machine learning models in jupyter notebook. <br /> 
Static- Static files for heroku apps.<br /> 
Templates- Templates for flask app.<br /> 
Procfile- Heroku Profile<br /> 
Requirements.txt-  List of all the dependencies needed<br /> 
depoly.py- Flask app<br /> 

## How to run the project
1. Clone this github repository.
2. Download all the dependencies. (pip install -r requirements.txt)
3. You might want to use virtual envirnment to prevent clashes.
4. `Python deploy.py`

**Database used** - Mongodb Atlas

Algorithms and accuracy

### Feature-Title

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                |  0.494912790      |
| Linear SVM                 |  0.612645348      |
| Logistic Regression        |  0.6024709        |

### Feature- Post
| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                |  0.239098837      |
| Linear SVM                 |  0.349563953      |
| Logistic Regression        |  0.49273255       |
### Feature- URL
| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                |  0.4375           |
| Linear SVM                 |  0.53488372`      |
| Logistic Regression        |  0.54796511       |
### Feature- Post+Title
| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                |  0.4992732        |
| Linear SVM                 |  0.6061046        |
| Logistic Regression        |  0.585029         | 
