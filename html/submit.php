<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Database file
    $db = new SQLite3('alfred.db');

    // Check if database connection is successful
    if (!$db) {
        die("Failed to connect to the database.");
    }

    // Get form data
    $engineeringController = $_POST['engineeringController'];
    $datetime = $_POST['datetime'];
    $response = $_POST['response'];
    $building = $_POST['building'];
    $floorArea = $_POST['floorArea'];
    $paBroadcast = $_POST['paBroadcast'] === 'yes' ? 1 : 0;
    $comName = $_POST['comName'];
    $wardenPresent = $_POST['wardenPresent'] === 'yes' ? 1 : 0;
    $standDown = $_POST['standDown'];
    $description = $_POST['description'];

    // Prepare the SQL statement
    $stmt = $db->prepare('INSERT INTO incident_log (
        Engineering_Controller, DateTime, Response, Building, Floor_Area, PA_Broadcast, COM_Name, Warden_Present, Stand_Down_Time, Description
    ) VALUES (:engineeringController, :datetime, :response, :building, :floorArea, :paBroadcast, :comName, :wardenPresent, :standDown, :description)');

    // Bind parameters
    $stmt->bindValue(':engineeringController', $engineeringController, SQLITE3_TEXT);
    $stmt->bindValue(':datetime', $datetime, SQLITE3_TEXT);
    $stmt->bindValue(':response', $response, SQLITE3_TEXT);
    $stmt->bindValue(':building', $building, SQLITE3_TEXT);
    $stmt->bindValue(':floorArea', $floorArea, SQLITE3_TEXT);
    $stmt->bindValue(':paBroadcast', $paBroadcast, SQLITE3_INTEGER);
    $stmt->bindValue(':comName', $comName, SQLITE3_TEXT);
    $stmt->bindValue(':wardenPresent', $wardenPresent, SQLITE3_INTEGER);
    $stmt->bindValue(':standDown', $standDown, SQLITE3_TEXT);
    $stmt->bindValue(':description', $description, SQLITE3_TEXT);

    // Execute the statement
    $result = $stmt->execute();

    if ($result) {
        echo "Data inserted successfully!";
    } else {
        echo "Error inserting data.";
    }

    // Close the statement and database connection
    $stmt->close();
    $db->close();
}
?>