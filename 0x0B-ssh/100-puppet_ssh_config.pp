#connect to server without a password
file_line { 'no password':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => '    PasswordAuthentication no',
}
file_line { 'change private key':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => '    IdentityFile ~/.ssh/school'
}
