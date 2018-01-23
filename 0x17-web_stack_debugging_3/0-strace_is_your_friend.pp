exec { 'test.php':
     command => "sed -i 's/phpp/php/' test.php",
     path => '/bin',
}
