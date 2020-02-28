<?php

if (@file_exists($OMEGA['FILE']))
{
    if ((@fileperms($OMEGA['FILE']) & 0x8000) == 0x8000)
    {
        if ($h = @fopen($OMEGA['FILE'], 'r'))
        {
            $size = @filesize($OMEGA['FILE']);
            if ($size == '0')
                return '';
            else
            {
                if ($data = fread($h, $size))
                    return base64_encode($data);
                else
                    return error("%s: Permission denied", $OMEGA['FILE']);
            }
            fclose($h);
        }
        else
            return error("%s: Permission denied", $OMEGA['FILE']);
    }
    else
        return error("%s: Not a file", $OMEGA['FILE']);
}
else
    return error("%s: No such file or directory", $OMEGA['FILE']);

?>
