import numpy as np
import pandas as pd

#Series Creation
series = pd.Series([1, 3, 5, np.nan, 6, 8])
print("Series:", series)

#colan operator
print("Slicing Series using colon operator:\n", series[1])
print("Slicing Series using colon operator:\n", series[:4])
print("Slicing Series using colon operator:\n", series[-3:])

#Series from Dictionary
dict_series = pd.Series({'a': 1, 'b': 2, 'c': 3})
print("Series from Dictionary:\n", dict_series)

#DataFrame from Dictionary
dict_data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
             'Age': [24, 27, 22, 32],
             'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df_dict = pd.DataFrame(dict_data)
print("DataFrame from Dictionary:\n", df_dict)

#Date Range Generation
date_range = pd.date_range('20230101', periods=6)
print("Date Range:", date_range)

#DataFrame Creation with Random Numbers
df = pd.DataFrame(np.random.randn(6, 4), index=date_range, columns=list('ABCD'))
print("DataFrame:\n", df)

sports1 = pd.Series([1,2,3,4], index=['cricket', 'football', 'tennis', 'hockey'])
# print(sports1)
sports2 = pd.Series([1,2,5,4,8], index=['cricket', 'football', 'badminton', 'hockey', 'golf'])
# print(sports2)
sports3 = sports1 + sports2
# print(sports3)

sports3 = sports1.add(sports2, fill_value=0)
print(sports3)

#DataFrame Operations
from numpy.random import randn as rnd
dataframe = pd.DataFrame(rnd(10, 5), columns=['A', 'B', 'C', 'D', 'E'])

#Seeding the random number generator for reproducibility
np.random.seed(5)
print(np.random.randint(3, 4))

#Example DataFrame
example_df = pd.DataFrame(rnd(10, 5), index='A B C D E F G H I J'.split(), columns='Score1 Score2 Score3 Score4 Score5'.split())
np.random.seed(5) # Resetting seed to ensure same random numbers
print(np.random.randint(3, 4))
print(example_df)

print(example_df[['Score1', 'Score2']])

#new column
example_df['Score6'] = example_df['Score1'] + example_df['Score2']

#drop column
example_df2 = example_df.drop('Score6', axis=1)

#drop column inplace
example_df.drop('Score6', axis=1, inplace=True)
print(example_df2)
print(example_df)

#drop row
example_df3 = example_df.drop('A', axis=0)
print(example_df3)

#dot operator
print(example_df.Score1)

#location operator (single row and/or single column)
print(example_df.loc['A'])
print(example_df.loc['A', 'Score1'])
#location operator (multiple rows and multiple columns)
print(example_df.loc[['A', 'B', 'C'], ['Score1', 'Score2']])

#conditional selection
print(example_df > 0.5) #returns boolean dataframe
print(example_df[example_df > 0.5]) #only values greater than 0.5 will be shown, rest will be NaN
print(example_df[example_df['Score1'] > 0.5]) #only rows where Score1 > 0.5
print(example_df[example_df['Score1'] > 0.5]['Score3']) #only Score3 values where Score1 > 0.5

#reset index
example_df_reset = example_df.reset_index()

newIndex ='IN JP CN RU UK US FR CA AU DE'.split()
example_df['Countries'] = newIndex
print(example_df)

example_df.set_index('Countries')
print(example_df)

example_df.set_index('Countries', inplace=True)
print(example_df)

#drop values
example_df.dropna()
print(example_df)

example_df.dropna(axis=1) #drop columns with NaN values
print(example_df)

example_df.dropna(thresh=5) #drop rows with 5 non-NaN values
print(example_df)

example_df.fillna(value='No Score') #fill NaN values with 'No Score'
print(example_df)

#missing value treatment
example_df['Score1'].fillna(value=example_df['Score1'].mean(), inplace=True)
print(example_df)


example_df['Score1'].fillna(value=example_df['Score1'].mean())
print(example_df)

