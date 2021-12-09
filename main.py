import os
import glob
from db.models import ins_file, check_file, get_file_to_send
from resources.logger import logger
from resources.mail import send_message


if __name__ == "__main__":
    try:
        os.chdir("C:/GIT/uploading_files_to_mail/uploading_files_to_mail/db/")
        files = glob.glob("*.py")

        for row in files:
            if check_file(row) is None:
                ins_file(row)
            else:
                logger.info("Файл вже наявний в БД: " + str(row))

        file_send = get_file_to_send()
        for i in file_send:
            print("Файл на відправку: ")
            print(i['file_name'])
            send_message("TEST")    #i['file_name'])
    except ValueError as err:
        logger.error("[main.py] - ValueError: " + str(err))
    except TypeError as err:
        logger.error("[main.py] - TypeError: " + str(err))
    except Exception as err:
        logger.error("[main.py] - Exception: " + str(err))
