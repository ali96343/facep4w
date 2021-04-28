start=$SECONDS

linkchecker --check-extern  --no-robots  http://localhost:8000/angflat
linkchecker --check-extern  --no-robots  http://localhost:8000/bulma
linkchecker --check-extern  --no-robots  http://localhost:8000/bulma-ad
linkchecker --check-extern  --no-robots  http://localhost:8000/bulmaadmin
linkchecker --check-extern  --no-robots  http://localhost:8000/chen
linkchecker --check-extern  --no-robots  http://localhost:8000/concept
linkchecker --check-extern  --no-robots  http://localhost:8000/corona
linkchecker --check-extern  --no-robots  http://localhost:8000/desk
linkchecker --check-extern  --no-robots  http://localhost:8000/gentelella
linkchecker --check-extern  --no-robots  http://localhost:8000/kapella
linkchecker --check-extern  --no-robots  http://localhost:8000/kit
linkchecker --check-extern  --no-robots  http://localhost:8000/lte3
linkchecker --check-extern  --no-robots  http://localhost:8000/ngx
linkchecker --check-extern  --no-robots  http://localhost:8000/notika
linkchecker --check-extern  --no-robots  http://localhost:8000/octopus
linkchecker --check-extern  --no-robots  http://localhost:8000/sb
linkchecker --check-extern  --no-robots  http://localhost:8000/srt
linkchecker --check-extern  --no-robots  http://localhost:8000/tailwind
linkchecker --check-extern  --no-robots  http://localhost:8000/volt
linkchecker --check-extern  --no-robots  http://localhost:8000/vuenotus
linkchecker --check-extern  --no-robots  http://localhost:8000/vuestic
linkchecker --check-extern  --no-robots  http://localhost:8000/vuetim
linkchecker --check-extern  --no-robots  http://localhost:8000/wind

end=$SECONDS
#you can now either just print the difference:

echo "duration: $((end-start)) seconds."
