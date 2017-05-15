while true
do
  echo "initialisation"
  ping -c 1 google.com
  if [ $? -eq 0 ]
  then
    echo "réseau accessible"
    break 
  else
    echo "réseau inaccessible, maj de la conf"
    cp $FRR_HOME/$FRR_CONF/wpa /etc/wpa_supplicant/wpa_supplicant.con
    sudo wpa_cli reconfigure
    sleep 3
    #ajouter une image pour informer
  fi
done
