<?php

$message = "===================\n";
$message .= date('%c') . ", ${_SERVER['REMOTE_ADDR']}\n";
$message .= "Сторінка: #${_POST['page']}#\n";
$message .= "Повний текст: #${_POST['fulltext']}#\n";
$message .= "Виділине: #${_POST['translation']}#\n";
$message .= "Опис проблеми: #${_POST['problem']}#\n";
$message .= "Імʼя: #${_POST['name']}#\n";
$message .= "e-mail: #${_POST['email']}#\n";
$message .= "\n";

$to = "hedrok@gmail.com";
$subject = "[гпімр] Повідомлення про помилку";

$headers = "From: .@гпімр.укр";

file_put_contents("/home/hedro105/reports.txt", $message, FILE_APPEND);
mail($to, $subject, $message, $headers);
echo "All ok!\n<br/>";
