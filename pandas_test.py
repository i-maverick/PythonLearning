# import datetime
# import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#
# plt.close()
#
# goog = web.DataReader('GOOG', 'google', datetime.datetime(2017, 1, 1), datetime.datetime.now())
# goog[['Open', 'Close']].plot()
# plt.show()

names = ['imdbID', 'title', 'year', 'score', 'votes', 'runtime', 'genres']
pd.set_option('display.width', 0)
data = pd.read_csv('imdb_top_10000.txt', delimiter='\t', names=names).dropna()
data.runtime = [int(r.split(' ')[0]) for r in data.runtime]
data.genres = [', '.join(g.split('|')) for g in data.genres]
data.title = [t[0:-7] for t in data.title]
data.runtime[data.runtime == 0] = np.nan
print data.head()
print data[['score', 'runtime', 'year', 'votes']].describe()

print data[(data.votes > 5e4) & (data.score < 5)][['title', 'year', 'score']]
print data[data.score == data.score.min()][['title', 'year', 'score']]
print data[data.score == data.score.max()][['title', 'year', 'score']]
print data['genres'].count()
# genre_count = np.sort(data.genres.sum())[::-1]
# pd.DataFrame({'Genre Count': genre_count})
