import os

from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT", "3000"))
HOST = os.getenv("HOST", "0.0.0.0")
AMQP_URL = os.getenv(
    "AMQP_URL",
    "amqp://guest:guest@localhost:5672/%2F?connection_attempts=20&retry_delay=1",
)
CHARGE_POINT_ID = "charge_point_id"
RPC_SEND_QUEUE = "rpc"
