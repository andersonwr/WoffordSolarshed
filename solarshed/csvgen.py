import logging
import datetime
import time
import csv
import os
from random import randint

from controllers.renogy_rover import RenogyRover

logger = logging.getLogger(__name__)

SCRAPE_DELAY = 10
CSV_PATH = 'controllerCSVs/'
HEADERS = "Time|BatteryPercentage|BatteryVoltage|BatteryTemperature|ControllerTemperature|ChargingStatus|LoadVoltage|LoadCurrent|LoadPower|SolarVoltage|SolarCurrent|SolarPower".split("|")

curr_date = datetime.date.today()

while True:
    fname = CSV_PATH + str(curr_date) + '.csv'
    if(not os.path.isfile(fname)):
        with open(fname, 'w', newline = "") as temp:
            csv.writer(temp).writerow(HEADERS)
	
    while datetime.date.today() == curr_date:
        try:
            with open(fname, 'a', newline = "") as w:
                '''
                controller = RenogyRover('/dev/ttyUSB0', 1),
                csv_writer.writerow([time.localtime(),
                    controller.battery_percentage(),
                    controller.battery_voltage(),
                    controller.battery_temperature(),
                    controller.controller_temperature(),
                    controller.charging_status(),
                    controller.load_voltage(),
                    controller.load_current(),
                    controller.load_power(),
                    controller.solar_voltage(),
                    controller.solar_current(),
                    controller.solar_power()])
                '''
                csv.writer(w).writerow([time.strftime("%H:%M:%S") for i in range(len(HEADERS))])
            time.sleep(SCRAPE_DELAY)
        except:
            logger.exception('problem updating gauges')
        
        curr_date = datetime.date.today()
