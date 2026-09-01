<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ get('titulo_pagina', 'Fluxograma') }}</title>
    <link rel="stylesheet" href="/static/css/base.css?v=2">
    {{!get('css_extra','') }}
</head>
<body>
    <header>
        <nav class="navbar">
            <a href="/" class="btn-navbar">
                <div class="btn-navbar-content">
                    Fluxograma
                </div>
            </a>
            <a href="/" class="btn-navbar">
                <div class="btn-navbar-content">
                    Adicionar Materias
                </div>
            </a>
            <a href="/" class="btn-navbar">
                <div class="btn-navbar-content">
                    Lista de Matérias
                </div>
            </a>
        </nav>
    </header>

    <main>
        {{!base}}
    </main>

    <footer>
        &copy; 2026 G18 - Projeto de Algoritmos . Todos os direitos reservados.
    </footer>
</body>
</html>