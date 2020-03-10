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

// set_smart_date($smart_date) (type => string):
//      Return an unix timestamp from a value returned by
//      Omega python get_smart_date() function.
//
//      >>> # if a date string is given, return timestamp
//      >>> set_smart_date("2011-09-11 13:29:42")
//      1315747782
//  NOTE: if string is empty or NULL, function returns current time

function set_smart_date($smart_date)
{
    if ($smart_date)
        return strtotime($smart_date);
    return time();
}

?>
