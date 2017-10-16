<<<<<<< HEAD
<?php

class REST{
	
	/*
	 * Make generic RESTful API calls using the provided methods.	 
	 */
	 //Global variables
	 private $method;
	 private $uri;
	 private $query;
	 private $paths;
	 
	 public function __construct() {
		 $this->method = $_SERVER['REQUEST_METHOD'];
		 $this->query = $_SERVER['QUERY_STRING'];
		 $this->uri = trim(str_replace('?'.$this->query,"",$_SERVER['REQUEST_URI']), "/");
		 $this->paths = explode("/", $this->uri);
	 }
	 
	 public function __destruct() {
		 unset($method, $uri, $query, $paths);
	 }
	 
	public function request() {
		$resource;
		$isApi;

		//Make sure there is a query
		if ($this->query != NUll){
		$this->query = explode('&', $this->query);
		}
	
		//Get the end points for our request
		$isApi = array_shift($this->paths);
		
		if ($isApi == "api") {
			$resource = array_shift($this->paths);
			if ($resource == ""){
				header('HTTP/1.1 400 Bad Request');
			}
		} else {
			header('HTTP/1.1 404 Page Not Found');
		}
	
		if($this->method == 'POST'){
			$resource($resource);
		} elseif ($this->method == 'GET'){
			$resource($resource);
		} elseif ($this->method == 'PUT'){
			$resource($resource);
		} elseif ($this->method == 'DELETE'){
			$resource($resource);
		} elseif ($this->method == 'OPTIONS'){
			$resource($resource);
		} else {
			header('HTTP/1.1 405 Method Not Allowed');
			header('Allow: GET, PUT, DELETE');
		}
		
		
		unset($isApi,$resource);
		
	}
}

=======
<?php

class REST{
	
	/*
	 * Make generic RESTful API calls using the provided methods.	 
	 */
	 //Global variables
	 private $method;
	 private $uri;
	 private $query;
	 private $paths;
	 
	 public function __construct() {
		 $this->method = $_SERVER['REQUEST_METHOD'];
		 $this->query = $_SERVER['QUERY_STRING'];
		 $this->uri = trim(str_replace('?'.$this->query,"",$_SERVER['REQUEST_URI']), "/");
		 $this->paths = explode("/", $this->uri);
	 }
	 
	 public function __destruct() {
		 unset($method, $uri, $query, $paths);
	 }
	 
	public function request() {
		$resource;
		$isApi;

		//Make sure there is a query
		if ($this->query != NUll){
		$this->query = explode('&', $this->query);
		}
	
		//Get the end points for our request
		$isApi = array_shift($this->paths);
		
		if ($isApi == "api") {
			$resource = array_shift($this->paths);
			if ($resource == ""){
				header('HTTP/1.1 400 Bad Request');
			}
		} else {
			header('HTTP/1.1 404 Page Not Found');
		}
	
		if($this->method == 'POST'){
			$resource($resource);
		} elseif ($this->method == 'GET'){
			$resource($resource);
		} elseif ($this->method == 'PUT'){
			$resource($resource);
		} elseif ($this->method == 'DELETE'){
			$resource($resource);
		} elseif ($this->method == 'OPTIONS'){
			$resource($resource);
		} else {
			header('HTTP/1.1 405 Method Not Allowed');
			header('Allow: GET, PUT, DELETE');
		}
		
		
		unset($isApi,$resource);
		
	}
}

>>>>>>> e2e9243bca8ba8cc2e7b8d1b3a4bd313d019ef9a
?>