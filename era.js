function eratostenes(n) {
    let primos = Array(n + 1).fill(true);
    let p = 2;
    while (p * p <= n) {
        if (primos[p] === true) {
            for (let i = p * p; i <= n; i += p) {
                primos[i] = false;
            }
        }
        p++;
    }
    let resultado = [];
    for (let p = 2; p <= n; p++) {
        if (primos[p]) {
            resultado.push(p);
        }
    }
    return resultado;
}

let n = 100000000;
let inicio = Date.now();
let res = eratostenes(n);
let fin = Date.now();

console.log(res);
console.log("Tiempo de ejecución: " + (fin - inicio) / 1000 + " segundos");