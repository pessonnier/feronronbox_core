# rien
echo "****************"
date
echo "****************"
echo "initialisation"
ping -c 1 google.com
if [ $? ]
then
  echo "réseau accessible"
else
  echo "réseau inaccessible, maj de la conf"
  cp $FRR_HOME/$FRR_CONF/wpa /etc/wpa_supplicant/wpa_supplicant.con
  sudo wpa_cli reconfigure
  sleep 3
fi
