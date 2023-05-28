// Declaração da função que imprime nome completo e empresa
function formataNomeEmpresa() {
  const nome = "Lucas";
  const sobrenome = "Jozefovicz";
  const empresa = "Kenzie Academy Brasil";

  console.log(
    `O nome completo é: ${nome} ${sobrenome}\nTrabalha na ${empresa}`
  );
}

// Execução da função declarada acima
formataNomeEmpresa();

//---------------------------------

// 1- Desenvolva uma função que mostre no console a frase "Hello World!".

function helloWord() {
  console.log("Hello, Word!");
}
helloWord();

// 2- Desenvolva uma função para saber se o(a) aluno(a) possui métricas para virar monitor(a).
// Requisitos:

// 100 de Entregas
// 100 de Entrevistas Técnicas
// 100 de Presença

function monitor() {
  const entregas = 100;
  const entrevistaTecnica = 100;
  const presenca = 100;

  if (entregas === 100 && entrevistaTecnica === 100 && presenca === 100) {
    console.log("possivel monitor");
  } else {
    console.log("escolher outro aluno");
  }
}

monitor();

// 3- Desenvolva uma função que recebe três variáveis com valores numéricos e identifica qual deles é o maior.

function numMaior() {
  const valor1 = 15;
  const valor2 = 10;
  const valor3 = 5;

  if (valor1 > valor2 && valor1 > valor3) {
    console.log(`${valor1} é o maior valor`);
  } else if (valor2 > valor1 && valor2 > valor3) {
    console.log(`${valor2} é o maior valor`);
  } else {
    console.log(`${valor3} é o maior valor`);
  }
}
numMaior();

// 4- Desenvolva uma função para mostrar no console a seguinte frase: "Meu nome é -nome e sobrenome-, e tenho -idade- anos".

function dadosPessoais() {
  const nome = "Naymi";
  const sobrenome = Prestes;
  const idade = 25;

  console.log(`meu nome é ${nome} ${sobrenome}, tenho ${idade} anos`);
}

// ----------------------- FUNCÇÕES COM RETORNO -------------------------

function calcularAreaCirculo() {
  const pi = 3.14;
  const areaCirculoDeRaioQuatro = pi * 4 * 4;
  return areaCirculoDeRaioQuatro;
}
console.log(calcularAreaCirculo());

// ------------------------------ PARAMETRO DE FUNÇÕES ----------------------------

function calcularAreaCirculo2(area) {
  const pi = 3.14;
  const areaCirculoDeRaioQuatro = pi * area * area;
  return areaCirculoDeRaioQuatro;
}
console.log(calcularAreaCirculo2(5));

// área do retangulo

function calculaAreaRetangulo(base, altura) {
  console.log(`base igual a: ${base}`);
  console.log(`altura igual a: ${altura}`);
  const areaRetangulo = (base * altura) / 2;
  return areaRetangulo;
}
console.log(calculaAreaRetangulo(5, 10));

// ------------ EXERCICIO FUNÇÕES COM PARAMETRO -----------------------

// 1- Desenvolva uma função com apenas um parâmetro. A função deve retornar o valor de caractere P se o parâmetro for positivo, e N se o parâmetro for zero ou negativo.
function valor(num) {
  if (num > 0) {
    return "P";
  } else {
    return "N";
  }
}
console.log(valor(0));

// 2- Desenvolva uma função que informe a quantidade de dígitos de um determinado número inteiro informado por parâmetro.

function digitos(dig) {
  const re = `${dig}`;
  return `${re.length} digitos`;
}
console.log(digitos(80));

// 3- Desenvolva uma função que some dois números passados por parâmetro. A soma só deve acontecer se o primeiro número passado por parâmetro for maior que o segundo.
// Caso contrário você deverá retornar a seguinte frase: "O primeiro número não maior que o segundo."

function maiorNumero(v1, v2) {
  //const result = v1 + v2;
  if (v1 > v2) {
    return `${v1} + ${v2} = ${v1 + v2}`;
  } else {
    return "O primeiro número não é maior que o segundo.";
  }
}
console.log(maiorNumero(4, 2));

// 4- Desenvolva uma função com 2 parâmetros. O primeiro deve se chamar palavra, e o segundo deve se chamar letra. Se a palavra passada no primeiro parâmetro começar com a letra passada como segundo parâmetro, retorne true. Se a palavra passada no primeiro parâmetro não começar com a letra passada no segundo parâmetro, retorne false.

function palavras(palavra, letra) {
  if (palavra[0] === letra) {
    return true;
  }
  return false;
}
console.log(palavras("amor", "a"));

// 5- Desenvolva uma função com dois parâmetros para saber se o horário corresponde com o funcionamento do /pergunta. O primeiro parâmetro deve-se chamar inicio, e o segundo deve-se chamar termino. Se o horário de inicio for maior ou igual a 11 e menor ou igual a 18, retorne "O /pergunta está em horário de funcionamento." Caso contrário retorne "O /pergunta não está em horário de funcionamento."

function atendimento(inicio, termino) {
  if (inicio >= 11 && termino <= 18) {
    return "O /pergunta está em horário de funcionamento.";
  }
  return "O /pergunta não está em horário de funcionamento.";
}
console.log(atendimento(11, 19));

// ----------------------- ECERCICIO DEBUGANDO COM CONSOLE.LOG --------------------------------------

// const algarismosEmUmNumero = (n) => {
//   let str = `${n}`;
//   let contagem = str.length;
//   console.log(contagem);

