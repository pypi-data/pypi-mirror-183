from pytimeparse.timeparse import timeparse
import time
import tensorflow as tf
import math
import os
import requests

notifier_bot_token = None
notifier_chat_id = None

def test_notifier():
    check_setup()
    send_telegram_message("Test Message. If you have recieved this, everything is configured correctly.")

def check_setup():
    global notifier_bot_token
    global notifier_chat_id
    try:
        notifier_bot_token = os.environ["TRAINING_NOTIFIER_TOKEN"]
        notifier_chat_id = os.environ["TRAINING_NOTIFIER_CHAT_ID"]
    except:
        raise Exception("Could not find required enviornment variables (TRAINING_NOTIFIER_TOKEN, TRAINING_NOTIFIER_CHAT_ID). Are they set?")

def convert_seconds_to_string(seconds):
    seconds = round(seconds)
    if seconds > 60:
        minutes = int(math.floor(seconds / 60))
        seconds = seconds - (minutes * 60)
        if minutes > 60:
            hours = int(math.floor(minutes / 60))
            minutes = minutes - (hours * 60)

            return f"{hours}:{minutes:02d}:{seconds:02d}"
        return f"{minutes}:{seconds:02d}"
    return str(seconds) + "s"


class NotifierCallback(tf.keras.callbacks.Callback):
    def __init__(self, epochs, min_time="5m", epoch_updates=False, metrics=None, verbose=0):
        check_setup()
        self.epoch_updates = epoch_updates
        self.epochs = epochs
        self.metrics = metrics
        self.verbose = verbose
        try:
            self.min_seconds = timeparse(min_time)
        except:
            raise Exception(f"Invalid minimum time {min_time}. Should be in format '5m' or '2h30m'")

    def on_epoch_end(self, epoch, logs=None):

        metrics_string =""
        if self.metrics is not None:
            for metric in self.metrics:
                if metric in logs.keys():
                    metrics_string += f" {metric} : {logs[metric]} ;"

        message = ""
        if self.epochs == epoch + 1:
            # The training session is done
            message = f"Finished training on epoch {epoch + 1}! " + metrics_string
            self.send_message(message, is_end=True)
        else:
            # The training session is not done
            seconds_left = (self.epochs - (epoch + 1)) * ((time.time() - self.start_time) / (epoch + 1))
            message = f"Epoch {epoch + 1} completed. ETA {convert_seconds_to_string(seconds_left)} " + metrics_string
            self.send_message(message)

        if not self.verbose == 0:
            print(message)

    def on_train_begin(self, logs=None):
        self.start_time = time.time()
        self.last_message_time = self.start_time

    def send_message(self, message, is_end=False):
        now_time = time.time()
        if is_end and (now_time - self.start_time) > self.min_seconds:
            send_telegram_message(message)
        elif self.epoch_updates and ((now_time - self.last_message_time) > self.min_seconds):
            self.last_message_time = now_time
            send_telegram_message(message)


def send_telegram_message(message):
    response = requests.post(
            url=f'https://api.telegram.org/bot{notifier_bot_token}/sendmessage',
            data={'chat_id': notifier_chat_id, 'text': message}
        ).json()
