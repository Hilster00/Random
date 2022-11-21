#include <stdio.h>

//funcao para printar a digonal principal da matriz
void diagonal_principal(int *matriz, int tamanho){
    int i;
    
    printf("Valores:[");
    for(i=0;i<tamanho-1;i++){
        printf("%d,",*(matriz+i+(i*tamanho)));
    }
    printf("%d]",*(matriz+i+(i*tamanho)));
}



int main(){
    int tamanho=0,i,j;
    while(tamanho<1){
        printf("Digite o tamanho da matriz:");
        scanf("%d", &tamanho);
    }
    int matriz[tamanho][tamanho];
    
    for(i=0;i<tamanho;i++){
        for(j=0;j<tamanho;j++){
            printf("Digite o valor da matriz[%i][%i]:",i,j);
            scanf("%d",&matriz[i][j]);
        }
    }
    
    diagonal_principal(&matriz[0][0],tamanho);
    
    return 0;
}
