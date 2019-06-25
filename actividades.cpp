//Greedy ordenamiento de actividades
#include<stdio.h>
#include<iostream>
#define MAX 50

using namespace std;
int result[MAX]  ; //  Resultado
int in_act[MAX]  ; // Inicio actividad
int fin_act[MAX] ; //  Fin actividad


//Definicion de actividades
void ingresar_actividades(int n)
{
     for(int i=0; i<n; i++)
     {
            do
            {
                 cout << "  Actividad " << i+1 << endl<< endl ;
                 cout << "\tinicio : " ; cin >> in_act[i] ;
                 cout << "\tfinal  : " ; cin >> fin_act[i] ;
                 cout << endl ;
                 
            }while( in_act[i] > fin_act[i] ) ;  // evita que el inicio sea mayor que el final 

     }

}
//Imprimir el resultado

void imp_res(int n) 
{
     cout<<" Actividades ingresadas. "<<endl<<endl ;
     
     cout<<"\t\t Ai     :  " ;
     
     for(int i=0; i<n; i++) 
         cout<< i+1 <<' ';
         
     cout<<endl<<"\t\t-------------------------"<<endl ;
     
     
     cout<<"\t\t inicio :  " ;
     
     for(int i=0; i<n; i++)
         cout<< in_act[i] <<' ';
      
     cout<<endl ;
     cout<<"\t\t fin    :  " ;
     
     for(int i=0; i<n; i++)
         cout<< fin_act[i] <<' ';
         
}
//Orden por tiempo de finalizacion

void Ord_fin ( int n)
{
     int aux1, aux2, aux3, band = 1 ;

     for(int i=n-1; i>0 && band==1; i--)
     {
          band = 0;

          for(int j=0; j<i; j++)
          {
                 if( fin_act[j] > fin_act[j+1])
                 {
                      aux1   = fin_act[j]   ;
                      fin_act[j]   = fin_act[j+1] ;
                      fin_act[j+1] = aux1   ;

                      aux2   = in_act[j]   ;
                      in_act[j]   = in_act[j+1] ;
                      in_act[j+1] = aux2   ;

                      band = 1 ;
                 }
          }
     }
     
     imp_res(n) ;
     
}
//orden por tiempo de inicio

void Ord_in ( int n)
{
     int aux1, aux2, aux3, band = 1 ;

     for(int i=n-1; i>0 && band==1; i--)
     {
          band = 0;

          for(int j=0; j<i; j++)
          {
                 if( in_act[j] > in_act[j+1])
                 {
                      aux1   = fin_act[j]   ;
                      fin_act[j]   = fin_act[j+1] ;
                      fin_act[j+1] = aux1   ;

                      aux2   = in_act[j]   ;
                      in_act[j]   = in_act[j+1] ;
                      in_act[j+1] = aux2   ;

                      band = 1 ;
                 }
          }
     }
     
     imp_res(n);
     
}
//Orden por duracion

void Ord_dur ( int n)
{
     int aux1, aux2, aux3, band = 1 ;
     for(int i=n-1; i>0 && band==1; i--)
     {
          band = 0;

          for(int j=0; j<i; j++)
          {
                 if( (fin_act[j+1] - in_act[j+1]) < (fin_act[j] - in_act[j]))
                 {
                      aux1   = fin_act[j];
                      fin_act[j]   = fin_act[j+1];
                      fin_act[j+1] = aux1;

                      aux2   = in_act[j];
                      in_act[j]   = in_act[j+1];
                      in_act[j+1] = aux2;

                      band = 1;
                 }
          }
     }
     
     imp_res(n) ;
     
}
/*                         Devolviendo solucion
------------------------------------------------------------------------*/

void resultado()
{
    cout<<endl<<" La solucion voraz es: \n\n\t" ;
    
    int i = 0 ;
     
     while( 1 )
     {
            cout<<"A" << result[i] + 1 << ""  ;
            i ++ ;
            
            if(result[i]==0)
               break ;                     
     }
}
/*                         Algoritmo de solucion
------------------------------------------------------------------------*/

void sel_act( int n )
{    
     cout<<"Ordenamiento por tiempo de finalizacion"<<endl;
     Ord_fin ( n ) ;
     cout<<endl;
     cout<<"Ordenamiento por tiempo de incio"<<endl;
     Ord_in( n ) ;
     cout<<endl;
     cout<<"Ordenamiento por duracion"<<endl;
     Ord_dur( n ) ;
 
     int z , k = 1 ;

     result[0] = 0 ;
     z    = 0 ;

     for( int i=1; i<n; i++ )
     {
          if( in_act[i] >= fin_act[z] )
          {
              result[k] = i ;     // actividad seleccionada
              z    = i ;
              k++ ;

          }

     }
     
     
     resultado() ;

}
//Mensaje en pantalla
void scm()
{
    cout<<endl;
    cout<<"\t     º           METODO DE SELECCION DE ACTIVIDADES       º "<< endl ;
    
    cout<<"\t\t Hola mundo "<< endl; //nuevo
    
    cout<<endl;
}
                          
int main()
{	
    system("color 02");  scm();
    
    int N  ;
    cout<<"  Defina el numero de actividades: ";
    cin>> N ;

    cout<<endl ;

    ingresar_actividades( N );
    
    system("cls");   scm();
    
    sel_act( N ) ;


   cout<<endl<<endl ;
   system("pause");
   return 0 ;
   
/*   
Menu para seleccionar diferentes casos en el algoritmo greedy

printf("\n---------------MENU---------------\n");
printf("1) ......Tiempo de finalizacion.....\n");
printf("2) ........Tiempo de inicio.........\n");
printf("3) ........Tiempo de duracion.......\n");
printf("4) ............SALIR...........\n");	
scanf("%d",&op);
switch (op){
	case 1: Ord_fin();
	break;
	case 2: Ord_in();
	break;
	case 3: Ord_dur();
	break;
}	*/
}
