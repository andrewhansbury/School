<!DOCTYPE hmtl>
<html>
<title>HW03</title>

<head>
</head>
<h1>HW03 - Multiplication Table</h1>



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
function convertHex($number, $base)
{

    $converted = '';
    while ($number > 0) {
        $digit = (int) $number % $base;
        if ($digit < 10) {
            $converted = strval($digit) . "" . $converted;
        } else {
            $converted = chr($digit + 55) . "" . $converted;
        }
        $number =  intdiv((int)$number, $base);
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
        echo '<th>' . convertHex($i, 16) . '</th>';
    }

    echo '</tr> ';


    for ($i = 1; $i < 21; $i++) {
        echo '<tr>';
        echo '<th>' . $i . '</th>';
        echo '<th>' . convertHex($i, 16) . '</th>';


        for ($j = 1; $j < 21; $j++) {
            $num = convertHex($i * $j, 16);

            echo '<td>' . $num . '</td>';
        }
        echo '</tr>';
    }

    echo '</table>';


    ?>
</body>

</html>