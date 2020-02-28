<?

!import(dirAccess)

// If directory has read access, just return success.
if (dirAccess($OMEGA['DIR'], 'r'))
    return 'ok';
// Otherwise, determine the error message to return.
else
{
    if (@file_exists($OMEGA['DIR']))
    {
        if ((@fileperms($OMEGA['DIR']) & 0x4000) == 0x4000)
            return error("%s: Permission denied", $OMEGA['DIR']);
        else
            return error("%s: Not a directory", $OMEGA['DIR']);
    }
    else
        return error("%s: No such file or directory", $OMEGA['DIR']);
}

?>
