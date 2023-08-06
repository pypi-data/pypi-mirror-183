import io
import requests
import jsonlines
from powerml.utils.run_ai import run_ai
from powerml.utils.config import get_config
import logging

logger = logging.getLogger(__name__)


class PowerML:
    def __init__(self, config={}):
        self.config = get_config(config)
        self.current_model = "text-davinci-003"

    def predict(self,
                prompt: str,
                model: str = "",
                stop: str = "",
                max_tokens: int = 128,
                temperature: int = 0,
                ) -> str:
        if model == "":
            model = self.current_model
        logger.debug("Predict using model: " + model)
        # if the model is one of our models, then hit our api
        return run_ai(prompt,
                      max_tokens=max_tokens,
                      api="powerml",
                      model=model,
                      stop=stop,
                      temperature=temperature,
                      key=self.config["powerml.key"],
                      )

    def fit(self,
            data: list[str],
            model: str = ""):
        if model == "":
            model = self.current_model
        logger.debug("Fit using model: " + model)
        # Upload filtered data to train api
        headers = {
            "Authorization": "Bearer " + self.config["powerml.key"],
            "Content-Type": "application/json", }
        response = requests.post(
            headers=headers,
            url="https://api.staging.powerml.co/v1/train",
            json={
                "dataset": self.__make_dataset_string(data),
                "model": model
            })
        model_details = response.json()['model']
        self.current_model = model_details["model_name"]
        return model_details

    def __make_dataset_string(self, training_data):
        string = io.StringIO()
        with jsonlines.Writer(string) as writer:
            for item in training_data:
                writer.write({"prompt": item})
        return string.getvalue()
