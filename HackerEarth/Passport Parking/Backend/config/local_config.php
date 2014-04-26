<?php

$config = array(
    "db" => array(
        "db1" => array(
            "dbname" => "cal",
            "username" => "root",
            "password" => "root",
            "host" => "localhost"
        ),
        "db2" => array(
            "dbname" => "database2",
            "username" => "dbUser",
            "password" => "pa$$",
            "host" => "localhost"
        )
    ),
    "urls" => array(
        "baseUrl" => "http://example.com"
    ),
    "paths" => array(
    )
);

/*
    Error reporting.
*/
ini_set("error_reporting", "true");
error_reporting(E_ALL|E_STRCT);