import logging

# ANSI cores
COLORS = {
    "ADD-1": "\033[91m",  # vermelho
    "ADD-2": "\033[92m",  # verde
    "POP-1": "\033[94m",  # azul
    "POP-2": "\033[93m",  # amarelo
    "BUSCA": "\033[1;35m",  # magenta
}
RESET = "\033[0m"

class ColorFormatter(logging.Formatter):
    def format(self, record):
        color = COLORS.get(record.threadName, "")
        record.msg = f"{color}{record.msg}{RESET}"
        return super().format(record)

def Logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setFormatter(ColorFormatter("[%(threadName)s] %(asctime)s %(message)s"))
    logger.handlers = [handler]
    
    return logger