import sys
import os
import getopt

try:
    from .config import config as CONF, paths as PATHS
except ModuleNotFoundError as e:
    pass


def validateCommandLineSwitches():
    """
    Description
        Parses the spherobot command line arguments.
        and Returns command line options and arguments.
        If there is any option or argument is missing,
        Program stops and exist.

    Parameters
        None

    Returns
        options : iterable object that holds command line options and arguments
    """

    # Get the arguments from the command-line except the filename
    argv = sys.argv[1:]

    try:
        # Check if user is asking for help
        # print(argv)
        if len(argv) == 1 and argv[0] == CONF.CLI_SWITCH_HELP:
            options, arguments = getopt.getopt(argv, 'h', ["help"])
            # print("HELP CHECK")
            return options

        # Check if user has entered all the mandatory command line arguments
        # Define the getopt parameters
        options, arguments = getopt.getopt(argv, 'a:n:k:m:f:l:u:p:r:o:b:',
                                           ["app", "flow", "link", "username", "password"])

        # for opt, arg in options:
        #     print(arg)

        return options

    except getopt.GetoptError as e:
        print(e)
        sys.exit(2)  # No need to proceed with test if the test launcher arguments are missing

def parse_cli():
    """
    Parse command line arguments

    :return:
    """

    # Get Command Line Arguments
    cli = sys.argv

    # Proceed or not!!!
    if len(cli) <= 1:
        """Check if any command is present or not"""
        raise Exception("Mandatory command line arguments are missing!")

    # 1. Install Framework Directory Structure and Framework Files
    for index in range(1, len(cli)):
        """Iterate every command line argument"""

        # print(cli[index])

        if cli[index] == "-i" or cli[index]=="--install":
            #install_framework()
            # Wow!!! Installation Complete
            #print("Speedboat installed successfully.")
            pass



    # 2. Download and Install Drivers
    from tools import chrome_version
    print("Installed chrome version: " + chrome_version.get_chrome_version() )

def install_framework():
    """
    Install base nstaff

    :return:
    """

    # Created directory structure
    try:
        import dir_structure as ds
    except ModuleNotFoundError as e:
        from nstaff import dir_structure as ds

    ds.create_dir_structure()

    # Install drivers

def system_command(command):
    """
    Description
        This function executes the given <command>

    Parameters
        command -> str obj : command to execute

    Returns
        status_code - integer status code. 0 means success and any other mean failure.
    """

    try:
        # Execute the given <command>
        status_code = os.system(command)
    except Exception as e:
        print(e)

    # return with status_code.
    return status_code

def install_prerequisites():
    """
    Description
        Check if pre-requisites are installed based on the product under test.
        If any pre-requisite is missing, spherobot prompts user to install
        the prerequisite and stops the test execution.
        If any dependence tool is missing, spherobot auto installs them through
        pip.

    Parameters
        None

    Returns
        None
    """

    # Install dependencies from requirements.txt
    try:
        system_command("pip3 install virtualenv")
        system_command("pip3 install -r requirements.txt")
    except Exception as e:
        #system_command("pip install virtualenv")
        #system_command("pip install -r requirements.txt")
        pass
    finally:
        pass

    system_command("virtualenv venv")

    try:
        system_command("python3 -m virtualenv env")
    except Exception as e:
        system_command("python -m virtualenv env")

    system_command("source venv/bin/activate")



