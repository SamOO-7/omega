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

// Establish connection
$host = $OMEGA["HOST"];
$user = $OMEGA["USER"];
$pass = $OMEGA["PASS"];
$conn = @mssql_connect($host, $user, $pass);
if (!$conn)
    return error("ERROR: %s", @mssql_get_last_message());


// Select database (if any)
if (isset($OMEGA["BASE"]))
{
    $select = @mssql_select_db($OMEGA['BASE'], $conn);
    if (!$select)
        return error("ERROR: %s", @mssql_get_last_message());
}


// Send query
$query = mssql_query($OMEGA['QUERY'], $conn);
if (!$query)
    return error("ERROR: %s", @mssql_get_last_message());


// Query type: GET (information gathering)
$rows = @mssql_num_rows($query);
if (is_int($rows))
{
    $result = array();
    $obj = mssql_fetch_array($query, MSSQL_ASSOC);
    $result[] = array_keys($obj);
    $result[] = array_values($obj);
    while ($line = mssql_fetch_array($query, MSSQL_ASSOC))
        $result[] = array_values($line);
    return array('GET', $rows, $result);
}


// Query type: SET (write into the database)
$rows = @mssql_rows_affected();
if (is_int($rows))
    return array('SET', $rows);

return error("ERROR: %s", @mssql_get_last_message());

?>
