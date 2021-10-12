#!/bin/bash

# https://github.com/linkchecker/linkchecker
# array=($(ls -d */)) ;  for i in "${array[@]}" ; do 
# echo $i; 
# linkchecker --check-extern  --no-robots  http://localhost:8000/$i
# done

start=$SECONDS

linkchecker --check-extern  --no-robots  http://localhost:8000/flat
linkchecker --check-extern  --no-robots  http://localhost:8000/bulma
linkchecker --check-extern  --no-robots  http://localhost:8000/chen
linkchecker --check-extern  --no-robots  http://localhost:8000/ngx
linkchecker --check-extern  --no-robots  http://localhost:8000/corona
linkchecker --check-extern  --no-robots  http://localhost:8000/desk
linkchecker --check-extern  --no-robots  http://localhost:8000/gentelella
linkchecker --check-extern  --no-robots  http://localhost:8000/kapella
linkchecker --check-extern  --no-robots  http://localhost:8000/kit
linkchecker --check-extern  --no-robots  http://localhost:8000/lte3
linkchecker --check-extern  --no-robots  http://localhost:8000/ngx
linkchecker --check-extern  --no-robots  http://localhost:8000/notika
linkchecker --check-extern  --no-robots  http://localhost:8000/tail
linkchecker --check-extern  --no-robots  http://localhost:8000/volt
linkchecker --check-extern  --no-robots  http://localhost:8000/wind

end=$SECONDS

#you can now either just print the difference:

echo "duration: $((end-start)) seconds."
