<style>html, body, div {width: 100%; height: 100%;}</style>
<div style="font: 20px Helvetica Neue, Helvetica, Arial, sans-serif; text-align: center;">

<?php

$error = "Sorry, we encountered an error saving your email. <br />Please try again later.";
$success = "Thanks for signing up!";

$fh = fopen("lumo_signups.txt", 'w') or die($err);
fwrite($fh, $_POST['email'], 128); // 128 bytes is more than enough
fwrite($fh, "\n");
fclose($fh);
echo($success);

?>
</div>