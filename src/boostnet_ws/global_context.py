import dataclasses
from typing import TYPE_CHECKING

from asyncio import Event
from typing import Optional, Dict

from aio_pika.abc import (
    AbstractRobustChannel,
    AbstractRobustQueue,
)

if TYPE_CHECKING:
    from .cp import ChargePointClient


@dataclasses.dataclass
class GlobalContext:
    clients: Dict[str, "ChargePointClient"]
    amqp_channel: Optional[AbstractRobustChannel] = None
    rpc_recv_queue: Optional[AbstractRobustQueue] = None
    rpc_send_queue: Optional[AbstractRobustQueue] = None
    shutdown_event: Optional[Event] = None


ctx = GlobalContext({})


def set_global_context(amqp_channel, rpc_recv_queue, rpc_send_queue, shutdown_event):
    global ctx
    ctx.amqp_channel = amqp_channel
    ctx.rpc_recv_queue = rpc_recv_queue
    ctx.rpc_send_queue = rpc_send_queue
    ctx.shutdown_event = shutdown_event
