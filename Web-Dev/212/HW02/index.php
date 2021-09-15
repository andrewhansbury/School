<!DOCTYPE hmtl>
<html>
    <title>HW02</title>

    <head>
    </head>
    <h1>HW02 - Multiplication Table</h1>

    

    <style>
    table, td {
    border:1px solid black;
    background-color: lightblue;
    }
    th {
    
    font-weight: bold;
    border:1px solid black;
    }
    </style>

    


    <?php 
    function convertHex($number){
            
            $converted = '';
            while ($number>0){
                $digit = (int) $number % 16;
                if ($digit < 10){
                    $converted = strval($digit) . "" . $converted;
                }
                else{
                    $converted = chr($digit + 55) . "" . $converted;
                }
                $number =  intdiv((int)$number, 16);
            }
            return $converted;
        }
    ?>

    <body>
        <?php 


        echo "<table> <th> Multiply <br> ";
        
        
        for ($i = 1; $i<21; $i++){
            echo '<td>' . $i . '</td>';
        }
        echo ' <tr>';
        echo '<td> </td>';

        for ($i = 1; $i<21; $i++){
            echo '<td>' . convertHex($i) . '</td>';
        }
        
        echo '</tr> </th>';

        
        for ($i = 0; $i<21; $i++){
            echo '<tr>';
            
            if ($i != 0){
                echo '<th>' . $i . '</th>';
                echo '<th>' . convertHex($i) . '</th>';
            }
            
            for ($j = 0; $j <21; $j++){
                $num = convertHex($i*$j);
                
                echo '<td>' . $num . '</td>';
            
            }
            echo '</tr>';
        }

        echo '</table>';


        ?>
    </body>

</html>