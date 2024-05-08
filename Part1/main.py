import argparse
import threading
import time

import clustering_lab_4 as cl
import duckdb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from fetch_data_from_tech import fetching
from sklearn.cluster import KMeans
from to_db import to_db


def input_listener():
	global user_input
	while True:
		user_input = input()
		if user_input.lower() == "quit":
			print("Quit commend received, waiting for response")
			break


if __name__ =="__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument('--minutes',type=int,default=5)
	parser.add_argument('--seconds',type=int, default=0)
	parser.add_argument('--num',type=int,default=400)

	args = parser.parse_args()


	user_input = ""
	input_thread = threading.Thread(target=input_listener)
	input_thread.start()


	time_interval = args.minutes*60+args.seconds
	exec_sign = True
	start_time = -99999
	while True:
		current_time = time.time()
		if (current_time-start_time)>time_interval:
			start_time = current_time
			exec_sign = True
		else:
			time.sleep(1)
			exec_sign = False

		if exec_sign:
			print("<<<<<<<<< data collectiong process start >>>>>>>>>>>>")
			# data collecting process
			try:
				try:
					con = duckdb.connect('r_tech.db')
					init_data = con.sql("SELECT * FROM r_tech").df()
					con.close()
				except:
					init_data = pd.DataFrame()

				raw_data = fetching(args.num)
			except:
				print("data collection failed, the whole script would stop.")
				break
			print("<<<<<<<<< data collectiong process end >>>>>>>>>>>>")

			print("<<<<<<<<< data preprocessing start >>>>>>>>>>>>")

			try:
				fetched_data = cl.Preprocessing(raw_data)
				data = pd.concat([fetched_data,init_data],ignore_index=True)
				data.drop_duplicates(inplace = True)
				data.drop_duplicates(subset=['Title', 'Post URL', 'Total Comments', 'ID'], inplace = True)
				print("Input data shape:",data.shape)
			except Exception as e:
				print("data preprocessing failed, the whole script would stop.")
				print(e)
				break

			print("<<<<<<<<< data preprocessing end >>>>>>>>>>>>")


			# update data in database
			to_db("r_tech",data)

			print("<<<<<<<<< data clustering start >>>>>>>>>>>>")
			try:
				# clustering data
				kmeans = KMeans(n_clusters=10)
				model,data = cl.clustering(data,kmeans,10)
			except:
				print("data clustering failed, the whole script would stop.")
				break
			print("<<<<<<<<< data clustering end >>>>>>>>>>>>")


			# update clusters in database
			to_db("clusters",data)
			print("Waiting for next process... ")
			# end_time = time.time()
			# sleep_time = max(0,time_interval-(end_time-start_time))

		if user_input.lower() == "quit":
			input_text = input("Please enter a message or keywords to Cluster:")
			closest_cluster = cl.find_closest_cluster(input_text,kmeans,model)
			print(closest_cluster)
			# Display messages from the selected cluster
			if closest_cluster is not None:
				cluster_messages = data[data['cluster'] == closest_cluster]['Keywords']
				print(data.head(5))
				print(f"Messages in Cluster {closest_cluster}:")
				for message in cluster_messages:
					print(f"- {message}")

				# Visualize the cluster
				plt.ion()
				cluster_df = data[data['cluster'] == closest_cluster]
				plt.figure(figsize=(10, 6))
				plt.title(f'Cluster {closest_cluster} Distribution')
				plt.xlabel('Cluster')
				plt.ylabel('Count')
				sns.countplot(data=cluster_df, x='cluster')
				plt.pause(2)
				plt.ioff()
			else:
			    	print("No cluster found for the input text.")
			break
