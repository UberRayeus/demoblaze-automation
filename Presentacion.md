# demoblaze-automation
Demoblaze Automation Selenium Test Suite


Esta test suit fue desarrollada a fin de proponer una solucion a lo requerido por la prueba Teorica sugerida.
El presente documento detalla ciertas particularidades del desarrollo propuesto y describe el funcionamiento del mismo. 

**1) ALCANCES:** Dado el corto margen de tiempo disponible, ciertos aspectos del framework fueron simplificados respecto a su ejecucion ideal. A saber:

      -- No se ha incluido un sistema de registro mediante Screenshots para los errores.
      -- No se ha desarrollado un modelo de paginacion de objetos modular sino que se ha implementado la totalidad de las funciones al 
         interior de un unico modulo de testeo.
      -- No se ha desarrollado una suite comprensiva sino una verificación de los Happy Path.
      -- El manejo de las esperas aun puede ser optimisado para una mejor utilizacion de los recursos de procesamiento. 

La test suite cubre los requerimientos minimamente indispensables para el corecto testeo de las funcionalidades descriptas.
Mediante una modularizacion de la paginacion de objetos y el desarrollo de un mayor abanico de Test Cases que incluyan casos negativos relevantes y casos positivos mas exhaustivos puede proyectarse el desarrollo de una Test Suit que garantice una adecuada cobertura para 
el desarrollo de regresiones comprensivas. A saber:

      -- Las localizaciones de elementos debieran ser repartidas en distintos modulos de inicializacion para garantizar el buen mantenimiento del codigo a la hora de expandir la test suite.
      -- Las funciones de screenshot y lectura de json debieran independizarse en su correspondiente modulo utilitario. 

**2) FUNCIONAMIENTO:** 

      La test suite se encuentra desarrollada en Python 3.10.11 y utiliza las librerias Selenium y Pytest. 
      Correr la suite mediante el siguiente comando genera un reporte Html respecto al resultado de los test cases.
            --pytest -v --html=report.html ./tests/test_compra_E2E.py

      El archivo data.json contiene los campos relevantes para la ejecucion de los test case. Alli debe definirse:
            -- Las credenciales del usuario que ejecuta la test suite
            -- Los elementos cuya compra se desea testear.
            -- Las credenciales necesarias para la compra incluyendo la **Tarjeta de Credito**
      


