from gnutools.fs import load_config as _load_config, parent
import os
from tqdm import tqdm
import re


def load_config():
    filename = f"{parent(__file__)}/config.yml"
    cfg = _load_config(filename)
    return cfg


def allow_spark(spark):
    cfg = load_config()
    spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", cfg.username)
    spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", cfg.password)
    spark.sparkContext._jsc.hadoopConfiguration().set(
        "fs.s3a.endpoint", f"http://{cfg.host}"
    )
    spark.sparkContext._jsc.hadoopConfiguration().set(
        "spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem"
    )
    spark.sparkContext._jsc.hadoopConfiguration().set(
        "spark.hadoop.fs.s3a.path.style.access", "true"
    )
    spark.sparkContext._jsc.hadoopConfiguration().set(
        "fs.s3a.multipart.size", "104857600"
    )
    return spark


def split_bucket_name(root):
    path = root.split("miniofs://")[1]
    splits = path.split("/")
    bucket, prefix = splits[0], "/".join(splits[1:])
    return bucket, prefix


def listfiles(root, patterns=[]):
    from miniofs import client

    bucket, prefix = split_bucket_name(root)
    files = [
        f"miniofs://{bucket}/{obj.object_name}"
        for obj in client.list_objects(bucket, recursive=True, prefix=prefix)
    ]
    if len(patterns) > 0:
        results = []
        for p in patterns:
            results += [f for f in files if len(re.split(p, f)) > 1]
    else:
        results = files
    return results


def download_file(file, filestore="/FileStore"):
    from miniofs import client

    bucket, object_name = split_bucket_name(file)
    output_file = os.path.join(f"{filestore}/{bucket}", object_name)
    os.makedirs(parent(output_file), exist_ok=True)
    client.fget_object(
        bucket,
        object_name,
        output_file,
    )
    return output_file


def download_files(root, patterns=[], filestore="/FileStore"):
    files = listfiles(root, patterns)
    return [
        download_file(file, filestore=filestore)
        for file in tqdm(
            files, total=len(files), desc=f"Downloading objects to {filestore}"
        )
    ]


def split_object_name(file, filestore="/FileStore"):
    splits = file.split(filestore)[1].split("/")[1:]
    bucket = splits[0]
    object_name = "/".join(splits[1:])
    return bucket, object_name


def upload_file(file, filestore="/FileStore"):
    from miniofs import client

    bucket, object_name = split_object_name(file, filestore=filestore)
    client.fput_object(
        bucket,
        object_name,
        file,
    )
    return f"miniofs://{bucket}/{object_name}"


def exists(file, filestore="/FileStore"):
    bucket, object_name = split_object_name(file, filestore=filestore)
    return len(listfiles(f"miniofs://{bucket}/{object_name}")) > 0


def upload_files(files, filestore="/FileStore", overwrite=True):
    def _upload_file(file):
        if overwrite:
            return upload_file(file, filestore=filestore)
        elif not exists(file, filestore=filestore):
            return upload_file(file, filestore=filestore)
        else:
            bucket, object_name = split_object_name(file, filestore=filestore)
            return f"miniofs://{bucket}/{object_name}"

    return [
        _upload_file(file)
        for file in tqdm(
            files, total=len(files), desc=f"Uploading objects from {filestore}"
        )
    ]
