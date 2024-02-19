```
docker build -t opencv-one . && docker run --rm -v $(pwd):/app -it opencv-one
```

```
RUN pkg-config --modversion opencv4
```

```
g++ -std=c++11 -o image_addition one.cpp `pkg-config --cflags --libs opencv4`
```
