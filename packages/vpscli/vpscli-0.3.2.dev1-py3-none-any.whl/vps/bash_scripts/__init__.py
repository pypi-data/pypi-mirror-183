UTILS = '''
#!/usr/bin/env bash

LOG_FILE=/tmp/bashfast.log
LOG_FILE_SIZE=$(( 1024 * 1024 * 10 ))
LOG_FILE_NUMBER=10

date_format() {
    if [[ $OSTYPE =~ "darwin" ]]; then
        gdate +"[%Y-%m-%d %T.%3N]"
    else
        date +"[%Y-%m-%d %T.%3N]"
    fi
}

log::rotate() {
    if [ -f "$LOG_FILE" ]; then
        if [ ! -w "$LOG_FILE" ]; then
            n=$(random::randint 10)
            LOG_FILE="/tmp/bashfast$n.log"
            touch "$LOG_FILE"
            echo "Log file is not writable, create new log file: $LOG_FILE"
        fi

        if [ "$(wc -c < "$LOG_FILE")" -gt "$LOG_FILE_SIZE" ]; then
            local i=1
            while [ -f "$LOG_FILE.$i" ]; do
                i=$((i+1)) 
            done
            for (( j=i; j>0; j-- )); do
                if [ $j -ge $((LOG_FILE_NUMBER-1)) ]; then
                    rm -f "$LOG_FILE.$j"
                fi
                if [ -f "$LOG_FILE.$j" ]; then
                    mv "$LOG_FILE.$j" "$LOG_FILE.$((j+1))"
                fi
            done
            mv "$LOG_FILE" "$LOG_FILE.1"
            echo "$(date_format) Rotated log file $LOG_FILE to $LOG_FILE.1" >> "$LOG_FILE"
        fi
    else 
        touch "$LOG_FILE"
    fi
}

log::print() {
    level=$1
    color=$2
    log::rotate
    df=$(date_format)
    lv="[$level]"
    cl=$(cecho $color "${@:3}\n")
    echo $df $lv $cl |tee -a $LOG_FILE
}

log::debug() {
    log::print "DEBUG" GRAY "$@"
}

log::info() {
    log::print "INFO" CYAN "$@"
}

log::error() {
    log::print "ERROR" LRED "$@"
}

log::warn() {
    log::print "WARN" LYELLOW "$@"
}

cecho() {
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[0;33m'
    BLUE='\033[0;34m'
    MAGENTA='\033[0;35m'
    CYAN='\033[0;36m'
    LIGHTGRAY='\033[0;37m'
    GRAY='\033[1;90m'
    LRED='\033[1;91m'
    LGREEN='\033[1;92m'
    LYELLOW='\033[1;93m'
    LBLUE='\033[1;94m'
    LMAGENTA='\033[1;95m'
    LCYAN='\033[1;96m'
    NC='\033[0m' # No Color
    printf "${!1}${2}${NC}"
}

int(){ printf '%d' ${1:-} 2>/dev/null || :; }

random::randint() {
    arg=10
    if [[ "$#" -ge 0 ]]; then arg=$1; fi
    range=$(date +%s%N | cut -b10-19)
    range=$(int $range)
    echo $(( $range % $arg ))
}

yield::bool() {
    # return true if $1 is not empty or false otherwise
    if [ -z $1 ]; then
        echo false
    else
        echo true
    fi
}

check_socks5 () { 
    # check whether socks5 is valid or not
    yield::bool $(timeout 10 curl -s --socks5 localhost:$1 ipinfo.io)
}
'''

WARP = '''
#!/usr/bin/env bash

. /app/utils.sh

cter=0
for i in `seq 3`; do 
    if [[ $(check_socks5 23333) == true ]]; then
        echo "okay"
    else
        ((cter++))
        sleep 3
    fi 
done 

if [[ $cter -eq 3 ]]; then
    log::warn "warp-cli failed."
    warp-cli disconnect
    warp-cli connect
else
    log::info "warp-cli still VALID"
fi 
'''

