def Command_cleanup(command_result_2):
    for i in len(command_result_2):
        try:
            command_result_2.remove(" ")
        except ValueError:
            pass

        try:
            command_result_2.remove(".")
        except ValueError:
            pass

        try:
            command_result_2.remove(",")
        except ValueError:
            pass

        try:
            command_result_2.remove("?")
        except ValueError:
            pass

        try:
            command_result_2.remove("~")
        except ValueError:
            pass

        try:
            command_result_2.remove("/")
        except ValueError:
            pass

    return command_result_2