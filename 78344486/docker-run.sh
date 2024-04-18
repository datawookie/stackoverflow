#!/bin/bash

docker run -it \
    --mount=type=bind,source=./test,target=/home/glue_user/workspace/test \
    --mount=type=bind,source=./libs,target=/home/glue_user/workspace/libs \
    -w /home/glue_user/workspace \
    -e DISABLE_SSL=true \
    -e "PYTHONPATH=$PYTHONPATH:/home/glue_user/workspace/deps" \
    --rm \
    --name glue_unit_tests amazon/aws-glue-libs:glue_libs_4.0.0_image_01 \
    -c "mkdir -p deps/ && pip install -r test/requirements.txt -r libs/requirements.txt -t deps/; cd test && pytest || exit 1"
