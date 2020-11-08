# TPCD_Practica1

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4261145.svg)](https://doi.org/10.5281/zenodo.4261145)

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

