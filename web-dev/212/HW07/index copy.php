<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>HW07</title>
    <style>
        table,
        th,
        td {
            border: 1px solid black;
        }
    </style>
</head>





<body>
    <h1>HW07 - Uploading - Andrew Hansbury</h1>

    <form action="upload.php" method="post" enctype="multipart/form-data">
        Select image to upload:
        <input type="file" name="fileToUpload" id="fileToUpload">
        <input type="submit" value="Upload Image" name="submit">
    </form>




    <?php
    echo print_r($_POST);
    if (isset($_POST)) {
        echo "<h4>Current Uploads</h4>";
        $path = "./uploads/";
        $files = scandir($path);
        echo "<table>";
        echo "<tr>
          <th></th> <th> File Name </th> <th> Size </th> <th> Pic </th>
            </tr> ";
        foreach ($files as $file) {
            if ($file != "." && $file != "..") {

                echo "<tr>
                      <td> <form method=\"post\" action =\"index.php\">
                      <button name = \"Delete\" type=\"submit\" value=" . $path . str_replace(' ', '%', $file) . ">Delete</button>
                    </form> 
                    

                    <form method=\"post\" action =\"\">
                      <button name = \"Publish\" type=\"submit\" value=" . $path . str_replace(' ', '%', $file) . ">Publish</button>
                    </form> 
                    
                    
                    </td>
                      <td> $file </td>
                      <td>" . strval(filesize($path . $file)) . "</td> 
                      <td> 
                      <img src= \"$path$file\" width = 200> </img>
                      </td>
                      
                    </tr>";
            }
        }


        echo "</table>";

        //Published Table

        echo "<h4>Current Published</h4>";

        $path2 = "./published/";
        $files = scandir($path2);
        echo "<table>";
        echo "<tr>
          <th></th> <th> File Name </th> <th> Size </th> <th> Pic </th>
            </tr> ";
        foreach ($files as $file) {
            if ($file != "." && $file != "..") {

                echo "<tr>
                      <td> <form method=\"post\" action =\"index.php\">
                      <button name = \"Delete\" type=\"submit\" value=" . $path2 . str_replace(' ', '%', $file) . ">Delete</button>
                    </form> 
                    
                    </td>
                      <td> $file </td>
                      <td>" . strval(filesize($path2 . $file)) . "</td> 
                      <td> 
                      <img src= \"$path2$file\" width = 200> </img>
                      </td>
                      
                    </tr>";
            }
        }


        echo "</table>";
    }

    if (isset($_POST['Delete'])) {
        $name = $_POST['Delete'];
        $name = str_replace('%', ' ', $name);
        unlink($name);
    }

    if (isset($_POST['Publish'])) {
        $name = $_POST['Publish'];
        $fixedname = str_replace('%', ' ', $name);
        $name = str_replace('./uploads/', "./published/", $fixedname);
        rename($fixedname, $name);
    }

    ?>


</body>

</html>