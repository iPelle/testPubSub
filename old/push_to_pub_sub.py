#https://ohadp.com/setup-an-mvp-for-googles-pub-sub-in-2-mins-408084f5b35e
import json
import os

os.environ['GOOGLE_CLOUD_DISABLE_GRPC'] = 'true'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.expanduser('~') + '/' + '.my_certificates/google_cloud_personal.json'

from google.cloud import pubsub #pip install google-cloud-pubsub

topic_name = 'mesecondTopic'
project = 'crested-pursuit-216317'
data = {'amount': 10}

#pubsub_client = pubsub.Client()
#pbsub_client = pubsub.PublisherClient()
publisher = pubsub.PublisherClient()

topic_path = publisher.topic_path(project, topic_name)

topic = publisher.create_topic(topic_path)
print('Topic created: {}'.format(topic))
topic_path = publisher.topic_path(project, topic_name)

#Create topic


#payments_topic = pubsub_client.topic('myTopic')

def publish_message(data):
    data = json.dumps(data)
    data = data.encode('utf-8')
    print 'before pushing'
    message_id = publisher.publish(topic_path, data=data)
    print('Message '+repr(message_id)+'published.')


def process_order_aync(data):
    publish_message(data)

#process_order_aync({'amount': 10})