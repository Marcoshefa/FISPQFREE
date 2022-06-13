# FISPQFREE

Software para geração de FISPQ

## Prerequeriment

- Python >= 3.6
- Banco de dados MYSQL >=5.6

## Install

### Clone of the project
``` 
git clone https://github.com/Marcoshefa/FISPQFREE.git

cd FISPFREE
```
### Install dependencies

```
cd api

pip3 install -r requerements.txt
```


## Running

Access the `db` folder and execute `setup.sql` file in your database.

then, running in command line:

```
FLASK_APP=api/app.py flask run
```

open http://localhost:5000/