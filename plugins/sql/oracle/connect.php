<?php

//            ---------------------------------------------------
//                              Omega Framework                                
//            ---------------------------------------------------
//                  Copyright (C) <2020>  <Entynetproject>       
//
//        This program is free software: you can redistribute it and/or modify
//        it under the terms of the GNU General Public License as published by
//        the Free Software Foundation, either version 3 of the License, or
//        any later version.
//
//        This program is distributed in the hope that it will be useful,
//        but WITHOUT ANY WARRANTY; without even the implied warranty of
//        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
//        GNU General Public License for more details.
//
//        You should have received a copy of the GNU General Public License
//        along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
