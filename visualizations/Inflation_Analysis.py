import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Inflation Analysis for Whole Market

data = pd.read_csv("transfers2.csv")

data2 = data[["Year", "TransferFee"]]

data3 = data2[data2['TransferFee']!= -1]

# Don't include Free Transfers

data4 = data3[data2['TransferFee']!= 0]

# Making list of stds and means and years

TFdatam = []
TFdatas = []
TFyear = []

# for i in range(8):
#     print(type(float("201" + str(i))))

for i in range(8):
    TFdatam.append(np.mean(data4[data4.Year == float("201" + str(i))].TransferFee))

for i in range(8):
    TFdatas.append(np.std(data4[data4.Year == float("201" + str(i))].TransferFee))

for i in range(8):
    TFyear.append(float("201" + str(i)))

x = TFyear
y = TFdatam
yerr = TFdatas

plt.figure()
plt.errorbar(x, y, yerr=yerr, fmt='o', label='Mean with 1' + r'$\sigma$' + ' errors')
plt.title("Soccer Transfer Fee Market Inflaton")
plt.xlabel('Year')
plt.ylabel('Transfer Fee (10 Million Euros)')
plt.legend(loc='upper left')

plt.show()

# Inflation Analysis by League

datal = pd.read_csv("mergedData.csv")

leagues1 = datal[["Next Club League"]].dropna()

# Explore Unique Leagues

leagues2 = np.array(leagues1)

newleagues = []

for i in leagues2:
  if i not in newleagues:
    newleagues.append(i)

print(newleagues)

# Separate Data by League

datatot = datal[["Next Club League", "Year", "Transfer Fee"]].dropna()
datatot = datatot.reset_index(drop=True)

# Premier League

pleague1 = datatot[['Next Club League']] == 'Premier League'
pleague2 = []
for i in range(len(pleague1)):
    pleague2.append(pleague1.ix[i, 'Next Club League']
)
pleague3 = datatot[pleague2]
pleague3 = pleague3.reset_index(drop=True)

TFdatamp = []
TFdatasp = []
TFyearp = []

for i in range(8):
    print(type(float("201" + str(i))))

for i in range(8):
    TFdatamp.append(np.mean(pleague3[pleague3.Year == float("201" + str(i))][['Transfer Fee']]))

for i in range(8):
    TFdatasp.append(np.std(pleague3[pleague3.Year == float("201" + str(i))][['Transfer Fee']]))

for i in range(8):
    TFyearp.append(float("201" + str(i)))

x = TFyearp
y = TFdatamp
yerr = TFdatasp

plt.errorbar(x, y, yerr=yerr, fmt='o', label='Premier League', color='r', alpha=0.5)
# plt.title("Premier League")
plt.xlabel('Year')
plt.ylabel('Transfer Fee (10 Million Euros)')
plt.legend(loc='upper left')

# Bundeliga

pleague1 = datatot[['Next Club League']] == 'Bundesliga'
pleague2 = []
for i in range(len(pleague1)):
    pleague2.append(pleague1.ix[i, 'Next Club League']
)
pleague3 = datatot[pleague2]
pleague3 = pleague3.reset_index(drop=True)

TFdatamp = []
TFdatasp = []
TFyearp = []

for i in range(8):
    print(type(float("201" + str(i))))

for i in range(8):
    TFdatamp.append(np.mean(pleague3[pleague3.Year == float("201" + str(i))][['Transfer Fee']]))

for i in range(8):
    TFdatasp.append(np.std(pleague3[pleague3.Year == float("201" + str(i))][['Transfer Fee']]))

for i in range(8):
    TFyearp.append(float("201" + str(i)))

x = TFyearp
y = TFdatamp
yerr = TFdatasp

plt.errorbar(x, y, yerr=yerr, fmt='o', label='Bundesliga', color='gold', alpha=0.5)
# plt.title("Bundesliga")
plt.xlabel('Year')
plt.ylabel('Transfer Fee (10 Million Euros)')
plt.legend(loc='upper left')

# Ligue 1

pleague1 = datatot[['Next Club League']] == 'Ligue 1'
pleague2 = []
for i in range(len(pleague1)):
    pleague2.append(pleague1.ix[i, 'Next Club League']
)
pleague3 = datatot[pleague2]
pleague3 = pleague3.reset_index(drop=True)

TFdatamp = []
TFdatasp = []
TFyearp = []

for i in range(8):
    print(type(float("201" + str(i))))

