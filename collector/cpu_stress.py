# cpu_stress.py
import multiprocessing

def cpu_load():
    while True:
        pass  # Keep CPU busy

if __name__ == "__main__":
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=cpu_load)
        p.start()
        processes.append(p)