def prepare_test_launcher(options):
    """
    Description
        This function parses the given command line arguments supplied in the <options> parameter
    and prepares the pytest command to trigger the test execution

    Parameters
        options -> iterable object : Holds Spherobot command line arguments

    Returns
        str obj : String representation of pytest command
        Foe example:
            pytest --reruns 2 --reruns-delay 1  -s -v  -n 1 -k hqp  --url=https://staging.v2.spherewms.com --username=erpanchdev@gmail.com --password=Passw0rd$ tests/v2
    """

    # Add support for re-running a test if it fails,
    # because sometimes a test fails with many other unknown reasons
    # That are not actual test failures
    # test_launcher = "pytest --reruns 2 --only-rerun AssertionError --reruns-delay 1 "
    test_launcher = "pytest "

    # add -s and -v (increase verbosity) switch
    test_launcher += " -s -v "

    # add support for test results in xml format
    test_launcher += " --junitxml=" + PATHS.TEST_OUTPUT_DIR + "/result.xml "

    # application under test
    app_test_dir = None

    # boolean variable to check if -a switch is provided
    is_app_switch_found = False

    # boolean variable to check if -l switch is provided
    is_link_switch_found = False

    # boolean variable to check if -m switch is provided
    marker_switch_found = False

    # boolean variable to check if -u switch is provided
    is_username_switch_found = False

    # boolean variable to check if -p switch is provided
    is_password_switch_found = False

    # boolean variable to check if -r switch is provided
    is_rerun_switch_found = False

    # command builder
    command = "speedboat.py "

    # set browser = chrome always by default
    # in future, we will support more browsers,
    # and then, we probably support a new switch -b for the same.
    # but for now, make it always set to chrome
    update_report_configuration_yaml_file(field_constants.REPORT_BROWSER, config_spherobot.BROWSER_CHROME)

    # set default name to ""
    update_report_configuration_yaml_file(field_constants.NAME, constants.EMPTY)

    for opt, arg in options:
        """
        Iterate through command line options and arguments
        """

        command += opt + constants.SPACE + arg + constants.SPACE

        if opt == '-h':
            """if option is -h"""

            # print the spherobot help text
            print(colored("{0}".format(_help.SPHEROBOT_LAUNCHER_HELP), color_info))

            # sleep for 2 seconds
            sleep_time_after_each_spherobot_action(config_spherobot.SLEEP_TIME)

            # stop spherobot and return to console
            sys.exit(3)

        elif opt == config_spherobot.CLI_SWITCH_APP:
            """If option is -a"""

            # save that app switch is found
            is_app_switch_found = True

            # get the application under test information from the argument
            app_under_test = arg.upper()

            # set global wait for V3 app
            if arg.upper() == apps.V3:
                config_v2.wait = 30

            # print user message
            print(colored("Application under test is {0}".format(app_under_test),
                          color_info))

            runtime_test_configuration.APP_UNDER_TEST = arg.upper
            app_test_dir = update_runtime_and_report_configurations_based_on_apps_selection(arg.lower())

        elif opt == config_spherobot.CLI_SWITCH_KEY:
            """If option is -k"""

            # add the -k switch to test launcher command
            test_launcher += constants.SPACE + opt + constants.SPACE + arg + constants.SPACE

        elif opt == config_spherobot.CLI_SWITCH_MARKER:
            """If option is -m"""

            # add the -m switch to test launcher command
            test_launcher += constants.SPACE + opt + constants.SPACE + arg + constants.SPACE

            # update report configuration
            update_report_configuration_yaml_file(field_constants.REPORT_MARKER, arg.lower())

            # marker switch found
            marker_switch_found = True

        elif opt == config_spherobot.CLI_SWITCH_LINK:
            """If option is -l"""

            # link switch found
            is_link_switch_found = True

            # update report configuration
            update_report_configuration_yaml_file(field_constants.APP_LINK, arg)

            # update oms report configuration

            oms_link = arg.replace(constants.DOT + apps.V2.lower() + constants.DOT,
                                   constants.DOT + config_spherobot.TARGET_OMS + constants.DOT)
            update_report_configuration_yaml_file(field_constants.OMS_LINK, oms_link)

            # update run time test configuration with the actual application url
            runtime_test_configuration.APP_LINK = arg

            # update run time test configuration with the actual application url
            runtime_test_configuration.OMS_LINK = oms_link

            # add the --url switch to test launcher command
            test_launcher += constants.SPACE + "--app_link=" + arg

        elif opt == config_spherobot.CLI_SWITCH_USERNAME:
            """If option is -u"""

            # username switch found
            is_username_switch_found = True

            # add the --username switch to test launcher command
            test_launcher += constants.SPACE + "--username=" + arg

            # update run time test configuration with the actual username
            runtime_test_configuration.USERNAME = arg

            # set username in report configuration too
            update_report_configuration_yaml_file(field_constants.USERNAME, arg)

        elif opt == config_spherobot.CLI_SWITCH_PASSWORD:
            """If option is -p"""

            # password switch found
            is_password_switch_found = True

            # add the --password switch to test launcher command
            test_launcher += constants.SPACE + "--password=" + arg

            # update report configuration
            update_report_configuration_yaml_file(field_constants.PASSWORD, arg)

            # update run time test configuration with the actual username
            runtime_test_configuration.PASSWORD = arg

        elif opt == config_spherobot.CLI_SWITCH_RERUN:

            # rerun switch found
            is_rerun_switch_found = True

            # get random sleep time
            random_sleep_time = random.randint(4, 10)

            # add --rerun switch
            test_launcher += constants.SPACE + " --reruns " + str(arg) \
                             + " --reruns-delay " + str(random_sleep_time) + constants.SPACE
        elif opt == '-o':

            # get random sleep time
            random_sleep_time = random.randint(4, 10)

            if int(arg) not in [0, 1]:
                print(colored("-o switch supports only two values, 1 and 0, whereas 1 = True and 0 = False."
                              .format(config_spherobot.CLI_SWITCH_APP), color_error))
                # exit the spherobot program
                sys.exit(1)
            else:
                print(colored("-o switch {}".format(arg), color_success))

            config_v2.PICK_OVER_COMMIT = arg

            runtime_test_configuration.PASSWORD = arg

            print(colored("PICK OVER COMMIT SETTING: {}".format(config_v2.PICK_OVER_COMMIT), color_success))

            # sys.exit(1)
        elif opt == '-n':

            if int(arg) > 1:
                runtime_test_configuration.PARALLEL_RUN = True

            test_launcher += constants.SPACE + opt + constants.SPACE + arg

        else:
            """else """

            # add the opt switch and arg to test launcher command
            test_launcher += constants.SPACE + opt + constants.SPACE + arg

    # inform user and exit if app switch is not provided
    if not is_app_switch_found:
        """if app switch is not found"""
        print(colored(errors.MANDATORY_SWITCH_IS_MISSING.format(config_spherobot.CLI_SWITCH_APP), color_error))
        # exit the spherobot program
        sys.exit(1)
    elif not is_link_switch_found:
        """if link switch is not found"""
        print(colored(errors.MANDATORY_SWITCH_IS_MISSING.format(config_spherobot.CLI_SWITCH_LINK), color_error))
        # exit the spherobot program
        sys.exit(1)
    elif not is_username_switch_found:
        """if username switch is not found"""
        print(colored(errors.MANDATORY_SWITCH_IS_MISSING.format(config_spherobot.CLI_SWITCH_USERNAME), color_error))
        # exit the spherobot program
        sys.exit(1)
    elif not is_password_switch_found:
        """if password switch is not found"""
        print(colored(errors.MANDATORY_SWITCH_IS_MISSING.format(config_spherobot.CLI_SWITCH_PASSWORD), color_error))
        # exit the spherobot program
        sys.exit(1)
    elif not is_rerun_switch_found:
        """if rerun switch is not found"""

        # get random sleep time
        random_sleep_time = random.randint(4, 10)

        # Add support for re-running a test if it fails,
        # because sometimes a test fails with many other unknown reasons
        # That are not actual test failures
        # Thus, add --rerun switch
        test_launcher += " --reruns 1 --reruns-delay " + str(random_sleep_time) + constants.SPACE

    # add the correct test directory to test launcher command
    test_launcher += constants.SPACE + app_test_dir

    if not is_link_switch_found:
        """if Link switch is not provided"""

        # read credentials yaml file to get app link information
        credentials_yaml_file = Common.read_yaml(paths.CREDENTIALS_YAML_FILE)

        # update report configuration
        update_report_configuration_yaml_file(field_constants.APP_LINK, credentials_yaml_file[field_constants.APP_LINK])

        # update oms report configuration
        update_report_configuration_yaml_file(field_constants.OMS_LINK,
                                              credentials_yaml_file[field_constants.APP_LINK].replace(
                                                  constants.DOT + apps.V2.lower() + constants.DOT,
                                                  constants.DOT + config_spherobot.TARGET_OMS + constants.DOT
                                              ))

    if not marker_switch_found:
        """if marker switch is not found"""

        # update report configuration
        update_report_configuration_yaml_file(field_constants.REPORT_MARKER, markers.NOMARKERS)

    # add report configuration - screenshot directory
    update_report_configuration_yaml_file(field_constants.REPORT_SCREENSHOT_DIRECTORY, paths.TEST_OUTPUT_SCREENSHOT_DIR)

    # add report configuration - screenshot directory
    update_report_configuration_yaml_file(field_constants.REPORT_SCREENSHOT_DIRECTORY_WITH_SLASH,
                                          paths.TEST_OUTPUT_SCREENSHOT_DIR_WITH_SLASH)

    # add report configuration - screenshot relative directory
    update_report_configuration_yaml_file(field_constants.REPORT_SCREENSHOT_RELATIVE_DIRECTORY,
                                          constants.DOT + constants.FORWARD_SLASH + paths.TEST_SCREENSHOT_DIR)

    # add report configuration - test_output directory path
    update_report_configuration_yaml_file(field_constants.REPORT_TEST_OUTPUT_DIRECTORY_PATH_WITH_SLASH,
                                          paths.TEST_OUTPUT_DIR_WITH_SLASH)

    # inform user of received of command line arguments
    print(colored("Received the following command line request: {0}".format(command), color_info))

    # pause execution for 2 seconds
    sleep_time_after_each_spherobot_action(config_spherobot.SLEEP_TIME)

    print(colored("Preparing test launcher...", color_info))
    sleep_time_after_each_spherobot_action(config_spherobot.SLEEP_TIME)

    # Update application test configuration file
    update_app_test_configurations()

    # check internet speed test
    """
    host_internet_speed = Common.download_speed()
    config_v2.internet_speed = host_internet_speed

    if host_internet_speed >= 100:
        config_v2.wait = 30
    elif host_internet_speed >= 5:
        config_v2.wait = 90
    else:
        # no change
        pass
    """

    # update old max wait time
    config_v2.old_wait = config_v2.wait

    # update report configuration
    update_report_configuration_yaml_file(field_constants.INTERNET_SPEED, config_v2.internet_speed)
    print(colored("\nHost internet speed: {0} Mbps\n".format(config_v2.internet_speed), color_info))

    # return actual pytest test-launcher command to the caller
    return test_launcher  # + " -vv --order-scope=module"