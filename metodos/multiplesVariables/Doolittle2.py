/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package analisisnumerico;

import java.util.Arrays;

/**
 *
 * @author nicolasmunera
 */
public class FactorizacionDoolittle {

     public static void factorizacionDirectaDoolittle(double A[][], double[] b, int n){
        double [][] L = new double[n][n];
        double [][] U = new double[n][n];
       
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i<j){
                   U[i][j] = Double.POSITIVE_INFINITY;
                   L[i][j] = 0;
                }else if(i>j){
                    L[i][j] = Double.POSITIVE_INFINITY;
                    U[i][j] = 0;
                }else if(i==j){
                    L[i][j] = 1;
                    U[i][j] = Double.POSITIVE_INFINITY;
                }
            }
        }
        System.out.println("Etapa 0");
        System.out.println("Matriz A");
        imprimirMatriz(A, n);
        System.out.println("Matriz L");
        imprimirMatriz(L, n);
        System.out.println("Matriz U");
        imprimirMatriz(U, n);
              
        for(int k = 1; k < n+1; k++){
            System.out.println("Etapa "+k);
            System.out.println("Encontrar la columna "+k+" de L y la fila "+ k+" de U.");
            System.out.println("Matriz A");
            imprimirMatriz(A, n);
            double suma = 0;
            for(int p = 0; p < k-1; p++){
                suma += L[k-1][p] * U[p][k-1];
            }
            U[k-1][k-1] = (A[k-1][k-1] - suma)/L[k-1][k-1];
            
            for(int j = k+1; j < n+1; j++){
                suma = 0;
                for(int p = 0; p < k-1; p++){
                    
                    suma += L[k-1][p] * U[p][j-1];
                }
                U[k-1][j-1] = (A[k-1][j-1] - suma)/L[k-1][k-1];
            }
            System.out.println("Matriz L");
            imprimirMatriz(L, n);
            for(int i = k+1; i < n+1; i++){
                suma = 0;
                for(int p = 0; p < k-1; p++){
                    suma += L[i-1][p] * U[p][k-1];
                }
                L[i-1][k-1] = (A[i-1][k-1] - suma)/U[k-1][k-1];
            } 
            System.out.println("Matriz U");
            imprimirMatriz(U, n);
        }
        
        System.out.println("\nSustitución Progresiva Lz=b");
        double[] z = sustitucionProgresiva(L, b);
        System.out.println("Z:"+Arrays.toString(z));
        System.out.println("\nSustitución Regresiva Ux=z");
        double[] x = sustitucionRegresiva(U, z);
        for(int i = 0; i < x.length; i++){
            System.out.println("X" + (i+1) + " = " + x[i]);
        }
    }
    
    public static double[] sustitucionProgresiva(double[][] L, double[] b){
        int n = L.length;
        double x[] = new double[n];
        for(int i = 1; i < n+1; i++){
            double suma = 0;
            for(int p = i-1; p > 0; p--){
                double a = L[i-2][p];
                double c = x[p-1];
                suma += (L[i-1][p-1] * x[p-1]);
            }
            x[i-1] = (b[i-1] - suma) / L[i-1][i-1];
        }
        return x;
    }

    public static double[] sustitucionRegresiva(double[][] U, double[] z){
        int n = U.length;
        double[] x = new double[n];
       
        for(int i = n-1; i>=0; i--){
            double suma = 0;
            for(int j = i+1; j<n; j++){
                suma += U[i][j] * x[j];
            }
            x[i] = (z[i]- suma) /U[i][i];
        }
        return x;
    }
    
    public static void imprimirMatriz(double [][] matrix, int n){
        for(int i=0; i< n;i++){
            for(int j=0; j <n; j++){
                System.out.print(matrix[i][j]);
                printSpaces(String.valueOf(matrix[i][j]).length(),30);
            }
            System.out.print("\n");
        }
        System.out.println("");
    }
    
    public static void printSpaces(int n, int k){
        if(n<k){
            for(int i = 0; i<k-n;i++){
                System.out.print(" ");
            }
        }
    }
    
}