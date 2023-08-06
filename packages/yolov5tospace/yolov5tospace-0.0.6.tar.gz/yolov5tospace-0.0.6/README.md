# yolov5tospace
Automatically create  Gradio apps from YOLOv5 models and push to the Spaces

## installation

```bash
pip install yolov5tospace
```

## api usage

```python
from yolov5tospace import yolov5_to_space_pipeline

yolov5_to_space_pipeline(
    base_name="Visdrone",
    model_types=["yolov5n"],
    hfhub_username=YOUR-HFHUB-USERNAME,
    task="object-detection",
    test_images_folder=None,
)

```

or

```python
from yolov5tospace import yolov5_to_space_pipeline

yolov5_to_space_pipeline(
    base_name="Visdrone",
    hfhub_model_ids=[YOUR-HFHUB-MODELID-1, YOUR-HFHUB-MODELID-2],
    hfhub_username=YOUR-HFHUB-USERNAME,
    task="object-detection",
    test_images_folder=None,
)

```
