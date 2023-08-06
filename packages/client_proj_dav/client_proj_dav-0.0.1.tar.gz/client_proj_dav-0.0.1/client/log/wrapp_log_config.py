import logging
import os

log_wrapp_server = logging.getLogger('wrapp_server')
log_wrapp_client = logging.getLogger('wrapp_client')

forma = logging.Formatter('%(asctime)-10s %(message)s')

# Подготовка имени файла для логирования
path1 = os.path.dirname(os.path.abspath(__file__))
path1 = os.path.join(path1, 'wrapper_server.log')

path2 = os.path.dirname(os.path.abspath(__file__))
path2 = os.path.join(path2, 'wrapper_client.log')

handler_file_server = logging.FileHandler(path1, encoding='utf-8')
handler_file_client = logging.FileHandler(path2, encoding='utf-8')

handler_file_server.setFormatter(forma)
handler_file_client.setFormatter(forma)

log_wrapp_server.addHandler(handler_file_server)
log_wrapp_client.addHandler(handler_file_client)

log_wrapp_server.setLevel(logging.DEBUG)
log_wrapp_client.setLevel(logging.DEBUG)

if __name__ == '__main__':
    log_wrapp_server.info('Информационное сообщение')
    log_wrapp_client.info('Информационное сообщение')
