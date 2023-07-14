from Agents import BookStore, PromptMarket
from LLMs import chatglm6b


class ExampleConfig():
    def __init__(self):
        self.llm = chatglm6b
        self.json_paths = ['example1.json', 'example2.json']
        self.register_agents = [BookStore, PromptMarket]
        self.runner = 'auto'