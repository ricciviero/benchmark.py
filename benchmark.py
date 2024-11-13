import time
import numpy as np
import psutil
import platform
import threading

def cpu_stress_test(max_duration=15):
    def cpu_intensive_task():
        total = 0
        start_time = time.time()
        while time.time() - start_time < max_duration:
            for i in range(100_000):  # Ridotta complessità
                total += i ** 2 + i ** 0.5 - i ** 0.3
        print(f"Task completato: risultato parziale = {total}")

    print("Esecuzione dello stress test della CPU (limitato a 15 secondi)...")
    threads = []
    for _ in range(4):  # Ridotto a 4 thread per limitare la durata
        thread = threading.Thread(target=cpu_intensive_task)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print("Stress test della CPU completato.\n")

def memory_stress_test(max_duration=15):
    print("Esecuzione dello stress test della RAM (limitato a 15 secondi)...")
    start_time = time.time()
    arrays = []
    try:
        while time.time() - start_time < max_duration:
            arr = np.random.random(size=(100_000_000,))  # Ridotta la dimensione dell'array
            arrays.append(arr)
            print(f"Array creato, utilizzo RAM: {psutil.virtual_memory().used / (1024 ** 3):.2f} GB")
    except MemoryError:
        print("Memoria esaurita durante lo stress test della RAM.")
    finally:
        del arrays
        print("Stress test della RAM completato.\n")

def system_info():
    print("Informazioni di sistema:")
    print(f"Sistema operativo: {platform.system()} {platform.release()}")
    print(f"Processore: {platform.processor()}")
    print(f"Memoria totale: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB\n")

def main():
    print("== STRESS TEST TOOL ==")
    system_info()
    cpu_stress_test(max_duration=15)
    memory_stress_test(max_duration=15)
    print("Stress test completato.")

if __name__ == "__main__":
    main()