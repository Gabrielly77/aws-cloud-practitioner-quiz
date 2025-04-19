const quizData = [
    { pergunta: "Qual serviço AWS gerencia usuários?", opcoes: ["EC2", "IAM", "S3", "Lambda"], resposta: "IAM" },
    { pergunta: "Qual serviço AWS é usado para balanceamento de carga?", opcoes: ["S3", "EC2", "ELB", "RDS"], resposta: "ELB" }
];

let index = 0;

function carregarPergunta() {
    if (index < quizData.length) {
        document.getElementById("pergunta").innerText = quizData[index].pergunta;
        let opcoesHTML = "";
        quizData[index].opcoes.forEach(opcao => {
            opcoesHTML += `<button onclick="verificarResposta('${opcao}')">${opcao}</button>`;
        });
        document.getElementById("opcoes").innerHTML = opcoesHTML;
    } else {
        document.getElementById("pergunta").innerText = "Você completou o quiz!";
        document.getElementById("opcoes").innerHTML = "";
    }
}

function verificarResposta(opcaoEscolhida) {
    if (opcaoEscolhida === quizData[index].resposta) {
        alert("Correto!");
    } else {
        alert("Errado!");
    }
    index++;
    carregarPergunta();
}

window.onload = carregarPergunta;
