from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import boto3
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///DevOps_Final_Project.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
load_dotenv()
s3 = boto3.client('s3')

img_url = s3.generate_presigned_url('get_object',
                                    Params={'Bucket': os.getenv("BUCKET_NAME"),
                                            'Key': os.getenv("IMAGE_NAME")})


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        user = User(user_name=username, email=email)
        db.session.add(user)
        db.session.commit()
        db.session.user_name = username
        return redirect('/in_app')
    return render_template('form.html')


@app.route('/in_app', methods=['GET'])
def in_app():
    return render_template('in_app.html', name=db.session.user_name, img_url=img_url)


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
