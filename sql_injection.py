import mysql.connector

# Database connection settings
config = {
    'user': 'root',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'sql_infection_db'
}

def inject(username, password):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    
    # Perform SQL injection attack 
    query = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(username,password)

    cursor.execute(query)

    result = cursor.fetchall()

    cnx.close()

    return result 
