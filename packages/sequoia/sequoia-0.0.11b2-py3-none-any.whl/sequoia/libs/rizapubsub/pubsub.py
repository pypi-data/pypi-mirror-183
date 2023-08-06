import ujson
from google.cloud import pubsub_v1
from google.auth import jwt
from pydantic import BaseModel


class TaskData(BaseModel):
    topic: str
    task: str
    subtask: str
    data: dict


class PubSub:
    def __init__(self, config: dict, topic):
        self.config = config
        self.topic = topic

    def pub(self):
        credentials = jwt.Credentials.from_service_account_info(
            self.config,
            audience="https://pubsub.googleapis.com/google.pubsub.v1.Publisher",
        )
        return pubsub_v1.PublisherClient(credentials=credentials)

    def sub(self):
        credentials = jwt.Credentials.from_service_account_info(
            self.config,
            audience="https://pubsub.googleapis.com/google.pubsub.v1.Subscriber",
        )
        return pubsub_v1.SubscriberClient(credentials=credentials)

    def send(self, publisher, data: dict):
        project_id = self.config.project_id
        msg = ujson.dumps(data["data"]).encode("utf-8")
        topic_path = publisher.topic_path(project_id, self.topic)

        future = publisher.publish(
            topic_path,
            data=msg,
            module=data.get("module"),
            taskname=data.get("taskname")
        )
        pubsub_id = future.result()
        return pubsub_id
