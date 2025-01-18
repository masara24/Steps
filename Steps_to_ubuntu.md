
deb http://old-releases.ubuntu.com/ubuntu/ precise main restricted
deb-src http://old-releases.ubuntu.com/ubuntu/ precise main restricted
deb http://old-releases.ubuntu.com/ubuntu/ precise-updates main restricted
deb-src http://old-releases.ubuntu.com/ubuntu/ precise-updates main restricted

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
## team. Also, please note that software in universe WILL NOT receive any
## review or updates from the Ubuntu security team.
deb http://old-releases.ubuntu.com/ubuntu/ precise universe
deb-src http://old-releases.ubuntu.com/ubuntu/ precise universe
deb http://old-releases.ubuntu.com/ubuntu/ precise-updates universe
deb-src http://old-releases.ubuntu.com/ubuntu/ precise-updates universe

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu 
## team, and may not be under a free licence. Please satisfy yourself as to 
## your rights to use the software. Also, please note that software in 
## multiverse WILL NOT receive any review or updates from the Ubuntu
## security team.
deb http://old-releases.ubuntu.com/ubuntu/ precise multiverse
deb-src http://old-releases.ubuntu.com/ubuntu/ precise multiverse
deb http://old-releases.ubuntu.com/ubuntu/ precise-updates multiverse
deb-src http://old-releases.ubuntu.com/ubuntu/ precise-updates multiverse

## N.B. software from this repository may not have been tested as
## extensively as that contained in the main release, although it includes
## newer versions of some applications which may provide useful features.
## Also, please note that software in backports WILL NOT receive any review
## or updates from the Ubuntu security team.
deb http://old-releases.ubuntu.com/ubuntu/ precise-backports main restricted universe multiverse
deb-src http://old-releases.ubuntu.com/ubuntu/ precise-backports main restricted universe multiverse

deb http://security.ubuntu.com/ubuntu precise-security main restricted
deb-src http://security.ubuntu.com/ubuntu precise-security main restricted
deb http://security.ubuntu.com/ubuntu precise-security universe
deb-src http://security.ubuntu.com/ubuntu precise-security universe
deb http://security.ubuntu.com/ubuntu precise-security multiverse
deb-src http://security.ubuntu.com/ubuntu precise-security multiverse

## Uncomment the following two lines to add software from Canonical's
## 'partner' repository.
## This software is not part of Ubuntu, but is offered by Canonical and the
## respective vendors as a service to Ubuntu users.
# deb http://archive.canonical.com/ubuntu precise partner
# deb-src http://archive.canonical.com/ubuntu precise partner

## This software is not part of Ubuntu, but is offered by third-party
## developers who want to ship their latest software.
deb http://extras.ubuntu.com/ubuntu precise main
deb-src http://extras.ubuntu.com/ubuntu precise main



# windows
# git clone https://github.com/masara24/Steps.git
# git clone https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git

# ubuntu
# lsb_release -a

# apt-get update
# apt-get upgrade
# apt-get install 
# apt-get install openssh-server
# ps -e | grep ssh

# apt-get build-essential