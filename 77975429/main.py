import multiprocessing
from multiprocessing import Process, Queue, Manager
from fastapi import FastAPI

CLIENT_CORES = 5
DB_PROCS = 2
connection = "mongo_connection_string"

app = FastAPI()


def start_lifespan_resources():
    manager = Manager()

    global dbWorkers
    global clientWorkers
    global clientQueue
    global clientResponse

    dbQueue = Queue()
    clientQueue = Queue()
    clientResponse = manager.dict()
    psetObjects = manager.dict()
    dbWorkers = []
    clientWorkers = []

    config_processes(dbQueue, clientQueue, clientResponse, psetObjects)


def stop_lifespan_resources():
    for worker in dbWorkers + clientWorkers:
        worker.terminate()
        worker.join()

    print("All workers terminated.")


def config_processes(dbQueue, clientQueue, clientResponse, psetObjects):
    start_db_workers(dbQueue, psetObjects)
    start_client_workers(clientQueue, psetObjects, dbQueue, clientResponse)


def start_db_workers(dbQueue, psetObjects):
    print("Building db Workers")
    for p in range(DB_PROCS):
        dbworker = Process(target=db_worker, args=(connection, dbQueue, psetObjects, p))
        dbWorkers.append(dbworker)
        dbworker.start()
    print(f"db Pool of {DB_PROCS} db Worker(s) Built -OK")


def start_client_workers(clientQueue, psetObjects, dbQueue, clientResponse):
    print("Building client Workers")
    print(f"CLIENT CORES: {CLIENT_CORES}")
    for p in range(CLIENT_CORES):
        clientWorker = Process(
            target=client_worker, args=(clientQueue, psetObjects, dbQueue, clientResponse, p), name=f"client-worker-{p}"
        )
        clientWorkers.append(clientWorker)
        clientWorker.start()
    print(f"Client Pool of {len(clientWorkers)} Worker(s) Built -OK")


def db_worker(connection, dbQueue, pset_objects, n):
    print(f"built dbworker {n}")


def client_worker(clientQueue, psetObjects, dbQueue, clientResponse, p):
    print(f"built client worker {p}")


@app.on_event("startup")
def startup_event():
    start_lifespan_resources()


@app.on_event("shutdown")
def shutdown_event():
    stop_lifespan_resources()
