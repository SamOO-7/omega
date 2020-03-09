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

// matchRegexp($name, $regexp) (type => boolean):
//      This function has a behavior similar to glob(3).
//      It checks if the given $name matches $regexp.
//
//      $name (string):
//          A common string (may be a filename for some use cases).
//
//      $regexp (string):
//          The pattern used to compare the regex.
//
//  EXAMPLE:
//      >>> matchRegexp("data.txt", "*.txt")
//      True
//      >>> matchRegexp("data.txt", "[A-Z]*")
//      False
//      >>> matchRegexp("Data.txt", "[A-Z]*")
//      True

function matchRegexp($name, $regexp)
{
    if ($regexp == '')
        return (True);
    elseif (strstr($regexp, '*') === False)
    {
        if ($name == $regexp)
            return (True);
        else
            return (False);
    }
    else
    {
        $name = str_replace('.', '\.', $name);
        $match = '(^' . str_replace('*', '.*', $regexp) . '$)';
        if (preg_match($match, $name))
            return (True);
        else
            return (False);
    }
}

?>
