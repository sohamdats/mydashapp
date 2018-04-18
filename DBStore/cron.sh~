if [ $1=="remove" ]
then
    crontab -r
elif [ $1=="add" ]
then
   file_path=$PWD/"test.py"
   command="python $file_path"
   crontab -l > mycron
   echo "*/1 * * * * $command" >> mycron
   crontab mycron
   rm mycron
fi


