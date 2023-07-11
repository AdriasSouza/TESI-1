import threading
import time


# Função que será executada em uma thread
def minha_thread(nome):
    for i in range(5):
        print(f'Olá, sou a thread {nome}!')
        time.sleep(1)


# Criação e execução das threads
thread1 = threading.Thread(target=minha_thread, args=('Thread 1',))
thread2 = threading.Thread(target=minha_thread, args=('Thread 2',))

thread1.start()
thread2.start()

# Espera até que as threads terminem a execução
thread1.join()
thread2.join()

print('Programa finalizado.')
