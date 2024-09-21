import memcache

# Connect to the memcache server
client = memcache.Client(['localhost:11211'])

# Set a value in the cache
client.set('key', 'value')

# Get a value from the cache
value = client.get('key')
print(value)

# Delete a value from the cache
client.delete('key')