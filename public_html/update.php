<?php

function write($w)
{
    echo str_replace("\n", "<br/>\n", $w);
    static $handle = null;
    if (!$handle) {
        $handle = fopen('../update.log', 'a');
        if (!$handle) {
            exit(1);
        }
        fwrite($handle, "==========\n");
        fwrite($handle, date('Y-m-d H:i:s') . "\n");
    }
    fwrite($handle, $w);
}

$payload = file_get_contents('php://input');
write("Payload:\n-------\n");
write($payload);
write("\n-------\n");

$payload = json_decode($payload, true);
if (!$payload || !is_array($payload)) {
    write("Error: could not decode\n");
    exit(1);
}
if (!isset($payload['ref'])) {
    write("Error: no field 'ref'\n");
    exit(1);
}
if ($payload['ref'] != 'refs/heads/master') {
    write("Exiting: non-master push\n");
    exit(0);
}
write("all ok, updating\n");
write(shell_exec("export PATH=~/opt/bin:\$PATH; cd .. && git fetch && git reset --hard origin/master && ./generate-html.sh"));
