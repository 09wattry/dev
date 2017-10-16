<<<<<<< HEAD
<?php

/* 	OD API connection
*	The purpose of this script is to make a make a rest call to get a word list and return it to the caller.
*/
    include_once 'rest.php';
	include_once('../../../config/php/odapiconnection.php');
	include_once('../../../config/php/bingconnection.php');
	include_once('../../../config/php/querydb.php');
	
	$conn = new REST();
	
	function getWord(){
		
		$numberOfWords =       get("SELECT word_id 
										FROM word 
										ORDER BY word_id DESC LIMIT 1");
		
		$randNumber = rand(1, $numberOfWords[0]['word_id']);
		$used = get("SELECT word_id FROM request WHERE word_id="."'".$randNumber."'");
		
		if($used != null){
			echo "This has already been used. Please consult your DB word list";
		} else{
			$randWord = get("SELECT word,word_id FROM word WHERE word_id="."'".$randNumber."'");
			echo json_encode($randWord);
		}
		
	}
	
	function postMSRequest(){
		if(isset($_GET['word_id'])){
			$word_id = $_GET['word_id'];
			echo post("INSERT INTO REQUEST (word_id) VALUES (".$word_id.")");
		} else {
				echo "No record found.";
		} 
	}
	
	function bing(){
		/*$phrase = $_GET['phrase'];
		$bing = new bingRequest($phrase);
		echo $bing->bingit();*/
		
		
	}
	
	function wordlist($resource){
		
		if(isset($_GET['offset'])){
			$offset = $_GET['offset'];
		} else {
			$result = get("SELECT COUNT(*) FROM word WHERE category_key ="."'".$_GET['lex']."'");
			$offset =  $result[0]['COUNT(*)'];
		}
		
		$odi = new odiRequest($resource, $_GET['lang'], $_GET['lex'], $_GET['len'], $_GET['lim'], $offset);
		$json = $odi->makeRequest();
		$json = json_decode($json, true)["results"];
		foreach ($json as $word) {
			$wordlist[] = array ("word" => $word["word"], "category_key" => $_GET['lex'], "oed_id" => $word["id"]);
		}
		echo json_encode($wordlist);
	}
	
	$conn->request();
	
?>
=======
<?php

/* 	OD API connection
*	The purpose of this script is to make a make a rest call to get a word list and return it to the caller.
*/
    include 'rest.php';
	include_once('../../../config/php/odapiconnection.php');
	include_once('../../../config/php/querydb.php');
	
	$conn = new REST();
	
	function getWord(){
		
		$numberOfWords =       get("SELECT word_id 
										FROM word 
										ORDER BY word_id DESC LIMIT 1");
		
		$randNumber = rand(1, $numberOfWords[0]['word_id']);
		$used = get("SELECT word_id FROM request WHERE word_id="."'".$randNumber."'");
		
		if($used != null){
			echo "This has already been used. Please consult your DB word list";
		} else{
			$randWord = get("SELECT word,word_id FROM word WHERE word_id="."'".$randNumber."'");
			echo json_encode($randWord);
		}
		
	}
	
	function postMSRequest(){
		if(isset($_GET['word_id'])){
			$word_id = $_GET['word_id'];
			echo post("INSERT INTO REQUEST (word_id) VALUES (".$word_id.")");
		} else {
				echo "No record found.";
		} 
	}
	
	function wordlist($resource){
		
		if(isset($_GET['offset'])){
			$offset = $_GET['offset'];
		} else {
			$result = get("SELECT COUNT(*) FROM word WHERE category_key ="."'".$_GET['lex']."'");
			$offset =  $result[0]['COUNT(*)'];
		}
		
		$odi = new odiRequest($resource, $_GET['lang'], $_GET['lex'], $_GET['len'], $_GET['lim'], $offset);
		$json = $odi->makeRequest();
		$json = json_decode($json, true)["results"];
		foreach ($json as $word) {
			$wordlist[] = array ("word" => $word["word"], "category_key" => $_GET['lex'], "oed_id" => $word["id"]);
		}
		echo json_encode($wordlist);
	}
	
	$conn->request();
	
?>
>>>>>>> e2e9243bca8ba8cc2e7b8d1b3a4bd313d019ef9a
