import fire
from yolov5tospace import yolov5_to_space_pipeline


def app() -> None:
    """Cli app."""
    fire.Fire(yolov5_to_space_pipeline)


if __name__ == "__main__":
    app()
