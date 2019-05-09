<?php

    if ($_SERVER["REQUEST_METHOD"] == "POST") {

        // access
        $secretKey = '___enter_secret_key___';
        $captcha = $_POST['g-recaptcha-response'];

        if(!$captcha){
          // if not captcha
        }


        $ip = $_SERVER['REMOTE_ADDR'];
        $response=file_get_contents("https://www.google.com/recaptcha/api/siteverify?secret=".$secretKey."&response=".$captcha."&remoteip=".$ip);
        $responseKeys = json_decode($response,true);

        if(intval($responseKeys["success"]) !== 1) {
          // on captcha not ok
        } else {
            // on captcha ok
        }
    }

?>
