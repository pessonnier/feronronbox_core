echo "mise à jour"

cd $FRR_HOME
git clone https://github.com/pessonnier/ferronron_core.git
git clone https://github.com/pessonnier/$FRR_CONF.git
cd $FRR_HOME/ferronron_core
git pull
cd $FRR_HOME/$FRR_CONF
git pull
cd $FRR_HOME
