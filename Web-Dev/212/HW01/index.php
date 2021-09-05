<!Doctype html>

<html>

<script>
    function get_window_width(){
        var width = window.innerWidth;
        return width + " pixels"
    }

    function get_window_height(){
        var height = window.innerHeight;
        return height + " pixels"
    }
 </script>

<title>HW01</title>
    <h1>Andrew Hansbury</h1>
    <body>
        <p> 
        <?php
            $server_address = $_SERVER['SERVER_ADDR'];
            $client_address = $_SERVER['REMOTE_ADDR'];
            echo "Server address is: $server_address"; 
            echo "<br>";
            echo "Client address is: $client_address";
            echo "<br>"; 
        ?>

        <script> 
            document.write("Window inner height: " + get_window_height()); 
            document.write("<br>");
            document.write("Window inner width: " + get_window_width()); 
            document.write("<br>");
            
        </script>
        </p>
    </body>
    
    </html>