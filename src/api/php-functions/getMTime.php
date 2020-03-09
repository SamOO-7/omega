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

// getMTime($abspath, $date_fmt) (type => string):
//      Return $abspath file last modification time (mtime)
//      in $data_fmt format (the format used by the php date() function).
//
//      $abspath (string):
//          This variable should be an existing absolute file path
//
//      $date_fmt (string):
//          A string representing a date format. For more infos, take
//          a look at: http://www.php.net/manual/en/function.date.php

function getMTime($abspath, $date_fmt)
{
    $mtime = @filemtime($abspath);
    $result = @date($date_fmt, $mtime);
    return ($result);
}

?>
