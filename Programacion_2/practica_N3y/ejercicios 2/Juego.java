public class Juego {
    protected int numeroDeVidas;
    protected static int record = Integer.MAX_VALUE;
    protected int vidasIniciales;

    public Juego(int vidas) {
        if (vidas <= 0) {
            throw new IllegalArgumentException("Las vidas deben ser mayores que cero.");
        }
        this.vidasIniciales = vidas;
        this.numeroDeVidas = vidas;
    }

    public void reiniciaPartida() {
        numeroDeVidas = vidasIniciales;
    }

    public void actualizaRecord() {
        int vidasUsadas = vidasIniciales - numeroDeVidas;
        if (vidasUsadas < record) {
            record = vidasUsadas;
            System.out.println("Nuevo record: " + record + " intento(s) fallido(s).");
        } else {
            System.out.println("Record actual: " + record);
        }
    }

    public boolean quitaVida() {
        numeroDeVidas--;
        System.out.println("Vidas restantes: " + numeroDeVidas);
        return numeroDeVidas > 0;
    }
}
