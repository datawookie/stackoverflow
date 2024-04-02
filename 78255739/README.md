```
docker build -t 78255739 . && docker run --rm -it --memory="7m" --memory-swap="10m" -p 8080:80 --name phptest 78255739
```
