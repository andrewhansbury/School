<?php
// Enable session
session_start(); ?>
<html>

<head>
    <title>HW12</title>
</head>

<body>
    <script>
        // Use JavaScript to force use of https
        if (location.protocol !== "https:") {
            location.replace(window.location.href.replace("http:", "https:"));
        }
    </script>
    <h1>HW12 - Validation</h1>
    <?php
    include("passcheck.inc");
    //print "<pre>POSTstuff"; print_r($_POST); print "</pre>";
    //print "<pre>SESSIONstuff"; print_r($_SESSION); print "</pre>";
    function isloggedin()
    {
        $loggedin = false;
        if (isset($_SESSION['loggedin'])) {
            print "User is logged in as " . $_SESSION['loggedin'] . "<br />";
            $loggedin = true;
        }
        return $loggedin;
    }
    function logindata()
    {
        $logindata = false;
        if (isset($_POST['username'])) {
            $logindata = true;
        }
        return $logindata;
    }
    function validatelogin()
    {
        //  $validlogin=false;
        $validlogin = passcheck($_POST['username'], $_POST['userpass']);
        //  $validlogin=true; // for debugging only
        return $validlogin;
    }
    if (isloggedin()) {
        if (isset($_POST['logout'])) {
            print "Logging " . $_SESSION['loggedin'] . " out<br />";
            unset($_SESSION['loggedin']); // Log user out
        }
    } else { // User is not yet logged in
        print "Not logged in yet<br />";
        if (logindata()) {
            if (validatelogin()) {
                print "logging them in<br />";
                $_SESSION['loggedin'] = $_POST['username'];
            } else {
                print "Invalid login";
            }
        }
    }
    if (isloggedin()) {
        echo "
    <style>
    table,
    th,
    td {
        border: 1px solid black;
    }
</style>";




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

                        $output .= "<td> <form method=\"post\" action =\"\">
                    <button name = \"Edit\" type=\"submit\" value=" . $var["sessnum"]  . ">Edit</button>
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

                        $output .= "<td> <form method=\"post\" action =\"\">
                    <button name = \"Edit\" type=\"submit\" value=" . $var["sessnum"]  . ">Edit</button>
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

                        $output .= "<td> <form method=\"post\" action =\"\">
                    <button name = \"Edit\" type=\"submit\" value=" . $var["sessnum"]  . ">Edit</button>
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


                        $output .= "<td> <form method=\"post\" action =\"\">
                    <button name = \"Edit\" type=\"submit\" form=\"form1\" value=" . $var["sessnum"]  . ">Edit!</button>
                  </form> </td>";
                        $output .= '</tr>';
                    }
                }
            }
            $output .= '</table>';
            echo $output;
        }



        function display_add_form()
        {
            echo "
        <br>

        <h3> Add a Session </h3>

        <form action = \"\" method = \"post\">
    <label for=\"sessnum\">sessnum:</label>
    <input type=\"text\" id=\"sessnum\" name=\"sessnum\">
    <br>
    <label for=\"location\">location:</label>
    <input type=\"text\" id=\"location\" name=\"location\">
    <br>
    <label for=\"dayofweek\">dayofweek:</label>
    <input type=\"text\" id=\"dayofweek\" name=\"dayofweek\">
    <br>
    <label for=\"begintime\">begintime:</label>
    <input type=\"text\" id=\"begintime\" name=\"begintime\">
    <br>
    <label for=\"endtime\">endtime:</label>
    <input type=\"text\" id=\"endtime\" name=\"endtime\">
    <br>
    

   

    <input type=\"submit\" value=\"Add Session\">
    </form>

    <br>
    
    ";
        }

        function display_edit_form()
        {
            echo "<h3> Edit a Session </h3>";

            echo "<form action=\"\" method =\"POST\" id=\"form1\">
        
        <label for=\"newbegin\">New begintime:</label>
        <input type=\"text\" id=\"newbegin\" name=\"newbegin\">
        <br>

        <label for=\"newend\">New endtime:</label>
        <input type=\"text\" id=\"newend\" name=\"newend\">            
    
        </form>";
        }


        echo print_r($_POST);


        $conn = mysqli_connect(
            "localhost",
            "andrewhansbury",
            "m99c.xent",
            "andrewhansbury_HW11"
        ) or die("Couldn't Open Database!");
        $sql = "select * from session INNER JOIN location on session.location 
    = location.location WHERE `dayofweek` = $today_num";
        $result = mysqli_query($conn, $sql);

        display_data($result);

        display_edit_form();

        display_add_form();


        if (isset($_POST['sessnum'])) {

            #$sql1 = "INSERT INTO `location` (`location`,`l-name`,`latitude`,`longitude`) VALUES ($_POST[location], \"$_POST[lname]\", $_POST[latitude], $_POST[longitude])";
            $sql2 = "INSERT INTO `session` (`sessnum`,`location`,`dayofweek`,`begintime`, `endtime`) VALUES ($_POST[sessnum], $_POST[location], $_POST[dayofweek], $_POST[begintime], $_POST[endtime])";

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


        // if (isset($_POST['newbegin'])) {
        //     $newbegin = $_POST['newbegin'];
        //     $newend = $_POST['newend'];
        //     echo "<p style = \"color:blue;\">Press Edit to Change Session BeginTime to: <strong>" . $_POST['newbegin'] . "</strong> and Session Endtime to: <strong>" . $_POST['newend'] . "</strong> </p>";
        // }


        if (isset($_POST['Edit'])) {

            $edit_sql = "UPDATE `session` SET `begintime` = $_POST[newbegin], `endtime` = $_POST[newend] WHERE `sessnum` = $_POST[Edit]";
            echo $edit_sql;

            if (mysqli_query($conn, $edit_sql)) {
                echo "Record edited successfully (refresh to see results in table)";
                #echo $sql3;
            } else {
                echo "<p style = \"color:red;\"><strong>Error: " .  mysqli_error($conn) . "</strong></p>";
            }
        }

        print "<br>";

        print "\n<form method=\"POST\">";
        print "<input type=\"submit\" name=\"logout\" value=\"Log Out\" />";
        print "</form>";
    } else {
        // Display login form
        print "\n<form method=\"POST\">";
        print "Username: <input type=\"text\" name=\"username\" /><br />";
        print "Password: <input type=\"password\" name=\"userpass\" /><br />";
        print "<input type=\"submit\" />";
        print "</form>";
    }



    ?>
</body>

</html>