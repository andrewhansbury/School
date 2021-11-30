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
        $time = date("Hi");
        $output = "<table>";
    
        foreach($data as $key => $var) {
            //$output .= '<tr>';
            if ($time > $var['begintime'] && $time < $var['endtime']){
                if($key===0) {
                    $output .= '<tr>';
                    foreach($var as $col => $val) {
                        $output .= "<td><mark><strong>" . $col . '</strong></mark></td>';
                    }
                    $output .= '</tr>';
                    foreach($var as $col => $val) {
                        $output .= '<td><mark><strong>' . $val . '</strong></mark></td>';
                    }
                    $output .= '</tr>';
                }
                else {
                    $output .= '<tr>';
                    foreach($var as $col => $val) {
                        $output .= '<td><mark><strong>' . $val . '</strong></mark></td>';
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
    "andrewhansbury_HW10") or die("Couldn't Open Database!");
    $sql = "select * from session INNER JOIN location on session.location 
    = location.location WHERE `dayofweek` = $today_num";
    $result = mysqli_query($conn, $sql);
    
    display_data($result);
    
    ?>


</body>

</html>
