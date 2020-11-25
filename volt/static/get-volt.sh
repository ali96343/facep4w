DIR="/home/w3p/set1/py4web/apps/volt/static/tte"
if [ -d "$DIR" ]; then

   rm -rf $DIR
   mkdir $DIR
   cd $DIR

   git clone https://github.com/themesberg/volt-bootstrap-5-dashboard
   cd volt-bootstrap-5-dashboard/
   npm i && gulp build:dev

   cd ..

   if [[ "$VIRTUAL_ENV" != "" ]]
      then
            INVENV=1
            biorex -sv -t 1 -f 1
      else
            INVENV=0
            echo "run virtual env, pls"
   fi

   echo "Installing volt files in ${DIR}..."
fi



