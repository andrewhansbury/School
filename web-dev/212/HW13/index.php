<html>

<head>
  <title>HW13</title>
</head>
<style>
  td {
    width: 25%;
    font-size: 30px;
    text-align: center;
  }
</style>


<body>

  <center>
    <h1>HW13 - Javascript Tricks</h1>
    Press a button to turn it blue!
    <br />
    <br />
  </center>


  <?php
  echo "<table align=\"center\" id=\"tableID\" border=\"1\" style=\"cursor: pointer\">";
  echo "<tr>";
  for ($row = 1; $row < 5; $row++) {
    for ($col = 1; $col < 5; $col++) {
      echo "<td style=\"background-color: red;\">" . $row * $col . " </td>";
    }
    echo "</tr>";
  }

  echo "</table>";

  ?>

  <center>
    <p id="counterID" font-size=25> 0 </p>
  </center>

  <script>
    var clicked_counter = 0;

    var table = document.getElementById("tableID");
    if (table != null) {
      for (var i = 0; i < table.rows.length; i++) {
        for (var j = 0; j < table.rows[i].cells.length; j++)
          table.rows[i].cells[j].onclick = function() {
            tableText(this);
          };
      }
    }


    function tableText(tableCell) {
      var cell_color = window.getComputedStyle(tableCell, null).getPropertyValue('background-color');

      // Change color of clicked element
      tableCell.setAttribute('style', 'background-color: lightblue');

      //If its not already lightblue, increment
      if (cell_color != "rgb(173, 216, 230)") {
        //Increment counter under table
        clicked_counter++;
        document.getElementById("counterID").innerHTML = clicked_counter;
      }

      if (clicked_counter == 16) {
        window.location.href = "index2.html";
      }
    }
  </script>

</body>

</html>