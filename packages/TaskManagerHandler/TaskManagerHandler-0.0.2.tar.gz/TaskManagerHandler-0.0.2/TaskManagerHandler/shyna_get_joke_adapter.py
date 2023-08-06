from ShynaJokes import ShynaJokes
from chatterbot.logic import LogicAdapter


class ShynaJokeAdapter(LogicAdapter):
    s_joke = ShynaJokes.ShynaJokes()
    conf = []

    def __init__(self, chatbot, **kwargs):
        super(ShynaJokeAdapter, self).__init__(chatbot, **kwargs)

    def can_process(self, statement):
        try:
            cmd_list = ["how about a joke",
                        "how about some joke",
                        "I am sad",
                        "m sad",
                        "i'm sad",
                        "make me laugh",
                        "happy sentence",
                        "tell me a joke",
                        "joke please",
                        "make me smile", ]
            if str(statement).lower().startswith(tuple(cmd_list)):
                return True
            else:
                return False
        except AttributeError:
            return False
        except Exception as e:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        from chatterbot.conversation import Statement
        response = self.s_joke.shyna_pun_joke()
        confidence = 1
        # print(response)
        response_statement = Statement(text=str(response))
        response_statement.confidence = confidence
        return response_statement
