pip3 install poetry
poetry build
poetry publish

git add . && git commit -m "add change to project" && git push

psql --username netbox --password --host localhost netbox

\dt


SELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = 'netbox_acls_accesslist';

SELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = 'virtualization_virtualmachine';


virtualization_virtualmachine;

python manage.py makemigrations netbox_data_disk --dry-run


http://localhost:8000/plugins/data-disk/data-disk


https://github.com/ryanmerolle/netbox-acls
https://github.com/iDebugAll/nextbox-ui-plugin
https://github.com/PieterL75/netbox_ipcalculator/
https://github.com/hudson-trading/netbox-nagios

https://github.com/netbox-community/netbox-plugin-tutorial
https://github.com/netbox-community/netbox