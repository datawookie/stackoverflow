import os
import io
import logging
import sshtunnel
import paramiko
from dotenv import load_dotenv

load_dotenv()

SSH_HOST = os.environ.get("SSH_HOST")
SSH_USER = os.environ.get("SSH_USER")
SSH_PKEY = os.environ.get("SSH_PKEY")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("my_logger")

tunnel = sshtunnel.SSHTunnelForwarder(
    (SSH_HOST, 22),
    ssh_username=SSH_USER,
    ssh_pkey=paramiko.RSAKey.from_private_key(
        io.StringIO(SSH_PKEY),
    ),
    remote_bind_addresses=[("0.0.0.0", 5432)],
    logger=logger,
)

try:
    tunnel.start()
    print("SSH Tunnel successful")
except sshtunnel.BaseSSHTunnelForwarderError as e:
    print("SSH Tunnel failed")
    print(e)
