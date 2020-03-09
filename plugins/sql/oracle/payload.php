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

// Establish connection (for deprecated ORACLE_CRED)
function oracle_login($info, $connector, $serv_type)
{
    $conn_str = '( DESCRIPTION =
                    ( ADDRESS =
                        ( PROTOCOL = TCP )
                        ( HOST = ' . $info["HOST"] . ')
                        ( PORT = ' . $info["PORT"] . ') )
                    ( CONNECT_DATA =
                        ( ' . $connector . ' = ' . $info["CONNECTOR"] . ')
                        ( SERVER = ' . $serv_type . ') ) )';
    $c = @ocilogon($info["USER"], $info["PASS"], $conn_str);
    return ($c);
}

# DEFAULT CONNECT
if (isset($OMEGA['CONNSTR']))
{
    $user = $OMEGA["USER"];
    $pass = $OMEGA["PASS"];
    $connstr = $OMEGA["CONNSTR"];
    $charset = $OMEGA["CHARSET"];

    if ($charset)
        $conn = @ocilogon($user, $pass, $connstr, $charset);
    else
        $conn = @ocilogon($user, $pass, $connstr);
}
# DEPRECATED CONNECT
else
{
    $conn = False;
    if ($conn === False)
        $conn = oracle_login($OMEGA, "SERVICE_NAME", "POOLED");
    if ($conn === False)
        $conn = oracle_login($OMEGA, "SERVICE_NAME", "DEDICATED");
    if ($conn === False)
        $conn = oracle_login($OMEGA, "SID", "POOLED");
    if ($conn === False)
        $conn = oracle_login($OMEGA, "SID", "DEDICATED");
}

if ($conn === False)
{
    $err = @oci_error();
    return error("ERROR: ocilogon(): %s", $err["message"]);
}

// Send query
$query = @ociparse($conn, $OMEGA['QUERY']);
if (!$query)
{
    $err = @oci_error();
    return error("ERROR: ociparse(): %s", $err["message"]);
}
$statement_type = @ocistatementtype($query);

if (!ociexecute($query))
{
    $err = @oci_error($query);
    return error("ERROR: ociexecute(): %s", $err["message"]);
}

if ($statement_type == "SELECT")
{
    $result = array();
    $obj = oci_fetch_array($query, OCI_ASSOC+OCI_RETURN_NULLS);
    $result[] = array_keys($obj);
    $result[] = array_values($obj);
    while ($line = oci_fetch_array($query, OCI_ASSOC+OCI_RETURN_NULLS))
        $result[] = array_values($line);
    return array('GET', count($result) - 1, $result);
}
else
{
    $rows = @ocirowcount($query);
    return array('SET', $rows);
}

?>
