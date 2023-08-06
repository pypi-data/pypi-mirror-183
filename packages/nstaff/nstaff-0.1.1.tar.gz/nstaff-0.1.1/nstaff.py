# Namastey world _/\_
# ===================
#
# This is "Birbal".
# A bot designed and developed at NamasteyDigitalIndia.com,
# That helps software companies and software teams in automating various testing tasks.
#
# This file is the entry point of the "Birbal Automation Framework", BAF.
# speedboat.py is the command line utility to install, debug and run your automation tests-backup.
#
# Author: Panchdev Singh Chauhan
# Email: erpanchdev@gmail.com

import sys

color_info = 'magenta'
color_info_on = 'on_blue'
color_error = 'red'
color_error_on = color_info_on
color_success = 'green'
color_attribute = ['concealed']

def namastey_world(my_name=None):
    """
    Print the greeting message!

    :param my_name:
    :return:
    """

    greeting = "_/\_ Namastey "
    greeting += "World! " if my_name is None else my_name + "! "
    greeting += 'I am "Birbal".'
    print(greeting)



if __name__ == '__main__':
    """
    Entry point of the nstaff.
    """

    namastey_world()  # :)

    from nstaff import installer

    #print(sys.argv)

    # Install Pre-requisites
    installer.install_prerequisites()

    installer.install_framework()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
