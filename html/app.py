from flask import Flask, request, render_template, redirect
import sqlite3

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

init_db()  # Make sure this runs before app.run()