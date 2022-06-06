import logging

logging.basicConfig(filename="del.log", format="%(asctime)s %(message)s", filemode="w")
dlog = logging.getLogger()
dlog.setLevel(logging.DEBUG)


def replace(file, str_1, str_2):
    """
    :param file: file name
    :param str_1: Original string which is to be replaced
    :param str_2: string which will be replaced with str_1
    :return: 1 for success and 0 for error
    """
    try:
        file_name = open(file, "rt")
        dlog.debug(f"Successfully opened {file}")
        data = file_name.read()
        data = data.replace(str_1, str_2)
        file_name.close()
        file_name = open("file.txt", "wt")
        file_name.write(data)
        dlog.debug(f"replaced {str_1} with {str_2}")
        file_name.close()
        dlog.debug(f"Closed opened file")
        dlog.debug("1")
    except Exception as e:
        dlog.debug(e)
        dlog.debug(0)


replace(file="file.txt", str_1="placement", str_2="screening")
