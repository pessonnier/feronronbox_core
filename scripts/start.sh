echo alu
echo "***************"
date
echo "***************"
. $FRR_HOME/ferronron_core/scripts/miseajour.sh
. $FRR_HOME/ferronron_core/scripts/init.sh
sudo -E python3 $FRR_HOME/ferronron_core/scripts/interrupteurs.py &
sudo -E python3 $FRR_HOME/ferronron_core/scripts/play.py &
. $FRR_HOME/ferronron_core/scripts/supprime.sh
. $FRR_HOME/ferronron_core/scripts/upload.sh
python3 $FRR_HOME/ferronron_core/scripts/telecharge.py &
