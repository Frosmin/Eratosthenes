#include <iostream>
#include <vector>
#include <ctime>

std::vector<int> eratostenes(int n) {
    std::vector<bool> primos(n + 1, true);
    int p = 2;
    while (p * p <= n) {
        if (primos[p] == true) {
            for (int i = p * p; i <= n; i += p) {
                primos[i] = false;
            }
        }
        p++;
    }
    std::vector<int> resultado;
    for (int p = 2; p <= n; p++) {
        if (primos[p]) {
            resultado.push_back(p);
        }
    }
    return resultado;
}

int main() {
    int n = 100000000;
    std::clock_t inicio = std::clock();
    std::vector<int> res = eratostenes(n);
    std::clock_t fin = std::clock();

    for (int primo : res) {
        std::cout << primo << " ";
    }
    std::cout << std::endl;
    std::cout << "Tiempo de ejecución: " << (fin - inicio) / (double) CLOCKS_PER_SEC << " segundos" << std::endl;

    return 0;
}