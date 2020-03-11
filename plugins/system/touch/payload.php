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

!import(set_smart_date);

$target = $OMEGA['FILE'];
$ref = $OMEGA['REF'];

if ($ref !== NULL)
{
    if (($timestamp = @filemtime($ref)) === FALSE)
        return error("cannot stat '%s': No such file or directory", $ref);
}
else
    $timestamp = set_smart_date($OMEGA['TIME']);

if (@touch($target, $timestamp))
    return 'OK';

if (@file_exists($target))
    return error("%s: Permission denied", $target);

return error("%s: No such file or directory", $target);

?>
