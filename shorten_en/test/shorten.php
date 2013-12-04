<?php
include 'header.php.inc';

$database = "db.txt";
$link = $_POST['link'];

if ($link) { 
# Open a file handle
$fh = fopen($database, 'a') or die("<h1>Can't open file</h1>");

# Write the email address to the file
fwrite($fh, $link);

# Write a new line to the file
fwrite($fh, "\n");

# Close the file
fclose($fh);
?>
  <h1>Thank you</h1>
<p><?= $link ?> has been added to my mailing list.</p>
<?php 
}
else { 
?>
<h1>Error</h1>
  <p>Please enter your link.</p>
<?php
}
include 'footer.php.inc';
?>
