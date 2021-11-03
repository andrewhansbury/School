<!DOCTYPE html>
<html>

<head>
    <title>HW08</title>
</head>

<body>
    <h1>Bible Text Lookup</h1>

    <?php

    $conn = mysqli_connect("localhost", "andrewhansbury", "m99c.xent", "andrewhansbury_HW08") or die("Couldn't Open Database!");

    echo "<label for=Version>Version: </label>";
    echo "<select name=\"Version\"> \n";
    $sql = "SELECT * FROM `bible_version_key`";
    $result = mysqli_query($conn, $sql);
    while ($row = mysqli_fetch_assoc($result)) {
        echo "<option value= \"" . $row['version'] . "\">" . $row['abbreviation'] . "</option>\n";
    }


    echo "</select>\n";

    ?>




</body>

</html>