# mettre à jour les scriptes
# conf par défaut à supprimer et à personnaliser dans le bashrc par exemple
export FRR_HOME=/home/pi
export FRR_CONF=ferronron_squelette 

fbi -T 2 -d /dev/fb1 -noverbose -a $FRR_HOME/ferronron_core/acceuil.jpg

# les executer
. $FRR_HOME/ferronron_core/scripts/start.sh
