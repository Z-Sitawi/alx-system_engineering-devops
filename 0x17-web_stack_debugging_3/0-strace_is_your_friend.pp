# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.
exec { 'fix wordpress':
  command     => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
