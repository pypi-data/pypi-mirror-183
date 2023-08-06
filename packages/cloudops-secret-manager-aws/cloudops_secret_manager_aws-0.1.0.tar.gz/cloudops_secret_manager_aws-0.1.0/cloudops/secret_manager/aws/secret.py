import base64
import json
import logging
from typing import Optional

import boto3
import pydantic


class SecretConfig(pydantic.BaseModel):
    secret_id: str
    region: str
    description: str = ""


class Secret:
    def __init__(self, config: SecretConfig):
        self.config = config
        self.client = boto3.client(
            service_name="secretsmanager",
            region_name=self.config.region,
        )

    def exists(self) -> bool:
        logging.info("Checking if secret exists...")
        try:
            self.client.get_secret_value(SecretId=self.config.secret_id)
            return True
        except self.client.exceptions.ResourceNotFoundException:
            return False

    def create(self) -> None:
        logging.info("Creating secret...")
        self.client.create_secret(
            Name=self.config.secret_id,
            SecretString="{}",
            Description=self.config.description,
        )

    def delete(self) -> None:
        logging.info("Deleting secret...")
        self.client.delete_secret(SecretId=self.config.secret_id)

    def pull(self) -> dict:
        logging.info("Pulling latest secret version...")
        get_secret_value_response = self.client.get_secret_value(SecretId=self.config.secret_id)
        if "SecretString" in get_secret_value_response:
            secret = get_secret_value_response["SecretString"]
        else:
            secret = base64.b64decode(get_secret_value_response["SecretBinary"])
        return json.loads(secret)

    def push(self, payload: dict) -> None:
        logging.info("Pushing secret...")
        self.client.put_secret_value(
            SecretId=self.config.secret_id,
            SecretString=json.dumps(payload),
        )
