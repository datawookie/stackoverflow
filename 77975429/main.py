import multiprocessing
from multiprocessing import Process, Queue
from fastapi import FastAPI
from contextlib import asynccontextmanager

CLIENT_CORES = 5
connection = "mongo_connection_string"

@asynccontextmanager
async def lifespan(app: FastAPI):    
    manager = multiprocessing.Manager()

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

    config_processes(dbQueue,clientQueue,clientResponse,psetObjects)

    yield
    
    graceful_shutdown()

def config_processes(dbQueue,clientQueue,clientResponse,psetObjects):
    start_db_workers(dbQueue,psetObjects)

    start_client_workers(clientQueue,psetObjects,dbQueue,clientResponse)

def start_db_workers(dbQueue,psetObjects):
    print("Building db Workers")

    for p in range(DB_PROCS):
        dbworker = Process(target=db_worker,args=(connection,dbQueue,psetObjects,p))
        dbWorkers.append(dbworker)
        dbworker.start()

    print("db Pool of {} db Worker(s) Built -OK".format(DB_PROCS))

def start_client_workers(clientQueue,psetObjects,dbQueue,clientResponse):
    print("Building client Workers")
    print("CLIENT CORES: {}".format(CLIENT_CORES))
    
    for p in range(CLIENT_CORES):
        clientWorker = Process(target=client_worker,args=(clientQueue,psetObjects,dbQueue,clientResponse,p),name="client-worker-{}".format(p))
        clientWorkers.append(clientWorker)
        clientWorker.start()
    
    print("Client Pool of {} Worker(s) Built -OK".format(len(clientWorkers)))

def db_worker(connection,dbQueue,pset_objects,n):
    dbworker = DbWorker(connection,dbQueue,pset_objects,n)
    print("built dbworker {}".format(n))
    dbworker.listen()

def client_worker(clientQueue,psetObjects,dbQueue,clientResponse,p):
    clientworker = ClientWorker(clientQueue,psetObjects,dbQueue,clientResponse,p)
    print("built client worker {}".format(p))
    clientworker.listen()