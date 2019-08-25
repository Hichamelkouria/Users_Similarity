import numpy as np
import scipy.stats
import scipy.spatial
import random
from math import sqrt
import math
import warnings
import sys
#from sklearn.utils.extmath import np.dot

warnings.simplefilter("error")



def readingFile(filename):
	line_count = 0
	print(line_count)
	f = open(filename,"r")
	data = []
	for row in f:
		r = row.split(',')
		e = [int(r[0]), int(r[1]), int(r[2])] 
		line_count += 1
		data.append(e)
	print(line_count)
	return data,line_count




def similarity_user(data,user,users):
	print ("Hello User") 
	#f_i_d = open("sim_user_based.txt","w")
	user_similarity_cosine = np.zeros(users)
	user_similarity_jaccard = np.zeros(users)
	user_similarity_pearson = np.zeros(users)
	for user2 in range(users):
		if np.count_nonzero(user) and np.count_nonzero(data[user2]):
			user_similarity_cosine[user2] = format( 1-scipy.spatial.distance.cosine(user,data[user2]), '.12g')
			user_similarity_jaccard[user2] = format(1-scipy.spatial.distance.jaccard(user,data[user2]), '.12g')  
			try:
				if not math.isnan(scipy.stats.pearsonr(user,data[user2])[0]):
					user_similarity_pearson[user2] = format(scipy.stats.pearsonr(user,data[user2])[0], '.12g')  
				else:
					user_similarity_pearson[user2] = 0
			except:
				user_similarity_pearson[user2] = 0

			#f_i_d.write(str(user1) + "," + str(user2) + "," + str(user_similarity_cosine[user1][user2]) + "," + str(user_similarity_jaccard[user1][user2]) + "," + str(user_similarity_pearson[user1][user2]) + "\n")
	#f_i_d.close()
	np.savetxt("cosine.csv", user_similarity_cosine, delimiter=",", fmt="%s")
	np.savetxt("jaccard.csv", user_similarity_jaccard, delimiter=",", fmt="%s")
	np.savetxt("pearson.csv", user_similarity_pearson, delimiter=",", fmt="%s")
	return user_similarity_cosine, user_similarity_jaccard, user_similarity_pearson




def run(user,pourcentage):
	#read the data set
	users_data,users = readingFile("dataset.csv")
	userslist=[]
	#get similarity destance between the input user and the users in the dataset
	user_similarity_cosine, user_similarity_jaccard, user_similarity_pearson = similarity_user(users_data,user,users)
	user_row = 0
	for level in user_similarity_cosine:
		print (level)
		if level >= pourcentage/100 :
			userslist.append(user_row)
		user_row += 1		
	return userslist





#execution
result = run([2685,1422,2],90)
np.savetxt("result.csv", result, delimiter=",", fmt="%s")


