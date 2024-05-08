import duckdb
import pandas as pd

con = duckdb.connect('lab4_pt1/r_tech.db')

preproc_data = pd.read_csv("lab4_pt1/Preprocessed.csv")
con.sql("Drop table if exists r_tech")
con.sql("CREATE TABLE r_tech AS SELECT * FROM preproc_data")

# insert into the table "my_table" from the DataFrame "my_df"
con.sql("INSERT INTO r_tech SELECT * FROM preproc_data")

con.sql("SELECT * FROM r_tech").show()
