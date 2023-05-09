# Creat a manifest that fix all termintion of phpp.

exec { 'fix-wordpress':
command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
path    => '/usr/local/bin/:/bin/'
}
