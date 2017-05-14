echo "mise à jour"
echo $FRR_HOME
cd $FRR_HOME
echo "clone"
if [ ! -d "ferronron_core" ]
then
  git clone https://github.com/pessonnier/ferronron_core.git
fi
if [ ! -d $FRR_CONF ]
then
  git clone https://github.com/pessonnier/$FRR_CONF.git
fi
echo "pull"
cd $FRR_HOME/ferronron_core
git pull
cd $FRR_HOME/$FRR_CONF
git pull
cd $FRR_HOME
