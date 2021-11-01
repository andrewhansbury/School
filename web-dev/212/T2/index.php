<html>

<head>
    <title>Test 2 </title>
</head>

<body>
    <h1>Test 2 - Question 15</h1>

    <?php
    #include("pass.php");
    $conn = mysqli_connect("localhost", "andrewhansbury", "m99c.xent", "andrewhansbury_T2") or die("Could not open database");
    if ($_POST) {
        print "<pre>POST:";
        print_r($_POST);
        print "</pre>";
        if (isset($_POST['Add'])) {
            print "We will add something<br />";
            // INSERT INTO `StateList` (`StateCode`, `StateName`) VALUES ('BC', 'British Columbia');
            // INSERT INTO `StateList` (`StateCode`, `StateName`, `regioncode`) 
            //      VALUES ('ON', 'Ontario', 'C'); 
            $sql = "INSERT INTO `StateList` (`StateCode`, `StateName`, `regioncode`, `langcode`) " .
                "VALUES ('" . $_POST['statecode'] . "', '" . $_POST['statename'] . "', '" . $_POST['Region'] . "', '" . $_POST['Language'] . "');";
            print "Add sql: " . $sql . "<br />";
            if (mysqli_query($conn, $sql)) {
                echo "New record created successfully";
            } else {
                echo "Error: " . $sql . "<br>" . mysqli_error($conn);
            }
        } else {
            $sql = "SELECT * from StateList WHERE StateCode = \"" . $_POST['DELETE'] . "\";";
            $result = mysqli_query($conn, $sql);
            $row = mysqli_fetch_assoc($result);
            print "We are deleting " . $_POST['DELETE'] . ":" . $row['StateName'] . "<br />";
            $sql = "DELETE FROM `StateList` WHERE `StateList`.`StateCode` = '" . $_POST['DELETE'] . "';";
            //  print "SQL:" . $sql . "<br />";
            $result = mysqli_query($conn, $sql);
        } // end of delete section
    }
    print "<form method=\"POST\">";
    $sql = "select * from StateList ORDER BY StateName;";
    //print "SQL:" . $sql . "<br />";
    $result = mysqli_query($conn, $sql);
    // $row = mysqli_fetch_assoc($result);
    print "<table border=1><tr><th></td><th>Code</th><th>Name</th><th>Language</th></tr>";
    while ($row = mysqli_fetch_assoc($result)) {
        // <button name="DELETE" type="submit" value="72">Delete</button>
        $langs = array("cr" => "Creole", "fr" => "French", "es" => "Spanish", "en" => "English", "" => "");

        $delstate = $row['StateCode'];
        print "<tr><td><button name=\"DELETE\" type=\"submit\" value=\"" . $delstate . "\">Delete</button>" . "</td><td>" . $row['StateCode'] . "</td><td>" . $row['StateName'] .
            "</td><td>" . $langs[$row['langcode']] . "</td></tr> \n";
    }
    //mysqli_close($conn);
    ?>
    </form>
    </table>
    <form method="POST">
        State code:<input type="text" name="statecode"><br />
        State name:<input type="text" name="statename"><br />
        <?php
        //<select name="cars" id="cars">
        //  <option value="volvo">Volvo</option>
        //  <option value="saab">Saab</option>
        //  <option value="mercedes">Mercedes</option>
        //  <option value="audi">Audi</option>
        //</select> 
        print "<label for=Region>Region: </label>";
        print "<select name=\"Region\">\n";
        $sql = "SELECT * FROM `regions` ";
        $result = mysqli_query($conn, $sql);
        while ($row = mysqli_fetch_assoc($result)) {
            print "<option value=\"" . $row['regioncode'] . "\">" . $row['regionname'] . "</option>\n";
        }
        print "</select>\n";


        print "<label for=Language>Language: </label>";
        print "<select name=\"Language\">\n";
        $sql = "SELECT * FROM `language` ";
        $result = mysqli_query($conn, $sql);
        while ($row = mysqli_fetch_assoc($result)) {
            print "<option value=\"" . $row['langcode'] . "\">" . $row['language'] . "</option>\n";
        }
        print "</select>\n";

        mysqli_close($conn);
        ?>
        <br>
        <input type="submit" name="Add">
    </form>
</body>

</html>