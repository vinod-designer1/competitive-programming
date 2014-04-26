<?php
namespace Database;

class Database
{
	public function __construct()
    {
        $this->adapter = new MySqlAdapter;
    }
}