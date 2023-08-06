# add my own installation to path. It is 2 levels up from this file.
import sys, os
# sys.path.insert(0, (os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
sys.path.insert(0, 'C:/Users/Mike/Sync/code/mypysurreal/')
import pysurrealdb as surreal

import urllib.parse

conn = surreal.connect(user='test', password='test', database='test', namespace='test')

conn.drop('person')
conn.drop('is')
conn.drop('alien')
conn.insert('person', {'id': 1 , 'name': 'Mike', 'age': 42, 'description': '"This" is `a` test of strange encoding characters.'})
conn.insert('alien', {'id':2 ,'name': "'Mike'", 'age': 42, 'description': "'This' is `a` test of strange encoding characters."})

# r= surreal.table('test').where('name', 'like', "%this%").first()
# r= surreal.table('test').where('name', "\\'Mike\\'").first()
# r= surreal.table('test').where('name', "'Mike'").first()

conn.relate('person:1', 'is', 'alien:2', {'when': 'now'})

r =surreal.table('person').get()
print(r)

print(conn.table('is').get())

print(conn.query('select <-is<-alien from person'))
