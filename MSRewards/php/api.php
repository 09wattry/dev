<?php

/* 	OD API connection
*	The purpose of this script is to make a make a rest call to get a word list and return it to the caller.
*/
    include 'rest.php';
	include_once('../../../config/php/odapiconnection.php');
	include_once('../../../config/php/querydb.php');
	
	$conn = new REST();
	
	$json;
	function wordlist($resource){
		
		if(isset($_GET['offset'])){
			$offset = $_GET['offset'];
		} else {
			$result = querydb("SELECT COUNT(*) FROM word WHERE category_key ="."'".$_GET['lex']."'");
			$offset =  $result[0]['COUNT(*)'];
		}
		
		$odi = new odiRequest($resource, $_GET['lang'], $_GET['lex'], $_GET['len'], $_GET['lim'], $offset);
		$json = $odi->makeRequest();
		$json = json_decode($json, true)["results"];
		foreach ($json as $word) {
			$wordlist[] = array ("word" => $word["word"],
				"oed_id" => $word["id"],
				"category_key" => $_GET['lex']
			);
		}
		
		echo json_encode($wordlist);
	}
	
	$conn->request();
	
?>
