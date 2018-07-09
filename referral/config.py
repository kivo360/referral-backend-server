from decouple import config


DB_URL = config("SQLDATABASE")
REDISHOST = config("REDISHOST")
REDISPORT = config("REDISPORT")
TESTDB = config("SQLTEMP")
