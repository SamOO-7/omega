<?php

// If we fail to get a file descriptor, throw permission error
if (($file = @fopen($OMEGA['FILE'], 'w')) === False)
    return error("%s: Write permission denied", $OMEGA['FILE']);

// Decode new file contents info $data
$data = base64_decode($OMEGA['DATA']);

// If full data couln't be written, throw write error
if (@fwrite($file, $data) === False)
    return error("%s: Could not write to file", $OMEGA['FILE']);

@fclose($file);

if ($OMEGA['MTIME'])
{
    if (!touch($OMEGA['FILE'], $OMEGA['MTIME']))
        return "MTIME_FAILED";
}

?>
