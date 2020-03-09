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

// getOwner($abspath) (type => string):
//      Return the user name that owns the given $abspath.
//
//      If the owner of the file could not be determined,
//      the string "?" is returned as a fallback value.
//
//      $abspath (string):
//          This variable should be an existing absolute file path

function getOwner($abspath)
{
    if (function_exists('posix_getpwuid'))
    {
        $uid = @filegroup($abspath);
        $usr = @posix_getpwuid($uid);
        if (@is_string($usr['name']) && !@empty($usr['name']))
            return ($usr['name']);
    }
    return ("?");
}

?>
