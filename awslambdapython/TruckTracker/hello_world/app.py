import json
import random


def truck_tracker(event, context):
    if event.latitude and event.longitude:
        print('latitude: {}, longitude: {}', event.latitude, event.longitude)

def get_ticket(event, context):
    if event.payment and float(event.payment) > 0.0:
        return {
            "statusCode": 200,
            "body": json.dumps({
            "ticketNumber": random.randint()
            }),
        }
    else:
        return json.dumps({
            "statusCode": 400,
            "error": json.dumps({
            "message": "Please provide payment"
            })
        })
