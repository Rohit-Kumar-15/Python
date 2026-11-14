#Threading and Multiprocessing
import threading
import multiprocessing
import time

def task(name):
    print(f"{name} started")
    time.sleep(1)
    print(f"{name} finished")

def run_threads():
    print("THREADING")
    threads = [
        threading.Thread(target=task, args=(f"Thread {i}",))
        for i in range(1, 4)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def square(number):
    return number * number

def run_processes():
    print("\nMULTIPROCESSING")
    with multiprocessing.Pool() as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
    print("Squares:", results)

if __name__ == "__main__":
    run_threads()
    run_processes()
