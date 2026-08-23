import json
import os

from persistencia import GerenciadorPeristencia

banco = GerenciadorPeristencia()
graph = banco.carregar()
banco.salvar(graph)

