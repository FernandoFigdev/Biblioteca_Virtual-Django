document.getElementById("form-cadastro-usuario").addEventListener("submit", async function(event) {
    event.preventDefault();

    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;
    const confirmacaoSenha = document.getElementById("confirmacao-senha").value;
    const tipoUsuario = document.getElementById("tipo-usuario").value;

    if (senha !== confirmacaoSenha) {
        document.getElementById("mensagem").textContent = "As senhas não coincidem.";
        return;
    }

    // Obtém o token CSRF
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    try {
        const response = await fetch("http://127.0.0.1:8000/api/usuarios/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,  // Adiciona o token CSRF ao cabeçalho
            },
            body: JSON.stringify({
                nome_completo: nome,
                email: email,
                senha: senha,
                tipo_usuario: tipoUsuario,
            }),
        });

        if (response.ok) {
            document.getElementById("mensagem").textContent = "Usuário cadastrado com sucesso!";
            document.getElementById("mensagem").style.color = "green";
            document.getElementById("form-cadastro-usuario").reset();
        } else {
            const data = await response.json();
            document.getElementById("mensagem").textContent = data.detail || "Erro ao cadastrar usuário.";
        }
    } catch (error) {
        console.log(data); // Adicione isto para verificar o que está retornando
        document.getElementById("mensagem").textContent = "Erro ao conectar com o servidor.";
    }
});
