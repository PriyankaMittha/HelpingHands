<?php
$servername = "localhost"; 
$username = "root";
$password = "";
$database = "mydb";
$conn = new mysqli($servername, $username, $password, $database);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$sql = "CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    email VARCHAR(255) NOT NULL,
    dob DATE NOT NULL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";
if ($conn->query($sql) === TRUE) {
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $student_name = $_POST['student_name'];
        $address = $_POST['address'];
        $contact_number = $_POST['contact_number'];
        $email = $_POST['email'];
        $dob = $_POST['dob'];
        $username = $_POST['username'];
        $password = $_POST['password'];
        $insert_sql = "INSERT INTO students (student_name, address, contact_number, email, dob, username, password)
        VALUES ('$student_name', '$address', '$contact_number', '$email', '$dob', '$username', '$password')";

        if ($conn->query($insert_sql) === TRUE) {
            echo "Signup successful! <br> Data inserted into the database.";
        } else {
            echo "Error: " . $insert_sql . "<br>" . $conn->error;
        }
    }
} else {
    echo "Error creating table: " . $conn->error;
}
$conn->close();
?>