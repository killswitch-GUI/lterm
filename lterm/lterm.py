#!/usr/bin/env python

import os
import sys
import argparse
import shutil
import platform


class cli(object):

    """
    cli parser object for commands
    """

    def __init__(self, test_cmd=''):

        """
        populates init, builds cli command object
        """
        self.test_cmd = test_cmd
        self.args = self.cli_parser()
        

    def cli_parser(self):

        """
        cli parser using argparse
        """
        parser = argparse.ArgumentParser(add_help=False, description='''
            lterm is utility to log all bash windows opened by any user on the system.\n
            This offten is useful for data logging on critical systems.\n
            ''')
        parser.add_argument(
            "-i", action="store_true", help="Install logging")
        parser.add_argument(
            '-l', metavar="/root/test/", help='Logging location (full path)')
        parser.add_argument(
            '-r', action="store_true", help='Remove Logging and restore to intial state, \
            this will attempt to use the backup file created from -b')
        parser.add_argument(
            '-v', action="store_true", help='Set verbose output')
        parser.add_argument(
            '-b', action="store_true", help='Backup RC file during install')
        parser.add_argument('-h', '-?', '--h', '-help',
                            '--help', action="store_true", help=argparse.SUPPRESS)
        if not self.test_cmd:
            args = parser.parse_args()
        else:
            args = parser.parse_args(self.test_cmd.split())

        if args.h:
            parser.print_help()
            sys.exit()

        return args

class lterm(cli):

    """
    main lterm class for entry
    """

    RC = {  'DEBIAN' : '/etc/bash.bashrc',
            'UBUNTU' : '/etc/bash.bashrc',
            'DEFAULT' : '/etc/bash.bashrc'
    }

    RC_BACKUP = '.bak'
    DIR_PERM = 0733

    INSTALL_SCRIPT  = """test "$(ps -ocommand= -p $PPID | awk '{print $1}')" == 'script' || (script -f """ 
    INSTALL_SCRIPT2 = """.lterm/$(date +"%d-%b-%y_%H-%M-%S")_shell.log)\n"""

    def __init__(self, test_cmd=''):

        """
        populates init for main lterm class
        """
        cli.__init__(self, test_cmd)      # init the class
        self.verbose = self.args.v
        self.os = self._check_os()   # check current OS for proper RC file

    def execute(self):

        """
        main start point of execution
        """
        if self.args.i:
            if not self.args.l:
                print "[*] Please use (-l) and a path.."
                return
            self._install_rc()
        if self.args.r:
            if self.verbose:
                print "[*] Attempting to unistall RC script.."
                self._remove_rc()
            return
        return

    def _remove_rc(self):

        """
        uninstall rc script
        """
        b = self.RC[self.os] + self.RC_BACKUP
        if os.path.isfile(b):
            if self.verbose:
                print "[*] Backupfile detected, using this to restore"
            if not self._check_install():
                print "[*] Failed to find rc logging script installed.. now quiting"
            shutil.copy(b, self.RC[self.os])
        else:
            if self.verbose:
                print "[*] Backupfile not detected, using first line to restore"
            with open(self.RC[self.os], "r") as f:
                old = f.readlines()
            if not self._check_install():
                print "[*] Failed to find rc logging script installed.. now quiting"
                return
            with open(self.RC[self.os], "w") as f:
                old = f.writelines(old[1:])
        print "[*] Logging RC script removed."

    def _install_rc(self):

        """
        install rc script
        """
        if self._check_install():
            print "[*] RC script seems to be installed already... quiting!"
            return
        with open(self.RC[self.os], "r") as f:
            old = f.read()
        if self.args.b:
            self._backup_rc(old)
        script = ""
        script += self.INSTALL_SCRIPT
        script += str(self.args.l)
        script += self.INSTALL_SCRIPT2
        if self.verbose:
            print "[*] Installing bash RC hook: %s" % script
        with open(self.RC[self.os], "w") as f:
            f.write(script + old)
        if self.verbose:
            print "[*] Hook installed"
        dr = self.args.l + '.lterm'
        if not os.path.isdir(dr):
            os.mkdir(dr)
            os.chmod(dr, self.DIR_PERM)
            if self.verbose:
                print "[*] Logging director built: %s" % dr
        self._print_install()

    def _print_install(self):
        p = "\nlterm has installed a logging hook for all spawned bash terminals:"
        p += "\n\t* RC Logging script installed!"
        p += "\n\t* Bash RC Location: %s" % self.RC[self.os]
        if self.args.b:
            back = self.RC[self.os] + self.RC_BACKUP
            p += "\n\t* Bash RC Backupfile: %s" % back
        dr = self.args.l + '.lterm'
        p += "\n\t* Logging log location: %s" % dr
        print p


    def _backup_rc(self, data):

        """
        backup rc file
        """
        back = self.RC[self.os] + self.RC_BACKUP
        with open(back, "w") as f:
            f.write(data)
        if self.verbose:
            print "[*] Backupfile created: %s" % back

    def _check_install(self):

        """
        check if logging is already installed
        """
        with open(self.RC[self.os], "r") as f:
            line = f.readline()
        if self.INSTALL_SCRIPT in line:
            if self.verbose:
                print "[*] Logging script already in RC!"
            return True
        if self.verbose:
            print "[*] No logging rc script found"
        return False


    def _check_os(self):

        """
        check all platorm info
        """
        os = platform.platform()
        if 'debian' in os:
            if self.verbose:
                print "[*] Checking os found: 'DEBIAN'"
            return 'DEBIAN'
        if 'ubuntu' in os:
            return 'UBUNTU'
        else:
            return 'DEFAULT'


def main():
    l = lterm()
    l.execute()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)