for i in range(8):
    TFdatamp.append(np.mean(pleague3[pleague3.Year == float("201" + str(i))][['Transfer Fee']]))

for i in range(8):
    TFdatasp.append(np.std(pleague3[pleague3.Year == float("201" + str(i))][['Transfer Fee']]))

for i in range(8):
    TFyearp.append(float("201" + str(i)))

x = TFyearp
y = TFdatamp
yerr = TFdatasp

plt.errorbar(x, y, yerr=yerr, fmt='o', label='Ligue 1', color='grey', alpha=0.5)
# plt.title("Ligue 1")
plt.xlabel('Year')
plt.ylabel('Transfer Fee (10 Million Euros)')
plt.legend(loc='upper left')

# La Liga

pleague1 = datatot[['Next Club League']] == 'La Liga'
pleague2 = []
for i in range(len(pleague1)):
    pleague2.append(pleague1.ix[i, 'Next Club League']
)
pleague3 = datatot[pleague2]
pleague3 = pleague3.reset_index(drop=True)

TFdatamp = []
TFdatasp = []
TFyearp = []

for i in range(8):
    print(type(float("201" + str(i))))

for i in range(8):
    TFdatamp.append(np.mean(pleague3[pleague3.Year == float("201" + str(i))][['Transfer Fee']]))

for i in range(8):
    TFdatasp.append(np.std(pleague3[pleague3.Year == float("201" + str(i))][['Transfer Fee']]))

for i in range(8):
    TFyearp.append(float("201" + str(i)))

x = TFyearp
y = TFdatamp
yerr = TFdatasp

plt.errorbar(x, y, yerr=yerr, fmt='o', label='La Liga', color='blue', alpha=0.5)
# plt.title("La Liga")
plt.xlabel('Year')
plt.ylabel('Transfer Fee (10 Million Euros)')
plt.legend(loc='upper left')

# Serie A

pleague1 = datatot[['Next Club League']] == 'Serie A'
pleague2 = []
for i in range(len(pleague1)):
    pleague2.append(pleague1.ix[i, 'Next Club League']
)
pleague3 = datatot[pleague2]
pleague3 = pleague3.reset_index(drop=True)

TFdatamp = []
TFdatasp = []
TFyearp = []

for i in range(8):
    print(type(float("201" + str(i))))

for i in range(8):
    TFdatamp.append(np.mean(pleague3[pleague3.Year == float("201" + str(i))][['Transfer Fee']]))

for i in range(8):
    TFdatasp.append(np.std(pleague3[pleague3.Year == float("201" + str(i))][['Transfer Fee']]))

for i in range(8):
    TFyearp.append(float("201" + str(i)))

x = TFyearp
y = TFdatamp
yerr = TFdatasp

plt.errorbar(x, y, yerr=yerr, fmt='o', label='Serie A', color='green', alpha=0.5)
# plt.title("Serie A")
plt.xlabel('Year')
plt.ylabel('Transfer Fee (10 Million Euros)')
plt.legend(loc='upper left')

plt.title("Market Inflation by League, Mean with 1$\sigma$ errors")
plt.show()

# Seaborn Error Bar plot

fig, ax = plt.subplots()

pleague1 = datatot[['Next Club League']] == 'Premier League'
pleague2 = []
for i in range(len(pleague1)):
    pleague2.append(pleague1.ix[i, 'Next Club League']
)
pleague3 = datatot[pleague2]
pleague3 = pleague3.reset_index(drop=True)

sns.regplot('Year', 'Transfer Fee', data=pleague3, x_estimator=np.mean, x_jitter=0.1, color='r', scatter_kws={'alpha':0.7}, label='Premier League')

pleague1 = datatot[['Next Club League']] == 'Bundesliga'
pleague2 = []
for i in range(len(pleague1)):
    pleague2.append(pleague1.ix[i, 'Next Club League']
)
pleague3 = datatot[pleague2]
pleague3 = pleague3.reset_index(drop=True)

sns.regplot('Year', 'Transfer Fee', data=pleague3, x_estimator=np.mean, x_jitter=0.1, color='y', scatter_kws={'alpha':0.7}, label='Bundesliga')

pleague1 = datatot[['Next Club League']] == 'Ligue 1'
pleague2 = []
for i in range(len(pleague1)):
    pleague2.append(pleague1.ix[i, 'Next Club League']
)
pleague3 = datatot[pleague2]
pleague3 = pleague3.reset_index(drop=True)

