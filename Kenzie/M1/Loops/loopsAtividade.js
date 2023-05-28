// 1- Escreva uma função chamada renderUpToTwenty. Quando a função for chamada, os números de 0 a 20 devem ser impressos no console.

const renderUpToTwenty = () => {
  for (let i = 0; i <= 20; i++) {
    console.log(i);
  }
};
renderUpToTwenty();

// 2- Escreva uma função chamada tenInTenToAHundred(). Quando a função for chamada, os números de 10 a 100, contando de 10 em 10, devem ser impressos no console.

const tenInTenToAHundred = () => {
  for (let i = 10; i <= 100; i += 10) {
    console.log(i);
  }
};
tenInTenToAHundred();

// 3- Escreva uma função chamada oddUpToTwenty(). Quando a função for chamada, apresente no console os valores entre 0 e 20 que forem ímpares.

const oddUpToTwenty = () => {
  for (let i = 0; i < 20; i++) {
    if (i % 2 !== 0) {
      console.log(i);
    }
  }
};
oddUpToTwenty();
console.log("-------------------------");

// 4- Escreva uma função chamada evenUpToTwenty(). Quando a função for chamada, apresente no console os valores entre 0 e 20 que forem pares.

const evenUpToTwenty = () => {
  for (let i = 0; i <= 20; i++) {
    if (i % 2 === 0) {
      console.log(i);
    }
  }
};
evenUpToTwenty();
console.log("-------------------------");

// 5- Escreva uma função chamada fromNegativeToPositive(). Quando a função for chamada, apresente os valores de -10 a 0.

const fromNegativeToPositive = () => {
  for (let i = -10; i <= 0; i++) {
    console.log(i);
  }
};
fromNegativeToPositive();
console.log("-------------------------");

// 6- Escreva uma função chamada inDescendingDirection. Quando a função for chamada, apresente valores de 10 a 0 no console.

const inDescendingDirection = () => {
  for (let i = 10; i >= 0; i--) {
    console.log(i);
  }
};
inDescendingDirection();
console.log("-------------------------");

// 7- Escreva uma função chamada toSquare(). Quando a função for chamada, apresente o quadrado dos valores da sequência de 1 a 10.

const toSquare = () => {
  let result = 0;
  for (let i = 1; i <= 10; i++) {
    result = i ** 2;
    console.log(result);
  }
};
toSquare();
console.log("-------------------------");
