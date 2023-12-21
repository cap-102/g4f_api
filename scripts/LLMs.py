import g4f


class LLMS:
    class GPT3_5:
        @staticmethod
        def main(query, history:list=False):
            return Base.chatGPT(text=query, model=g4f.models.gpt_35_turbo, history=history) if history else Base.chatGPT(text=query, model=g4f.models.gpt_35_turbo)

    class GPT_4:
        @staticmethod
        def main(query, history: list = False):
            return Base.chatGPT(text=query, model=g4f.models.gpt_4, history=history) if history else Base.chatGPT(
                text=query, model=g4f.models.gpt_35_turbo)


class Base:
    @staticmethod
    def chatGPT(text:str, model, history:list=False):
        g4f.debug.logging = False
        g4f.debug.check_version = False
        response = False

        max_attempts = 3
        attempts = 0

        if history:
            history.append({"role": "user", "content": text})
        else:
            history = [{"role": "user", "content": text}]

        while not response and attempts < max_attempts:
            try:
                response = g4f.ChatCompletion.create(

                    model=model,
                    messages=history,
                )
            except Exception as e:
                print(f"Error: {e}")
                response = False
                attempts += 1

        if response:
            history.append({"role": "assistant", "content": response})
            return response, history
        else:
            return False
