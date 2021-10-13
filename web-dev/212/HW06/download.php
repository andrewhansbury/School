<?php

$file = "results.txt";
if (!file_exists($file)) die("File not found");
header("Content-Disposition: attachment; filename=\"" . basename($file) . "\"");
header("Content-Length: " . filesize($file));
readfile($file);

?>
