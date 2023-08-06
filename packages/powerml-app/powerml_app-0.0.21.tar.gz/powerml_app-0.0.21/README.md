# PowerML Python Package

## Installation

    pip install powerml_app

## Authentication
You will need two keys: PowerML and OpenAI.

To get a PowerML key, go to [https://staging.powerml.co/](https://staging.powerml.co/) and log in with your email. Contact our team if you are unable to log in and we'll add you!

To get an OpenAI key, go to [https://beta.openai.com/account/api-keys](https://beta.openai.com/account/api-keys).

## Configuration
In order to use this library, first create a config file at `~/.powerml/configure.yaml` with your PowerML and OpenAI keys. Here's an example:

    powerml:
        key: "<POWERML-KEY>"
    openai:
        key: "<OPENAI-KEY>"

By default, we will use these keys for the `PowerML` class:

    from powerml import PowerML
    powerml = PowerML()

You may also configure the `PowerML` class by passing in a dictionary:

    from powerml import PowerML
    config = {"powerml": {"key": "<POWERML-KEY>"}}
    powerml = PowerML(config)


## Usage

You can use the member functions of the PowerML class, `predict` and `fit`, to make predictions with the model and fit data to the model to improve and customize it. 

You can use `predict` to run any prompt off the bat:

    from powerml import PowerML

    powerml = PowerML()
    
    # Run base model
    myPrompt = "hello there"
    response = powerml.predict(prompt=myPrompt)

To fit data to the model, you can use `fit` as so:

    # Fit model to data
    myData = ["item2", "item3"]
    myModel = powerml.fit(myData)

To run this fitted model, you can use `predict` again, specifying the new model name:

    # Use new model
    myModelName = myModel["model_name"]
    response = powerml.predict(prompt=myPrompt, model=myModelName)


## PowerML Class

The `PowerML` class has member functions `fit` and `predict`.

### Predict

`predict` accepts the following arguments:

    def predict(self,
                prompt: str,
                model: str = "text-davinci-003",
                stop: str = "",
                max_tokens: int = 128,
                temperature: int = 0,
                ) -> str:

`predict` will return a string of the model's output.

`fit` accepts the following arguments:

    def fit(self,
            data: list[str],
            model: str = ""):

`fit` will return a dictionary object in the following format:

    {
        "model_id":"23",
        "project_id":"None",
        "user_id":"12",
        "job_id":"89",
        "model_name":"be894276039088c5f8db3f6bfaeb19953ed9ffe55f37a847a58f9fb320d307bc",
        "job_config":"{\"type\": \"prompt_tune\", \"model_name\": \"llama\"}",
        "prompt":"item2item3{{input}}",
        "creation_time":"2022-12-20 02:19:36.519260",
        "job":{
            "job_id":"89",
            "project_id":"None",
            "user_id":"12",
            "config":"{\"type\": \"prompt_tune\", \"model_name\": \"llama\"}",
            "status":"COMPLETED",
            "name":"be894276039088c5f8db3f6bfaeb19953ed9ffe55f37a847a58f9fb320d307bc",
            "metric":"None",
            "history":"None",
            "start_time":"2022-12-20 02:19:36.369450",
            "end_time":"2022-12-20 02:19:35.837668"
        }
    }
    

## PowerMLTopicModel Class

The `PowerMLTopicModel` class is an example class designed to extract topics from the prompt.

### Usage
To instantiate a `PowerMLTopicModel`, you just need to pass in some sample topics for it to consider.

    # Topics, e.g. ["vscode", "web", "dashboard"]
    topics = get_list_of_topics()
    
    model = PowerMLTopicModel(topics)

To customize your `PowerMLTopicModel` instance, you can pass it examples to fit to.

    # Examples in json for the model to fit to, in the format:
    # [
    #    { "example": "Using VS here for my IDE", labels: ["vscode"] },
    #    { "example": "A dashboard on Chrome", labels: ["web", "dashboard"] },
    # ]
    examples = get_json_examples()
    
    model.fit(examples)

Now, you can run this model on new examples with `predict`:

    new_example = "Move invite teammates page to its own base route . per designs:   This PR just moves existing views around and adds a new base route (i.e. no new functionality)"
    
    example_topics = model.predict(new_example)

### Methods

`__init__` is defined as follows:

    def __init__(self, topics: list[str], config={}):

`fit` is defined as follows:

    def fit(self, 
            examples: list[
                {"example": str, "labels": list[str]}
            ]):

where examples is a list of dictionaries with format `{"example": str, "labels": list[str]}`.

`predict` is defined as follows:

    def predict(self, prompt: str):

## PowerMLLearnTopics Class

The `PowerMLLearnTopics` class is an example class designed to generate topics from a list of data. This is a batch process and may take a few minutes.

### Usage

    data = get_list_of_data()
    
    learn_topics = PowerMLLearnTopics()
    learn_topics.add_data(data)
    topics = learn_topics.get_topics()

#### Usage with `PowerMLTopicModel`
Topics can be learned by `PowerMLLearnTopics`, then used in `PowerMLTopicModel`. 

First, get topics from `PowerMLLearnTopics`:
    
    topics = learn_topics.get_topics()

Then, get topics from `PowerMLLearnTopics`:

    topic_model = PowerMLTopicModel(topics)
    
Finally, use `PowerMLTopicModel` as you normally would (as above) to fit it to examples, and then predict on new examples:

    topic_model.fit(examples)
    example_topics = model.predict(new_example)


### Methods

`__init__` is defined as follows:

    def __init__(self, config={}, num_subsamples=100, sample_size=50):

`add_data` is defined as follows:

    def add_data(self, documents):

where documents is a list of strings.

`get_topics` is defined as follows:

    def get_topics(self):

and returns a set of strings

`get_filtered_topics` is defined as follows:

    def get_topics(self):

and returns a set of strings. This method can be used to apply an extra fuzzy filter on the topics to remove duplicates and unrelated topics.
