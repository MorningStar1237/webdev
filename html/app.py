from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
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
    # Render the confirmation page
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)