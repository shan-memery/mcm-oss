"""
Khinshan Khan - __main__.py.

This module is the  heart and entry-point of the mcm-oss program.
"""
from mcm_oss import cli
from mcm_oss import oss


def main():
    """Execute helpful information about program and then start interactive cli."""
    print('''
Welcome to mcm-oss: A simple and basic operating system simulation.

Some commands implemented:
  A  size    creates a new common process
  AR size    the same as 'A #size' but the new process is an RT-process
  Q          ends the time slice for the currently running process
  t          terminates the currently running process
  d  number  process that currently uses the CPU requests the hard disk #number
  D  number  hard disk #number finishes the work for one process
  S  r       shows state of the process queue
  S  i       shows state of the disks
  S  m       shows state of the memory

The way this cli utility handles signals:
    SIGINT  -  ^C  -  Ctrl+c  -  exits current command
    EOF     -  ^D  -  Ctrl+d  -  exits program
    ''')
    ram_size, disks_max = cli.initialize()
    # TODO: add more initialization settings
    print("Initialized simulation. You may now begin interacting with it.")
    with oss.OSS(ram_size, disks_max) as OSS:
        while True:
            context, arguments = cli.interactive()
            if not context:
                print(f'mcm-oss: {arguments}: command not found')
            else:
                print(context, arguments)
                if(context == 'S'):
                    OSS.show(arguments)


if __name__ == '__main__':
    main()
