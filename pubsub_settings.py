# install these pip requirements
google-cloud-pubsub==0.23

# create the topic and subscription once
gcloud beta pubsub topics create myTopic
gcloud beta pubsub subscriptions create --topic myTopic