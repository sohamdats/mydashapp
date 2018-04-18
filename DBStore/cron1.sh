file_path=$PWD/"dbstore.py"
py=`which python`
command="$py $file_path"
crontab -l > mycron
echo "*/1 * * * * $command" >> mycron
crontab mycron
rm mycron



