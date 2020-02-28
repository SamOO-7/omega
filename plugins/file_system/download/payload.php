<?php

// Check if the file exists
if (!@file_exists($OMEGA['FILE']))
    return error("%s: No such file or directory", $OMEGA['FILE']);

// If the path is not a regular file, throw error.
if ((@fileperms($OMEGA['FILE']) & 0x8000) != 0x8000)
    return error("%s: Not a file", $OMEGA['FILE']);

// Get file contents, or throw error (unreadable file).
if (($data = @file_get_contents($OMEGA['FILE'])) === False)
    return error("%s: Permission denied", $OMEGA['FILE']);

// Return the file data (in base64 format)
return base64_encode($data);

?>
