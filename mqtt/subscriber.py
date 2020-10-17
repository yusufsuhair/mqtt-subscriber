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
    user="root",
    password="",
    database="iot"
)


def on_message(mosq, obj, msg):
    # This callback will be called for messages that we receive that do not
    # match any patterns defined in topic specific callbacks, i.e. in this case
    # those messages that do not have topics $SYS/broker/messages/# nor
    # $SYS/broker/bytes/#
    # print(msg.topic + " tak match " + str(msg.qos) + " " + str(msg.payload))

    mycursor = mydb.cursor()
    val = (mycursor.lastrowid, int(msg.qos), date.today())
    sql = "INSERT INTO data (id,point,created_at) VALUES (%s, %s, %s)"
    mycursor.execute(sql, val)
    mydb.commit()


mqttc = mqtt.Client()

mqttc.on_message = on_message
mqttc.connect("localhost", 1883, 60)
mqttc.subscribe("iot", 0)
mqttc.loop_forever()
