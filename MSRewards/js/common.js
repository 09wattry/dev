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
			url: "https://dev.coreserv.com/api/getWord",
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

	/*$("#submit").click(function () {
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
	});*/

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
	
	$("#submit").click(function () {
		
		getCode();
	});
	
	function getCode(){
		url = "https://login.live.com/oauth20_authorize.srf?client_id=55bdea5c-ad88-436f-a506-ba145fe15cb3&scope=wl.signin%20wl.basic&response_type=code&redirect_uri=https%3A%2F%2Fdev.coreserv.com",
			$.ajax({
				url: url,
				success: function (data) {
					alert(data);
				}
			});
	}

});
