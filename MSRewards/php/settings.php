<<<<<<< HEAD
<?php

	$indicesServer = array('PHP_SELF', 
	'argv', 
	'argc', 
	'GATEWAY_INTERFACE', 
	'SERVER_ADDR', 
	'SERVER_NAME', 
	'SERVER_SOFTWARE', 
	'SERVER_PROTOCOL', 
	'REQUEST_METHOD', 
	'REQUEST_TIME', 
	'REQUEST_TIME_FLOAT', 
	'QUERY_STRING', 
	'DOCUMENT_ROOT', 
	'HTTP_ACCEPT', 
	'HTTP_ACCEPT_CHARSET', 
	'HTTP_ACCEPT_ENCODING', 
	'HTTP_ACCEPT_LANGUAGE', 
	'HTTP_CONNECTION', 
	'HTTP_HOST', 
	'HTTP_REFERER', 
	'HTTP_USER_AGENT', 
	'HTTPS', 
	'REMOTE_ADDR', 
	'REMOTE_HOST', 
	'REMOTE_PORT', 
	'REMOTE_USER', 
	'REDIRECT_REMOTE_USER', 
	'SCRIPT_FILENAME', 
	'SERVER_ADMIN', 
	'SERVER_PORT', 
	'SERVER_SIGNATURE', 
	'PATH_TRANSLATED', 
	'SCRIPT_NAME', 
	'REQUEST_URI', 
	'PHP_AUTH_DIGEST', 
	'PHP_AUTH_USER', 
	'PHP_AUTH_PW', 
	'AUTH_TYPE', 
	'PATH_INFO', 
	'ORIG_PATH_INFO') ; 

	echo '<table cellpadding="10">' ; 
	foreach ($indicesServer as $param) {
		if (isset($_SERVER[$param])){
			 echo '<tr><td>'.$param.'</td><td>' . $_SERVER[$param] . '</td></tr>' ; 
		} else{
			echo '<tr><td>'.$param.'</td><td>-</td></tr>' ; 
		}
		
	}
	echo '</table>' ; 

=======
<?php

	$indicesServer = array('PHP_SELF', 
	'argv', 
	'argc', 
	'GATEWAY_INTERFACE', 
	'SERVER_ADDR', 
	'SERVER_NAME', 
	'SERVER_SOFTWARE', 
	'SERVER_PROTOCOL', 
	'REQUEST_METHOD', 
	'REQUEST_TIME', 
	'REQUEST_TIME_FLOAT', 
	'QUERY_STRING', 
	'DOCUMENT_ROOT', 
	'HTTP_ACCEPT', 
	'HTTP_ACCEPT_CHARSET', 
	'HTTP_ACCEPT_ENCODING', 
	'HTTP_ACCEPT_LANGUAGE', 
	'HTTP_CONNECTION', 
	'HTTP_HOST', 
	'HTTP_REFERER', 
	'HTTP_USER_AGENT', 
	'HTTPS', 
	'REMOTE_ADDR', 
	'REMOTE_HOST', 
	'REMOTE_PORT', 
	'REMOTE_USER', 
	'REDIRECT_REMOTE_USER', 
	'SCRIPT_FILENAME', 
	'SERVER_ADMIN', 
	'SERVER_PORT', 
	'SERVER_SIGNATURE', 
	'PATH_TRANSLATED', 
	'SCRIPT_NAME', 
	'REQUEST_URI', 
	'PHP_AUTH_DIGEST', 
	'PHP_AUTH_USER', 
	'PHP_AUTH_PW', 
	'AUTH_TYPE', 
	'PATH_INFO', 
	'ORIG_PATH_INFO') ; 

	echo '<table cellpadding="10">' ; 
	foreach ($indicesServer as $param) {
		if (isset($_SERVER[$param])){
			 echo '<tr><td>'.$param.'</td><td>' . $_SERVER[$param] . '</td></tr>' ; 
		} else{
			echo '<tr><td>'.$param.'</td><td>-</td></tr>' ; 
		}
		
	}
	echo '</table>' ; 

>>>>>>> e2e9243bca8ba8cc2e7b8d1b3a4bd313d019ef9a
?>