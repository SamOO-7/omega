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

// Check if the file exists
if (!@file_exists($OMEGA['FILE']))
    return error("%s: No such file", $OMEGA['FILE']);

// If the path is not a regular file, throw error.
if ((@fileperms($OMEGA['FILE']) & 0x8000) != 0x8000)
    return error("%s: Not a file", $OMEGA['FILE']);

// Get file contents, or throw error (unreadable file).
if (($data = @file_get_contents($OMEGA['FILE'])) === False)
    return error("%s: Permission denied", $OMEGA['FILE']);

// Return the file data (in base64 format)
return base64_encode($data);

?>
