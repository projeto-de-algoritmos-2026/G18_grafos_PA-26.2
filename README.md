# G18_grafos_PA-26.2

---

*Número da Lista*: 18  
*Conteúdo da disciplina*: Grafo 1

---

## Alunos

| Matrícula  | Aluno                          |
|------------|-------------------------------|
| 251023282  | Josef Wojtyla Barros de Souza |
| 251020226  | Eduardo de Sousa Brito        |

---

## Sobre

Este projeto implementa um **Planejador de Fluxograma de Matérias** usando grafos com lista de adjacência.

O usuário cadastra matérias com suas respectivas cargas horárias e pré-requisitos. O sistema então aplica um **algoritmo de ordenação topológica** para distribuir as matérias em semestres, respeitando:

- As dependências entre matérias (pré-requisitos)
- Um limite máximo de horas por semestre definido pelo usuário

A interface é uma aplicação web simples construída com o microframework **Bottle (Python)**.

### Funcionalidades

- [x] Cadastro de matérias com carga horária e pré-requisitos
- [x] Validação de pré-requisitos (a matéria pré-requisito deve existir antes)
- [x] Prevenção de duplicidade de matérias
- [x] Geração automática do fluxograma por semestres
- [x] Visualização da lista de matérias e suas dependências

---

## Vídeo de Apresentação

[Youtube](https://youtu.be/jkYmwi9yjkA)

---

## Instalação

### Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- `pip` instalado

### Passo a passo

**1. Clone o repositório:**

```bash
git clone https://github.com/projeto-de-algoritmos-2026/G18_grafos_PA-26.2.git
cd G18_grafos_PA-26.2
```

**opcional:**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt

python main.py

acesse:
http://localhost:8080

```
