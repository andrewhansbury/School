<!DOCTYPE hmtl>
<html>


<head>
    <title>HW03</title>
</head>


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


function printTable()
        {
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
        }

?>


<body>
    <h1>HW03 - Multiplication Table</h1>


    <?php
    print_r($_POST);

    if ($_POST) {
        $fcolor = $_POST['color'];
    } else {
        $fcolor = "lightblue";
    }
    ?>

    <form method="POST" action="">
        <label for=colors> Select your background: Background: </label>
        <select name="color">
            <option value=White> White </option>
            <option value=Lightblue> Lightblue </option>
            <option value=Yellow> Yellow </option>
            <option value=Coral> Coral </option>
            <option value=Lightgreen> Lightgreen </option>
        </select>
    </form>
    <br>

    <p>Select the number base


        <?php
        //All the buttons
        for ($i = 2; $i < 17; $i++) {
            echo "
        <input type=submit value = $i name = strval($i)>
        ";
        }
        echo "</p>";

        ?>







        <?php

        //Printing the multiplication table
        printTable();
        

        ?>

</body>

</html>