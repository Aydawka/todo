from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from flask_cors import CORS



app=Flask(__name__)
mysql=MySQL(app)

CORS(app)
app.config['MYSQL_USER']='root1'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_tasks'
app.config['MYSQL_CURSORCLASS']='DictCursor'




@app.route('/',methods=['GET'])
def get_all_tasks():
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM tasks")
	rv=cur.fetchall()
	return jsonify(rv)


@app.route('/',methods=['POST'])
def add_task():
	cur=mysql.connection.cursor()
	title=request.get_json()['title']
	cur.execute('INSERT INTO tasks')
	mysql.connection.commit()
	result={'title':title}
	return jsonify({'result':result})


if __name__=='__main__':
	app.run(debug=True)
