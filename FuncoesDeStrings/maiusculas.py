# Para esta função, iremos sempre tratar usando números na casa decimal
def maiusculas ( frase ) :

    string_concatenada = ""
    vazio = 1

    for i in range ( 0, len ( frase ) ) :

        if ( ord ( frase[i] ) >= 65  and ord ( frase[i] ) <= 90 ) :

            string_concatenada += frase[i]
            vazio = 0

    if ( vazio == 1 ) :

        return ""


    return string_concatenada