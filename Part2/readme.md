# Lab4-part1

Python: 3.11.4
Pandas: 2.0.3
Numpy: 1.24.3
PRAW: 7.7.1

### fetch_data_from_tech.py

To run the script:
> python3 fetch_data_from_tech.py

Then the script will downloading some data from subreddit/tech, the default number of post is 5000
If you want to change the number of post, you can run command like:
> python3 fetch_data_from_tech.py --num 3000

You will get some information on the screen like:
![image](https://github.com/thoughtfuldata/DSCI560-project/assets/55038803/a1ea2d26-f34c-4dd8-a497-f425aee69f5e)

## Preprocessing Data

execute data_preprocessing_lab 4.py

Pandas: 2.0.3
Re: 2.2.1
Spacy: 3.6.1
nltk: 3.8.1

### Dataframe after preprocessing:
1. Keywords
2. Topics
3. Remove duplicate values
4. Filter out domain from URLs

<img width="1068" alt="Screenshot 2023-09-23 at 8 47 57 PM" src="https://github.com/thoughtfuldata/DSCI560-project/assets/48021329/8bbb0470-e981-4155-b780-546c6e6451a0">





## Storing the data

We are using duckdb(SQL OLAP) to store the data.

1. The script that imports the preprocessed CSV into our duckdb database is "to_db.py". Quick note for replication, must use pandas 2.0.3 as there is currently a bug when working with pandas and duckdb.

> python3 to_db.py
