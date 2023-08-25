<!DOCTYPE html>
<html>
<head>
    <title>Display Name - GET</title>
</head>
<body>

<h2>Display Name - GET</h2>

<?php
if (isset($_GET['name'])) {
    $name = $_GET['name'];
    echo "Hello, $name!";
} else {
    echo "No name submitted.";
}
?>

</body>
</html>
