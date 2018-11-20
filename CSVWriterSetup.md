# Wofford SolarShed CSV Setup
This guide is aimed at providing the necessary steps for getting the .csv writer script, `csvgen.py`, running on a Raspberry Pi. This script allows for a daily log of readings from the controller to be saved in .csv, or comma-separated-value, files. These files can be opened easily with software such as Excel, MatLab, and R.

This guide assumes your Pi will be running Raspbian and will be connected to the internet.

## The Pi
To set up the Raspberry Pi itself, we recommend following the [official documentation](https://www.raspberrypi.org/documentation/setup/).
To connect the Pi to the Renogy Rover controller, connect the supplied data cable's USB end to the Pi and the proprietary end to the Rover.

## Downloading The Software
#### Using Git:
To quickly download the SolarShed software, run the following command on the Pi's terminal:

`git clone http://github.com/andersonwr/WoffordSolarShed/`

This will clone the software package to your current directory in the terminal.
#### Using a Browser:
You may also download the package by going to the [GitHub Repository](http://github.com/andersonwr/WoffordSolarShed/), clicking "Clone or download", and then "Download Zip."

## Software Auto-Setup
**TODO**
We intend to write a script that will allow for a quick, one-command setup of the software, automatically configuring the .csv writer to run when the Pi boots. In the meantime, please refer to the steps below.

## Downloading Requisite Python Libraries
This script relies on a few other Python libraries. To download them, run the following command on the Pi's terminal:
`pip3 install pyserial MinimalModbus`

## Running the Script
#### Manually:
To run the .csv writer script, navigate to `<save location>/WoffordSolarShed/solarshed/` in your terminal and run the command `python3 csvgen.py`. You can stop the script by typing CTRL+C.

#### Automatically:
**TODO**
The script can also be configured to run automatically at certain times, such as every time the Pi boots. This can be done by adding a cron job to the system. 

## Pausing the Script
**TODO**
We intend to add a Python script or find a terminal command that will stop a instance of the writer script running in the background. This will allow the current day's .csv file to be accessed.

## The Script Itself
#### Input
The script obtains the values to be saved via a direct connection with the Renogy Rover.
#### Output
The script generates a .csv file for each day, which will be written to `/WoffordSolarShed/solarshed/controllerCSVs/YYYY-MM-DD.csv`. The generated .csv files include the following columns of data:
  - Time
  - BatteryPercentage
  - BatteryVoltage
  - BatteryTemperature
  - ControllerTemperature
  - ChargingStatus
  - LoadVoltage
  - LoadCurrent
  - LoadPower
  - SolarVoltage
  - SolarCurrent
  - SolarPower

By default, a new row of data is added every ten seconds, based on the current values of the controller. This can be changed by modifying the line `SCRAPE_DELAY = 10` near the top of the `csvgen.py` file.

## Remote Connection
**TODO**