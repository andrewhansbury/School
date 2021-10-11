<!DOCTYPE html>
<html>
    <head>
        <title>HW06</title>
    </head>
<body>

<h1>HW06 - Telephone Exchanges</h1>

<form action="index.php" method="post">
City: <input type="text" name="city">
State: <input type="text" name="state"><br>
<input type="submit">
</form>

<?php

if (isset($_POST["city"])){

    echo "City: " . $_POST["city"] ;
    echo "State: " . $_POST["state"];     

}
?>



</body>
</html>