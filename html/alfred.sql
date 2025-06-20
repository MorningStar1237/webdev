CREATE TABLE IF NOT EXISTS incident_log (
    Engineering_Controller TEXT,
    DateTime DATETIME,
    Response TEXT,
    Building TEXT,
    Floor_Area TEXT,
    PA_Broadcast BOOLEAN,
    COM_Name TEXT,
    Warden_Present BOOLEAN,
    Stand_Down_Time TIME,
    Description TEXT
);