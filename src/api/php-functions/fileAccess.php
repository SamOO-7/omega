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

// fileAccess($abspath, $mode) (type => boolean):
//      Check if $abspath has $mode permission.
//      
//      $abspath (string):
//          This variable must link to a regular file.
//      $mode (char):
//          'r': Check if readable
//          'w': Check if writable
//          'x': Check if executable
//
// EXAMPLE:
//      >>> fileAccess("/etc/passwd", 'r')
//      True
//      >>> fileAccess("/etc/passwd", 'w')
//      False

function fileAccess($abspath, $mode)
{
    // Assuming cases where user wants to check write access, he
    // will then pass 'w' as mode argument. Therefore, we just can't
    // allow this mode internally, because doing a fopen() with 'w' mode
    // will empty the file in case of success, which is clearly stupid.
    if ($mode != 'r' && $mode != 'x')
        $mode = 'a';

    if ($mode == 'x')
        return @is_executable($abspath);

    // fopen() the given file path and return True in case of success
    $old_mtime = @filemtime($abspath);
    $old_atime = @fileatime($abspath);
    if ($h = @fopen($abspath, $mode))
    {
        fclose($h);
        @touch($abspath, $old_mtime, $old_atime);
        return (True);
    }
    else
        return (False);
}

?>
