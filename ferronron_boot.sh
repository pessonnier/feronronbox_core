# mettre à jour les scriptes
cd /home/pi
git clone https://github.com/pessonnier/ferronron_core.git
git clone https://github.com/pessonnier/ferronron_squelette.git
cd /home/pi/ferronron_core
git pull
cd /home/pi/ferronron_squelette
git pull

# les executer
./ferronron_core/scripts/start.sh
