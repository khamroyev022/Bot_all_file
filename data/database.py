import mysql.connector


def sql_connect():
    connect = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'Telegram bot'
    )
    return connect

