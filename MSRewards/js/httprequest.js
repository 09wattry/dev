/*
 *	Author: Ryan Wattrus
 *	Purpose: Establish an ajax call to php data layer and access api.
 */

$(document).ready(function () {

	var jsondata;

	$("#update").click(function () {

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
