function amiya() {

if [ $# = 0 ]; then
	echo "please let me know what you want: "
	echo "* <create_experiments>"
	echo "* <add_experiment>"


elif [ $1 = "create_experiments" ]; then
	if [ $# = 1 ]; then
		echo 'expected 2 para, but just 1 found'
	else
		echo "create an experiments $green<$2>$none_c for $yellow$NOW$none_c? [Y/n] "
		read -r input
		if [ $input = "Y" ]; then 
			echo "CONFIRMED, creating now"
			mkdir ~/Experiments/$2
			touch ~/Experiments/$2/index
			echo "$NOW: <$2>" >> ~/Experiments/$2/index
			echo "$now='$2'" >> ~/Documents/projects/peanuts/amiya/experiments_list.sh
			echo "\n"$(date "+%B(%Y)") "[$2]" >> ~/Experiments/README
			echo "$green ---> FINISHED"
		elif [ $input = "n" ]; then 
			echo 'CANCELED'
		else
			echo 'Invalid input'
		fi		
	fi


elif [ $1 = "add_experiment" ]; then
	if [ $# = 1 ]; then
		echo "expected 2 para, but just 1 found"
	else
		echo "add an experiment $green<$2>$none_c to $yellow${(P)now}($now)$none_c? [Y/n] "
		read -r input
		if [ $input = "Y" ]; then 
			echo 'CONFIRMED, creating now'
			mkdir ~/Experiments/${(P)now}/$2
			echo "\n<$2>" $(date "+%Y-%m-%d %H:%M:%S") >> ~/Experiments/${(P)now}/index
		elif [ $input = "n" ]; then 
			echo 'CANCELED'
		else
			echo 'Invalid input'
		fi		
	fi

else
	echo "no command found !!!"


fi
}

. ~/Documents/projects/peanuts/amiya/knowledge.sh

_amiya(){
    local cur cword words  # 定义变量，cur表示当前光标下的单词
    read -cn cword  # 所有指令集
    read -Ac words  # 当前指令的索引值
    cur="$words[$cword-1]" # 当前指令值
    if [ $cur = "amiya" ];then
        reply=(create_experiments add_experiment)
    fi
}
compctl -K _amiya amiya   # -K 表示使用函数

