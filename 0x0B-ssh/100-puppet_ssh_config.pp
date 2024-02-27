#!/usr/bin/env bash
#setting up a client SSH configuration to connect to a server without typing a password.
# Define SSH client configuration
file { '/etc/ssh/ssh_config':
  ensure => file,
}

# Configure SSH client to use private key ~/.ssh/school
file_line { 'SSH Private Key':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#?IdentityFile\s.*$',
}

# Configure SSH client to refuse password authentication
file_line { 'ssh_password_authentication':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^#?PasswordAuthentication\s.*$',
}
