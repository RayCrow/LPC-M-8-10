function counter-to-zero {
    echo "Se hará un contador desde tu número ($desde) hasta 0"
        echo "$desde"
        for ($desde -ne 0){
            if ($desde -gt 0){
                $desde = $desde -1
                echo $desde
            }
            if ($desde -lt 0) {
                $desde = $desde +1
                echo $desde  
            } 
        }
}

$desde = Read-Host "Ingresa un número diferente de 0"
do {counter-to-zero {$desde}} while( $desde -ne 0 )