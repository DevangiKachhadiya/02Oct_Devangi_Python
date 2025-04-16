from flask import Flask,render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/flaskdbb"

db = SQLAlchemy(app) #DB Init

# DB Model
class stud(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(20))
    city = db.Column(db.String(20))
    sub = db.Column(db.String(20))



@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "POST":
        nm = request.form['name']
        ct = request.form['city']
        sub = request.form['sub']

        stdata = stud(name=nm, city=ct, sub=sub)
        db.session.add(stdata)
        db.session.commit()
        print("Record Inserted!")
    else:
        print("Error!")
    return render_template('index.html')

@app.route('/showdata')
def showdata():
    stdata = stud.query.all()
    return render_template("showdata.html", stdata=stdata)

@app.route('/updatedata/<int:id>/',methods=['GET', 'POST'])
def updatedata(id):
    std=stud.query.get_or_404(id)
    if request.method =='POST': 
        std.name=request.form['name']
        std.city=request.form['city']
        std.sub=request.form['sub']

        db.session.commit()
        print('record updated!')
        return redirect('/showdata')
    return render_template('updatedata.html', std=std)
 


@app.route("/deletedata/<int:id>", methods=['GET'])
def deletedata(id):
    stid = stud.query.get_or_404(id)
    db.session.delete(stid)
    db.session.commit()
    print("Record Deleted!")
    return redirect("/showdata")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port= 5500)