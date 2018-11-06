import java.util.Scanner;

public class GSeidel {
    
    public static void main(String [] args){
		
        /*double [][] numeros = {{45,13,-4,8},
                            {-5,-28,4,-14},
                            {9,15,63,-7},
                            {2,3,-8,-42}};*/

        //double [] b = {-25,82,75,-43};

        //double [] x0 = {2,2,2,2};

        Scanner scan = new Scanner(System.in);

		int tamA, iter;
        double tolerancia;


		System.out.println("Ingrese el tamaño de la matriz cuadrada A: ");
		tamA = scan.nextInt();
		
		double [][] matrizA = new double[tamA][tamA];
		

        System.out.println("Ingrese cada valor de la matriz de coeficientes empezando por la primera fila");
		for(int i = 0;i < tamA;i++){
			for(int j = 0;j < tamA;j++){
				System.out.print("Posicion [" + i + "]" + "[" + j + "]: ");
				matrizA[i][j] = scan.nextDouble();
				
			}
			
		}

        
        double [] b = new double[tamA];

        System.out.println("Ingrese los " + tamA + " valores del vector b");
        for(int i = 0;i < tamA;i++){
            System.out.print("Posicion [" + i + "]: ");
                b[i] = scan.nextDouble();
        }
                            
        
        
        
        double [] x0 = new double[tamA];

        System.out.println("Ingrese los " + tamA + " valores del vector de x aproximados");
        for(int i = 0;i < tamA;i++){
            System.out.print("Posicion [" + i + "]: ");
                x0[i] = scan.nextDouble();
        }

        System.out.println("Ingrese el número de iteraciones: ");
        iter = scan.nextInt();

        System.out.println("Ingrese la tolerancia: ");
        tolerancia = scan.nextDouble();


        gaussSeidel(matrizA,b,tolerancia,iter,x0,tamA);
        
        
    }
    
	public static void gaussSeidel(double[][] A, double [] b, double tol, int iter, double[] x0, int n)
    {
        double[] x = new double[n];
        double aux;
        int cont = 0;
        double error = tol+1;
        
        System.out.println("Iteracion x1" + "\t" + "x2" + "\t" + "x3" + "\t" + "x4" + " ... " + "xn" + "\t" + "error");
        System.out.print(0 + " | ");
        imprimirVector(x0,n);
        System.out.println();
        
        while(error > tol && cont < iter)
        {
            if(cont != 0)
                System.out.print(cont + " | ");
            error = 0;
                	
            for(int i = 0; i < n; i++)
            {
                if(cont != 0)
                    System.out.print(x[i] + " ");
                double suma = 0;
                
                for (int j = 0; j < n; j++)
                {
                    if (i != j)
                    {
                        suma += A[i][j]*x0[j];
                    }
                }

                x[i] = (b[i] - suma)/A[i][i];
                aux = x[i]-x0[i];
                error += Math.abs(aux);
                x0[i] = x[i];
                
            }
            
            if(cont != 0)
                System.out.println(error);
            cont++;
        }
        
        
        if(error < tol)
        {
            System.out.println("La solucion aproxima del sistema es: ");
            System.out.print("x = [");


            for(int i = 0; i < n; i++){
                System.out.print(x[i] + ", ");
            }
            System.out.println("]");

        }else{
                
            System.out.println("Fracaso en esas iteraciones" + "\t" + cont);
                
        }   
    }
	
	public static void imprimirVector(double[] vector, int n){
        for(int i = 0;i<n;i++){
            System.out.print(vector[i] + " ");
        }
    }
    
}