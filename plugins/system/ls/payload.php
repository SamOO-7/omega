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

!import(getOwner)
!import(getGroup)
!import(getMTime)
!import(getPerms)
!import(getSize)
!import(dirAccess)
!import(fileAccess)
!import(matchRegexp)

function printLst($lsdir, $regex)
{
    $text = array();
    if ($dh = @opendir($lsdir))
    {
        while (($elem = readdir($dh)) !== FALSE)
        {
            if (matchRegexp($elem,$regex))
            {
                $elempath = $lsdir.$elem;
                $mode  = getPerms($elempath);
                $wmode = getPerms($elempath, 'win');
                $owner = getOwner($elempath);
                $group = getGroup($elempath);
                $size  = getSize($elempath);
                $time  = getMTime($elempath, 'D M d H:i:s O Y');
                $text[] = array($mode, $wmode, $owner, $group, $size, $time, $elem);
            }
        }
        closedir($dh);
    }
    return ($text);
}

$lsdir = $OMEGA['TARGET'] . $OMEGA['SEPARATOR'];
$regex = '';
$ERROR = '';

if (!dirAccess($lsdir,'r'))
{
    if (@is_dir($lsdir))
        $ERROR = error("cannot open %s: Permission denied", substr($lsdir,0,-1));
    elseif ($OMEGA['PARSE'])
    {
        $split = strrpos($OMEGA['TARGET'], $OMEGA['SEPARATOR']) + 1;
        $lsdir = substr($OMEGA['TARGET'], 0, $split);
        $regex = substr($OMEGA['TARGET'], $split);
    }
}

if (strstr(substr($lsdir, 0, -1), $OMEGA['SEPARATOR']) === FALSE)
    $dirname = $lsdir;
else
    $dirname = substr($lsdir, 0, -1);

if (dirAccess($lsdir, 'r'))
{
    $R = array($dirname, $regex, printLst($lsdir, $regex));
    if (!count($R[2]))
        return error("%s: no elements matching '%s'", $dirname, $regex);
    else
        return $R;
}

elseif (!$ERROR)
{
    if (@is_dir($lsdir))
        return error("cannot open %s: Permission denied", $dirname);
    else
        return error("cannot access %s: No such file or directory.", $dirname);
}

else
    return $ERROR;

?>
