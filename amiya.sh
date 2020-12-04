. ~/Documents/projects/peanuts/amiya/experiments_list.sh
. ~/Documents/projects/peanuts/amiya/knowledge.sh

if [ $# = 0 ]; then
	echo "please let me know what you want: "
	echo "* <create_experiments>"
	echo "* <add_experiment>"


elif [ $1 = "create_experiments" ]; then
	if [ $# = 1 ]; then
		echo 'expected 2 para, but just 1 found'
	else
		echo "create an experiments $green<$2>$none_c for $yellow$NOW$none_c? "
		read -r -p "[Y/n] " input
		if [ $input = "Y" ]; then 
			echo 'CONFIRMED, creating now'
			mkdir ~/Experiments/$2
			touch ~/Experiments/$2/index
			echo "$NOW: <$2>" >> ~/Experiments/$2/index
			echo "$now='$2'" >> ./experiments_list
			echo "$green ---> FINISHED"
		elif [ $input = "n" ]; then 
			echo 'CANCELED'
		else
			echo 'Invalid input'
		fi		
	fi


elif [ $1 = "add_experiment" ]; then
	if [ $# = 1 ]; then
		echo 'expected 2 para, but just 1 found'
	else
		echo "add an experiment $green<$2>$none_c to $yellow${!now}(¥now)$none_c? "
		read -r -p "[Y/n] " input
		if [ $input = "Y" ]; then 
			echo 'CONFIRMED, creating now'
		elif [ $input = "n" ]; then 
			echo 'CANCELED'
		else
			echo 'Invalid input'
		fi		
	fi


else
	echo "no command found !!!"


fi