<!DOCTYPE html>
<html>

<head>
    <title>HW10</title>
</head>

<style>
    table,
    th,
    td {
        border: 1px solid black;
    }
</style>

<body>
    <?php

    echo "<h1> HW10 - Add and Delete sessions </h1>";

    $day_num = array(
        'Sunday' => 1,
        'Monday' => 2,
        'Tuesday' => 3,
        'Wednesday' => 4,
        'Thursday' => 5,
        'Friday' => 6

    );

    $today_num = $day_num[date("l")];


    function display_data($data)
    {
        echo "<h2> " . date("l") . "'s Open Stations </h2>";

        $time = date("Hi");
        $output = "<table>";

        foreach ($data as $key => $var) {
            //$output .= '<tr>';
            if ($time > $var['begintime'] && $time < $var['endtime']) {
                if ($key === 0) {
                    $output .= '<tr>';
                    foreach ($var as $col => $val) {
                        $output .= "<td><mark><strong>" . $col . '</strong></mark></td>';
                    }
                    $output .= '</tr>';
                    foreach ($var as $col => $val) {
                        $output .= '<td><mark><strong>' . $val . '</strong></mark></td>';
                    }
                    $output .= "<td> <form method=\"post\" action =\"\">
                    <button name = \"Delete\" type=\"submit\" value=" . $var["sessnum"]  . ">Delete</button>
                  </form> </td>";
                    $output .= '</tr>';
                } else {
                    $output .= '<tr>';
                    foreach ($var as $col => $val) {
                        $output .= '<td><mark><strong>' . $val . '</strong></mark></td>';
                    }
                    $output .= "<td> <form method=\"post\" action =\"\">
                    <button name = \"Delete\" type=\"submit\" value=" . $var["sessnum"]  . ">Delete</button>
                  </form> </td>";

                    $output .= '</tr>';
                }
            } else {
                if ($key === 0) {
                    $output .= '<tr>';
                    foreach ($var as $col => $val) {
                        $output .= "<td>" . $col . '</td>';
                    }
                    $output .= '</tr>';
                    foreach ($var as $col => $val) {
                        $output .= '<td>' . $val . '</td>';
                    }
                    $output .= "<td> <form method=\"post\" action =\"\">
                    <button name = \"Delete\" type=\"submit\" value=" . $var["sessnum"]  . ">Delete</button>
                  </form> </td>";
                    $output .= '</tr>';
                } else {
                    $output .= '<tr>';
                    foreach ($var as $col => $val) {
                        $output .= '<td>' . $val . '</td>';
                    }

                    $output .= "<td> <form method=\"post\" action =\"\">
                    <button name = \"Delete\" type=\"submit\" value=" . $var["sessnum"]  . ">Delete</button>
                  </form> </td>";
                    $output .= '</tr>';
                }
            }
        }
        $output .= '</table>';
        echo $output;
    }

    function space_remove($str)
    {
        if (strpos($str, ' ') !== false) {
            return str_replace(' ', '_', $str);
        }
    }

    function space_adder($str)
    {
    }



    function display_form()
    {
        $conn = mysqli_connect(
            "localhost",
            "andrewhansbury",
            "m99c.xent",
            "andrewhansbury_HW10"
        ) or die("Couldn't Open Database!");
        echo "
        <br>

        <h3> Add a Session </h3>

        <form action = \"\" method = \"post\">
        ";
        // <label for=\"sessnum\">sessnum:</label>
        // <input type=\"text\" id=\"sessnum\" name=\"sessnum\">
        // <br>


        echo "
    <label for=\"location\">location:</label>
    
    <select name=\"location\" id=\"location\">";

        $sql = "SELECT `location` FROM `location` WHERE 1";
        $result = mysqli_query($conn, $sql);

        while ($row = $result->fetch_assoc()) {
            echo "<option value=" . $row['location'] . ">" . $row['location'] . "</option>";
        }
        echo "</select>
    <br>


    <label for=\"dayofweek\">dayofweek:</label>
    <select name=\"dayofweek\" id=\"dayofweek\">";

        $sql = "SELECT DISTINCT `dayofweek` FROM `session` WHERE 1";
        $result = mysqli_query($conn, $sql);

        while ($row = $result->fetch_assoc()) {
            echo "<option value=" . $row['dayofweek'] . ">" . $row['dayofweek'] . "</option>";
        }
        echo "</select>
    <br>
    <label for=\"begintime\">begintime:</label>
    <input type=\"text\" id=\"begintime\" name=\"begintime\">
    <br>
    <label for=\"endtime\">endtime:</label>
    <input type=\"text\" id=\"endtime\" name=\"endtime\">
    <br>
    ";
        // <label for=\"l-name\">l-name:</label>
        // <select name=\"l-name\" id=\"l-name\">";

        //     $sql = "SELECT DISTINCT `l-name` FROM `location` WHERE 1";
        //     $result = mysqli_query($conn, $sql);

        //     while ($row = $result->fetch_assoc()) {
        //         echo "<option value=" . space_remove($row['l-name']) . ">" . $row['l-name'] . "</option>";
        //     }
        //     echo "</select>

        echo "
    <label for=\"latitude\">latitude:</label>
    <input type=\"text\" id=\"latitude\" name=\"latitude\" value = 0>
    <br>
    <label for=\"longitude\">longitude:</label>
    <input type=\"text\" id=\"longitude\" name=\"longitude\" value = 0>
    <br>
    <br>

    <input type=\"submit\" value=\"Add Session\">
    </form>

    <br>
    
    ";
    }


    echo print_r($_POST);


    $conn = mysqli_connect(
        "localhost",
        "andrewhansbury",
        "m99c.xent",
        "andrewhansbury_HW10"
    ) or die("Couldn't Open Database!");
    $sql = "select * from session INNER JOIN location on session.location 
    = location.location WHERE `dayofweek` = $today_num";

    $result = mysqli_query($conn, $sql);

    display_data($result);

    display_form();



    if (isset($_POST['dayofweek'])) {


        $result = mysqli_query($conn, "SELECT MAX(`sessnum`) FROM `session`");
        $row = mysqli_fetch_assoc($result);
        print_r($row);
        $session = $row['MAX(`sessnum`)'];
        echo $session;



        #$sql1 = "INSERT INTO `location` (`location`,`l-name`,`latitude`,`longitude`) VALUES ($_POST[location], \"$_POST[lname]\", $_POST[latitude], $_POST[longitude])";
        $sql2 = "INSERT INTO `session` (`sessnum`,`location`,`dayofweek`,`begintime`, `endtime`) VALUES ($session+1, $_POST[location], $_POST[dayofweek], $_POST[begintime], $_POST[endtime])";

        if (mysqli_query($conn, $sql2)) { #&& mysqli_query($conn, $sql2)) {
            echo "New record created successfully (refresh to see results in table)";
        } else {
            echo "<p style = \"color:red;\"><strong>Error: " .  mysqli_error($conn) . "</strong></p>";
        }
        // echo "<br>";
        // echo $sql1;
        // echo "<br>";
        // echo $sql2;
    }

    if (isset($_POST['Delete'])) {
        $sessnum = $_POST['Delete'];
        $sql3 = "DELETE FROM `session` WHERE `sessnum` = $sessnum";
        if (mysqli_query($conn, $sql3)) {
            echo "Record deleted successfully (refresh to see results in table)";
            #echo $sql3;
        } else {
            echo "<p style = \"color:red;\"><strong>Error: " .  mysqli_error($conn) . "</strong></p>";
        }
    }

    ?>


</body>

</html>