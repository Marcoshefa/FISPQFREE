function trocaCor() {
    let elemento = document.getElementById("titulo");
    elemento.style.color = 'blue';
}

function chamaLogin() {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    let corpoRequisicao = {
        "email": email,
        "password": password
    }
    let rota = 'http://localhost:5000/login'

    fetch(rota, {
        method: 'POST',
        headers: {
            'Accept': '*/*',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(corpoRequisicao)
    })
    .then(result => {
        if (result.ok) {
            result.json().then(resposta => {
                mostraAlerta(true, resposta.message)
            })
        } else {
            result.text().then(erro => {
                mostraAlerta(false, erro)
            })
        }
    })
}

function mostraAlerta(status, mensagem) {
    let divAlerta = document.getElementById("alerta");
    divAlerta.style.display = 'block';

    if (status === true) {
        divAlerta.style.background = 'green';
    } else {
        divAlerta.style.background = 'red';
    }

    divAlerta.innerHTML = mensagem;
}

function limpar() {
    let divAlerta = document.getElementById("alerta");
    divAlerta.style.display = 'none';

    document.getElementById("email").value = '';
    document.getElementById("password").value = '';
}