import java.math.*;

import com.udojava.evalex.*;

public class Secante {
	
	public static void main(String[] args) {
		System.out.println("Hola estamos corriendo el metodo de la secante");
		ensayo(2, 3, 0.0001, 8);
	}

	public static void ensayo(double x1, double x2,  double tolerancia, int niteraciones){
		System.out.println("Imprimiendo datos de entrada:");
		System.out.println(x1);
		System.out.println(x2);
		System.out.println(tolerancia);
		System.out.println(niteraciones);
		double suma = x1+x2+tolerancia+niteraciones;
		System.out.println("Suma: " + suma);

		Expression expression = new Expression("sin(45)").setPrecision(50);
  		BigDecimal result = expression.eval();
  		System.out.println("Expression: " + result);

	}

}
