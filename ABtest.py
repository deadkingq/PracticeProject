import pandas as pd

train=pd.read_csv('/users/seven/downloads/Translation_Test/user_table.csv')
test=pd.read_csv('/users/seven/downloads/Translation_Test/test_table.csv')


#check the info
#train.info()
#test.info()
# The users in test is more than users in train table

#train.describe()
# The age data is normal

#check the dupe
#len(train)==len(train.user_id.unique())

#merge the data
data=train.merge(test, on='user_id', how='outer')

#check it's true Spain coverts much better than other Latin country
#grouped=data[data['test']==0].groupby(['country'])['conversion'].mean()
#grouped.sort_values()

# A simple t test, no point to keep Spain part
#data_test=data[data['country']!='Spain']
#from scipy.stats import ttest_ind
#t1=data_test[data_test['test']==1]
#t2=data_test[data_test['test']==0]
#ttest_ind(t1['conversion'], t2['conversion'])

#Ttest_indResult(statistic=-7.4225120959547688, pvalue=1.15144687852198e-13)
#True difference in means is not equal to zero


#plot day by day
data_test_by_day=data['conversion'].groupby([data['date'],data['test']]).mean().unstack()
data_test_by_day['ratio']=data_test_by_day[1]/data_test_by_day[0]
data_test_by_day.plot(y='ratio',kind='line')