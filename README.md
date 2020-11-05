# TPCD_Practica1

## Requeriments
- Python 3.6
- Pipenv (per tal de crear un entorn virtual amb les dependències necessàries)
## Execució
```
$ pipenv install
$ pipenv shell

$ cd src
$ scrapy crawl fotocasa_flats -t csv -o ../csv/data.csv
$ python gencat/means.py ../csv/data.csv ../csv/data_final.csv
```

