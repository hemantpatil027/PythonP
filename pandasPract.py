import numpy as np
import pandas as pd


# dtfr = pd.DataFrame(dict1)
# print(dtfr.name.values)
# dtfr.to_csv("file1.csv")
# print(dtfr)

csv_file = pd.read_csv("nba.csv")
# random_values = np.random.randint(1, 10, len(csv_file))
# csv_file['State'] = random_values
print(csv_file.describe())
states = ['m.p', 'maharashtra', 'assam', 'rajasthan']
random_values = np.random.choice(states, len(csv_file))
csv_file['State'] = random_values
print(csv_file)

# pdser = pd.Series(np.random.randint(1,10,5))
# print(pdser)
# pdser.to_csv("randomNo.csv",index=False,header=False)

# print(type(pdser))
# print(pdser.index)

# pddtfr = pd.DataFrame(np.random.rand(10,2))
# print(pddtfr)
# print(pddtfr.T)
# print(pddtfr.to_numpy())
# print(pddtfr.sort_index(axis=0, ascending=False))

# print("size\n",pddtfr.size)
# print("max\n",pddtfr.max())
# print("mean\n",pddtfr.mean())
# print("corr\n",pddtfr.corr())

# print("median\n",pddtfr.median())
# print("std\n",pddtfr.std())

csv_file = pd.read_csv("nba.csv")
# print(csv_file)
# print(csv_file.loc[csv_file["College"] == 'Texas'] )
# print(csv_file[(csv_file["Age"] == 24) &
#                (csv_file["College"] == 'Texas')])
# data_24_texas = csv_file[(csv_file.Team == 'Boston Celtics')]
# csv_file['extra'] = np.nan
# csv_file['extra'] = csv_file[csv_file.Position == 'PG'].Name
# print(csv_file.extra)
# print(csv_file[(csv_file.Age < 22) & (csv_file.Position < 'SG')].College.count())

# # print(data_24_texas[['Name', 'Salary']])
# # name_sal = data_24_texas[['Name', 'Salary']]
# data_24_texas.plot(x='Name', y='Salary', kind='bar', rot=45, fontsize=7,grid=True)

# plt.show()
# print(data_24_texas["Name"])
# data_24_texas_names = data_24_texas["Name"]
# print(data_24_texas_names)
# print(data_24_texas.loc[:,"Name"])
# print(type(data_24_texas))
# print(data_24_texas.loc["Name"])
# # print(type(csv_file))
# print(csv_file.head(2))
# print(csv_file.loc[3:6,"Age"])

# name_col = pd.read_csv("nba.csv",index_col="Age")
# print(csv_file.get(["Age","Name"]).head())
# print(csv_file.where(csv_file["Age"] == 25))
# print(csv_file.where(csv_file["College"] == 'Texas'))

# no_index_csv = pd.read_csv("nba.csv")
# print(no_index_csv)



