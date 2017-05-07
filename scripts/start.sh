echo alu

$FRR_HOME/ferronron_core/scripts/init.sh
python3 $FRR_HOME/ferronron_core/scripts/interrupteurs.py &
python3 $FRR_HOME/ferronron_core/scripts/play.py &
$FRR_HOME/ferronron_core/scripts/supprime.sh
python3 $FRR_HOME/ferronron_core/scripts/telecharge.py &
