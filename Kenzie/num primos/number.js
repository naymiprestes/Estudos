const primeNumber = () => {
  let num = 4;
  for (i = 0; i <= num; i++) {
    if (num % 1 === 0 && num % num === 0) {
      return `${num} é um numero primo`;
    }
    return `${num} não é um número primo`;
  }
};
console.log(primeNumber(4));
