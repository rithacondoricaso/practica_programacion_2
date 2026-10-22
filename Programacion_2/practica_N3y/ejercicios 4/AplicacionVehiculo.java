public class AplicacionVehiculo {
    public static void main(String[] args) {
        VehiculoAutonomo vehiculo = new VehiculoAutonomo("VA-01", "4K", 120);
        vehiculo.activarSensores();
        vehiculo.mostrarEstado();
        vehiculo.desactivarSensores();
    }
}
