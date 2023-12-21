from flask import jsonify
from scripts import LLMS


class Base:
    @staticmethod
    def checkMissingFields(data):
        if 'query' not in data or 'model' not in data or 'token' not in data:
            base = "Missing required fields. "
            if 'query' not in data:
                return jsonify({'error': f'{base}Please, specify your query.'}), 400
            elif 'token' not in data:
                return jsonify({'error': f'{base}Please, specify your token.'}), 400
            elif 'history' not in data:
                return jsonify({'error': f'{base}Please, specify your history or make the value to false.'}), 400
        else:
            return False

    @staticmethod
    def dialogMaker(data, model:str='gpt-3'):
        result = False

        if model == 'gpt-3':
            result = LLMS.GPT3_5.main(query=data['query'], history=data['history'])
        elif model == 'gpt-4':
            result = LLMS.GPT_4.main(query=data['query'], history=data['history'])

        if result:
            answer, history = result
            return jsonify({'error': False, 'answer': answer, 'history': history}), 200
        else:
            return jsonify({'error': f'Unknown error.'}), 500

    @staticmethod
    def getValidKeys():
        return ['sk-92a02b6638ss87c']

    @staticmethod
    def checkToken(data):
        token = str(data['token']).lower()
        valid_tokens = Base.getValidKeys()
        if token not in valid_tokens:
            return jsonify({'error': f'Wrong token.'}), 422
