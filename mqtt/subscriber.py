#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2014 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation
# All rights reserved.

# This shows a simple example of an MQTT subscriber using a per-subscription message handler.

import paho.mqtt.client as mqtt
import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
    host="localhost",
    user="pi",
    password="yusuf",
    database="iot"
)


def on_message(mosq, obj, msg):
    # This callback will be called for messages that we receive that do not
    # match any patterns defined in topic specific callbacks, i.e. in this case
    # those messages that do not have topics $SYS/broker/messages/# nor
    # $SYS/broker/bytes/#
    # print(msg.topic + " tak match " + str(msg.qos) + " " + str(msg.payload))

<<<<<<< HEAD
    print(str(msg.qos));
    mycursor = mydb.cursor()
    val = (mycursor.lastrowid, int(msg.qos), date.today())
    sql = "INSERT INTO iot (id,pts,created_at) VALUES (%s, %s, %s)"
=======
    payload = str(msg.payload)
    payload = payload.translate({ord("'"): None})
    payload = payload.translate({ord("b"): None})
    payload = payload.replace(' ', '')
    # payload.translate({ord("'"): None})
    print(int(payload)-20)
    mycursor = mydb.cursor()
    val = (mycursor.lastrowid, int(payload), date.today())
    sql = "INSERT INTO data (id,pts,created_at) VALUES (%s, %s, %s)"
>>>>>>> 3c026cf98f83baaa6dbef3c42ad4f3bc24599d5f
    mycursor.execute(sql, val)
    mydb.commit()


mqttc = mqtt.Client()

mqttc.on_message = on_message
mqttc.connect("localhost", 1883, 60)
<<<<<<< HEAD
mqttc.subscribe("testTopic", 0)
=======
mqttc.subscribe("testTopic")
>>>>>>> 3c026cf98f83baaa6dbef3c42ad4f3bc24599d5f
mqttc.loop_forever()
