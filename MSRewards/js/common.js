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
