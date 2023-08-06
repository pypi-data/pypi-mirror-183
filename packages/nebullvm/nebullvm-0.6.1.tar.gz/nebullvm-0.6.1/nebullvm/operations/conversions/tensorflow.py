import logging
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Union

from nebullvm.config import ONNX_OPSET_VERSION
from nebullvm.optional_modules.onnx import onnx
from nebullvm.optional_modules.tensorflow import tensorflow as tf, tf2onnx
from nebullvm.tools.base import ModelParams, DataType

logger = logging.getLogger("nebullvm_logger")


def convert_tf_to_onnx(model: tf.Module, output_file_path: Union[str, Path]):
    """Convert TF models into ONNX.

    Args:
        model (tf.Module): TF model.
        output_file_path (Path): Path where storing the output file.
    """
    with TemporaryDirectory() as temp_dir:
        tf.saved_model.save(model, export_dir=temp_dir)

        try:
            subprocess.check_output(["python3", "--version"])
            python_cmd = "python3"
        except subprocess.CalledProcessError:
            python_cmd = "python"

        onnx_cmd = [
            python_cmd,
            "-m",
            "tf2onnx.convert",
            "--saved-model",
            f"{temp_dir}",
            "--output",
            f"{output_file_path}",
            "--opset",
            f"{ONNX_OPSET_VERSION}",
        ]
        try:
            subprocess.run(onnx_cmd)
            onnx.load(output_file_path)
        except Exception:
            logger.warning(
                "Something went wrong during conversion from tensorflow"
                " to onnx model. ONNX pipeline will be unavailable."
            )
            return None

        return output_file_path


def convert_keras_to_onnx(
    model: tf.keras.Model,
    model_params: ModelParams,
    output_file_path: Union[str, Path],
):
    """Convert keras models into ONNX.

    Args:
        model (tf.Module): keras model.
        model_params (ModelParams): Model Parameters as input sizes and
            dynamic axis information.
        output_file_path (Path): Path where storing the output file.
    """
    spec = (
        tf.TensorSpec(
            (model_params.batch_size, *input_info.size),
            tf.float32 if input_info.dtype is DataType.FLOAT else tf.int32,
            name=f"input_{i}",
        )
        for i, input_info in enumerate(model_params.input_infos)
    )
    tf2onnx.convert.from_keras(
        model,
        input_signature=spec,
        opset=ONNX_OPSET_VERSION,
        output_path=output_file_path,
    )
