from flask import Flask,render_template,request
from sent_mail import mail
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml')) #to secure our da ta
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app) #created an object with app configuretion


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        city = request.form['city']
        location = request.form['location']
        occupation = request.form['occupation']
        reference = request.form['reference']
        remarks = request.form['remarks']

        mail.smail(email)

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email, contact, city, location, occupation, reference, remarks) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (name, email, contact, city, location, occupation, reference, remarks))
        mysql.connection.commit()
        cur.close()
        
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)