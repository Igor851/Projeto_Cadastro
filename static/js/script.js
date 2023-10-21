
 function Calcular(){
    let nota1 = parseInt(document.getElementById('n1').value)
    let tipo = typeof(nota1)
    let soma = nota1 + 2
    document.getElementById('resultado').innerHTML = 'o resultado é ' + soma + ' ' + nota1 + tipo
    
}

function Trocar(){
    document.getElementById('resultado').style.color = "red"
}

