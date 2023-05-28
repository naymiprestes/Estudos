// 1- Escreva uma função que apresente como resultado os quadrados dos números inteiros existentes na faixa de valores de 15 a 200.

const squareNumber = () => {
  let square = 0;
  for (let i = 15; i <= 200; i++) {
    square = i ** 2;
    console.log(square);
  }
};
squareNumber();
console.log("---------------------------------");

// 2-

const sumNumber = () => {
  let sum = 0;
  for (let i = 1; i <= 100; i++) {
    sum += i;
  }
  console.log(sum);
};
sumNumber();
console.log("---------------------------------");

// 3- Escreva uma função que apresente todos os valores numéricos menores que 200 que são divisíveis por 4.

const divisibleByFour = () => {
  for (let i = 0; i < 200; i++) {
    if (i % 4 === 0) {
      console.log(i);
    }
  }
};
divisibleByFour();
console.log("---------------------------------");

// 4- Escreva uma função que calcule o resultado da soma e da média aritmética dos valores pares situados na faixa numérica de 50 até 70.

// média_aritmética = soma / qtd_numeros_pares_no_intervalo⁠
// Saída: A soma é 660 e a média é 60.

const sumAverage = () => {
  let sum = 0;
  let average = 0;

  for (let i = 50; i <= 70; i++) {
    if (i % 2 === 0) {
      sum += i;
    }
    console.log("i", i);
    console.log("sum", sum);
    // average = sum / i;
  }
  console.log(`soma: ${sum} - média aritmética: ${average}`);
};
sumAverage();
console.log("---------------------------------");
