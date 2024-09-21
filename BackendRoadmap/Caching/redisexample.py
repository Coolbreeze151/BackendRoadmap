import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Check if the data is already cached
cached_data = r.get('my_key')
if cached_data:
    # Data is already cached, use it
    print('Using cached data:', cached_data.decode())
else:
    # Data is not cached, fetch it from the source
    data = fetch_data_from_source()

    # Cache the data for future use
    r.set('my_key', data)

    # Use the fetched data
    print('Fetched data:', data)