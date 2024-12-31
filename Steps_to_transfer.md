### run

```
pip install flask
python Steps_to_transfer.py
# get the ip
# check the file, under uploads
```

### curl

```
curl - O http://{ip}/downloadfile/a.s

curl -T file.txt http://{ip}/upload

curl -F 'file=@/path/to/your/file.txt' http://{ip}/upload

```