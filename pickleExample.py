import pickle
import shelve

arr = {1: 'one', 2: ['two', 'second', 'duo']}
f = open('data.pkl', 'wb')
pickle.dump(arr, f)
f.close()

r = open('data.pkl', 'rb')
a = pickle.load(r)
print a

db = shelve.open('data.txt')
db['1'] = 'one'
db.close()

db = shelve.open('data.txt')
print db['1']
