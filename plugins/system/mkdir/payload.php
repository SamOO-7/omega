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

// simple mkdir
$file = $OMEGA['DIR'];
$parent = dirname($file);
$errmsg = "cannot create directory '%s': %s";

if (file_exists($file))
    return error($errmsg, $file, "File exists");

if (mkdir($file))
    return 'OK';

if (!file_exists($parent))
    return error($errmsg, $file, "No such file or directory");

if (!is_dir($parent))
    return error($errmsg, $file, "Not a directory");

return error($errmsg, $file, "Permission denied");

?>
