# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.
# See LICENSE file in the project root for full license information.
from typing import Optional

import logging
import pydantic
import sys


def get_logger(name: str,
               log_level: int = logging.INFO,
               log_file_name: Optional[str] = None,
               log_to_console: bool=True) -> logging.Logger:
    """
    Return the logger, capable to log into file and/or to console.

    :param name: the name of the logger.
    :param log_level: The logging verbosity level.
    :param log_file_name: The file to be sed to write logs if any.
    :param log_to_console: Boolean showing if we want to log into the console.
    :returns: The logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    if log_to_console:
        # Configure the stream handler (stdout)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.INFO)
        stream_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)
    
    if log_file_name:
        file_handler = logging.FileHandler(log_file_name)
        file_handler.setLevel(log_level)
        file_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    return logger


class Message(pydantic.BaseModel):
    content: str
    role: str = "user"


class ChatRequest(pydantic.BaseModel):
    messages: list[Message]
    use_metadata_inference: bool = False
