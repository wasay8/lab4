import duckdb
import pandas as pd

def to_db(table_name, dataframe):
	print("starting data storing -----")
	con = duckdb.connect('r_tech.db')

	con.sql(f"Drop table if exists {table_name}")
	con.sql(f"CREATE TABLE {table_name} AS SELECT * FROM dataframe")

	# insert into the table "my_table" from the DataFrame "my_df"
	# con.sql("INSERT INTO r_tech SELECT * FROM preproc_data")

	con.sql(f"SELECT * FROM {table_name}").show()

	con.close()