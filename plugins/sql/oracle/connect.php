<?php

if (!function_exists("oci_connect"))
    return error("ERROR: PECL OCI8 >= 1.1.0 required");

$user = $OMEGA["USER"];
$pass = $OMEGA["PASS"];
$connstr = $OMEGA["CONNSTR"];
$charset = $OMEGA["CHARSET"];

if ($charset)
    $conn = @ocilogon($user, $pass, $connstr, $charset);
else
    $conn = @ocilogon($user, $pass, $connstr);

if ($conn === False)
{
    $err = @oci_error();
    return error("ERROR: %s: %s", $err["code"], $err["message"]);
}

return "OK";

?>
