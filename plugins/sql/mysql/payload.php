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

!import(mysqli_compat)

// Establish connection
$host = $OMEGA["HOST"];
$user = $OMEGA["USER"];
$pass = $OMEGA["PASS"];
$conn = @mysqli_connect($host, $user, $pass);
if (!$conn)
    return error("ERROR: %s: %s", @mysqli_connect_errno(), @mysqli_connect_error());


// Select database (if any)
if (isset($OMEGA["BASE"]))
{
    $select = @mysqli_select_db($conn, $OMEGA['BASE']);
    if (!$select)
        return error("ERROR: %s: %s", @mysqli_errno($conn), @mysqli_error($conn));
}


// Send query
$query = mysqli_query($conn, $OMEGA['QUERY']);
if (!$query)
    return error("ERROR: %s: %s", @mysqli_errno($conn), @mysqli_error($conn));


// Query type: GET (information gathering)
$rows = @mysqli_num_rows($query);
if (is_int($rows))
{
    $result = array();
    $obj = mysqli_fetch_array($query, MYSQLI_ASSOC);
    $result[] = array_keys($obj);
    $result[] = array_values($obj);
    while ($line = mysqli_fetch_array($query, MYSQLI_ASSOC))
        $result[] = array_values($line);
    return array('GET', $rows, $result);
}


// Query type: SET (write into the database)
$rows = @mysqli_affected_rows($conn);
if (is_int($rows))
    return array('SET', $rows);

return error("ERROR: %s: %s", @mysqli_errno($conn), @mysqli_error($conn));

?>
