from flask import Flask,jsonify,request,render_template,url_for
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
	cur.close()
	return  render_template('home.html',computer=data)

if __name__=='__main__':
	app.run(debug=True)
