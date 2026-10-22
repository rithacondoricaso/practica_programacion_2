public class AplicacionJuegos {
    public static void main(String[] args) {
        JuegoAdivinaNumero normal = new JuegoAdivinaNumero(3);
        JuegoAdivinaPar pares = new JuegoAdivinaPar(3);
        JuegoAdivinaImpar impares = new JuegoAdivinaImpar(3);

        System.out.println("\\n=== Juego de cualquier numero ===");
        normal.juega();
        System.out.println("\\n=== Juego de numeros pares ===");
        pares.juega();
        System.out.println("\\n=== Juego de numeros impares ===");
        impares.juega();
    }
}
