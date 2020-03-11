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

// mkdir recursively
$errmsg = "cannot create directory '%s': %s";

$path = $OMEGA['DRIVE'];
$err = NULL;

foreach ($OMEGA['PATH_ELEMS'] as $elem)
{
    $path .= $OMEGA['PATH_SEP'] . $elem;
    if (mkdir($path))
        $err = NULL;
    else
    {
        if (!file_exists($path))
            $err = error($errmsg, $path, "No such file or directory");
        elseif (!is_dir($path))
            $err = error($errmsg, $path, "Not a directory");
        else
            $err = error($errmsg, $path, "Permission denied");
    }
}
if ($err !== NULL)
    return $err;
else
    return 'OK';

?>
