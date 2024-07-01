# make changes to our configuration files

exec { "add_identityfile_to_ssh_config":
  command => "echo 'IdentityFile ~/.ssh/school >> /etc/ssh/ssh_config'",
  provider => shell,
}

exec { "turn_off_password_authentication":
  command => "sed -i 's/^# *PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/ssh_config",
  provider => shell,
}

