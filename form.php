<?php
$to = "raymondz@princeton.edu";
$subject = "Lumo Sign-up";
$email = $_REQUEST['email'] ;
$headers = "From: $email";
$sent = mail($to, $subject, $email, $headers) ;
if($sent)
{print "Your mail was sent successfully."; }
else
{print "Sorry, we encountered an error sending your mail."; }
?>