#Grouping
grouped = example_df.groupby('Score2') #group by Score2 column
print(grouped.mean()) #mean value
print(grouped.median()) #median value
print(grouped.min()) #minimum value
print(grouped.max()) #maximum value
print(grouped.count()) # count of non-NaN values
print(grouped.describe()) # descriptive statistics
print(grouped.describe(include='all')) #include='all' gives statistics for all columns including non-numeric ones
print(grouped.describe().transpose()) # transpose of describe
print(grouped.std()) # standard deviation
print(grouped.info()) # info about the grouped object

group1 = grouped
group2 = example_df.groupby('Score3')
group3 = example_df.groupby('Score4')

#Merging, Joining, and Concatenating
concat_df = pd.concat([group1, group2, group3]) # concatenate along rows
print(concat_df)
concat_group = pd.concat([group1, group2, group3], axis=1) # concatenate along columns
print(concat_group)

#Merging DataFrames
merge_group = pd.merge(group1, group2, left_index=True, right_index=True, how='outer') # outer join, default
print(merge_group)
merge_group_inner = pd.merge(group1, group2, left_index=True, right_index=True, how='inner') # inner join, only common keys
print(merge_group_inner)

#Joining DataFrames
group1.join(group2, how='outer') # outer join, default
print(group1)
group1.join(group2, how='inner') # inner join, only common keys
print(group1)

#Apply Method
def half(x):
    return x / 2
example_df_half = example_df.apply(half)
print(example_df_half)

example_df[['Score1', 'Score2']].apply(half)
print(example_df[['Score1', 'Score2']])

#Vale counts
print(example_df['Score2'].value_counts())

#Sorting
example_df_sorted = example_df.sort_values(by='Score1') # sort by Score1 column
print(example_df_sorted)

#Data Loading
# df_loaded = pd.read_csv('file_path.csv') # load from CSV file
# df_loaded = pd.read_excel('file_path.xlsx') # load from Excel file
# df_loaded = pd.read_json('file_path.json') # load from JSON file
# df_loaded = pd.read_html('file_path.html') # load from HTML file
# df_loaded = pd.read_sql('SQL_query', connection_object) # load from SQL database
# df_loaded = pd.read_csv('file_path.csv', nrows=100) # load first 100 rows from CSV file
# df_loaded = pd.read_csv('file_path.csv', skiprows=10) # skip
# df_loaded = pd.read_csv('file_path.csv', usecols=['col1', 'col2']) # load specific columns
# df_loaded = pd.read_csv('file_path.csv', dtype={'col1': str, 'col2': int}) # specify data types for columns
# df_loaded = pd.read_csv('file_path.csv', parse_dates=['date_col']) # parse date columns
# df_loaded = pd.read_csv('file_path.csv', na_values=['NA', '?']) # specify additional strings to recognize as NaN
# df_loaded = pd.read_csv('file_path.csv', chunksize=1000) # load data in chunks of 1000 rows

#Plotting Data via Pandas
#df_loaded.plot() # basic plot
#df_loaded['col1'].plot(kind='hist') # histogram
#df_loaded.plot(x='col1', y='col2', kind='scatter') #
#df_loaded.plot(kind='box') # box plot
#df_loaded.plot(kind='bar') # bar plot
#df_loaded.plot(kind='line') # line plot
#df_loaded.plot(kind='area') # area plot
#df_loaded.plot(kind='pie', y='col1') # pie chart
#df_loaded.plot(kind='hexbin', x='col1', y='col2', gridsize=25) # hexbin plot
#df_loaded.plot(kind='density') # density plot
#df_loaded.plot(kind='kde') # kernel density estimate plot
#df_loaded.plot(subplots=True) # separate subplots for each column
#df_loaded.plot(title='My Plot') # add title to plot
#df_loaded.plot(figsize=(10, 6)) # specify figure size
#df_loaded.plot(style='--') # specify line style
#df_loaded.plot(color='red') # specify line color
#df_loaded.plot(grid=True) # add grid to plot
#df_loaded.plot(logy=True) # logarithmic scale for y-axis
#df_loaded.plot(xlim=(0, 100), ylim=(0, 50)) # set limits for x and y axes
#df_loaded.plot(legend=True) # show legend
