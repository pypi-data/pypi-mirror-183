import warnings
from io import BytesIO
from base64 import encode as base64_encode

from typing import Any, Dict
from flask import Flask
from werkzeug.datastructures import FileStorage
from imagekitio import ImageKit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions
from imagekitio.models.results.UploadFileResult import UploadFileResult


class ImagekitIO:

    app: Flask = None
    _ik: ImageKit = None

    def __init__(self, app: Flask = None) -> None:
        if app:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:

        if not app.config.get('IMAGEKITIO_URL_ENDPOINT') or \
                not app.config.get('IMAGEKITIO_PRIVATE_KEY') or \
                not app.config.get('IMAGEKITIO_PUBLIC_KEY'):

            raise warnings.warn(
                'You must provide IMAGEKITIO_URL_ENDPOINT, IMAGEKITIO_PRIVATE_KEY and IMAGEKITIO_PUBLIC_KEY')

        url_endpoint = app.config.get('IMAGEKITIO_URL_ENDPOINT')
        private_key = app.config.get('IMAGEKITIO_PRIVATE_KEY')
        public_key = app.config.get('IMAGEKITIO_PUBLIC_KEY')

        self.app = app
        self._ik = ImageKit(public_key, private_key, url_endpoint)
        return

    def upload_file(self, file: FileStorage, file_name: str,
                    options: UploadFileRequestOptions = None) -> UploadFileResult:

        data = BytesIO()
        base64_encode(file.stream, data)
        data.seek(0)

        return self._ik.upload_file(file, file_name, options)

    def url(self, options: Dict[str, Any]) -> str:
        return self._ik.url(options)
