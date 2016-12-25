<?php

$message = "===================\n";
$message .= date('%c') . ", ${_SERVER['REMOTE_ADDR']}\n";
$message .= "page: #${_POST['page']}#\n";
$message .= "fulltext: #${_POST['fulltext']}#\n";
$message .= "translation: #${_POST['translation']}#\n";
$message .= "problem: #${_POST['problem']}#\n";
$message .= "email: #${_POST['email']}#\n";
$message .= "name: #${_POST['name']}#\n";
$message .= "email: #${_POST['email']}#\n";
$message .= "\n";

file_put_contents("/home/hedro105/reports.txt", $message, FILE_APPEND);
echo "All ok!\n<br/>";
