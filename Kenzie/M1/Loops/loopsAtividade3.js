// 1- A função quando chamada deve apresentar os valores da sequência numérica de Fibonacci até o décimo quinto termo.

const fibonacciNumbers = () => {
  let anterior = 0,
    proximo = 0;
  //proximo + anterior

  for (let atual = 0; atual <= 5; atual++) {
    console.log("result anterior", (anterior = atual));
    console.log("anterior", anterior);
    console.log("result proximo", (proximo = atual + anterior));
    console.log("proximo", proximo);
  }
};
fibonacciNumbers();
