$priv = Get-NetIPAddress -AddressFamily IPv4
$resultado1 = "Get-NetIPAdress`n $priv`n"

$public = Invoke-WebRequest ifconfig.me
$resultado2 = "Invoke-WebRequest ifconfig.me`n $public`n"

$seg_red_priv = $priv[4]
$nmap = nmap.exe -sP $seg_red_priv
$nmap2 = nmap.exe $seg_red_priv
$resultado3 = "Nmap Redpriv`n $nmap`n $nmap2`n"
 

$nmapweb = nmap.exe -sP linkedin.com
$nmapweb2 = nmap.exe linkedin.com
$resultado4 = "Nmap Sitio Web`n $nmapweb`n $nmapweb2`n"

#PARTE 3
$pwd = Get-Location
New-Item -ItemType "file" -Path $pwd\"File.txt"
Add-Content -Value $resultado1,$resultado2,$resultado3,$resultado4 -Path $pwd\"File.txt"