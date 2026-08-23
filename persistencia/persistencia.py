import json
import os

class GerenciadorPersistencia:
    def __init__(self, nome_arquivo =  'fluxo.json'):
        self.arquivo = nome_arquivo

    def carregar(self):
        if not os.path.exists(self.arquivo):
            return {}

        with open(self.arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def salvar(self, dados):
        with open(self.arquivo, 'w', enconding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        

