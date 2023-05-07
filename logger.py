from datetime import datetime


class Logger:
    def __init__(self, log_path: str) -> None:
        self.log_file = open(log_path, "w")

    def log(self, message: str) -> None:
        datetime_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        message = datetime_str + " " + message
        print(message)
        try:
            self.log_file.write(message + "\n")
            self.log_file.flush()
        except:
            print ("could not write to log file")

    def __del__(self):
        self.log_file.close()
