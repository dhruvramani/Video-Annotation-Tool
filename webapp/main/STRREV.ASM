; STRREV(S1, S2)

.MODEL SMALL
.STACK
.DATA
    STR DB 'ABCD$'
    ; STRLEN : LEN DW $-S
.CODE 
MAIN PROC FAR
    MOV AX, @DATA
    MOV DS, AX
    MOV CL, 4
    MOV BL, 2 ; STRLEN/2
    LEA SI, STR
    MOV DI, SI
    XXX :
        MOV AH, [SI]
        MOV AL, [DI]
        ADD AL, CL
        SUB AL, 1
        MOV [SI], AL
        MOV [DI + CL - 1], AH ; TODO - Shift properly
        INC SI
        DEC CL
        CMP CL, BL
    JNZ XXX

    LEA DI, STR
        
    YYY: 
        MOV DL, [DI]
        MOV AH, 02H
        INT 21H
        INC DI
        LOOP YYY

    MOV AX, 4COOH
    INT 21H

MAIN ENDP
END MAIN