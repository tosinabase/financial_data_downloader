
```
sudo -u postgres psql

CREATE DATABASE fin_data_downloader;
CREATE USER fin_data_downloader WITH PASSWORD 'fin_data_downloader';
GRANT ALL PRIVILEGES ON DATABASE fin_data_downloader TO fin_data_downloader;
```
