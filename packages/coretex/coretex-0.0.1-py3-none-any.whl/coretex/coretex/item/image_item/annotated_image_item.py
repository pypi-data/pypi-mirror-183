from __future__ import annotations

from typing import Optional

import os
import json

import numpy as np

from .base_image_item import BaseImageItem
from ...annotation import CoretexImageAnnotation, ImageDatasetClasses
from ....codable import KeyDescriptor
from ....networking import NetworkManager, RequestType


class AnnotatedImageItem(BaseImageItem):

    def __init__(self) -> None:
        super().__init__()

        self.coretexAnnotation: Optional[CoretexImageAnnotation] = None

    @property
    def coretexAnnotationsPath(self) -> str:
        return os.path.join(self.path, "annotations.json")

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()

        descriptors["imageData"] = KeyDescriptor(isEncodable = False)
        descriptors["coretexAnnotation"] = KeyDescriptor(isEncodable = False)

        return descriptors

    def saveAnnotation(self, coretexAnnotation: CoretexImageAnnotation) -> bool:
        parameters = {
            "id": self.id,
            "data": coretexAnnotation.encode()
        }

        response = NetworkManager.instance().genericJSONRequest(
            endpoint = "session/save-annotations",
            requestType = RequestType.post,
            parameters = parameters
        )

        if not response.hasFailed():
            self.coretexAnnotation = coretexAnnotation

        return not response.hasFailed()

    def load(self) -> None:
        super().load()

        # load annotations if they exist
        if os.path.exists(self.coretexAnnotationsPath):
            with open(self.coretexAnnotationsPath, "r") as annotationsFile:
                self.coretexAnnotation = CoretexImageAnnotation.decode(
                    json.load(annotationsFile)
                )

    def extractSegmentationMask(self, classes: ImageDatasetClasses) -> np.ndarray:
        if self.coretexAnnotation is None:
            raise ValueError(">> [Coreted] Coretex annotation value is None")

        return self.coretexAnnotation.extractSegmentationMask(classes)
