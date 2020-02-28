<?php

if (!@file_exists($OMEGA['FILE']))
    return error("%s: No such file or directory", $OMEGA['FILE']);

if (!@chmod($OMEGA["FILE"], $OMEGA["MODE"]))
    return error("%s: Permission denied", $OMEGA['FILE']);

return 'ok';

?>
