echo "Which version would you like to activate?"
read -p "1. Real life 2. Fun" var_version
if [ "$var_version" = "1"]
then
  echo "Initiating Traffic Light Sequence"
  sudo python real.py
else
  echo "Initiating Traffic Light Simulator"
  sudo python fun.py
fi
