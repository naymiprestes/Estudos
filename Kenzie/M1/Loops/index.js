// ------------------ WHILE ------------------------

//Adicionamos uma condição após a palavra-chave "while",
// e fornecemos um bloco que é executado até que a condição seja avaliada como false.

// const fruits = ["banana", "maça", "abacate"];
// let i = 0;
// while (i < fruits.length) {
//   console.log(fruits[i]); //valor
//   console.log(i); //índice
//   i = i + 1;
// }

// ------------------- DO WHILE --------------------------

// É basicamente o mesmo que while, mas a condição é avaliada depois que o bloco de código é executado.
// O bloco será executado pelo menos uma vez.

// const list = ["a", "b", "c"];
// let i = 0;
// do {
//   console.log(list[i]); //valor
//   console.log(i); //índice
//   i = i + 1;
// } while (i < list.length);

// ---------------------- FOR ---------------------

// 1 - A inicialização: momento em que a variável de controle será declarada. Essa instrução será executada apenas uma vez.
// 2 - A condição de parada: é nesse momento que será definido até que ponto o loop deve executar:
//    ° Se a condição for false o loop for é encerrado;
//    ° Se a condição for true o loop for é executado.
// 3 - A iteração: Atualiza o valor da variável de controle caso a condição seja true.
// 4 - Por último, a condição é avaliada novamente. Esse processo continua até que a condição seja false.

// Exibir os números de 1 à 5
const n = 5;
// looping de i = 1 até 5
// em cada iteração, i é aumentado em 1
for (let i = 1; i <= n; i++) {
  console.log(i); // imprimindo o valor de i
}
