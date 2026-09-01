% rebase('base.tpl', titulo_pagina='Fluxograma', css_extra='<link rel="stylesheet" href="/css/fluxo.css">')

<div class="fluxograma">
    <h1>Visualizar Fluxograma</h1>

    <div class="resultado-fluxo">
        um quadrado gigantesco com o fluxograma aqui 😨
    </div>

    <form action="/fluxograma" method="POST">
        <div>
            <label for="lim_horas">Limite de Horas por semestre</label>
            <input type="number" id="lim_horas" name="lim_horas" min="1" required>
        </div>
        <button type="submit">Calcular Fluxograma</button>
    </form>
</div>

<div class="materias">

    <div class="config">
    <h1>Configurar Matérias</h1>

    <form action="/add" method="POST">
        <div>
            <label for="materia">Nome/Código da Matéria</label>
            <input type="text" id="materia" name="materia" required>
        </div>
        <div>
            <label for="horas">Horas de Matéria</label>
            <input type="number" id="horas" name="horas" min="1" required>
        </div>
        <div>
            <label>Pré-Requisitos</label>
            <div id="container-requisitos">
                <div class="requisito-linha" style="margin-bottom: 5px;">
                    <input type="text" name="requisitos" placeholder="Ex.: CIC0004 ou APC">
                </div>
            </div>
            <button type="button" onclick="adicionarRequisito()" style="margin-top: 5px; font-size: 0.9em;">
                Adicionar outro pré-requisito
            </button>
        </div>
        <button type="submit">Adicionar Matéria</button>
    </form>
</div>

<div class="lista-materias">
    <h1>Lista de Matérias</h1>

    % for materia, componentes in grafo.items():
        <div class="materia-info">
            <p>{{materia}}</p>
            <p>{{horas[materia]}} Horas</p>
            <p>Pré-requisito de:
                % if componentes:
                    <span>{{', '.join(componentes)}}</span>
                % else:
                    <span>Nenhuma matéria.</span>
                % end
            </p>
            <form action="/exclude" method="POST">
                <input type="hidden" name="materia_alvo" value="{{materia}}">
                <button type="submit">Excluir matéria</button>
            </form>
        </div>
    % end
</div>

</div>

<script>
    function adicionarRequisito() {
        const container = document.getElementById('container-requisitos');

        const novaLinha = document.createElement('div');
        novaLinha.className = 'requisito-linha';
        novaLinha.style.marginBottom = '5px';

        novaLinha.innerHTML = `
            <input type="text" name="requisitos" placeholder="Ex.: CIC0004 ou APC">
            <button type="button" onclick="this.parentElement.remove()" style="color: red; border: none; background: none; cursor: pointer;">Remover</button>
        `;

        container.appendChild(novaLinha);
    }
</script>