<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>HW07</title>
  <style> table, th, td{ border:1px solid black;}</style>
</head>
<body>
    <h1>Uploading</h1>
    <?php

    $path = "./uploads/";
    $files = scandir($path);
    echo "<table>";
      echo "<tr>
       <th></th> <th> File Name </th> <th> Size </th> <th> Pic </th>
         </tr> ";
         foreach ($files as $file){
                 echo "<tr>
                <td> </td>
                <td> $file </td>
                 <td>" . strval(filesize( $path . $file)) . "</td> 
                 <td> 
                 <img src= $path . $file width = 100 >
                 </td>
               </tr>";
          }
         
         
         echo "</table>" ; 
    ?>
    
    
</body>
</html>