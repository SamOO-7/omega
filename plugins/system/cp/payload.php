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

!import(fileAccess)

$src = $OMEGA['SRC'];
$dst = $OMEGA['DST'];

// backup source mtime to copy the same for destination later
$src_mtime = @filemtime($src);
$src_atime = @fileatime($src);

// check source file access and get source file's buffer
if (!@file_exists($src))
    return error("cannot stat '%s': No such file or directory", $src);
if (!@is_file($src))
    return error("cannot copy '%s': Not a regular file", $src);
if (($buffer = @file_get_contents($src)) === False)
    return error("cannot open '%s' for reading: Permission denied", $src);

// if dst is a directory, append source's basename to it.
if (@is_dir($dst))
{
    if (substr($dst, -1) != $OMEGA['PATH_SEP'])
        $dst .= $OMEGA['PATH_SEP'];
    $dst .= basename($src);
}

// if destination does not exists, we don't care about FORCE option.
if (!@file_exists($dst))
{
    $file = @fopen($dst, 'w');
    if ($file !== False && @fwrite($file, $buffer) !== False)
    {
        @fclose($dst);
        @touch($dst, $src_mtime, $src_atime);
        return array($src, $dst);
    }
    $dir = substr($dst, 0, (strrpos($dst, $OMEGA['PATH_SEP']) + 1));
    if (@is_dir($dir))
        $msg = "Permission denied";
    else
        $msg = "No such file or directory";
    return error("cannot create regular file '%s': %s", $dst, $msg);
}

// check destination file access
if ((@fileperms($dst) & 0x8000) != 0x8000)
    return error("cannot overwrite '%s': Not a regular file", $dst);
if (!fileAccess($dst, 'w'))
    return error("cannot create regular file '%s': Permission denied", $dst);
if (!$OMEGA['FORCE'])
    return error("cannot overwrite '%s' without '-f' (force) option", $dst);

// try to write source buffer to destination file
$file = @fopen($dst, 'w');
if ($file === False || @fwrite($file, $buffer) === False)
    return error("cannot create regular file '%s': Permission denied", $dst);

@fclose($dst);
@touch($dst, $src_mtime, $src_atime);
return array($src, $dst);
