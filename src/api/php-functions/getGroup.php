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

// getGroup($abspath) (type => string):
//      Return group owner of the given file path.
//
//      If the group owner of the file could not be determined,
//      the string "?" is returned as a fallback value.
//
//      $abspath (string):
//          This variable should be an existing absolute file path

function getGroup($abspath)
{
    if (function_exists('posix_getgrgid'))
    {
        $gid = @filegroup($abspath);
        $grp = @posix_getgrgid($gid);
        if (@is_string($grp['name']) && !@empty($grp['name']))
            return ($grp['name']);
    }
    return ("?");
}

?>
