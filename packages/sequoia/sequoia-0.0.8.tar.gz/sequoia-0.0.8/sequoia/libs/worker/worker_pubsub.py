from libs.rizapubsub import PubSub
from libs.worker.execute_worker import ExecuteJob
from core.config import config
from core.db import SessionLocal
# from core.logger import logger


async def run():
    pubsub = PubSub(config.GCP_PUBSUB, config.GCP_PUBSUB.pubsub_topic)
    session = SessionLocal()
    t = ExecuteJob(
        session=session
    )

    while True:
        subscrb = pubsub.sub()

        with subscrb:
            subpath = subscrb.subscription_path(  # type: ignore
                config.GCP_PUBSUB.project_id,
                config.GCP_PUBSUB.pubsub_subscription  # type: ignore
            )

            # get messages
            response = subscrb.pull(  # type: ignore
                request={"subscription": subpath, "max_messages": 2}
            )

            ack_ids = []
            for msg in response.received_messages:

                # action to msg
                try:
                    # logger.info("Received: {}".format(msg.message))
                    await t.do_task(msg.message)

                except Exception as e:
                    print(e)
                    # logger.warning(f"pubsub fail: {e}")
                    pass

                ack_ids.append(msg.ack_id)

            # Acknowledges the received messages so they
            # will not be sent again.
            tot = len(response.received_messages)
            if tot > 0:
                subscrb.acknowledge(  # type: ignore
                    request={
                        "subscription": subpath,
                        "ack_ids": ack_ids,
                    }
                )