//   if (n !== parseInt(n)) {
//     console.log("entrou aqui");
//     contagem = contagem - 1;
//   }
//   return contagem;
// };
// algarismosEmUmNumero(3.141517);

const algarismosEmUmNumero = (n) => {
  let str = `${n}`;
  let contagem = str.length;
  console.log(contagem);

  if (n !== parseInt(n)) {
    contagem = contagem - 1;
    console.log(contagem);
  }
  console.log(contagem);
  return contagem;
};
algarismosEmUmNumero(3.141517);

// ---------------------------- REUTILIZANDO FUNÇÕES ------------------------
// numero par

const par = (num) => {
  if (num % 2 === 0) {
    return `${num} é um número par`;
  }
  return `${num} é um número impar`;
};
console.log(par(5));

const nomesPares = (etiqueta) => {
  if (par(etiqueta.length)) {
    return "verde";
  }
  return "vermelho";
};
console.log(nomesPares("sabonete"));

//------------------- EXERCICIO REUTILIZANDO FUNÇÕES -----------------------

// 1- Declare uma função somaReutilizavel que receberá dois parâmetros a e b.
// ° Desenvolva a lógica deste algoritmo para obter o resultado da soma dos dois parâmetros.
// ° Após isso e já fora da função, declare uma variável resultado e atribua um valor 0 a ela.
// ° Utilizando a função somaReutilizavel, você deve realizar a operação 10 + 10 e multiplicar por 5, armazenando o valor total na variável resultado.
// ° Mostre o valor da variável resultado através do console.

let resultado = 0;
const somaReutilizavel = (a, b) => {
  resultado = (a + b) * 5;
  console.log(resultado);
};
somaReutilizavel(4, 4);

// 2- É necessário obter o nome completo de um usuário e depois selecionar apenas as letras iniciais do nome e sobrenome, e para isso é possível desenvolver três funções para a tarefa ser concluída. Siga os tópicos a seguir:

// ° Declare uma função letraInicial que receberá dois parâmetros nome e sobrenome e retornará a apenas a primeira letra maiúscula de nome e a primeira letra maiúscula de sobrenome.
// ° Declare uma função nomeCompleto que não receberá parâmetros e retornará uma frase contendo as iniciais do nome e sobrenome. É necessário reutilizar a função letraInicial para retornar a seguinte frase: "As letras inicias do meu nome completo são -letraInicialDoNome- -letraInicialDoSobrenome-"
// ° Mostre a frase através do console.

const letraInicial = (nome, sobrenome) => {
  return `${(nome[0] + sobrenome[0]).toUpperCase()}`;
};
// console.log(letraInicial("Naymi", "Prestes"));

const nomeCompleto = () => {
  console.log(
    `As letras iniciais do seu nome são ${letraInicial("naymi", "Prestes")}`
  );
};
nomeCompleto();

// 3- O objetivo deste exercício é desenvolver três funções para obter um resultado final. É necessário obter o número de letras de um produto e verificar se o total de caracteres é par ou ímpar. Siga os tópicos a seguir:

// ° Declare uma função par que receberá um parâmetro n, e este parâmetro representa um número. Desenvolva a lógica para retornar true se o número foi par ou false se não for par.
// ° Declare uma função impar que receberá uma parâmetro n, e este parâmetro representa um número. Desenvolva a lógica para retornar true se o número foi ímpar ou false se não for ímpar.
// ° Declare uma função letrasProduto que receberá um parâmetro produto, e este produto representará uma string. Você deverá obter o número de caracteres, ou seja, o tamanho da palavra produto e reutilizando as funções par e impar você deverá verificar se o tamanho é par ou ímpar.
// ° Retorne "O número de letras deste produto é par" se o tamanho da palavra produto for par ou "O número de letras deste produto é ímpar" se o tamanho da palavra produto for ímpar.

const numPar = (n) => {
  if (n % 2 === 0) {
    return true;
  }
  return false;
};
console.log(numPar(2));

const numImpar = (n) => {
  if (n % 2 === 1) {
    return true;
  }
  return false;
};
console.log(numImpar(2));

const letrasProduto = (produto) => {
  //   let str = `${produto}`;
  //   let tam = str.length;

  if (numPar(produto.length)) {
    return "o tamanho desse produto é par";
  }
  return "o tamanho desse produto é impar";
};
console.log(letrasProduto("sabonetee"));

// --------------------- EXERCICIO ENCONTRANDO BUGS ---------------------------

//1 - Ao receber 80 para o peso e 1.80 para altura, a função deve retornar 24.691358024691358
function calculaIMC(peso, altura) {
  let alturaAoQuadrado = altura * altura;
  let imc = peso / alturaAoQuadrado;
  return imc;
}
console.log(calculaIMC(80, 1.8));

// 2- Ao receber os parâmetros: ("Pedro", 2002, 2030) a função deve retornar "Em 2030 Pedro terá 28 anos de idade".

function calculaIdade(nome, anoFuturo, anoNascimento) {
  let idade = anoFuturo - anoNascimento;
  return `Em ${anoFuturo} ${nome} terá ${idade} anos de idade`;
}
console.log(calculaIdade("Pedro", 2030, 2002));

// 3- Ao receber 3.14159265 a função deve retornar 9.
function algarismosEmUmNumero2(n) {
  let str = `${n}`;
  let contagem = str.length;

  if (n !== parseInt(n)) {
    return (contagem = contagem - 1);
  }
  return n;
}
console.log(algarismosEmUmNumero2(3.14159265));