sns.regplot('Year', 'Transfer Fee', data=pleague3, x_estimator=np.mean, x_jitter=0.1, color='grey', scatter_kws={'alpha':0.7}, label='Ligue 1')

pleague1 = datatot[['Next Club League']] == 'La Liga'
pleague2 = []
for i in range(len(pleague1)):
    pleague2.append(pleague1.ix[i, 'Next Club League']
)
pleague3 = datatot[pleague2]
pleague3 = pleague3.reset_index(drop=True)

sns.regplot('Year', 'Transfer Fee', data=pleague3, x_estimator=np.mean, x_jitter=0.1, color='b', scatter_kws={'alpha':0.7}, label='La Liga')

pleague1 = datatot[['Next Club League']] == 'Serie A'
pleague2 = []
for i in range(len(pleague1)):
    pleague2.append(pleague1.ix[i, 'Next Club League']
)
pleague3 = datatot[pleague2]
pleague3 = pleague3.reset_index(drop=True)

sns.regplot('Year', 'Transfer Fee', data=pleague3, x_estimator=np.mean, x_jitter=0.1, color='g', scatter_kws={'alpha':0.7}, label='Serie A')

ax.legend()
ax.set(xlabel='Year', ylabel='Transfer Fee (10 Million Euros)')
ax.set_title('Market Inflation by League, Mean with 1$\sigma$ Errors')

sns.plt.show()

# Profit by All Unique Teams in Dataset

# Select all Unique Teams

# Check that All Teams Both Send and Recieve

datatot2 = datal[["Previous Club", "Next Club", "Year", "Transfer Fee"]].dropna()
datatot2 = datatot2.reset_index(drop=True)

print(len(datatot2[["Previous Club"]].dropna().drop_duplicates())
 == len(datatot2[["Next Club"]].dropna().drop_duplicates())
)

# Make list of unique clubs

uclubs = np.array(datatot2[["Previous Club"]].dropna().drop_duplicates())

# Gross Revenues

gains = []
for i in range(len(uclubs)):
    gains.append(tuple((uclubs[i], np.sum(datatot2[['Transfer Fee']][(datatot2[['Previous Club']] == uclubs[i]).values]).values)))

# Gross Expenses

losses = []
for i in range(len(uclubs)):
    losses.append(tuple((uclubs[i], np.sum(datatot2[['Transfer Fee']][(datatot2[['Next Club']] == uclubs[i]).values]).values)))

# Net Profit

netprofit = []
for i in range(len(uclubs)):
    netprofit.append(tuple((uclubs[i], gains[i][1] - losses[i][1])))

# Converting netprofit to list

netprofit2 = []
for i in range(len(netprofit)):
    netprofit2.append(tuple((netprofit[i][0].tolist()[0], netprofit[i][1].tolist()[0])))

# Convert to Pandas data frame

profits = pd.DataFrame(list(netprofit2), columns=['Club', 'Net Profit'])

# Sorting by net profit

profits.sort_values(by='Net Profit', ascending=False)

topfive = profits.sort_values(by='Net Profit', ascending=False)[:5]

# Bar Plots

# top five

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

ax = sns.barplot(x='Club', y='Net Profit', data=topfive)
ax.set(xlabel='Club', ylabel='Net Profit (10 Million Euros)')
plt.title('  Top Five Clubs by Transfer Fee Net Profit (2010-2017)')
plt.tight_layout()
plt.xticks(rotation=45)

# bottom five

bottomfive = profits.sort_values(by='Net Profit', ascending=True)[:7]
bottomfive = bottomfive.reset_index(drop=True)
bottomfive.drop(0, inplace=True)
bottomfive.drop(1, inplace=True)
bottomfive.drop(3, inplace=True)
bottomfive.drop(4, inplace=True)
bottomfive = bottomfive.reset_index(drop=True)
d = {'Club': ['Manchester City', 'Manchester United'], 'Net Profit': [-1.05687500e+09, -9.97875000e+08]}
df = pd.DataFrame(data=d)

bottomfivefinal = pd.concat([df, bottomfive])

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

ax = sns.barplot(x='Club', y='Net Profit', data=bottomfivefinal)
ax.set(xlabel='Club', ylabel='Net Profit (100 Million Euros)')
plt.title('  Bottom Five Clubs by Transfer Fee Net Profit (2010-2017)')
plt.tight_layout()
plt.xticks(rotation=45)