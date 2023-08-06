from miniofs.functional import *
from minio import Minio

__version__ = "0.0.4a"
cfg = load_config()
client = Minio(
    cfg.host,
    secure=False,
    access_key=cfg.username,
    secret_key=cfg.password,
)
