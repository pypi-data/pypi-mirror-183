
from powerml import PowerML
import logging

logger = logging.getLogger(__name__)


class PowerMLTopicModel:
    def __init__(self, topics=None, config={}, model_name=None):
        self.model = PowerML(config)
        self.model_name = model_name
        self.topics = topics

        if (topics is None) and (model_name is None):
            raise ValueError("Must specify topics or model_name")

    def fit(self, examples):
        if self.topics is None:
            raise ValueError("Must specify topics to call fit")

        prefix = "List of topics we should consider extracting from messages:"
        example_string = prefix + "\n" + "\n".join(self.topics)

        for example in examples:
            new_string = "\n\nMessage: " + example["example"]
            new_string += "\nExtract the relevant topics from the above message:"
            for label in example["labels"]:
                new_string += "\n-" + label

            if len(example_string) + len(new_string) > 3072:
                break

            example_string += new_string

        suffix = """
Message: {{input}}
Extract the relevant topics from the above message:
-"""
        example_string += suffix

        new_model = self.model.fit(
            [example_string], model="text-davinci-003")

        logger.debug("Got new model: " + new_model["model_name"])
        # Note: model_name is also stored in the PowerML class.
        # This step is no longer strictly necessary unless multiple models are
        # being used or you wish to explicitly switch between models.
        self.model_name = new_model["model_name"]

    def predict(self, prompt):
        if self.model_name is None:
            result = self.model.predict(prompt)
        else:
            result = self.model.predict(prompt, model=self.model_name)

        return post_process(result)


def post_process(topics):
    return [topic.strip() for topic in topics.split("-")]
