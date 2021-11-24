<!DOCTYPE html>
<html>

<head>
    <title>HW08</title>
</head>

<body>
    <h1>Bible Text Lookup - Andrew Hansbury</h1>

    <?php

    $conn = mysqli_connect("localhost", "andrewhansbury", "m99c.xent", "andrewhansbury_HW08") or die("Couldn't Open Database!");


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
    if (isset($_POST['passage'])){
        echo "<input type=\"text\" name=\"passage\" value=\"" . $_POST['passage'] .  " \">";
    } 
    else{
        echo "<input type=\"text\" name=\"passage\" >";
    }
    

    //Submit Button
    echo "<input type=\"submit\" name=\"Submit\">";
    echo "</form>";

    //Displaying the Bible passage
    $version = "";
    if (isset($_POST['Submit'])) {
        $version = $_POST['Version'];
        echo "<br><strong>$version</strong>";

        //find passage
        $passage = $_POST['passage'];
        $passage = str_replace(".", "", $passage);

        //check for Jude
        $check_jude = substr($passage, 0, strpos($passage, " ") );
        $sql = "SELECT `b` FROM `key_abbreviations_english` WHERE `a` = \"$check_jude\"";
        $result = mysqli_query($conn, $sql);
        #echo mysqli_num_rows($result);
        echo "<br>";
        $book_ID= 0; 
        //echo print_r(r)
        if(strpos($check_jude, "j") !== false){
            $res =  mysqli_fetch_row($result);
            foreach ($res as $value) {
                $book_ID = $value;
            }
        }

        if ($book_ID == 65){
            $verse = substr($passage, strpos($passage, " "), strlen($passage));

            //Get the table name for the version 
            $sql = "SELECT `table` FROM `bible_version_key` WHERE `version` = \"$version\"";
            $result = mysqli_query($conn, $sql);
            $row = mysqli_fetch_assoc($result);
            $verse_table = $row["table"];

            $sql = "SELECT `t` FROM $verse_table WHERE `b` = $book_ID AND `c` = 1 AND `v` = $verse";
            $result = mysqli_query($conn, $sql);
            $row = mysqli_fetch_assoc($result);
            $full_response = $row["t"];
            echo "<br>" . $full_response;
            
        }

        //NON JUDE
        else{
            //Book Parsing
            $book_num = "";
            $book = strtok($passage,":"); //String up until ":"
            if (is_numeric($book[0])){

                $book_num = strval($book[0]) . " ";
                if ($book[1] == " "){
                    $book = substr($book,2);
                }
                else{
                $book = substr($book, 1);
                }
            }
            $pos = strpos($book, " ");
            $book = substr($book, 0, $pos);
            $book = $book_num . $book;
            $book = ucfirst($book);

          
            $colon_pos = strpos($passage, ":") - strpos($passage, " ");
            $chapter =  substr($passage, strpos($passage, " "), $colon_pos);
            
            while(strpos($chapter," ") !== false){
        
                $chapter = substr($chapter, strpos($chapter, " ")+1, strlen($chapter)+1);
            }
            $verse = substr($passage, strpos($passage, ":")+1);
            

            $sql = "SELECT `b` FROM `key_abbreviations_english` WHERE `a` = \"$book\"";
            $result = mysqli_query($conn, $sql);
            #echo mysqli_num_rows($result);
            echo "<br>";
            $book_ID; 
            $res =  mysqli_fetch_row($result);
            foreach ($res as $value) {
                $book_ID = $value;
            }

            //Get the table name for the version 
            $sql = "SELECT `table` FROM `bible_version_key` WHERE `version` = \"$version\"";
            $result = mysqli_query($conn, $sql);
            $row = mysqli_fetch_assoc($result);
            $verse_table = $row["table"];

            //Actually getting the response 
            $sql = "SELECT `t` FROM $verse_table WHERE `b` = $book_ID AND `c` = $chapter AND `v` = $verse";
            $result = mysqli_query($conn, $sql);
            $row = mysqli_fetch_assoc($result);
            $full_response = $row["t"];
            echo "<br>" . $full_response;

        }
        
    }

    ?>

</body>

</html>