import logging
import os

log = logging.getLogger('client')

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(message)s ")

# Подготовка имени файла для логирования
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'app_client.log')

file_handler = logging.FileHandler(path, encoding='utf-8')
file_handler.setFormatter(formatter)

log.addHandler(file_handler)
log.setLevel(logging.DEBUG)

if __name__ == '__main__':
    log.info('Информационное сообщение')
