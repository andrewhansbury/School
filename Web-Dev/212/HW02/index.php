<!DOCTYPE hmtl>
<html>
    <title>HW02</title>
    <h1>HW02 - Multiplication Table</h1>

    <body>
        <?php 
        function convertHex($number){
            echo $number .=' <br>';
            
            $converted = '';
            while ($number!=0){
                //$digit = 0;
                $digit = (int) $number % 16;
                echo $digit .= '<br>';

                if ($digit < 10){
                    #echo 'poop <br>';
                    $converted .= strval($digit);
                    echo $converted;
                }
                else{
                    $converted .= chr($digit + 55);
                    echo $converted;
                }
                $number = (int) $number/16;
            
            
            }
            echo $converted .= "asjbfie";
        }
        convertHex(122);
        ?>
    </body>

</html>