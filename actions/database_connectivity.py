import psycopg2

def DataUpdate(user_name,phone):
    """Inserts a new row into the rasa_slot table with the provided name.

    Args:
        name (str): The user name to be inserted.

    Returns:
        int: The number of rows inserted (should be 1 for successful insertion).

    Raises:
        psycopg2.OperationalError: If there's an issue connecting to the database.
    """
    connection = None
    print("---------------------")
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host="98.70.11.123",
            user="postgres",
            password="postgre",  # Assuming password is 'postgre'
            database="postgres",
            port=5432
        )

        # Create a cursor object to execute database operations
        print("Checkpost 1111111111111111")
        cursor = connection.cursor()
        sql = "INSERT INTO t1 (user_name,phone) VALUES (%s,%s)"
        print("Checkpost-4444444")

        # Create a tuple containing the name value
        val = (user_name,phone)
        print("Checkpost-55555")

        # Execute the INSERT statement with the name value
        cursor.execute(sql, val)

        # Commit the changes to the database
        connection.commit()
        # # Prepare the SQL statement with placeholder for name
        # sql = "INSERT INTO t1 (name) VALUES (%s)"
        # print("Checkpost-22222222222222")

        # # Create a tuple containing the name value
        # val = (name,)
        # print("Checkpost-33333333333")

        # # Execute the INSERT statement with the name value
        # cursor.execute(sql, val)

        # # Commit the changes to the database
        # connection.commit()

        # Print the number of rows inserted (should be 1)
        #print(cursor.rowcount, "record inserted")
    #     sql = "INSERT INTO t1 (phone) VALUES (%s)"
    #     print("Checkpost-4444444")

    #     # Create a tuple containing the name value
    #     val = (phone,)
    #     print("Checkpost-55555")

    #     # Execute the INSERT statement with the name value
    #     cursor.execute(sql, val)

    #     # Commit the changes to the database
    #    # connection.commit()
    #     sql = "INSERT INTO t1 (user_name) VALUES (%s)"
    #     print("Checkpost-666")

    #     # Create a tuple containing the name value
    #     val = (user_name,)
    #     print("Checkpost-777")

    #     # Execute the INSERT statement with the name value
    #     cursor.execute(sql, val)

    #     # Commit the changes to the database
    #     connection.commit()
    except psycopg2.OperationalError as err:
        print("Error connecting to PostgreSQL database:", err)
    finally:
        # Ensure proper connection closure (if established)
        if connection:
            cursor.close()
            connection.close()



