from powerml import PowerML
import re
from collections import Counter
import random
from tqdm import tqdm
from transformers import GPT2Tokenizer
from transformers.utils import logging


class PowerMLLearnTopics:
    def __init__(self, config={}, num_subsamples=10, sample_size=40):
        self.model = PowerML(config)
        self.messages = []
        self.num_subsamples = num_subsamples
        self.sample_size = sample_size
        self.memo_top_topics = {}
        self.memo_fltered_top_topics = {}
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        logging.set_verbosity(40)

    def add_data(self, documents):
        self.messages.extend(documents)
        random.shuffle(self.messages)

    def get_topics(self):
        # If get_topics has been called on the same messages array
        # Then use the previous results
        hash_docs = hash(frozenset(self.messages))
        if hash_docs in self.memo_top_topics:
            return self.memo_top_topics[hash_docs]

        num_samples = len(self.messages)
        if self.num_subsamples * self.sample_size > num_samples:
            self.num_subsamples = num_samples // self.sample_size
            self.num_subsamples += 1 if len(
                self.messages) % self.sample_size else 0

        topic_type = 'one-word system components'
        prompt = f'What are the {topic_type} that these messages discuss?\n\n1.'
        num_samples = len(self.messages)
        sample_index = 0
        topic_counter = Counter()
        for i in tqdm(range(self.num_subsamples)):
            if sample_index > num_samples:
                break
            examples, sample_index = self.__subsample(
                self.messages, sample_index, self.sample_size)
            prompt = self.__add_examples(examples, prompt)
            output = self.model.predict(
                prompt, max_tokens=256, temperature=0.7)
            topics = self.__parse_output(output)
            topic_counter.update(topics)
            sorted_topics = self.__sort_topics(topic_counter)
        top_topics = self.__get_top_topics(sorted_topics)
        self.memo_top_topics[hash_docs] = top_topics
        return top_topics

    def get_filtered_topics(self):
        hash_docs = hash(frozenset(self.messages))
        if hash_docs in self.memo_fltered_top_topics:
            return self.memo_fltered_top_topics[hash_docs]
        top_topics = self.get_topics()
        not_topics = self.__filter_top_topics(top_topics)
        filtered_top_topics = list(set(top_topics) - set(not_topics))
        self.memo_fltered_top_topics[hash_docs] = filtered_top_topics
        return filtered_top_topics

    def __count_tokens(self, string):
        return len(self.tokenizer(string)['input_ids'])

    def __add_examples(self, examples, prompt, max_total_tokens=4000, max_output_tokens=256):
        for example in examples:
            new_prompt = f'"{example}"\n\n' + prompt
            if self.__count_tokens(new_prompt) < max_total_tokens - max_output_tokens:
                prompt = new_prompt
            else:
                break
        return prompt

    def __parse_output(self, output):
        list_pattern = re.compile(r"\d+\.\s")
        # include enumerated list prompt
        items = list_pattern.sub("", f'1. {output}')
        parsed = []
        for i in items.split('\n'):
            ii = i.split(',')
            stripped = [iii.strip().replace('.', '') for iii in ii if iii]
            parsed.extend(stripped)
        return parsed

    def __subsample(self, data, start_index, sample_size):
        # Assume data is pre-shuffled
        end_index = start_index + sample_size
        return data[start_index:end_index], end_index

    def __sort_topics(self, topic_counter):
        return sorted(topic_counter.items(), key=lambda x: x[1], reverse=True)

    def __get_top_topics(self, sorted_topics):
        # Return and save all that have more than count 1
        return [elt for elt, count in sorted_topics if count > 1]

    def __filter_top_topics(self, top_topics):
        prompt = 'Which of the above are not technical system-level topics?'
        prompt = f'{top_topics}\n\n{prompt}\n\n1.'
        output = self.model.predict(prompt, max_tokens=500, temperature=0.7)
        output = self.__parse_output(output)
        return output
