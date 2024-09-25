from influxdb import InfluxDBClient

# Connect to InfluxDB
client = InfluxDBClient(host='localhost', port=8086)

# Create a new database
client.create_database('mydb')

# Switch to the new database
client.switch_database('mydb')

# Define a JSON data point
data = [
    {
        "measurement": "temperature",
        "tags": {
            "location": "room1",
        },
        "fields": {
            "value": 25.5
        }
    }
]

# Write the data point to InfluxDB
client.write_points(data)

# Query the data from InfluxDB
result = client.query('SELECT * FROM temperature')

# Print the query result
print(result.raw)

# Close the connection to InfluxDB
client.close()