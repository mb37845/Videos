from flask import Flask,request,jsonify,g,current_app
import sqlite3
import os
from dotenv import load_dotenv 
from flask_cors import CORS
import config

load_dotenv() 

app = Flask(__name__)
CORS(app)

app.config.from_object(config)

DB_NAME = os.getenv("DATABASE_NAME")
   
@app.route('/init_db',methods = ['POST'])
def db():
    config.init_db()
    return 'Database initialized.'

@app.route('/',methods = ['GET'])
def home():
    return('Welocme To This Page')


@app.route('/video',methods = ['POST'])
def video():
    data = request.get_json()
    video_name = data["video_name"]
    video_link = data["video_link"]
    conn = sqlite3.connect("videos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM videos WHERE title  = ? and url = ? ",(video_name,video_link))
    video = cursor.fetchall()
    if len(video) == 1: 
     response = jsonify({'url': video[0][1],'comment':video[0][2]}) , 200
    
    else :
     response = jsonify({'video': ""}) , 404
     
    conn.commit()
    conn.close()
    return (response)

if __name__ == '__main__':
    app.run(debug = True)

