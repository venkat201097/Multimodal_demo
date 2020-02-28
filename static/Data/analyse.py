import pandas as pd

subject = 10
train = pd.read_csv('S{}/train.csv'.format(subject))

b = [train[train['Session']==i] for i in range(6)]

for x,i in enumerate(b):
	for j in range(0,len(i),10):
		print(x,j//10+1,i[j:j+10].describe()['Time'].mean(),i[j:j+10].describe()['PlayCount'].mean())

test = pd.read_csv('S{}/test.csv'.format(subject))

for i in range(6):
	d = {'i':0,'a':0}
	for j,row in test[test['Session']==i].iterrows():
		if row['Label']==row['Response']:
			d[row['Test_Phase']]+=1
	print(d)