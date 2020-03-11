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

// If directory has read access, just return success.
if (dirAccess($OMEGA['DIR'], 'r'))
    return 'ok';
// Otherwise, determine the error message to return.
else
{
    if (@file_exists($OMEGA['DIR']))
    {
        if ((@fileperms($OMEGA['DIR']) & 0x4000) == 0x4000)
            return error("%s: Permission denied", $OMEGA['DIR']);
        else
            return error("%s: Not a directory", $OMEGA['DIR']);
    }
    else
        return error("%s: No such file or directory", $OMEGA['DIR']);
}

?>
