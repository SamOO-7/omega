<?php

// Disable SSL verification
putenv('LDAPTLS_REQCERT=never');

if(!$ldapConnexion = ldap_connect($OMEGA['HOST'])) {
   return error("Socket connexion failed ");
}
ldap_set_option($ldapConnexion, LDAP_OPT_PROTOCOL_VERSION, $OMEGA['VERSION']);

// Authentication or anonymous
if($OMEGA['LOGIN'] != " " and $OMEGA['PASS'] != " ") {
    $isAuth = ldap_bind($ldapConnexion, $OMEGA['LOGIN'], $OMEGA['PASS']);
} else {
    $isAuth = ldap_bind($ldapConnexion);
}

if(!$isAuth) {
    if (ldap_get_option($ldapConnexion, LDAP_OPT_DIAGNOSTIC_MESSAGE, $extended_error)) {
        return error("Error: Autentication failed %s", $extended_error);
    } else {
        return error("Autentication failed  ");
    }
}

$result = ldap_list($ldapConnexion, $OMEGA['BASE_DN'], "(objectClass=*)");
$datas  = ldap_get_entries($ldapConnexion, $result);

ldap_close($ldapConnexion);

if(!$datas) {
    return error('Something went wrong. Check your credentials.');
}

// Fix for printing
function clearNode(&$node) {
    foreach($node as $key => &$val) {
        if(!is_array($val)) {
            if(!ctype_print($val)) {
                $val = base64_encode($val);
            }
        } else {
            clearNode($val);
        }
    }
}

clearNode($datas);

return $datas;
?>
