conf = {
    "type":
    "service_account",
    "project_id":
    "konverzi-ignite",
    "private_key_id":
    "da734cc8d4735de9433916529285f64c9db6928a",
    "private_key":
    "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCYcfE0o/T2XdBT\nmjngvgqPyJBu+TuFMkzll9LYy9KSUg4qBGGmEdmnq8FHfPoM46FLZIuZEhfiPPsW\nANA3MdvuLzNOEleJW6s7ohzblM9hic2oOVRh0EcXAGf4IAwt2KGnLEGx7r3wd7Om\nJxy1smDzi8O+63SUm5aBaGHXeeykRbrlawy3XFU99qCN4u2Mk8utCJNqZAhbtvc7\n69r5pPXA5BmNTtMkIfbMA9cTla9ILowwoEqTZR6F7sx38VX9ecTQaxjicPpLfP2S\nJ4YoqVnsj6zhJKACCx8r1uCXcN6OTOYqPwNWNAlyNoU2Mw1q8nYWW8iTdqfdsPY/\nV/S48GK9AgMBAAECggEAEac+OKuU6jO+dHP7aFZxiCmAak1z0k6bH4pHmSHvSlD0\nwXJc8XuHMja+TN5A4Z25l662yLzS5bjMlcV11zJvpsMyBIQ0vVwPdfolr9rpcgDg\nfy7WYfZZySTbpVzmtCduPtrt56I/PhnKhL7qQPM9bW6dth3zk+L5mJZDIE4G9JXN\n03M1eao98TJErK5ImZCT9/Eixgdsd94KcKE3JoIsBu+RLazRb1k8hHzy7p32Dzvi\nj4tUS3o14Fw+TC4zPl5wwWlCHtkxocLiPz9Tsp82LMSV1Hj8gNFSJyGq0na7obi4\nZRoqWHyz4Em+Ke/Vz9AWJFRPFTV+MllymwVWSfhREQKBgQDLOVY0hNwT0D3ZzYNk\ncdKW9ejPyQLFNKWRgitRSWb1biAERWK+xwmx1ck8LoukeNlRDDPUAG/y5kqG5vnr\nU0y6M9F9j59AqVUOLtH28Ded7l9PruKojw0qKvSuC5xGK7q+kUSjfeLBGbGV4tEd\ngO1M3Kivmqn2/65qL1t0IN8Q8QKBgQDACL3pVDNGlU66QWha/VnxZOhNN6P78XE8\ne4lpEg/0u5Wwf6fnU27qEnA5giY1+uzFKtHQ8KGNzEgnKNYKnoPuQbEosucHCpBv\nsyiHeOi2tMVjbSSYaF0swWf61WGMn2Cw+hCdKht8G5QbgAKLF8XDbwgLwbzzHz4c\nXDjwgZTujQKBgB3mH6K2cVKQ7qierdgXTu5a25fGcRvmdP2Fcy4QaI9vVlKKis6a\npfh+BY9PIche50ofS3jDX7US4KAcV2Sh6sXyXb3lZX6z6wmdJdL44JXhvjARANPf\nyAYOL9Vza9h/Eoh7Augy2yuhxhjROAbpMwB97mt3i84FK/n/YasiMu9hAoGBAKHn\nPOZ53PlHbKbP+oGsVKaW4twnaxRBTa0mooV5ewZlGSFDn3YC++JRRVjXCAw+0Fyz\na05zcmGwt6x8W2l8l9LKg+jCXNGs8HWcYTFGmT1hT4IyRMZSRywyq83pFWOQA99y\nFYvMMnwCbG57EKngkxXgiLIQ15NK5fzXLBJpzf0JAoGBALh7xEEkR2BUitrTFqnK\nmqy2uDr3aVNVB9Smphs6+f3c6dSEA7dlgOk4ZhlKAiqxkp1ZbkQiFhbLy8K9x3On\ngAr4by/1xK0uj4NI1b4dnWeXe3TCb0UsE7w7S9rcQt3qp+vjeF0IP/w+oN87UtO5\n/MUXYRcaxCbv3Ri2uHtuOx8X\n-----END PRIVATE KEY-----\n",
    "client_email":
    "johny-adminer@konverzi-ignite.iam.gserviceaccount.com",
    "client_id":
    "106669843803122607232",
    "auth_uri":
    "https://accounts.google.com/o/oauth2/auth",
    "token_uri":
    "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url":
    "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url":
    "https://www.googleapis.com/robot/v1/metadata/x509/johny-adminer%40konverzi-ignite.iam.gserviceaccount.com"
}

import json
import os
from google.auth import jwt
from google.cloud import pubsub_v1

service_account_info = conf  # json.load(open("konverzi-ignite.json"))


def pub():
    audience = "https://pubsub.googleapis.com/google.pubsub.v1.Publisher"
    credentials = jwt.Credentials.from_service_account_info(
        service_account_info, audience=audience)
    # credentials_pub = credentials.with_claims(audience=audience)
    publisher = pubsub_v1.PublisherClient(credentials=credentials)
    topic_name = 'projects/{project_id}/topics/{topic}'.format(
        project_id='konverzi-ignite',
        topic='ignite_maintasks',  # Set this to something appropriate.
    )
    # publisher.create_topic(name=topic_name)
    future = publisher.publish(topic_name, b'My first message!', spam='eggs')
    c = future.result()
    print('send', c)


# pub()


def sub():

    def callback(message):
        print(message.data)
        message.ack()

    audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"
    credentials = jwt.Credentials.from_service_account_info(
        service_account_info, audience=audience)

    # credentials_sub = credentials.with_claims(audience=audience)

    while True:
        subscriber = pubsub_v1.SubscriberClient(credentials=credentials)
        with subscriber:
            subpath = subscriber.subscription_path("konverzi-ignite",
                                                   "maintasks_sub")

            # get messages
            response = subscriber.pull(request={
                'subscription': subpath,
                'max_messages': 10
            })

            ack_ids = []
            for msg in response.received_messages:

                # action to msg
                try:
                    # logger.warning("Received: {}".format(msg.message))
                    print('receive pubsub')
                    print("Received: {}".format(msg.message))

                except Exception as e:
                    print('pubsub fail', e)
                    pass

                ack_ids.append(msg.ack_id)

            # Acknowledges the received messages so they will not be sent again.
            tot = len(response.received_messages)
            if tot > 0:
                subscriber.acknowledge(request={
                    "subscription": subpath,
                    "ack_ids": ack_ids,
                })


sub()