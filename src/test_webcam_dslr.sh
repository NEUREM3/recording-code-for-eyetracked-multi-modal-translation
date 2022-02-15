#!/bin/bash
#sudo rmmod v4l2loopback
sudo modprobe v4l2loopback devices=1 exclusive_caps=1
pkill gphoto2
gphoto2 --stdout --capture-movie | ffmpeg -i - -vcodec rawvideo -pix_fmt yuv420p -threads 0 -f v4l2 /dev/video2
sudo rmmod v4l2loopback