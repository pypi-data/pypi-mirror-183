pip3 install poetry
poetry build
poetry publish

git add . && git commit -m "add change to project" && git push

psql --username netbox --password --host localhost netbox

\dt


SELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = 'netbox_acls_accesslist';

SELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = 'virtualization_virtualmachine';


virtualization_virtualmachine;