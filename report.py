from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reports.db'
db = SQLAlchemy(app)

# class MyDateTime(db.TypeDecorator):
#     impl = db.DateTime
    
#     def process_bind_param(self, value, dialect):
#         if type(value) is str:
#             return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
#         return value

class StoreReports(db.Model):
    # TODO: Create A database to store all the form
    # to later display in the form 

    id = db.Column(db.Integer, primary_key=True)
    report_name = db.Column(db.String(100), nullable=False)
    report_date = db.Column(db.Text, nullable=False)
    report_hrs = db.Column(db.Text, nullable=False)
    report_vid = db.Column(db.Text, nullable=False)
    report_plc = db.Column(db.Text, nullable=False)
    report_rv = db.Column(db.Text, nullable=False)
    report_bs = db.Column(db.Text, nullable=False)
    report_min = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return 'Report No ' + str(self.id)

@app.route('/')
@app.route('/home')
def report_home():
    return render_template('index.html')

@app.route('/reports', methods=['GET', 'POST'])
def new_report():
    if request.method == 'POST':
        # if the request mode is post get all data from form and store in a variable
        report_name = request.form['r-name']
        report_date = request.form['r-date']
        report_hrs = request.form['hrs']
        report_vid = request.form['vid']
        report_rv = request.form['rv']
        report_bs = request.form['bs']
        report_plc = request.form['plc']
        report_min = request.form['min']
        new_report = StoreReports(report_name=report_name, report_date=report_date, report_hrs=report_hrs, report_vid=report_vid, report_rv=report_rv, report_bs=report_bs, report_plc=report_plc, report_min=report_min)
        db.session.add(new_report)
        db.session.commit()
        return redirect('/reports')
    else:
        all_reports = StoreReports.query.order_by(StoreReports.id).all()
        return render_template('report.html', reports=all_reports)

@app.route('/reports/delete/<int:id>')
def delete(id):
    reports = StoreReports.query.get_or_404(id) #check the id or return 404 error
    db.session.delete(reports) #if found delete report
    db.session.commit() #commit the change in the database to reflect changes in front end
    return redirect('/reports') #when done redirect to same page

@app.route('/reports/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    editreport = StoreReports.query.get_or_404(id)
    if request.method == 'POST':
        # create an object that holdes the previously submitted data based on the id
        editreport.report_name = request.form['r-name']
        editreport.report_date = request.form['r-date']
        editreport.report_hrs = request.form['hrs']
        editreport.report_vid = request.form['vid']
        editreport.report_rv = request.form['rv']
        editreport.report_bs = request.form['bs']
        editreport.report_plc = request.form['plc']
        editreport.report_min = request.form['min']
        db.session.commit()
        return redirect('/reports')
    else:
        return render_template('edit.html', reports=editreport)


if __name__ == "__main__":
    app.run(debug=True)



