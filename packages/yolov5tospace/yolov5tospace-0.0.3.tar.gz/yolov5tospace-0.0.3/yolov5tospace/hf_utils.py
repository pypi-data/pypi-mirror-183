import logging

LOGGER = logging.getLogger(__name__)


def upload_space_to_hfhub(space_dir, repo_id, token, private=False):
    """
    Uploads a dataset to the Hugging Face Hub.
    Args:
        space_dir (str): Path to the local space directory.
        repo_id (str): The name of the space repository to upload to.
        token (str): The token to use to authenticate to the Hugging Face Hub.
        private (bool, optional): Whether the repository should be private. Defaults to False.
    """
    from huggingface_hub import upload_folder, create_repo

    LOGGER.info(f"Uploading space to hf.co/{repo_id}...")

    create_repo(
        repo_id=repo_id,
        token=token,
        private=private,
        exist_ok=True,
        repo_type="space",
        space_sdk="gradio",
    )
    upload_folder(
        folder_path=space_dir,
        repo_id=repo_id,
        token=token,
        repo_type="space",
        commit_message="upload space files",
    )

    LOGGER.info(f"Space uploaded to hf.co/{repo_id}!")
