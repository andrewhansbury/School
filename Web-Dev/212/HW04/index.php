<html>

<head>
    <title>HW04</title>

    <?php
    $pictures = array(
        "Camel.JPG", "Cheetah.JPG", "CuteKitty.gif",
        "Meerkat.JPG", "Otter.JPG", "RedPanda.JPG", "Rhino.JPG", "Tiger.gif", "Zebra.JPG"
    );
    ?>


    <style>
        body {
            background-color: lightgreen;
        }

        img {
            max-width: 100%;
            height: auto;
        }


        @media only screen and (max-width : 800px) {
            h1.computer {
                display: none;
            }

            [class*="col-"] {
                width: 50%;
            }
        }

        @media only screen and (min-width: 801px) {
            h1.mobile {
                display: none;
            }

            [class*="col-"] {
                width: 25%;
            }
        }
    </style>

</head>

<body>
    <h1 class="mobile"> HW04 for Cell Phones - Andrew Hansbury </h1>
    <h1 class="computer"> HW04 for Computers - Andrew Hansbury </h1>

    <?php

    foreach ($pictures as $value) {
        echo "<img class = col-3 src = HW04_Artifacts/" . $value . " width = 100% />";
    }

    ?>

</body>




</html>