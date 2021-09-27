<!DOCTYPE hmtl>

<html>
<title>HW05</title>


<style>
table, th, td {
  border:1px solid black;
}
</style>

<?php
$dir = "/home/andrewhansbury/public_html/CPTR-212/HW05//verbiage/";
$files = [];

if (is_dir($dir)) {
    if ($dh = opendir($dir)) {
        while (($file = readdir($dh)) !== false) {
            if (($file != ".") and ($file != "..")){
                array_push($files, $file);
            }
        }
        closedir($dh);
    }
}

?>

<body>
    <h1>HW05 - TEXT ANALYSIS</h1> 
    <h2>List of files:</h2>
    <table>
        <tr>
            <th>File name</th>
            <th>Size</th>
        </tr>

        <?php
        sort($files);
            for ($i = 0; $i < count($files); $i++){
                $fs = filesize($dir . $files[$i]);
                echo "<tr>
                    <td>$files[$i]</td>
                    <td> $fs </td>
                </tr>";
            }
        ?>

    </table>

    <h2>Word List:</h2>
    <table>
        <tr>
            <th>Word</th>
            <th>Number</th>
        </tr>

        <?php
            $str = "";
            for ($i = 0; $i<count($files); $i++){
                $str .= file_get_contents($dir . $files[$i]) ." \n";
            }
        

            $str = str_replace("\n", " ", $str);
            $str = str_replace(",", " ", $str);
            $str = str_replace(".", " ", $str);
            $str = str_replace("  ", " ", $str);
            $str = preg_replace( '/\s+/', ' ', $str);
            $str = trim($str);
            $str = strtolower($str);
            $str_arr = explode(" ", $str);

            $counters = [];

            foreach ($str_arr as $word){

                if (isset($counters[$word])){
                    $counters[$word]++;
                }
                else{
                    $counters[$word] = 1;
                }
            }
            
            arsort($counters);
            $keys = array_keys($counters);

            for ($i = 0; $i < count($keys); $i++){
                $key = $keys[$i];
                echo "
                    <tr>
                        <td> $keys[$i] </td>
                        <td> $counters[$key] </td> 
                    <tr>
                ";
            }
            
        ?>

    </table>

</body>

</html>