PROMPT = r'''
export LS_OPTIONS='--color=auto'
eval "`dircolors`"
alias ls='ls $LS_OPTIONS'
alias ll='ls $LS_OPTIONS -l'
alias l='ls $LS_OPTIONS -lA'

PS1="\[\e[32m\][\[\e[m\]\[\e[95m\]\u\[\e[m\]\[\e[34m\]@\[\e[m\]\[\e[32m\]\h\[\e[m\]:\[\e[36m\]\w\[\e[m\]\[\e[32m\]]\[\e[m\]\[\e[32;47m\]\\$\[\e[m\]"
'''

VIM_CONFIG = '''
syntax on
set nu
set ai
set tabstop=4
set ls=2
set autoindent
'''

EMACS_CONFIG = '''
(setq frame-background-mode 'dark)
(global-display-line-numbers-mode)
(add-hook 'text-mode-hook 'auto-fill-mode)
'''

SAR_PERL = '''
#!/usr/bin/env perl

my $CONFIG_STR =
  '# Default settings for /etc/init.d/sysstat, /etc/cron.d/sysstat
# and /etc/cron.daily/sysstat files
#

# Should sadc collect system activity informations? Valid values
# are "true" and "false". Please do not put other values, they
# will be overwritten by debconf!
ENABLED="true"
';

my $FILE = '/etc/default/sysstat';
open my $fh, '>', $FILE or die "Can't open $FILE: $!";
print $fh $CONFIG_STR;
close $fh;

print "enable sysstat [OK]\n";

# ---------------------------------------------------------------------
$CONFIG_STR = '
# The first element of the path is a directory where the debian-sa1
# script is located
PATH=/usr/lib/sysstat:/usr/sbin:/usr/sbin:/usr/bin:/sbin:/bin

# Activity reports every 10 minutes everyday
* * * * * root command -v debian-sa1 > /dev/null && debian-sa1 20 3

# Additional run at 23:59 to rotate the statistics file
59 23 * * * root command -v debian-sa1 > /dev/null && debian-sa1 60 2
';

$FILE = '/etc/cron.d/sysstat';
open $fh, '>', $FILE or die "Can't open $FILE: $!";
print $fh $CONFIG_STR;
close $fh;

print "setting report frequency [OK] \n";

# ---------------------------------------------------------------------
$FILE       = '/etc/sysstat/sysstat';
$CONFIG_STR = '# sysstat configuration file. See sysstat(5) manual page.

# How long to keep log files (in days).
# Used by sa2(8) script
# If value is greater than 28, then use sadc\'s option -D to prevent older
# data files from being overwritten. See sadc(8) and sysstat(5) manual pages.
HISTORY=28

# Compress (using xz, gzip or bzip2) sa and sar files older than (in days):
COMPRESSAFTER=10

# Parameters for the system activity data collector (see sadc(8) manual page)
# which are used for the generation of log files.
# By default contains the `-S DISK\' option responsible for generating disk
# statisitcs. Use `-S XALL\' to collect all available statistics.
SADC_OPTIONS="-S DISK"

# Directory where sa and sar files are saved. The directory must exist.
SA_DIR=/var/log/sysstat

# Compression program to use.
ZIP="xz"

# By default sa2 script generates yesterday\'s summary, since the cron job
# usually runs right after midnight. If you want sa2 to generate the summary
# of the same day (for example when cron job runs at 23:53) set this variable.
#YESTERDAY=no

# By default sa2 script generates reports files (the so called sarDD files).
# Set this variable to false to disable reports generation.
#REPORTS=false
';

open $fh, '>', $FILE or die "Can't open $FILE: $!";
print $fh $CONFIG_STR;
close $fh;
print "setting sysstat history [OK] \n";

# ---------------------------------------------------------------------

`systemctl restart sysstat`;
print "restart sysstat [OK] \n";
'''
