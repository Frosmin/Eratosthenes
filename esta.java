import java.util.ArrayList;
import java.util.Arrays;

public class Eratostenes {
    public static ArrayList<Integer> eratostenes(int n) {
        boolean[] primos = new boolean[n + 1];
        Arrays.fill(primos, true);
        int p = 2;
        while (p * p <= n) {
            if (primos[p]) {
                for (int i = p * p; i <= n; i += p) {
                    primos[i] = false;
                }
            }
            p++;
        }
        ArrayList<Integer> resultado = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (primos[i]) {
                resultado.add(i);
            }
        }
        return resultado;
    }

    public static void main(String[] args) {
        int n = 100000000;
        long inicio = System.currentTimeMillis();
        ArrayList<Integer> res = eratostenes(n);
        long fin = System.currentTimeMillis();

        for (int primo : res) {
            System.out.print(primo + " ");
        }
        System.out.println();
        System.out.println("Tiempo de ejecución: " + (fin - inicio) / 1000.0 + " segundos");
    }
}