<?

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

// MySQL compat mode for php 4:
// define mysqli_*() functions from mysql_*() ones if MYSQLI is not available
// loosely, only defined functions that are actually in use by mysql plugin.

if (!function_exists("mysqli_connect")) {

    // definitions
    //
    define("MYSQLI_ASSOC", MYSQL_ASSOC);

    // functions
    //
    function mysqli_connect($host, $user, $pass) {
        return mysql_connect($host, $user, $pass);
    }

    function mysqli_connect_error() {
        return mysql_error();
    }

    function mysqli_connect_errno() {
        return mysql_errno();
    }

    function mysqli_error($conn) {
        return mysql_error($conn);
    }

    function mysqli_errno($conn) {
        return mysql_errno($conn);
    }

    function mysqli_select_db($conn, $base) {
        return mysql_select_db($base, $conn);
    }

    function mysqli_query($conn, $query_str) {
        return mysql_query($query_str, $conn);
    }

    function mysqli_num_rows($query) {
        return mysql_num_rows($query);
    }

    function mysqli_fetch_array($result, $resulttype) {
        return mysql_fetch_array($result, $resulttype);
    }

    function mysqli_affected_rows($conn) {
        return mysql_affected_rows($conn)
    }

}

?>
