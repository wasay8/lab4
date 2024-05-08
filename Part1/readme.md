# Clustering Algorithm 
Using both Word2Vec and TF-IDF for text analysis, it was observed that Word2Vec outperformed TF-IDF in terms of performance.

## Libraries:
Pandas version: 1.5.3, 
Regex (re) version: 2.2.1,
spaCy version: 3.6.1,
NLTK version: 3.8.1,
Gensim version: 4.3.2,
scikit-learn (sklearn) version: 1.2.2, 
Matplotlib version: 3.7.1,
Seaborn version: 0.12.2

Execute file Clustering_lab_4.py

## Clusters and keywords:
<img width="1104" alt="Screenshot 2023-09-29 at 11 49 08 AM" src="https://github.com/thoughtfuldata/DSCI560-project/assets/48021329/7add9ec2-8e36-4ae9-92bb-7e776fa73e51">

## Elbow methods:
<img width="1060" alt="Screenshot 2023-09-29 at 11 49 25 AM" src="https://github.com/thoughtfuldata/DSCI560-project/assets/48021329/f284aa61-104a-4f95-b93c-740ddd328831">

## Predicting Cluster:
<img width="945" alt="Screenshot 2023-09-29 at 11 49 46 AM" src="https://github.com/thoughtfuldata/DSCI560-project/assets/48021329/a15c2af0-c8bc-4262-a5cd-225ec505995e">

## Automation
To do the automation task, please enter following command in cmd:
> python3 main.py

Then the script will start srcaping data, preprocessing and clustering automatically 
To set the time interval between two process, you can use attributes --minutes and --seconds. And to set the num of post in each downloading, you can use --num
> python3 main.py --num 500 --minutes 1 --seconds 20

Then the wait time would be 1 min and 20 seconds, downloading 500 posts in each process
![image](https://github.com/thoughtfuldata/DSCI560-project/assets/55038803/f12d3bec-76e4-42ad-ae28-a7db5ffee977)


And you can enter "quit" to exit the script, the script would ask you the question about finding the cluster that matches closest, you can type any information like "Hello world" to get the result.
The result would like the screenshot in section Predicting Cluster
![image](https://github.com/thoughtfuldata/DSCI560-project/assets/55038803/48a430eb-a30b-4d52-a86f-56c631b73ef6)


