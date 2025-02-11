from flask import Flask, jsonify
import psycopg2
import redis
import os

app = Flask(__name__)

# Database Configuration
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_USER = os.getenv("POSTGRES_USER", "user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
POSTGRES_DB = os.getenv("POSTGRES_DB", "testdb")

# Redis Configuration
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")

def check_postgres():
    try:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            dbname=POSTGRES_DB
        )
        conn.close()
        return True
    except Exception as e:
        return str(e)

def check_redis():
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        r.ping()
        return True
    except Exception as e:
        return str(e)

@app.route('/health', methods=['GET'])
def health_check():
    db_status = check_postgres()
    redis_status = check_redis()

    if db_status is True and redis_status is True:
        return jsonify({"status": "connected to both redis and database"}), 200
    else:
        return jsonify({
            "status": "error",
            "database": db_status if db_status is not True else "ok",
            "redis": redis_status if redis_status is not True else "ok"
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
