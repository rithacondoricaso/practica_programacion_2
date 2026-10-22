import java.util.Random;
import java.util.Scanner;

public class JuegoAdivinaNumero extends Juego {
    protected int numeroAAdivinar;
    protected final Scanner teclado;

    public JuegoAdivinaNumero(int vidas) {
        super(vidas);
        teclado = new Scanner(System.in);
    }

    public boolean validaNumero(int numero) {
        return numero >= 0 && numero <= 10;
    }

    public void juega() {
        reiniciaPartida();
        numeroAAdivinar = new Random().nextInt(11);
        System.out.println("Adivina un numero entre 0 y 10.");

        while (numeroDeVidas > 0) {
            System.out.print("Tu intento: ");
            if (!teclado.hasNextInt()) {
                System.out.println("Entrada no valida. Escribe un entero.");
                teclado.next();
                continue;
            }

            int intento = teclado.nextInt();
            if (!validaNumero(intento)) {
                System.out.println("El numero debe estar entre 0 y 10.");
                continue;
            }

            if (intento == numeroAAdivinar) {
                System.out.println("Acertaste!!");
                actualizaRecord();
                return;
            }

            if (!quitaVida()) {
                System.out.println("Sin vidas. El numero era " + numeroAAdivinar);
                return;
            }

            System.out.println(intento < numeroAAdivinar
                    ? "El numero a adivinar es mayor."
                    : "El numero a adivinar es menor.");
        }
    }
}
