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

// If we fail to get a file descriptor, throw permission error
if (($file = @fopen($OMEGA['FILE'], 'w')) === False)
    return error("%s: Write permission denied", $OMEGA['FILE']);

// Decode new file contents info $data
$data = base64_decode($OMEGA['DATA']);

// If full data couln't be written, throw write error
if (@fwrite($file, $data) === False)
    return error("%s: Could not write to file", $OMEGA['FILE']);

@fclose($file);

if ($OMEGA['MTIME'])
{
    if (!touch($OMEGA['FILE'], $OMEGA['MTIME']))
        return "MTIME_FAILED";
}

?>
