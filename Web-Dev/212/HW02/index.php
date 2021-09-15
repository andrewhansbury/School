<!DOCTYPE hmtl>
<html>
<title>HW02</title>

<head>
</head>
<h1>HW02 - Multiplication Table</h1>



<style>
    table,
    td {
        border: 1px solid black;
        background-color: lightblue;
    }

    th {

        font-weight: bold;
        border: 1px solid black;
    }
</style>




<?php
function convertHex($number)
{

    $converted = '';
    while ($number > 0) {
        $digit = (int) $number % 16;
        if ($digit < 10) {
            $converted = strval($digit) . "" . $converted;
        } else {
            $converted = chr($digit + 55) . "" . $converted;
        }
        $number =  intdiv((int)$number, 16);
    }
    return $converted;
}
?>

<body>
    <?php


    echo "<table>
        <tr>
         <th rowspan = 2, colspan =2>Multiply </th> ";


    for ($i = 1; $i < 21; $i++) {
        echo '<th>' . $i . '</th>';
    }
    echo '</tr>';

    echo '<tr>';
    for ($i = 1; $i < 21; $i++) {
        echo '<th>' . convertHex($i) . '</th>';
    }

    echo '</tr> ';


    for ($i = 1; $i < 21; $i++) {
        echo '<tr>';


        echo '<th>' . $i . '</th>';
        echo '<th>' . convertHex($i) . '</th>';


        for ($j = 1; $j < 21; $j++) {
            $num = convertHex($i * $j);

            echo '<td>' . $num . '</td>';
        }
        echo '</tr>';
    }

    echo '</table>';


    ?>
</body>

</html>