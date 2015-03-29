*= $c000

ldx #$0

.loop
    txa

    adc #$30
    jsr $FFD2

    lda #$8D
    jsr $FFD2

    inx

    cpx #$A
    beq .end
    jmp .loop

.end
