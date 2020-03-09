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

// getSize($abspath) (type => string):
//      Returns the size of the given file path in human format.
//
//      $abspath (string):
//          This variable should be an existing absolute file path
//
//  EXAMPLE:
//      >>> getSize("/etc/passwd")
//      "1.4K"

function getSize($abspath)
{
    $size = @filesize($abspath);
    $units = array('', 'K', 'M', 'G', 'T');

    for ($i = 0; $size >= 1024 && $i < 4; $i++)
        $size /= 1024;
    $result = str_replace('.', ',', round($size, 1)) . $units[$i];
    return ($result);
}

?>
