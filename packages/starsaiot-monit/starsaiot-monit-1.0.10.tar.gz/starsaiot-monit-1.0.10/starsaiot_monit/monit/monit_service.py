import time
import json
from time import sleep, strftime
from starsaiot_monit.monit.mqtt_connector import MqttConnector
from starsaiot_monit.logger import logger
from starsaiot_monit.conf import Conf
from starsaiot_monit.monit.utils.local_storage import get

class MonitService:
    def __init__(self, config_file=None):
        self.stopped = False
        config = Conf()
        self._msg_id=0
        while True:
            if config.dynamicRegister():
                break
            else:
                sleep(5)

        # self._monitJson = config.getMonitJson()
        self._monitJson = {
            "deviceId":get("device_id"),
            "deviceToken":get("device_token")
        }
        logger.info("Gateway started.")

        self._mqtt_connect = MqttConnector(self._monitJson['deviceId'])
        self._mqtt_connect.open()
        # self.subscribe()
        self.realtime()


        try:
            while not self.stopped:
                try:
                    sleep(.1)
                except Exception as e:
                    logger.exception(e)
                    break
        except KeyboardInterrupt:
            self.__stop_monit()
        except Exception as e:
            logger.exception(e)
            self.__stop_monit()
            self.__close_connectors()
            logger.info("The monit has been stopped.")

    def realtime(self):
        sleep(2)
        deviceId = self._monitJson['deviceId']
        while self._mqtt_connect.getConneted:
            current_time = strftime('%Y-%m-%d %H:%M:%S')
            msgId = deviceId + '_' + str(int(time.mktime(time.localtime(time.time()))))
            data = json.dumps({
                "deviceId": deviceId,
                "id": self._msg_id,
                "msgBody": current_time,
                "msgId": msgId,
                "msgKey": "heartbeat",
                "msgTopic": "\/sys\/platform\/device\/realtime",
                "msgVersion": "V3.0.0",
                "sendTime": current_time
            })
            self._mqtt_connect.sendMsg("/sys/platform/device/realtime", data, 0)
            # self._client.publish("/sys/platform/device/realtime", '{}', 0)
            self._msg_id+=1
            sleep(60)

    def __stop_monit(self):
        self.stopped = True
        logger.info("Stopping...")
        self.__close_connectors()
        logger.info("The monit has been stopped.")

    def __close_connectors(self):
        self._mqtt_connect.close()

    def subscribe(self):
        sleep(1)
        self._mqtt_connect.subscribe('/device/log/' + self._monitJson['deviceId'])
        self._mqtt_connect.subscribe('/device/app/' + self._monitJson['deviceId'])
        self._mqtt_connect.subscribe('/device/cmd/monitor/' + self._monitJson['deviceId'])
