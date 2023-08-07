import json
import logging

from .cancellable_iterator import cancellable_iterator
from .global_context import ctx

logger = logging.getLogger(__name__)


async def rpc_recv_queue_consumer():
    logger.info("START: RPC iterator")
    assert ctx.rpc_recv_queue is not None
    assert ctx.shutdown_event is not None

    async with ctx.rpc_recv_queue.iterator() as queue_iter:
        async for message in cancellable_iterator(queue_iter, ctx.shutdown_event):
            async with message.process():
                body = message.body.decode()
                decoded = json.loads(body)
                charge_point_id = decoded["id"]
                logger.info(
                    "IN: RPC %s: %s", dict(cp=charge_point_id), decoded["message"]
                )
                if charge_point_id not in ctx.clients:
                    logger.warning("SEND ERR (disconnected): %s", charge_point_id)
                    continue
                await ctx.clients[charge_point_id].send_message_to_charge_point(decoded)
        logger.info("EXIT: RPC iterator loop")
    logger.info("EXIT: RPC iterator")
