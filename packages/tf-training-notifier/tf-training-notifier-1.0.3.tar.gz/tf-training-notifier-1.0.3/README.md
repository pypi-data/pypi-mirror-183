# Tensorflow Training Notifier

A python package which periodically notifies you of your Tensorflow job's progress. 

## Installation

The python package can be installed via pip.

```bash
pip install tf-training-notifier
```

## Setup

The package relies on two envionrmnet variables ("TRAINING_NOTIFIER_TOKEN" and "TRAINING_NOTIFIER_CHAT_ID") being set. These variables point towards the Telegram bot token and the Telegram chat ID. Instructions on how to get and set those up can be found [here](https://bart1259.github.io/tf-training-notifier/).

## Usage

### Setting up the notifier

```python
import trainingnotifier
EPOCHS = 15
# The default notifier which only notifies the user when the job is completed.
notifier = trainingnotifier.NotifierCallback(EPOCHS)
model.fit(x_train, y_train, epochs=EPOCHS, callbacks=[notifier])
```

```python
# Creates a notifier that will update the user ONCE (if the job takes more than 2 minutes) 
#  when the job is done. It will also report the loss in this message.
notifier = trainingnotifier.NotifierCallback(EPOCHS, min_time="2m", metrics=["loss"])
```

```python
# Creates a new notifier that will notify the user, at soonest, every 10 minutes with 
#  the jobs ETA and loss values. If the job takes longer than 10 minutes than it will send 
#  a notification that the job is done
notifier = trainingnotifier.NotifierCallback(EPOCHS, epoch_updates=True, min_time="10m", metrics=["loss"])
```

### To test if the system was setup properly.

```python
# This function tests the notification system. If the target user recieves a Telegram test 
#  message, then the enviornment variables have been set correctly.
trainingnotifier.test_notifier()
```