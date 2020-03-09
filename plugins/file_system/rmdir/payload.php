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

!import(dirAccess)

$dir = $OMEGA["DIR"];

if (!@file_exists($dir))
    return error("failed to remove '%s': No such file or directory", $dir);

if ((@fileperms($dir) & 0x4000) != 0x4000)
    return error("failed to remove '%s': Not a directory", $dir);

if (@rmdir($dir) === FALSE)
{
    if (dirAccess($dir, 'r'))
        return error("failed to remove '%s': Directory not empty", $dir);
    return error("failed to remove '%s': Permission denied", $dir);
}

?>
