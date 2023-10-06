#  SPRINT_6_PROYECTO
## Urban Grocers_TestApi's


## OBJETIVO: 

-  Automatizar las pruebas desde esta lista de comprobación.
-  Cargar el código en GitHub.
-  Enviar el repositorio a revisión.

## Api's utilizadas:
- api/v1/users
- /api/v1/kits

## Listas de Comprobación:
###### Se procedió a comprobar la siguiente lista
-Test_1: Crear 1 kit con el número permitido de carácteres (1)//Código de respuesta esperada "201".
-Test_2: Crear 1 kit con el número permitido de carácteres (511)//Código de respuesta esperada "201".
-Test_3: Crear 1 kit con el número permitido de carácteres (0)//Código de respuesta esperada "400".
-Test_4: Crear 1 kit con el número permitido de carácteres (512)//Código de respuesta esperada "400".
-Test_5: Crear 1 kit con el número permitido de carácteres ("№%@")//Código de respuesta esperada "201".
-Test_6: Crear 1 kit con el número permitido de carácteres con espacios en blanco en campo nombre //Código de respuesta esperada "201".
-Test_7: Crear 1 kit con el número permitido  de carácteres: número entero //Código de respuesta esperada "201".
-Test_8: Crear 1 kit sin el nombre segun el parámetro requerido//Código de respuesta esperada "400".
-Test_9: Crear 1 kit con parámetro diferente (números)//Código de respuesta esperada "400".


## Resultado:


- Test_1: Kit creado con éxito, se consiguió resultado esperado "201".
- Test_2: Kit creado con éxito, se consiguió resultado esperado "201".
- Test_3: BUGG encontrado, no sé consiguió resultado esperado "400", se consiguió crear registro "201".
- Test_4: BUGG encontrado, no sé consiguió resultado esperado "400", se consiguió crear registro "201".
- Test_5: Kit creado con éxito, se consiguió resultado esperado "201".
- Test_6: Kit creado con éxito, se consiguió resultado esperado "201".
- Test_7: Kit creado con éxito, se consiguió resultado esperado "201".
- Test_8: BUGG encontrado, no sé consiguió resultado esperado "400", se consiguió respuesta código "500".
- Test_9: BUGG encontrado, no sé consiguió resultado esperado "400", se consiguió crear registro "201".