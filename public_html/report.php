<?php

$message = "===================\n";
$message .= date('c') . ", ${_SERVER['REMOTE_ADDR']}\n";
$message .= "Сторінка: #${_POST['page']}#\n";
$message .= "Повний текст: #${_POST['fulltext']}#\n";
$message .= "Виділене: #${_POST['translation']}#\n";
$message .= "Опис проблеми: #${_POST['problem']}#\n";
$message .= "Імʼя: #${_POST['name']}#\n";
$message .= "e-mail: #${_POST['email']}#\n";
$message .= "\n";

$to = "0_0@xn--c1asif2i.xn--j1amh";
$subject = "[гпімр] Повідомлення про помилку";

$headers = "From: .@xn--c1asif2i.xn--j1amh";

file_put_contents("/home/hedro105/reports.txt", $message, FILE_APPEND);
$t = mail($to, $subject, $message, $headers);
echo "All ok!\nMail: $t\n<br/>";
