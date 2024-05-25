#pip install sqlalchemy
#pip install flask-sqlalchemy

import os, sys, click, urllib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://MAIN/Bon_vino'
db = SQLAlchemy(app)

SQLALCHEMY_TRACK_MODIFICATIONS = False

from Bon_vino import db

class Transaction(db.model):
    id = db.Column(db.Integer, primary_key=True)
    añada = db.Column(db.Integer)
    #fechaActualizacion = db.Column(db.date)
    imagenEtiqueta = db.Column(db.Integer)
    nombre = db.Column(db.String(50))
    notaDeCataBodega = db.Column(db.String(50))
    #precio = db.Column(db.Decimal)

    def __repr__(self):
        return 'Transaction ID: {}'.format(self.transactionID)
    
    def listar():
        

"""
    # Make sure to replace below data with your DB values
DATABASE_HOST = "10.10.10.110"
DATABASE_NAME = "Bon_vino"
DATABASE_USERNAME = "admin" 
DATABASE_PASSWORD = "admin@123"

app = Flask(__name__)

# to elimate the error, if the password contains special characters like '@' 
DATABASE_PASSWORD_UPDATED = urllib.parse.quote_plus(DATABASE_PASSWORD)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://'+DATABASE_USERNAME+':'+DATABASE_PASSWORD_UPDATED+'@'+DATABASE_HOST+'/'+DATABASE_NAME
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# check if the connection is successfully established or not
with app.app_context():
    try:
        # db.session.execute('SELECT 1')
        db.session.execute(text('SELECT 1'))
        print('\n\n----------- Connection successful !')
    except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)


class Test(db.Model):
    __tablename__ = 't_test'
    __table_args__ = {'extend_existing': True} # allows you to modify the existing table without raising an error.
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    applicationnumber = db.Column(db.String(15))
    source = db.Column(db.String(50))

    def __init__(self, applicationnumber, source):
        self.applicationnumber = applicationnumber
        self.source = source
        print("Executed __init__ !")


@app.route('/api/test', methods=['POST'])
def insert():
    try:
        applicationnumber = request.json['applicationnumber']
        source = request.json['source']
        
        try:
            t_test_obj = Test(applicationnumber, source)
            db.session.add(t_test_obj)
            db.session.commit()
            print("\nRow commited --------")
            return jsonify({'status': 'success', 'message': 'Values inserted successfully.'}), 201
        except Exception as e :
            error=f"Exception Raised : {e}, errorOnLine: {sys.exc_info()[-1].tb_lineno}, file : {os.path.basename(__file__)}"
            click.secho(error, fg="red")
            return jsonify({'status': 'failure', 'message': f"{error}"}), 500

    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# MSSQL query to create table t_test 
'''
CREATE TABLE t_test(
    [id] [int] IDENTITY(1,1) NOT NULL,
    [applicationnumber] [varchar](50) NOT NULL,
    [source] [varchar](50) NULL
)
'''

# API JSON request
'''
{"applicationnumber": "IM012345",
"source": "ABCD"
}
'''
"""