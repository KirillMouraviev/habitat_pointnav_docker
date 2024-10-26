xhost +local:docker || true
docker run --runtime=nvidia --gpus all --rm --name pointnav_docker \
--env="DISPLAY=$DISPLAY" \
--env="QT_X11_NO_MITSHM=1" \
--device /dev/nvidia0:/dev/nvidia0 \
--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
-env="XAUTHORITY=$XAUTH" \
--volume="$XAUTH:$XAUTH" \
--privileged \
-p $2:8888 -e jup_port=$2 \
-v /home/kirill/data/:/data \
-v ${HOME}/.Xauthority:/root/.Xauthority:rw \
-v /home/kirill/pointnav_habitat_docker:/root pointnav_docker
