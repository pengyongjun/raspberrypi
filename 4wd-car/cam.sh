#! /bin/bash
basepath=$(cd `dirname $0`; pwd)

sudo modprobe bcm2835-v4l2

cd /home/pi/4wd-car/mjpg-streamer/mjpg-streamer-experimental/
./mjpg_streamer -i "./input_uvc.so -d /dev/video0 -n -y -f 25 -r 640x480" -o "./output_http.so -n -w ./www"

cd basepath