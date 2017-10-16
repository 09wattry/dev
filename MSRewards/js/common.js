<<<<<<< HEAD
/*
 *	Author: Ryan Wattrus
 *	Purpose: Establish an ajax call to php data layer and access api.
 */

$(document).ready(function () {

	var count = 1;
	var intervals;

	function runSearches(json) {
		var word_id = json[0]['word_id'];
		var search_word = json[0]['word'].trim();
		var word = json[0]['word'].trim()

		var url = 'https://www.bing.com/search?q=' + search_word + '&go=Submit+Query&qs=ds&form=QBLH';
		//var url =
		url = encodeURI(url);

		$.ajax({
			url: url,
			method: 'GET',
			dataType: 'html',
			xhrFields: {
				withCredentials: true
			},
			crossDomain: true,
			success: function (data) {
				console.log("Success");
				postMSRequest(word_id, word, "Success");
			},
			error: function (xhr, textStatus, err) {
				//console.log(data.message + " " + "Fatal Error: We were unable to fetch a word. Please report an error.");
				//postMSRequest(word_id, word, "Failed");
			},
			complete: function(jqXHR, textStatus ){
				postMSRequest(word_id, word, "Success");
			}
		});

		clearInterval(intervals);
	}

	function handleError(data) {}

	function getWord() {
		$.ajax({
			url: "http://dev.msrewards.local/api/getWord",
			method: 'GET',
			dataType: 'json',
			success: function (json) {
				runSearches(json);
			},
			error: function () {
				console.log("Fatal Error: We were unable to fetch a word. Please report an error.");
			}
		});
	}

	function postMSRequest(word_id, word, status) {
		var index = count;
		if (status == "success") {
			$.ajax({
				url: "http://dev.msrewards.local/api/postMSRequest?word_id=" + word_id,
				method: 'POST',
				success: function (json) {
					$("#results-table").append(
						"<tr>" +
						"<td>" + index + "</td><td>" + word + "</td><td>" + word_id + "</td><td>" + status + "</td>" +
						"</tr>");
				},
				error(error) {
					console.log(error + error.message);
				}
			});
		} else {
			$("#results-table").append(
				"<tr>" +
				"<td>" + index + "</td><td>" + word + "</td><td>" + word_id + "</td><td>" + status + "</td>" +
				"</tr>");
		}
		count++;
	}

	$("#submit").click(function () {
		var numRequests = $("#number-requests").val();
		if (numRequests <= 0) {
			alert("Please submit a number greater than 1");
		} else {

			intervals = setInterval(runWord, 3000);
			function runWord() {
				if (count > numRequests) {
					clearInterval(intervals);
				} else {
					getWord();
					clearInterval(intervals);
				}
			};

		}
	});

	$("#submit-button").click(function () {
		getWordList();
	});

	function getWordList() {
		var lang,
		lex,
		len,
		lim,
		url;

		lang = $('#language').val();
		lex = $('#lexical-category').val();
		len = $('#word-length').val();
		lim = $('#word-limit').val();
		url = "http://dev.msrewards.local/api/wordlist?lang=" + lang + "&lex=" + lex + "&len=" + len + "&lim=" + lim

			$.ajax({
				url: url,
				success: function (result) {
					$("#words").val(JSON.stringify(result));
				}
			});

	}

});
=======
/*
 *	Author: Ryan Wattrus
 *	Purpose: Establish an ajax call to php data layer and access api.
 */

$(document).ready(function () {
	
	var count = 1;
	
	function runSearches(data){
		var json = JSON.parse(data);
		var word_id = json[0]['word_id'].trim();
		var word = json[0]['word'].trim();
		
		url = "https://www.bing.com/search?q=definition:" + word;
			$.ajax({
				url: url,
				headers: {'Access-Control-Allow-Origin': '*'},
			});
			
		postMSRequest(word_id, word);
	}
	
	function getWord(){
		url = "http://dev.msrewards.local/api/getWord"
			$.ajax({
				url: url,
				method: 'GET',
				success: function (result) {
					runSearches(result);
				}
			});
	}
	
	function postMSRequest(word_id, word){
		url = "http://dev.msrewards.local/api/postMSRequest?word_id=" + word_id
			$.ajax({
				url: url,
				method: 'POST',
				success: function (result) {
					$("#results-table").append(
					"<tr>" + 
					"<td>" + count +"</td><td>" + word_id + "</td><td>" + word + "</td><td>Sucess</td>" +
					"</tr>"
					);
				}
			});
			count++;
	}
	
	$("#submit").click(function () {
		getWord();
	});

	$("#submit-button").click(function () {
		getWordList();
	});

	function getWordList() {
		var lang,
		lex,
		len,
		lim,
		url;

		lang = $('#language').val();
		lex = $('#lexical-category').val();
		len = $('#word-length').val();
		lim = $('#word-limit').val();
		url = "http://dev.msrewards.local/api/wordlist?lang=" + lang + "&lex=" + lex + "&len=" + len + "&lim=" + lim

			$.ajax({
				url: url,
				success: function (result) {
					$("#words").val(JSON.stringify(result));
				}
			});

	}

});
>>>>>>> e2e9243bca8ba8cc2e7b8d1b3a4bd313d019ef9a
