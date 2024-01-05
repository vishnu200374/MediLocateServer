from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'medilocate'
app.config['MYSQL_DATABASE'] = 'medi_locate'

# Create a connection object
mysql = MySQL(app)

@app.route('/')
def health_check():
    return 'ok'


@app.route('/signup', methods=['POST'])
def user_signup():
    user_info = request.get_json()
    print(user_info)
    cursor = mysql.connection.cursor()
    cursor.execute(f"INSERT INTO medi_locate.users(name, email, password) VALUES('{user_info['name']}', '{user_info['email']}', '{user_info['password']}')")
    mysql.connection.commit()
    cursor.close()
    return jsonify({'msg': 'Sign up successful'})


@app.route('/login', methods=['POST'])
def user_login():
    print(request.get_json())
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM medi_locate.users')
    users = cursor.fetchall()
    cursor.close()
    return jsonify({'msg': 'Logged in'})


if __name__ == '__main__':
    app.run()
