import random
import datetime

random.randint(1, 10)

now = datetime.datetime.now()
type(now)
print(now)

print(now.year)

print(now + datetime.timedelta(days=28))