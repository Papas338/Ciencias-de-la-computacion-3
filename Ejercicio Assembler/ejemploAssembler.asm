; Imprime los digitos hasta un numero determinado al derecho y al revés
	JMP start
; https://schweigi.github.io/assembler-simulator/instruction-set.html
inicio: DB "5" 	; Digito del 0 al 9 para imprimir
        DB 0	; Termina el string
fin: 	DB "/"	; Para que imprima hasta el 0
	DB 0	; Termina el string

start:
	MOV C, inicio   ; Guarda el valor de inicio en C 
	MOV D, 232	; Indica desde donde empieza el output

	CALL imprimirDigitos	
	CALL borrarDigitos

        HLT             ; Termina el programa

borrarDigitos:
	PUSH A
	PUSH B
	MOV A, [C]	; Guarda el caracter final
.ciclo2:
	DEC D		; Decrementa D

	MOV [D], A	; Imprime el caracter de A

	DEC A		; Decrementa A	
	
	CMP D, 232	; Verifica que no este en el inicio

	JNZ .ciclo2	; Si no lo esta vuelve al ciclo 
	
	POP B	
	POP A

	RET		; Termina el ciclo 2

imprimirDigitos:
	PUSH A
	PUSH B

	MOV B, fin	; Indica hasta que caracter imprimir
	MOV A, [C]	; Guarda el caracter del digito

.ciclo1:
	MOV [D], A	; Imprime en el output
	
	INC D		; Incrementa D para imprimir
	DEC A		; Decrementa A, el caracter
	
	CMP A, [B]	; Compara si termina

	JNZ .ciclo1	; Repite el ciclo si no

	POP B
	POP A

	RET		; Termina el ciclo 1