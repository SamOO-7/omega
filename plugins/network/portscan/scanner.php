<?php


$addr = $OMEGA['IP'];

$timeout = $OMEGA['TIMEOUT'];

$ports = range($OMEGA['PORT_MIN'], $OMEGA['PORT_MAX']);
shuffle($ports);

$result = array();

foreach ($ports as $port) {
    $fp = @fsockopen($addr, $port, $errno, $errstr, $timeout);
    if ($fp !== FALSE) {
        @fclose($fp);
        $result[] = array($port);
    }
    else {
        $result[] = array($port, $errno, $errstr);
    }
}

return $result;

?>
