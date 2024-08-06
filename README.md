# Algoritmo-Recursivo-Torre-de-Hanoi-Assembly-RISC-V

# Funcionamento do Algoritmo da Torre de Hanói
## Algoritmo da Torre de Hanói

<p align="justify">Torre de Hanói é um quebra-cabeça que consiste em uma base contendo três pinos, em um dos quais são dispostos alguns discos uns sobre os outros, em ordem crescente de diâmetro, de cima para baixo. O problema consiste em passar todos os discos de um pino para outro qualquer, usando um dos pinos como auxiliar, de maneira que um disco maior nunca fique em cima de outro menor em nenhuma situação. O número de discos pode variar sendo que o mais simples contém apenas três.</p>

[Torre de Hanói – Wikipédia, a enciclopédia livre](https://pt.wikipedia.org/wiki/Torre_de_Han%C3%B3i)

## Objetivo
<p align="justify">
O objetivo do quebra-cabeça é mover toda a pilha de discos para outra vareta, seguindo estas regras:

1. Apenas um disco pode ser movido por vez.
2. Cada movimento consiste em pegar o disco do topo de uma das pilhas e movê-lo para outra vareta.
3. Um disco maior não pode ser colocado em cima de um disco menor.</p>

## Solução Recursiva

<p align="justify">O algoritmo da Torre de Hanói pode ser resolvido de forma recursiva. A ideia é dividir o problema em subproblemas menores. Aqui está a descrição passo a passo do algoritmo:</p>

### Passos

1. Mova os `n-1` discos de `A` para `B`, usando `C` como auxiliar.
2. Mova o disco restante de `A` para `C`.
3. Mova os `n-1` discos de `B` para `C`, usando `A` como auxiliar.
---
# Algoritmo em Python 
## Código

```python
def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    torre_hanoi(n-1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    torre_hanoi(n-1, auxiliar, destino, origem)

if __name__ == '__main__':
    # Exemplo de uso
    n = int(input("Digite o número de discos: "))
    torre_hanoi(n, "A", "C", "B")
```

## Funcionamento do Algoritmo

O algoritmo resolve o problema da Torre de Hanói movendo `n` discos da vareta `origem` para a vareta `destino`, utilizando uma vareta `auxiliar` para ajudar. A função `torre_hanoi` é chamada recursivamente para resolver subproblemas menores.

### Passos Detalhados

1. **Caso Base**:
   - Se `n` é igual a 1 (caso base), apenas um movimento é necessário: mover o disco diretamente da `origem` para o `destino`.
   - ```python
     if n == 1:
         print(f"Mova o disco 1 de {origem} para {destino}")
         return
     ```
   - Isso imprime a instrução de mover o disco 1 e retorna para onde a função foi chamada.

2. **Passo Recursivo**:
   - Se `n` é maior que 1, o problema é dividido em três subproblemas:
     1. Mover `n-1` discos da `origem` para a `auxiliar`, usando o `destino` como auxiliar.
     2. Mover o disco `n` da `origem` para o `destino`.
     3. Mover os `n-1` discos da `auxiliar` para o `destino`, usando a `origem` como auxiliar.
   - ```python
     torre_hanoi(n-1, origem, auxiliar, destino)
     print(f"Mova o disco {n} de {origem} para {destino}")
     torre_hanoi(n-1, auxiliar, destino, origem)
     ```

### Exemplo de Execução

Vamos considerar um exemplo com `n = 3` discos e as varetas "A" (origem), "C" (destino) e "B" (auxiliar).

#### Passo a Passo da Recursão

1. **Primeira Chamada**: `torre_hanoi(3, "A", "C", "B")`
   - Mover 2 discos de "A" para "B" usando "C" como auxiliar:
     - **Chamada Recursiva**: `torre_hanoi(2, "A", "B", "C")`
       - Mover 1 disco de "A" para "C" usando "B" como auxiliar:
         - **Chamada Recursiva**: `torre_hanoi(1, "A", "C", "B")`
           - `print("Mova o disco 1 de A para C")`
       - `print("Mova o disco 2 de A para B")`
       - Mover 1 disco de "C" para "B" usando "A" como auxiliar:
         - **Chamada Recursiva**: `torre_hanoi(1, "C", "B", "A")`
           - `print("Mova o disco 1 de C para B")`
   - `print("Mova o disco 3 de A para C")`
   - Mover 2 discos de "B" para "C" usando "A" como auxiliar:
     - **Chamada Recursiva**: `torre_hanoi(2, "B", "C", "A")`
       - Mover 1 disco de "B" para "A" usando "C" como auxiliar:
         - **Chamada Recursiva**: `torre_hanoi(1, "B", "A", "C")`
           - `print("Mova o disco 1 de B para A")`
       - `print("Mova o disco 2 de B para C")`
       - Mover 1 disco de "A" para "C" usando "B" como auxiliar:
         - **Chamada Recursiva**: `torre_hanoi(1, "A", "C", "B")`
           - `print("Mova o disco 1 de A para C")`

#### Saída Final

A sequência de movimentos será:

1. Mova o disco 1 de A para C
2. Mova o disco 2 de A para B
3. Mova o disco 1 de C para B
4. Mova o disco 3 de A para C
5. Mova o disco 1 de B para A
6. Mova o disco 2 de B para C
7. Mova o disco 1 de A para C

### Armazenamento de Valores e Chamadas Recursivas

- **Pilha de Chamadas**:
  - Cada chamada recursiva é empilhada (stack pointer) até atingir o caso base (`n == 1`).
  - Após resolver o caso base, a função retorna e desempilha a próxima chamada recursiva (a que está salva no registrador ra).
- **Parâmetros**:
  - `n`, `origem`, `destino` e `auxiliar` são passados como argumentos para cada chamada.
  - Esses valores são armazenados no contexto da função atual na pilha de chamadas.
- **Retorno**:
  - O retorno da função ocorre após completar todas as chamadas recursivas e imprimir os movimentos necessários.

---
# Algoritmo em assembly
```assembly
    .data
	origem: .asciz " A "
	auxiliar: .asciz " B "
	destino: .asciz " C "
	mova: .asciz "Mova o disco "
	para: .asciz " para "
	de: .asciz " de "
	n: .asciz "\n"
	hanoi: .asciz " torre_hanoi "	
	base: .asciz " base "
```
Essa parte apenas define os textos que serão impressos, para  ajudar a visualizar o funcionamento do código

```assembly
.text
.global main

main:	
	li a0 3
	
	la a1 origem
	la a2 auxiliar
	la a3 destino
	jal ra torre_hanoi	#Chama a função pela primeira vez, 
				#armazenando o primeiro valor de link em ra
	li a7 93
	ecall
```
<p align="justify">Definindo os registradores a1, a2, a3 com os labels Origem, Auxiliar, Destino e realizando a primeira chamada da função torre_hanoi, esse será nosso primeiro endereço salvo no registrador ra. </p>

```assembly

    torre_hanoi:
	
	addi sp sp -20 # Decrementa o ponteiro de pilha para salvar espaco para os registradores
	###########################################
	# Armazenando os valores dos registraores #
	# na stack pointer			  #	
	###########################################
	
	sw ra 16(sp) 
	sw a3 12(sp)
	sw a2 8(sp)
	sw a1 4(sp)
	sw a0 0(sp) 		
	
	
	###########################################
	# Verificação para o caso base 		  #	
	###########################################						
	li t1 1
	beq a0 t1 base_case #Caso base	
					
	addi a0 a0 -1	# Decrementando -1 do número de discos (n-1)
			# Parâmetro que será repassado para função
	
	#################################
	# Recuperando os valores	#
	# passados como parâmetro	#
	# e alternando os valores	#
	# Origem = Origem		#
	# Destino = Auxiliar		#
	# Auxiliar = Destino		#	
 	#################################
	lw a1 4(sp)
	lw a3 8(sp)
	lw a2 12(sp)	
	
	jal ra torre_hanoi #Chamada Recursiva com os novos parâmetros		
	
	#################################
	# Recuperando os valores	#
	# passados como parâmetro	#
	# e alternando os valores	#
	# Origem = Origem		#
	# Auxiliar = Auxiliar		#
	# Destino = Destino		#
 	#################################	
				
	lw a0 0(sp)
	lw a1 4(sp)
	lw a2 8(sp)
	lw a3 12(sp)	
					
	li a7 4
	la a0 mova
	ecall
	
	li a7 1
	lw a0 0(sp) #Recuperar o Vaor Original de a0, no caso, o valor que foi salvo em 0(sp)
	ecall
	
	li a7 4
	la a0 de
	ecall
	
	li a7 4
	mv a0 a1
	ecall	
	
	li a7 4
	la a0 para
	ecall	
	
	li a7 4
	mv a0 a3
	ecall
	
	li a7 4
	la a0 hanoi
	ecall	
	
	li a7 4
	la a0 n
	ecall
	#################################	
	# Recuperando os valores	#
	# passados como parâmetro	#
	# Origem = Auxiliar		#
	# Destino = Destino		#
	# Auxiliar = Origem		#
 	#################################
	lw a0 0(sp)  
	lw a2 4(sp)
	lw a1 8(sp)
	lw a3 12(sp)			
													
	
	addi a0 a0 -1 	 # Decrementando -1 do número de discos (n-1)
			 # Parâmetro que será repassado para função
	jal ra torre_hanoi	
	
	
	lw ra 16 (sp) # Restaurar o valor original de ra	
	addi sp sp 20 # Restaurar o ponteiro da p i l h a
	ret # Retornar ao endereco salvo em ra
```

Função responsável por resolver o algoritmo da torre de hanoi.

### Definição para criar uma stack pointer de 20 bytes, ou seja 5 posições

```assembly
    addi sp sp -20 # Decrementa o ponteiro de pilha para salvar espaco para os registradores
	###########################################
	# Armazenando os valores dos registraores #
	# na stack pointer			  #	
	###########################################
	
	sw ra 16(sp) 
	sw a3 12(sp)
	sw a2 8(sp)
	sw a1 4(sp)
	sw a0 0(sp) 		
```

Após criar a pilha os valores dos registradores são salvos nas posições da pilha, iniciando do final. Isso é necessário para ter os valores atuais da execução do programa salvo, dessa forma, na próxima chamada recursiva, o estado atual do programa estará salvo.

### Chamadas recursivas

```assembly

        ###########################################
    	# Verificação para o caso base 		  #	
    	###########################################						
    	li t1 1
    	beq a0 t1 base_case #Caso base	
    					
    	addi a0 a0 -1	# Decrementando -1 do número de discos (n-1)
    			# Parâmetro que será repassado para função
    	
    	#################################
    	# Recuperando os valores	#
    	# passados como parâmetro	#
    	# e alternando os valores	#
    	# Origem = Origem		#
    	# Destino = Auxiliar		#
    	# Auxiliar = Destino		#	
     	#################################
      
    	lw a1 4(sp)
    	lw a3 8(sp)
    	lw a2 12(sp)	
    	
    	jal ra torre_hanoi #Chamada Recursiva com os novos parâmetros
```

<p align="justify">A primeira coisa feita é verificar se o valor no registrador que representa a quantidade de discos, é igual ao caso base (1), se não o valor do registrador a0 será diminuído em 1, e serão feitas chamadas recursivas até o caso base ser atendido.
Antes de realizar a chamada recursiva é necessário carregar os valores salvos no estado atual da pilha de pontos, para os registradores a1, a2, a3.
</p>

### Impressão dos valores

```assembly
#################################
	# Recuperando os valores	#
	# passados como parâmetro	#
	# e alternando os valores	#
	# Origem = Origem		#
	# Auxiliar = Auxiliar		#
	# Destino = Destino		#
 	#################################	
				
	lw a0 0(sp)
	lw a1 4(sp)
	lw a2 8(sp)
	lw a3 12(sp)	
					
	...
    [Impressão dos valores]
    ...
    
```
<p align="justify">Antes de imprimir os valores dos registradores, é preciso, primeiro, recuperá-los utilizando a pilha de pontos, uma vez que essa parte do código está após uma chamada recursiva da função</p>

### Segunda chamada recursiva
```assembly
#################################	
	# Recuperando os valores	#
	# passados como parâmetro	#
	# Origem = Auxiliar		#
	# Destino = Destino		#
	# Auxiliar = Origem		#
 	#################################
	lw a0 0(sp)  
	lw a2 4(sp)
	lw a1 8(sp)
	lw a3 12(sp)			
													
	
	addi a0 a0 -1 	 # Decrementando -1 do número de discos (n-1)
			 # Parâmetro que será repassado para função
	jal ra torre_hanoi	
```
<p align="justify">Após realizar a impressão é preciso recuperar os valores da pilha outra vez, para realizar a segunda chamada recursiva, se necessária, com os valores do estado atual.</p>

### Retorno para o edereço do registrador ra

```assembly
        lw ra 16 (sp) # Restaurar o valor original de ra	
	addi sp sp 20 # Restaurar o ponteiro da p i l h a
	ret # Retornar ao endereco salvo em ra
```
<p align="justify"> Após todas as chamadas recursivas anteriores serem feitas o programa retorna para o endereço salvo em ra, dessa forma, o programa segue executando, mantendo os valores dos registradores das chamadas slavas, até que se encerre.</p>

### Caso Base

```assembly
base_case:	
	li a7 4
	la a0 mova
	ecall
	
	li a7 1
	li a0 1
	ecall
	
	li a7 4
	la a0 de
	ecall
	
	li a7 4
	mv a0 a1
	ecall	
	
	li a7 4
	la a0 para
	ecall	
	
	li a7 4
	mv a0 a3
	ecall	
	
	li a7 4
	la a0 base
	ecall	
	
	li a7 4
	la a0 n
	ecall	
	
		
	lw a0 0(sp) 	#################################
	lw a1 4(sp)	#				#
	lw a2 8(sp)	# Recuperando os valores	#
	lw a3 12(sp)	# passados como parâmetro	#
	lw ra 16 (sp)	# 				#	
	addi sp sp 20 	#################################
	ret # Retornar ao endereco salvo em ra

```
<p align="justify">Como estamos salvando os valores dos registradores dentro da função <b>torre_hanoi</b>, o caso base apenas imprime os valores, e após a impressão, é necessário carregar os valores salvos na stack pointer, dessa forma, o programa retorna para onde ocorreu a chamada para o caso base, mantendo os estados salvos.</p>
