<!DOCTYPE hmtl>
<html>
    <title>HW02</title>
    <h1>HW02 - Multiplication Table</h1>

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
        
        echo "<tr> <th> Multiply </th> </tr>";
        ?>
    </body>

</html>