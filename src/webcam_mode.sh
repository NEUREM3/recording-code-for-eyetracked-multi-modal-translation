#!/bin/bash
rm cam_record_default
camfile="$(pwd)/web_cam.py"
#Please include your venv path here
virt="../../virt/bin/activate"
echo $camfile
gnome-terminal -x bash -c "source $virt; python $camfile; exec bash"
expfile="$(pwd)/experiment.py"
gnome-terminal -x bash -c "source $virt; python $expfile --dummy; exec bash"