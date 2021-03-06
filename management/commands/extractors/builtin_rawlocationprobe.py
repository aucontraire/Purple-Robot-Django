import datetime
import json
import psycopg2
import pytz

CREATE_PROBE_TABLE_SQL = 'CREATE TABLE builtin_rawlocationprobe(id SERIAL PRIMARY KEY, user_id TEXT, guid TEXT, timestamp BIGINT, utc_logged TIMESTAMP, latitude DOUBLE PRECISION, longitude DOUBLE PRECISION, altitude DOUBLE PRECISION, accuracy DOUBLE PRECISION, provider TEXT, network_available BOOLEAN, gps_available BOOLEAN);'
CREATE_PROBE_USER_ID_INDEX = 'CREATE INDEX ON builtin_rawlocationprobe(user_id);'
CREATE_PROBE_GUID_INDEX = 'CREATE INDEX ON builtin_rawlocationprobe(guid);'
CREATE_PROBE_UTC_LOGGED_INDEX = 'CREATE INDEX ON builtin_rawlocationprobe(utc_logged);'

def exists(connection_str, user_id, reading):
    conn = psycopg2.connect(connection_str)

    if probe_table_exists(conn) == False:
        conn.close()
        return False

    cursor = conn.cursor()

    cursor.execute('SELECT id FROM builtin_rawlocationprobe WHERE (user_id = %s AND guid = %s);', (user_id, reading['GUID']))
    
    exists = (cursor.rowcount > 0)
    
    cursor.close()
    conn.close()
    
    return exists

def probe_table_exists(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT table_name FROM information_schema.tables WHERE (table_schema = \'public\' AND table_name = \'builtin_rawlocationprobe\')')
    
    probe_table_exists = (cursor.rowcount > 0)
            
    cursor.close()
    
    return probe_table_exists

def insert(connection_str, user_id, reading):
#    print(json.dumps(reading, indent=2))
    
    conn = psycopg2.connect(connection_str)
    cursor = conn.cursor()
    
    if probe_table_exists(conn) == False:
        cursor.execute(CREATE_PROBE_TABLE_SQL)
        cursor.execute(CREATE_PROBE_USER_ID_INDEX)
        cursor.execute(CREATE_PROBE_GUID_INDEX)
        cursor.execute(CREATE_PROBE_UTC_LOGGED_INDEX)
    
    conn.commit()
    
    reading_cmd = 'INSERT INTO builtin_rawlocationprobe(user_id, ' + \
                                                   'guid, ' + \
                                                   'timestamp, ' + \
                                                   'utc_logged, ' + \
                                                   'latitude, ' + \
                                                   'longitude, ' + \
                                                   'altitude, ' + \
                                                   'accuracy, ' + \
                                                   'provider, ' + \
                                                   'network_available, ' + \
                                                   'gps_available) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;'
    
    values = [ user_id, reading['GUID'], reading['TIMESTAMP'], datetime.datetime.fromtimestamp(reading['TIMESTAMP'], tz=pytz.utc), reading['LATITUDE'], reading['LONGITUDE'] ]
    
    if 'ALTITUDE' in reading:
        values.append(reading['ALTITUDE'])
    else:
        values.append(None)
    
    values.append(reading['ACCURACY'])
    values.append(reading['PROVIDER'])
        
    if 'NETWORK_AVAILABLE' in reading:
        values.append(reading['NETWORK_AVAILABLE'])
    else:
        values.append(None)

    if 'GPS_AVAILABLE' in reading:
        values.append(reading['GPS_AVAILABLE'])
    else:
        values.append(None)
    
    cursor.execute(reading_cmd, values)

    conn.commit()
        
    cursor.close()
    conn.close()
