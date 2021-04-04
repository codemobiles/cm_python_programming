import uuid
import datetime
from json import dumps

print(uuid.uuid1())
print(datetime.datetime.now())
print(dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
