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

    //passage search input
    echo "<label for=\"passage\">Citation: </label>";
    echo "<input type=\"text\" name=\"passage\">  ";

    //Submit Button
    echo "<input type=\"submit\" name=\"Submit\">";
    echo "</form>";

    //Displaying the Bible passage
    if (isset($_POST['Submit'])) {
        $version = $_POST['Version'];
        echo "<strong>$version</strong>";

        //find passage

        $passage = $_POST['passage'];

        $book = substr($passage, 0, strpos($passage, " "));

        $book = str_replace(".", "", $book);
        $book = ucfirst($book);

        $chap_offset = strpos($passage, ":") - strpos($passage, " ");

        $chapter =  substr($passage, strpos($passage, " "), $chap_offset);

        $verse = substr($passage, strpos($passage, ":"));

        echo $book;
        $sql = "SELECT `b` FROM `key_abbreviations_english` WHERE `a` = \"$book\"";
        $result = mysqli_query($conn, $sql);
        #echo mysqli_num_rows($result);
        echo "<br>";
        $res =  mysqli_fetch_row($result);
        foreach ($res as $value) {
            echo $value;
        }
        #print_r($result);

        // get num for book
        //$book_num = 
        //SELECT `b` FROM `key_abbreviations_english` WHERE `a` = $book

        //SELECT `b` FROM `key_english` WHERE n = $book

        //get table 
        //$table =
        //SELECT `table` FROM  `bible_version_key` WHERE `version` = $version



        //text query
        //SELECT `t` FROM $table WHERE `b` = $booknum AND `c` = $chapter AND `v` = $verse




    }

    ?>






</body>

</html>