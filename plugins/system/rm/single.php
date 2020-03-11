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

$src = $OMEGA["FILE"];

if (!@file_exists($src))
    return error("cannot remove '%s': No such file or directory", $src);

if ((@fileperms($src) & 0x8000) != 0x8000)
    return error("cannot remove '%s': Not a file", $src);

if (@unlink($src) === FALSE)
    return error("cannot remove '%s': Permission denied", $src);

return "ok";

?>
