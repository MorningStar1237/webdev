from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('alfred.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS emergency_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            engineering_controller TEXT,
            datetime TEXT,
            response TEXT,
            building TEXT,
            floor_area TEXT,
            pa_broadcast TEXT,
            com_name TEXT,
            warden_present TEXT,
            stand_down_time TEXT,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    conn = sqlite3.connect('alfred.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO emergency_log (
            engineering_controller, datetime, response, building, floor_area,
            pa_broadcast, com_name, warden_present, stand_down_time, description
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('engineeringController'),
        data.get('datetime'),
        data.get('response'),
        data.get('building'),
        data.get('floorArea'),
        data.get('paBroadcast'),
        data.get('comName'),
        data.get('wardenPresent'),
        data.get('standDown'),
        data.get('description')
    ))
    conn.commit()
    conn.close()
    return redirect('/')  # Redirect to home after submission

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)