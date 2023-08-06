import os
import shutil
from yolov5tospace.hf_utils import upload_space_to_hfhub
from yolov5tospace.space_utils import (
    generate_object_detection_app_file,
    generate_object_detection_space_card,
    generate_requirements_file,
)
import logging

__version__ = "0.0.8"

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
logging.basicConfig(level=LOGLEVEL)
LOGGER = logging.getLogger(__name__)


def yolov5_to_space_pipeline(
    base_name,
    hfhub_username,
    model_types=None,
    hfhub_model_ids=None,
    task="object-detection",
    test_images_folder=None,
    export_dir=".",
    keep_exported_files=False,
    hf_private: bool = False,
    hf_write_token: str = None,
):
    if task == "object-detection":
        object_detection_space_card = generate_object_detection_space_card(base_name)
        object_detection_app_file = generate_object_detection_app_file(
            base_name=base_name,
            model_types=model_types,
            hfhub_model_ids=hfhub_model_ids,
            hfhub_username=hfhub_username,
            task=task,
            test_images_folder=test_images_folder,
            export_dir=export_dir,
        )

        with open(f"{export_dir}/README.md", "w", encoding="utf-8") as f:
            f.write(object_detection_space_card)

        with open(f"{export_dir}/app.py", "w") as f:
            f.write(object_detection_app_file)
    else:
        raise ValueError(f"Task {task} is not supported.")

    requirements_file = generate_requirements_file()
    with open(f"{export_dir}/requirements.txt", "w") as f:
        f.write(requirements_file)
    LOGGER.info(f"Exported files to {export_dir}")

    space_id = f"{hfhub_username}/{base_name.strip().lower().replace(' ', '-')}-{task}"
    LOGGER.info(f"Uploading to huggingface.com/spaces/{space_id}")
    upload_space_to_hfhub(
        space_dir=export_dir, repo_id=space_id, token=hf_write_token, private=hf_private
    )

    if not keep_exported_files:
        shutil.rmtree(export_dir)
