<?php

namespace dev\msrewards;
	
class Constants
{
	const CLIENT_ID = '55bdea5c-ad88-436f-a506-ba145fe15cb3';
	const CLIENT_SECRET = 'fsh9Mn5E3GgrarFLChbeVX9';
	const REDIRECT_URI = 'http://localhost:80/oauth.php';
	const AUTHORITY_URL = 'https://login.microsoftonline.com/common';
	const AUTHORIZE_ENDPOINT = '/oauth2/v2.0/authorize';
	const TOKEN_ENDPOINT = '/oauth2/v2.0/token';
	const RESOURCE_ID = 'https://graph.microsoft.com';
	const SENDMAIL_ENDPOINT = '/v1.0/me/sendmail';
    const SCOPES='openid profile user.read mail.send';
}
?>