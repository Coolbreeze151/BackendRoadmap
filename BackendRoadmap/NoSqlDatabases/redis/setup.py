import redis

# Connect to Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Set a key-value pair
r.set('name', 'John Doe')

# Get the value for a key
name = r.get('name')
print(name.decode())

# Increment a value
r.incr('counter')

# Get the incremented value
counter = r.get('counter')
print(counter.decode())