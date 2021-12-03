<?php
session_start();
?>
<html>

<head>
    <title>Demonstrating password checking/session</title>
</head>

<body>

    <html>

    <head>
        <title>Password tester</title>
    </head>

    <body>
        <?php
        include("passcheck.inc");

        if ($_POST) { //We have a password to check
            print "<pre>User in POST array:";
            print($_POST['un']);
            print "</pre>";
            if (isset($_POST['un'])) {
                print "Testing password<br />";
                $pwr = passcheck($_POST['un'], $_POST['pw']);
                if ($pwr) {
                    print "Accepted";
                    $_SESSION['loggedinuser'] = $_POST['un'];
                } else {
                    print "Rejected";
                }
            }
        }
        print "<form method=\"POST\">";
        print "Username: <input type=\"text\" name=\"un\"><br />";
        print "Password: <input type=\"password\" name=\"pw\"><br />";
        print "<input type=\"submit\">";
        print "</form>";
        if ($_POST) {
            print "<pre>Username:";
            print $_POST['un'];
            print "</pre>";
            print "Testing password<br />";
            $pwr = passcheck($_POST['un'], $_POST['pw']);
            if ($pwr) {
                print "Accepted";
                $_SESSION['loggedinuser'] = $_POST['un'];
            } else {
                print "Rejected";
            }
        }
        ?>
    </body>

    </html>