<!DOCTYPE html>
<html>
<head>
    <title>Display Name - POST</title>
</head>
<body>

<h2>Display Name - POST</h2>

<?php
if (isset($_POST['name'])) {
    $name = $_POST['name'];
    echo "Hello, $name!";
} else {
    echo "No name submitted.";
}
?>

</body>
</html>
