echo alu

./ferronron_core/scripts/init.sh
python3 ./ferronron_core/scripts/interrupteurs.py &
python3 ./ferronron_core/scripts/play.py &
./ferronron_core/scripts/supprime.sh
python3 ./ferronron_core/scripts/telecharge.py &
