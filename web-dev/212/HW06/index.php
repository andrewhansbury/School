<!DOCTYPE html>
<html>

<head>
    <title>HW06</title>
</head>

<body>

    <h1>HW06 - Telephone Exchanges</h1>

    <form action="index.php" method="post">
        City: <input type="text" name="city" , value="<?php echo isset($_POST["city"]) ? $_POST["city"] : '' ?>">
        State: <input type="text" name="state" , value="<?php echo isset($_POST["state"]) ? $_POST["state"] : '' ?>"><br>
        <input type="submit">
    </form>

    <?php
    $book = file('allutlzd.txt');

    if (isset($_POST["city"]) && !empty($_POST['city'])) {
        $city = strtoupper($_POST["city"]);
        $state = strtoupper($_POST["state"]);
        $full_list = "";
        foreach ($book as $line) {
            if (strpos($line, $city) !== false && strpos($line, $state) !== false) {
                $result = substr($line, 3, 4) . ":" . substr($line, 8, 3) . ":" . $state . ":" . $city;
                echo $result . "<br>";
                $full_list .= $result . "\n";
            }
        }

        $write_file = fopen("results.txt", "w");
        fwrite($write_file, $full_list);
        fclose($write_file);
        echo " <form method=get action=.php> <button type=submit>Download</button> </form>";
    }
    ?>


</body>

</html>