# When, Where, and What? A New Dataset for Anomaly Detection in Driving Videos
[original repository](https://github.com/MoonBlvd/Detection-of-Traffic-Anomaly)

## prepare

Create a data directory and move necessary files from the data set directory.
download DoTA_fol_train_data, DoTA_fol_val_data from [here](https://drive.google.com/drive/folders/1IVCedrlPg03Fsg4tqDA2cWYlcdrsKUsp?usp=sharing)

Detection-of-Traffic-Anomaly/data$ ls
```
DoTA_fol_train_data  DoTA_fol_val_data  metadata_train.json  metadata_val.json  train_split.txt  val_split.txt
```

## run
```bash
cd Detection-of-Traffic-Anomaly/environments/gpu
docker compose up -d
docker compose exec core bash
poetry run python dataloader_example.py
```

## reference
[Detection-of-Traffic-Anomaly](https://github.com/MoonBlvd/Detection-of-Traffic-Anomaly)