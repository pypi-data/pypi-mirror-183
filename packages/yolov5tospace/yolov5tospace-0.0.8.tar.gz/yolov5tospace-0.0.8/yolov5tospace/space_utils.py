import os
import shutil

GRADIO_SDK_VERSION = "3.15.0"
YOLOV5_PACKAGE_VERSION = "7.0.5"


def generate_object_detection_space_card(base_name: str) -> str:
    return f"""---
title: {base_name} Object Detection
emoji: 🎮
colorFrom: red
colorTo: gray
sdk: gradio
sdk_version: {GRADIO_SDK_VERSION}
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
"""


def generate_image_classification_space_card(base_name: str) -> str:
    return f"""---
title: {base_name} Image Classification
emoji: 🎮
colorFrom: red
colorTo: gray
sdk: gradio
sdk_version: {GRADIO_SDK_VERSION}
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
"""


def generate_object_detection_app_file(
    base_name,
    model_types,
    hfhub_model_ids,
    hfhub_username,
    task="object-detection",
    test_images_folder=None,
    export_dir=".",
) -> str:

    if model_types:
        models_ids = [
            hfhub_username
            + "/"
            + model_type
            + "-"
            + base_name.strip().lower().replace(" ", "-")
            for model_type in model_types
        ]
        dataset_id = (
            hfhub_username
            + "/"
            + base_name.strip().lower().replace(" ", "-")
            + "-"
            + task
        )
    elif hfhub_model_ids:
        models_ids = hfhub_model_ids
        dataset_id = models_ids[-1]

    if task == "object-detection":
        app_title = base_name + " " + "Object Detection"
    elif task == "image-classification":
        app_title = base_name + " " + "Image Classification"

    # copy test images to export dir
    if test_images_folder is not None:
        test_images_folder = os.path.abspath(test_images_folder)
        target_images_folder = f"{export_dir}/test_images/"
        shutil.move(
            test_images_folder, target_images_folder
        )

        image_filenames = os.listdir(target_images_folder)
        examples = [
            ['test_images/' + image_filename, 0.25, models_ids[-1]]
            for image_filename in image_filenames
        ]
    else:
        examples = None

    return f"""
import json
import gradio as gr
import yolov5
from PIL import Image
from huggingface_hub import hf_hub_download

app_title = "{app_title}"
models_ids = {models_ids}
article = f"<p style='text-align: center'> <a href='https://huggingface.co/{{models_ids[-1]}}'>model</a> | <a href='https://huggingface.co/{dataset_id}'>dataset</a> | <a href='https://github.com/keremberke/awesome-yolov5-models'>awesome-yolov5-models</a> </p>"

current_model_id = models_ids[-1]
model = yolov5.load(current_model_id)

examples = {examples}


def predict(image, threshold=0.25, model_id=None):
    # update model if required
    global current_model_id
    global model
    if model_id != current_model_id:
        model = yolov5.load(model_id)
        current_model_id = model_id

    # get model input size
    config_path = hf_hub_download(repo_id=model_id, filename="config.json")
    with open(config_path, "r") as f:
        config = json.load(f)
    input_size = config["input_size"]

    # perform inference
    model.conf = threshold
    results = model(image, size=input_size)
    numpy_image = results.render()[0]
    output_image = Image.fromarray(numpy_image)
    return output_image


gr.Interface(
    title=app_title,
    description="Created by '{hfhub_username}'",
    article=article,
    fn=predict,
    inputs=[
        gr.Image(type="pil"),
        gr.Slider(maximum=1, step=0.01, value=0.25),
        gr.Dropdown(models_ids, value=models_ids[-1]),
    ],
    outputs=gr.Image(type="pil"),
    examples=examples,
    cache_examples=True if examples else False,
).launch(enable_queue=True)
"""


def generate_requirements_file() -> str:
    return f"""
yolov5=={YOLOV5_PACKAGE_VERSION}
gradio=={GRADIO_SDK_VERSION}
torch
huggingface-hub
"""
