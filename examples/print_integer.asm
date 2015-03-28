; this program does not work because JSR/RTS are not implemented yet
*= $c000

lda #$1
jsr .print_integer

; newline
lda #$8D
jsr $FFD2


jmp .end

; print single digit integer in lda
.print_integer
    adc #$30
    jsr $FFD2
    rts

.end
