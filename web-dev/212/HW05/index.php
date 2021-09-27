<!DOCTYPE hmtl>

<html>
<title>HW05</title>


<?php
$dir = "/home/andrewhansbury/public_html/CPTR-212/HW05//verbiage/";
$files = [];

if (is_dir($dir)) {
    if ($dh = opendir($dir)) {
        while (($file = readdir($dh)) !== false) {
            array_push($files, $file);
        }
        closedir($dh);
    }
}

print_r($files);

?>


<body>



</body>

</html>