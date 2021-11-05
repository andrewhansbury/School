<!DOCTYPE html>
<html>

<head>
    <title>HW08</title>
</head>

<body>
    <h1>Bible Text Lookup</h1>

    <?php

    $conn = mysqli_connect("localhost", "andrewhansbury", "m99c.xent", "andrewhansbury_HW08") or die("Couldn't Open Database!");


    if ($_POST) {
        print "<pre>POST:";
        print_r($_POST);
        print "</pre>";
    }


    //Version dropdown
    echo "<form method=\"POST\">";
    echo "<label for=Version>Version: </label>";
    echo "<select name=\"Version\"> ";
    $sql = "SELECT * FROM `bible_version_key`";
    $result = mysqli_query($conn, $sql);
    while ($row = mysqli_fetch_assoc($result)) {
        if ($row['abbreviation'] == "KJV") {
            echo "<option value=\"King James Version\" selected> KJV </option>";
        } else {
            echo "<option value= \"" . $row['version'] . "\">" . $row['abbreviation'] . "</option>";
        }
    }
    echo "</select> ";

    //Verse search input
    echo "<label for=\"verse\">Citation: </label>";
    echo "<input type=\"text\" name=\"verse\">  ";

    //Submit Button
    echo "<input type=\"submit\" name=\"Submit\">";
    echo "</form>";

    //Displaying the Bible Verse
    if (isset($_POST['Submit'])) {
        echo "<strong>POOP</strong>";
    }

    ?>






</body>

</html>