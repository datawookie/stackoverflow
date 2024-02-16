import os
import io
import logging
import sshtunnel
import paramiko
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("my_logger")

tunnel = sshtunnel.SSHTunnelForwarder(
    (os.environ.get("SSH_HOST"), 22),
    ssh_username=os.environ.get("SSH_USER"),
    ssh_pkey=paramiko.RSAKey.from_private_key(
        io.StringIO(os.environ.get("SSH_PKEY")),
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
