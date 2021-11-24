<!DOCTYPE html>
<html>

<head>
    <title>HW09</title>
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
    
    echo "<h1> " . date("l") . "'s Open Stations </h1>";


    $day_num = array(
        'Sunday' => 1,
        'Monday' => 2,
        'Tuesday' => 3,
        'Wednesday' => 4,
        'Thursday' => 5,
        'Friday' => 6

    );

    $today_num = $day_num[date("l")];
    

    function display_data($data) {
        echo date("Hi") . "<br>";
        $time = date("Hi");
        $output = "<table>";
    
        foreach($data as $key => $var) {
         
            if ($time > $var['begintime'] && $time < $var['endtime']){
                if($key===0) {
                    $output .= '<tr>';
                    foreach($var as $col => $val) {
                        $output .= "<td><strong>" . $col . '</strong></td>';
                    }
                    $output .= '</tr>';
                    foreach($var as $col => $val) {
                        $output .= '<td><strong>' . $val . '</strong></td>';
                    }
                    $output .= '</tr>';
                }
                else {
                    $output .= '<tr>';
                    foreach($var as $col => $val) {
                        $output .= '<td><strong>' . $val . '</strong></td>';
                    }
                    $output .= '</tr>';
            
                }
            }
            else{ 
                if($key===0) {
                    $output .= '<tr>';
                    foreach($var as $col => $val) {
                        $output .= "<td>" . $col . '</td>';
                    }
                    $output .= '</tr>';
                    foreach($var as $col => $val) {
                        $output .= '<td>' . $val . '</td>';
                    }
                    $output .= '</tr>';
                }
                else {
                    $output .= '<tr>';
                    foreach($var as $col => $val) {
                        $output .= '<td>' . $val . '</td>';
                    }
                    $output .= '</tr>';
                }
            }
            
        
        }
        $output .= '</table>';
        echo $output;
    }

   
    

    $conn = mysqli_connect("localhost", "andrewhansbury", "m99c.xent", 
    "andrewhansbury_HW09") or die("Couldn't Open Database!");
    $sql = "select * from session INNER JOIN location on session.location 
    = location.location WHERE `dayofweek` = $today_num";
    $result = mysqli_query($conn, $sql);
    
    
    //print_r($result);
    $db = mysqli_fetch_assoc($result);
    echo "<br><br>";
    //print_r($db);

    echo "<br><br>";

    $rows = array_keys($db);
    // echo "<table>";
    // echo "<tr>";
    // foreach ($rows as $row){
    //     echo "<th>$row</th>";
    // }
    // foreach ($db as $entry){
    //     echo "<tr> <td> $entry </td> </tr>";
    // }
    // echo "</tr>";
    // echo "</table>";

    display_data($result);
    
    ?>


</body>

</html>
