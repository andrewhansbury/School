<!DOCTYPE hmtl>
<html>

<head>
    <title>HW14</title>
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

function changeColor($color)
{
    echo "<style>
    table,
    td {
        border: 1px solid black;
        background-color: $color;
    } </style>";
}


function printTable($color, $base)
{
    changeColor($color);
    echo "<table>
        <tr>
         <th rowspan = 2, colspan =2>Multiply </th> ";

    for ($i = 1; $i < 21; $i++) {
        echo '<th>' . $i . '</th>';
    }
    echo '</tr>';

    echo '<tr>';
    for ($i = 1; $i < 21; $i++) {
        echo '<th>' . convertHex($i, $base) . '</th>';
    }

    echo '</tr> ';

    for ($i = 1; $i < 21; $i++) {
        echo '<tr>';
        echo '<th>' . $i . '</th>';
        echo '<th>' . convertHex($i, $base) . '</th>';


        for ($j = 1; $j < 21; $j++) {
            $num = convertHex($i * $j, $base);

            echo '<td>' . $num . '</td>';
        }
        echo '</tr>';
    }

    echo '</table>';
}

?>

<body>
    <h1>HW14 - Multiplication Table [REVISED!]</h1>

    <?php
    if (isset($_COOKIE["color"])) {
        $colors = ["White", "Lightblue", "Yellow", "Coral", "Lightgreen"];


        echo "<form method=\"POST\" action=\"index.php\">";
        echo "<label for=colors> Select your background: Background: </label>";
        echo "    <select name=\"color\">";



        for ($i = 0; $i < count($colors); $i++) {
            if ($_POST['color'] != $colors[$i]) {
                echo "<option value = $colors[$i]> $colors[$i] </option>";
                echo "selected";
            } else {
                echo "<option value = $colors[$i] selected> $colors[$i]   </option>";
            }
        }

        echo "</select>";

        echo "<br>";

        echo "<p>Select the number base:</p>";



        //All the buttons
        for ($i = 2; $i < 17; $i++) {
            echo "
        <input type=submit value = $i name = num>
        ";
        }
        echo "</form>";


        if (isset($_POST['color'])) {
            //delete cookies
            unset($_COOKIE["color"]);
            unset($_COOKIE["base"]);
            //set cookies
            setcookie("color", $_POST["color"], time() + (86400 * 15));
            setcookie("base", $_POST["num"], time() + (86400 * 15));
            $background = $_POST['color'];
            $base_val = $_POST['num'];
            echo "<h1> Base " . $base_val . "</h1> <br>";
            printTable($background, $base_val);
        } else {
            echo "<h1> Base " . $_COOKIE["base"] . "</h1> <br>";
            printTable($_COOKIE["color"], $_COOKIE["base"]);
        }
    }
    //else
    else {
        $colors = ["White", "Lightblue", "Yellow", "Coral", "Lightgreen"];


        echo "<form method=\"POST\" action=\"index.php\">";
        echo "<label for=colors> Select your background: Background: </label>";
        echo "    <select name=\"color\">";



        for ($i = 0; $i < count($colors); $i++) {
            if ($_POST['color'] != $colors[$i]) {
                echo "<option value = $colors[$i]> $colors[$i] </option>";
                echo "selected";
            } else {
                echo "<option value = $colors[$i] selected> $colors[$i]   </option>";
            }
        }

        echo "</select>";

        echo "<br>";

        echo "<p>Select the number base:</p>";



        //All the buttons
        for ($i = 2; $i < 17; $i++) {
            echo "
        <input type=submit value = $i name = num>
        ";
        }
        echo "</form>";

        if (isset($_POST['color'])) {
            setcookie("color", $_POST["color"], time() + (86400 * 15));
            setcookie("base", $_POST["num"], time() + (86400 * 15));
            $background = $_POST['color'];
            $base_val = $_POST['num'];
            echo "<h1> Base " . $base_val . "</h1> <br>";
            printTable($background, $base_val);
        } else {
            $background = "lightblue";
            $base_val = 10;
        }
    }


    ?>



</body>

</html>