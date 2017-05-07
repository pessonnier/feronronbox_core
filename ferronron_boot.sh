# mettre à jour les scriptes
export FRR_HOME=/home/pi
export FRR_CONF=ferronron_squelette

cd $FRR_HOME
git clone https://github.com/pessonnier/ferronron_core.git
git clone https://github.com/pessonnier/$FRR_CONF.git
cd $FRR_HOME/ferronron_core
git pull
cd $FRR_HOME/$FRR_CONF
git pull

# les executer
chmod +x $FRR_HOME/ferronron_core/scripts/start.sh
$FRR_HOME/ferronron_core/scripts/start.sh
