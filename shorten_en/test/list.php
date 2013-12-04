<?php
include 'header.php.inc';
# Open a file handle for reading
$fh = fopen('db.txt', 'r'); ?>
<h1>Link List</h1>
<ul>
<?php
$line = null;
while (($line = fgets($fh))) { ?>
  <li><?= $line ?></li>
<?php 
}
?>
</ul>
<?php
fclose($fh);
include 'footer.php.inc'; ?>
