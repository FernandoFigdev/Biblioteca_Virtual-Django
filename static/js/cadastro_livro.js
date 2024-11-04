document.getElementById("form-cadastro-livro").addEventListener("submit", async function(event) {
    event.preventDefault();

    const titulo = document.getElementById("titulo").value;
    const autor = document.getElementById("autor").value;
    const isbn = document.getElementById("isbn").value;
    const editora = document.getElementById("editora").value;
    const ano = document.getElementById("ano").value;
    const genero = document.getElementById("genero").value;
    const quantidade = document.getElementById("quantidade").value;

    // Obtém o token CSRF
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    try {
        const response = await fetch("http://127.0.0.1:8000/api/livros/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,  // Adiciona o token CSRF ao cabeçalho
            },
            body: JSON.stringify({
                titulo: titulo,
                autor: autor,
                isbn: isbn,
                editora: editora,
                ano_publicacao: ano,
                genero: genero,
                quantidade_total: quantidade,
                quantidade_disponivel: quantidade, // Inicialmente igual ao total
            }),
        });

        if (response.ok) {
            document.getElementById("mensagem").textContent = "Livro cadastrado com sucesso!";
            document.getElementById("mensagem").style.color = "green";
            document.getElementById("form-cadastro-livro").reset();
        } else {
            const data = await response.json();
            document.getElementById("mensagem").textContent = data.detail || "Erro ao cadastrar livro.";
        }
    } catch (error) {
        document.getElementById("mensagem").textContent = "Erro ao conectar com o servidor.";
    }
});
