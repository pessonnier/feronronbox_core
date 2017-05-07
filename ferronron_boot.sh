# mettre à jour les scriptes
# conf par défaut à supprimer et à personnaliser dans le bashrc par exemple
export FRR_HOME=/home/pi
export FRR_CONF=ferronron_squelette 

cd $FRR_HOME
git clone https://github.com/pessonnier/ferronron_core.git
git clone https://github.com/pessonnier/$FRR_CONF.git
cd $FRR_HOME/ferronron_core
git pull
cd $FRR_HOME/$FRR_CONF
git pull
cd $FRR_HOME

# les executer
. $FRR_HOME/ferronron_core/scripts/start.sh
