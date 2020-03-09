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

!import(dirAccess)
!import(fileAccess)
!import(can_change_mtime)

$path = $OMEGA['FILE'];
$follow_links = $OMEGA['FOLLOW_LINKS'];

if (!@file_exists($path) && !@is_link($path))
    return error("%s: No such file or directory", $OMEGA['FILE']);

// r['file_repr']
$file_repr = "'$path'";
if (!$follow_links && ($link_path = @readlink($path)))
        $file_repr .= " -> '" . $link_path . "'";

if ($follow_links && is_link($path))
{
    $path = realpath($path);
    if (!@file_exists($path))
        return error("%s: No such file or directory", $OMEGA['FILE']);
}

// r['stat']
@clearstatcache();
if (!($r = @lstat($path)))
    return error("%s: Permission denied", $OMEGA['FILE']);

if (is_dir($path))
{
    $r["readable"] = dirAccess($path, 'r') ? "Yes" : "No";
    $r["writable"] = dirAccess($path, 'w') ? "Yes" : "No";
}
else
{
    $r["readable"] = fileAccess($path, 'r') ? "Yes" : "No";
    $r["writable"] = fileAccess($path, 'w') ? "Yes" : "No";
}

$r["file_repr"] = $file_repr;

$r["atime"] = date("Y-m-d H:i:s O", $r["atime"]);
$r["mtime"] = date("Y-m-d H:i:s O", $r["mtime"]);
$r["ctime"] = date("Y-m-d H:i:s O", $r["ctime"]);

if (can_change_mtime($path))
    $r["mtime"] .= " [MUTABLE!]";
else
    $r["mtime"] .= " [IMMUTABLE]";

if (extension_loaded("posix"))
{
    $tmp = posix_getpwuid($r["uid"]);
    $r["posix_pwuid"] = $tmp["name"];
    $tmp = posix_getgrgid($r["gid"]);
    $r["posix_grgid"] = $tmp["name"];
}

return $r;

?>
