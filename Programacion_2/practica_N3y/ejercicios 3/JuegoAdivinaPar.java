public class JuegoAdivinaPar extends JuegoAdivinaNumero {
    public JuegoAdivinaPar(int vidas) { super(vidas); }

    @Override
    public boolean validaNumero(int numero) {
        if (numero < 0 || numero > 10) {
            System.out.println("Error: el numero debe estar entre 0 y 10.");
            return false;
        }
        if (numero % 2 != 0) {
            System.out.println("Error: debes ingresar un numero par.");
            return false;
        }
        return true;
    }
}
