# Clean Architecture: A Craftsman's Guide to Software Structure and Design — Ejemplos, Casos de Estudio y Diagramas


## Índice de capítulos
- [About This E-Book](#about-this-e-book)
- [Contents](#contents)
- [Foreword](#foreword)
- [Preface](#preface)
- [Acknowledgments](#acknowledgments)
- [About the Author](#about-the-author)
- [I Introduction](#i-introduction)
- [1 What Is Design and Architecture?](#1-what-is-design-and-architecture)
- [2 A Tale of Two Values](#2-a-tale-of-two-values)
- [II Starting with the Bricks: Programming Paradigms](#ii-starting-with-the-bricks-programming-paradigms)
- [3 Paradigm Overview](#3-paradigm-overview)
- [4 Structured Programming](#4-structured-programming)
- [5 Object-Oriented Programming](#5-object-oriented-programming)
- [6 Functional Programming](#6-functional-programming)
- [Ejemplos, Firmas y Estructuras Exactas](#ejemplos-firmas-y-estructuras-exactas)
- [III Design Principles](#iii-design-principles)
- [7 SRP: The Single Responsibility Principle](#7-srp-the-single-responsibility-principle)
- [Ejemplos de Código y Estructuras](#ejemplos-de-código-y-estructuras)
- [8 OCP: The Open-Closed Principle](#8-ocp-the-open-closed-principle)
- [9 LSP: The Liskov Substitution Principle](#9-lsp-the-liskov-substitution-principle)
- [10 ISP: The Interface Segregation Principle](#10-isp-the-interface-segregation-principle)
- [11 DIP: The Dependency Inversion Principle](#11-dip-the-dependency-inversion-principle)
- [IV Component Principles](#iv-component-principles)
- [12 Components](#12-components)
- [13 Component Cohesion](#13-component-cohesion)
- [14 Component Coupling](#14-component-coupling)
- [DESCRIPCIONES DE DIAGRAMAS EN PROSA](#descripciones-de-diagramas-en-prosa)
- [FÓRMULAS Y MÉTRICAS EXACTAS](#fórmulas-y-métricas-exactas)
- [COMPONENTES Y CLASES MENCIONADOS](#componentes-y-clases-mencionados)
- [V Architecture](#v-architecture)
- [15 What Is Architecture?](#15-what-is-architecture)
- [16 Independence](#16-independence)
- [17 Boundaries: Drawing Lines](#17-boundaries-drawing-lines)
- [18 Boundary Anatomy](#18-boundary-anatomy)
- [19 Policy and Level](#19-policy-and-level)
- [Ejemplos de Código y Diagramas](#ejemplos-de-código-y-diagramas)
- [20 Business Rules](#20-business-rules)
- [21 Screaming Architecture](#21-screaming-architecture)
- [22 The Clean Architecture](#22-the-clean-architecture)
- [23 Presenters and Humble Objects](#23-presenters-and-humble-objects)
- [24 Partial Boundaries](#24-partial-boundaries)
- [25 Layers and Boundaries](#25-layers-and-boundaries)
- [26 The Main Component](#26-the-main-component)
- [27 Services: Great and Small](#27-services-great-and-small)
- [Ejemplos, Diagramas y Estructuras](#ejemplos-diagramas-y-estructuras)
- [28 The Test Boundary](#28-the-test-boundary)
- [29 Clean Embedded Architecture](#29-clean-embedded-architecture)
- [FRAGMENTOS DE CÓDIGO, FIRMAS Y ESTRUCTURAS](#fragmentos-de-código-firmas-y-estructuras)
- [VI Details](#vi-details)
- [30 The Database Is a Detail](#30-the-database-is-a-detail)
- [31 The Web Is a Detail](#31-the-web-is-a-detail)
- [32 Frameworks Are Details](#32-frameworks-are-details)
- [33 Case Study: Video Sales](#33-case-study-video-sales)
- [Diagramas Arquitectónicos Descritos en Prosa](#diagramas-arquitectónicos-descritos-en-prosa)
- [34 The Missing Chapter](#34-the-missing-chapter)
- [Firmas, Estructuras y Ejemplos de Código](#firmas-estructuras-y-ejemplos-de-código)
- [Afterword](#afterword)
- [VII Appendix](#vii-appendix)
- [A Architecture Archaeology](#a-architecture-archaeology)
- [EJEMPLOS, FIRMAS Y ESTRUCTURAS TÉCNICAS](#ejemplos-firmas-y-estructuras-técnicas)
- [Index](#index)
- [Code Snippets](#code-snippets)

## About This E-Book

_Material del editor (información de licencia/formato del ebook), sin contenido de autor. No se resumió._

## Contents

_Es el índice de contenidos del libro (listado de títulos y páginas), no prosa técnica. No se resumió._

## Foreword

ESTE CAPÍTULO NO CONTIENE CÓDIGO, FIRMAS DE MÉTODOS, NI EJEMPLOS DE IMPLEMENTACIÓN. Es un capítulo introductorio de principios filosóficos y definiciones conceptuales escrito por Kevlin Henney (autor del Foreword) que establece marco teórico para el libro completo de Robert C. Martin. El contenido es enteramente en prosa técnica y citas autorizadas, sin artefactos de código ejecutable ni estructuras de datos específicas. Las únicas "estructuras" mencionadas son conceptuales (componentes, clases, funciones, módulos, capas, servicios) y metafóricas (edificios, turtles, Jenga towers, big-ball-of-mud). Los únicos identificadores técnicos son autoridades citadas: Grady Booch (definición de arquitectura), Brian Foote y Joseph Yoder (costo de mala arquitectura), Ralph Johnson (paradoja de decisiones tempranas), Tom Gilb (arquitectura como hipótesis), Robert C. Martin (velocidad y calidad), William Shakespeare (limitaciones de ejecución), y Kevlin Henney (autor).

## Preface

Este es el capítulo Prefacio del libro Clean Architecture. Contiene **cero ejemplos de código**, **cero firmas de métodos**, **cero diagramas técnicos** y **cero estructuras de datos concretas**. 

El capítulo es enteramente filosófico-histórico: establece mediante argumentación y anécdotas personales la premisa de que las reglas arquitectónicas son atemporales. Martin estructura su argumento mediante:
- Enumeración de dominios y arquitecturas construidas (no en código, sino como lista narrativa)
- Comparaciones históricas de hardware (máquinas 1960s vs. 2016)
- Experimentos mentales (programador de 1966 en 2016 IDE, y viceversa)
- Análisis de invariantes de código (if/while/assignment como primitivos eternos)

El único "ejemplo" técnico implícito es la referencia a lenguajes: Java, C#, Ruby, Fortran, C, PDP-8 assembly, machine code de Turing (1946). Pero no hay código ejecutable, pseudocódigo ni diagramas en este prefacio.

**Conclusión**: El prefacio es una argumentación pura sin ejemplificación técnica concreta. Es el marco conceptual que justifica el contenido técnico detallado que sigue en los capítulos posteriores del libro.

## Acknowledgments

El capítulo "Acknowledgments" NO contiene ejemplos de código, firmas de métodos, definiciones de clases, estructuras de datos, diagramas de secuencia, diagramas de clase, ni casos de uso concretos. Es un capítulo puramente administrativo y personal de reconocimiento.

El único contenido estructurado con valor semántico adicional es la referencia al capítulo "Screaming Architecture" mencionado en el párrafo de cierre, que en el contexto de Clean Architecture se refiere a un principio que establece que la arquitectura de un sistema de software debe comunicar su propósito e intención principal a través de su estructura visible, sin requerir inspección de detalles de implementación.

La estructura del reconocimiento mismo puede considerarse un ejemplo de principio arquitectónico aplicado a la documentación: la ausencia de jerarquía en el listado de contributors refleja un modelo no jerárquico de distribución de responsabilidad y reconocimiento.

## About the Author

No hay ejemplos de código, fragmentos técnicos, firmas de métodos, estructuras de clases o diagramas en este capítulo. "About the Author" es un capítulo introductorio/de créditos puramente biográfico que proporciona contexto sobre el autor de Clean Architecture, Robert C. Martin. No contiene: ejemplos de arquitectura de software, patrones de diseño, principios SOLID, discusiones técnicas de implementación, pseudocódigo o diagramas de secuencia/estructura. Su propósito es establecer la autoridad y trayectoria del autor, no presentar contenido técnico codificable o diagramable.

## I Introduction

Este capítulo es introductorio y motivacional. NO contiene ejemplos de código, firmas de métodos, diagramas de clase, secuencias, ni casos de uso concretos. 

Es un prefacio filosófico que establece la premisa y motivación del libro mediante retórica comparativa:
- Contraste entre "getting a program working" vs. "getting it right"
- Testimonios y contraejemplos (observaciones de proyectos reales sin detalles técnicos)
- Preguntas retóricas que establecen dolor points de mala arquitectura

El autor reserva ejemplos técnicos y patrones concretos para capítulos posteriores. Este capítulo es pura argumentación motivacional, no documentación técnica con código.

## 1 What Is Design and Architecture?

Este es un capítulo introductorio puramente conceptual de Clean Architecture. No contiene ejemplos de código, firmas de métodos, clases específicas, nor diagramas técnicos complejos.

Sin embargo, contiene los siguientes artefactos descriptivos en prosa:

1. **Analogía Arquitectónica**: Los planos de una casa residencial incluyen:
   - Decisiones macroscópicas: forma, elevaciones, distribución de espacios
   - Detalles microscópicos: ubicación exacta de tomacorrientes, interruptores, especificación de qué interruptor controla qué luz, ubicación de furnace (caldera), dimensiones y ubicación del calentador de agua, ubicación de la bomba de sumidero (sump pump), especificaciones de construcción detalladas de muros, techos y cimientos

2. **Casos de Estudio Métricos (cuantitativos)**:
   - Release 1: nómina de "cientos de miles de dólares mensuales" → genera funcionalidad significativa
   - Release 8: nómina de "$20 millones mensuales" → genera casi nada
   - Factor de degradación: costo por línea de código se multiplica por 40x
   - Productividad de desarrolladores: inicia ~100%, aproxima asintóticamente a ~0%

3. **Experimento Jason Gorman (TDD vs No-TDD)**:
   - Duración: 6 días
   - Tarea repetida: programa que convierte enteros a numerales romanos
   - Criterio de completitud: todos los acceptance tests pasan
   - Duración típica por día: ~30 minutos
   - Disciplina aplicada: test-driven development (TDD) en días 1, 3, 5
   - Resultado: TDD ~10% más rápido; el día TDD más lento superó el día no-TDD más rápido

4. **Principios Arquitectónicos Explícitos**:
   - "The goal of software architecture is to minimize the human resources required to build and maintain the required system"
   - "The only way to go fast, is to go well"
   - "Making messes is always slower than staying clean, no matter which time scale you are using"
   - "Their overconfidence will drive the redesign into the same mess as the original project"

El capítulo es fundamentalmente un ensayo sobre principios, no un tutorial técnico, por lo que omite intencionadamente código compilable o pseudocódigo ejecutable.

## 2 A Tale of Two Values


Este capítulo es fundamentalmente conceptual y de principios. No contiene código, firmas de métodos, nombres de clases, estructuras de implementación, ni ejemplos de código concreto. Su propósito es establecer argumentos lógicos y marcos conceptuales.

Las únicas entidades visuales mencionadas son:
- **Figure 2.1**: Eisenhower Matrix - una matriz 2x2 con ejes "Importance" (vertical, desde baja a alta) e "Urgency" (horizontal, desde baja a alta), dividiendo el espacio en cuatro cuadrantes correspondientes a las cuatro prioridades (urgente-importante, no-urgente-importante, urgente-no-importante, no-urgente-no-importante). No se proporciona en el texto la ubicación específica de "Behavior" vs "Architecture" dentro de la matriz, solo se describe textualmente.

- **Metáfora descriptiva** (no código): "Square pegs into round holes" - describe la fricción cuando la forma del sistema no coincide con la forma del requisito.

El capítulo es introductorio-filosófico: argumenta por principios lógicos (reductio ad absurdum, análisis de extremos, matriz de priorización) sin descender a implementación. Su valor está en los argumentos conceptuales, no en ejemplos técnicos ejecutables.


## II Starting with the Bricks: Programming Paradigms

Este capítulo es introductorio de naturaleza conceptual e histórica. No contiene ejemplos de código concretos, firmas de métodos, definiciones de clases, implementaciones de patrones de diseño, ni diagramas técnicos. 

El contenido se enfoca exclusivamente en:
1. Contexto histórico de la programación (Turing, Hopper, lenguajes)
2. Definición conceptual de paradigma como categoría abstracta independiente del lenguaje
3. Establecimiento del marco para los capítulos posteriores que presumiblemente cubrirán los tres paradigmas específicos

No hay fragmentos de código, pseudocódigo, diagramas de secuencia, diagramas de clase, o casos de uso implementados en esta sección. Es un preámbulo narrativo que prepara el terreno conceptual.

## 3 Paradigm Overview

Este capítulo es introductorio y histórico. No contiene ejemplos de código concretos, firmas de métodos, clases, ni descripciones de diagramas complejos más allá de una referencia a una imagen (media/Images/CH-UN03.jpg) que acompaña el título del capítulo sin descripción textual detallada en el contenido.

Las construcciones mencionadas son:
- Construcciones de control de flujo disciplinadas: if/then/else, do/while/until (no código específico mostrado, solo nombradas como reemplazo conceptual de goto)
- Punteros a función (mencionados como mecanismo de polimorfismo en OOP, sin firma específica)
- Sentencias de asignación (mencionadas como mecanismo controlado en programación funcional, sin ejemplos)

El capítulo enfatiza que los paradigmas son restricciones conceptuales sobre mecanismos de control (flujo de control directo, transferencia indirecta de control, asignación) más que patrones de implementación con código ejemplar.

## 4 Structured Programming

**Estructuras de Control Fundamentales (Teorema de Böhm-Jacopini):**

Estructura 1 - SECUENCIA:
```
statement1;
statement2;
statement3;
```

Estructura 2 - SELECCIÓN (if/then/else):
```
if (condition) {
    // path 1
} else {
    // path 2
}
```

Estructura 3 - ITERACIÓN (do/while):
```
do {
    // iteration body
} while (condition);
```

Alternativa de iteración (while):
```
while (condition) {
    // iteration body
}
```

**Técnicas de Prueba Formal Mencionadas (No implementadas en código, sino en notación matemática):**

- Prueba de Secuencia: Enumeración directa de inputs→outputs
- Prueba de Selección: Enumeración de ambas ramas; si ambas producen resultados matemáticos apropiados, la prueba es sólida
- Prueba de Iteración: Inducción matemática con tres componentes:
  1. Demostración de caso N=1 por enumeración
  2. Demostración de que si N es correcto entonces N+1 es correcto (por enumeración)
  3. Demostración de criterios de inicio y terminación por enumeración

**Leyes Científicas Mencionadas (Contexto Analógico, no código):**

- Segunda ley de Newton: F = ma
- Ley de gravitación: F = Gm₁m₂/r²

**Métodos No Permitidos en Structured Programming:**

```
// Goto irrestricto (PROHIBIDO en structured programming):
goto label;  // transferencia de control sin restricciones
// Solo permitido si target está dentro del scope actual de la función (lenguajes modernos)

// Transferencias de control PERMITIDAS (son abstracciones sobre goto):
break;          // Java con nombres en loops
continue;       // Continuar a siguiente iteración
throw exception; // Excepciones (control flow restringido)
return;         // Retorno de función
```

**Nota sobre Ejemplos de Código:** Este capítulo es fundamentalmente teórico-histórico sobre los principios y descubrimientos de Dijkstra. No contiene ejemplos de código concreto de aplicación, sino que describe formalmente los requisitos matemáticos para que código sea provable, y cómo testing se convierte en el mecanismo práctico para verificar corrección bajo el paradigma científico (falsabilidad) en lugar del paradigma matemático (prueba formal).

## 5 Object-Oriented Programming

### 1. Encapsulación Perfecta en C (pre-OO)

**point.h** (archivo de cabecera):
```c
struct Point;  
struct Point* makePoint(double x, double y);  
double distance (struct Point *p1, struct Point *p2);
```

**point.c** (implementación privada):
```c
#include "point.h"  
#include <stdlib.h>  
#include <math.h>  
   
struct Point {  
  double x,y;  
};  
   
struct Point* makepoint(double x, double y) {  
  struct Point* p = malloc(sizeof(struct Point));  
  p->x = x;  
  p->y = y;  
  return p;  
}  
   
double distance(struct Point* p1, struct Point* p2) {  
  double dx = p1->x - p2->x;  
  double dy = p1->y - p2->y;  
  return sqrt(dx*dx+dy*dy);  
}
```

---

### 2. Ruptura de Encapsulación en C++

**point.h** (cabecera C++ expone miembros):
```c++
class Point {  
public:  
  Point(double x, double y);  
  double distance(const Point& p) const;  
   
private:  
  double x;  
  double y;  
};
```

**point.cc** (implementación):
```c++
#include "point.h"  
#include <math.h>  
   
Point::Point(double x, double y)  
: x(x), y(y)  
{}  
  
double Point::distance(const Point& p) const {  
  double dx = x-p.x;  
  double dy = y-p.y;  
  return sqrt(dx*dx + dy*dy);  
}
```

---

### 3. Herencia Manual en C (simulación mediante composición y casting)

**namedPoint.h**:
```c
struct NamedPoint;  
   
struct NamedPoint* makeNamedPoint(double x, double y, char* name);  
void setName(struct NamedPoint* np, char* name);  
char* getName(struct NamedPoint* np);
```

**namedPoint.c**:
```c
#include "namedPoint.h"  
#include <stdlib.h>  
   
struct NamedPoint {  
  double x,y;          // Orden idéntico a struct Point
  char* name;          // Campo adicional
};  
   
struct NamedPoint* makeNamedPoint(double x, double y, char* name) {  
  struct NamedPoint* p = malloc(sizeof(struct NamedPoint));  
  p->x = x;  
  p->y = y;  
  p->name = name;  
  return p;  
}  
   
void setName(struct NamedPoint* np, char* name) {  
  np->name = name;  
}  
   
char* getName(struct NamedPoint* np) {  
  return np->name;  
}
```

**main.c** (uso polimórfico mediante cast):
```c
#include "point.h"  
#include "namedPoint.h"  
#include <stdio.h>  
   
int main(int ac, char** av) {  
  struct NamedPoint* origin = makeNamedPoint(0.0, 0.0, "origin");  
  struct NamedPoint* upperRight = makeNamedPoint(1.0, 1.0, "upperRight");  
  printf("distance=%f\n",  
    distance(  
             (struct Point*) origin,        // Cast: NamedPoint as Point
             (struct Point*) upperRight));  
}
```

---

### 4. Polimorfismo pre-OO: Programa `copy` en C

```c
#include <stdio.h>  
  
void copy() {  
  int c;  
  while ((c=getchar()) != EOF)  
    putchar(c);  
}
```

---

### 5. Implementación de Polimorfismo mediante Punteros a Funciones (UNIX I/O)

**Estructura FILE con punteros a funciones**:
```c
struct FILE {  
  void (*open)(char* name, int mode);  
  void (*close)();  
  int (*read)();  
  void (*write)(char);  
  void (*seek)(long index, int mode);  
};
```

**Implementación de driver (consola)**:
```c
#include "file.h"  
   
void open(char* name, int mode) {/*...*/}  
void close() {/*...*/};  
int read() {int c;/*...*/ return c;}  
void write(char c) {/*...*/}  
void seek(long index, int mode) {/*...*/}  
   
struct FILE console = {open, close, read, write, seek};
```

**Función polimórfica `getchar()`**:
```c
extern struct FILE* STDIN;  
   
int getchar() {  
  return STDIN->read();  // Llamada indirecta a través del puntero
}
```

---

### 6. Diagramas Conceptuales Descritos en Prosa

**Figura 5.1 — Source code dependencies versus flow of control (pre-polimorfismo)**:
- Árbol de llamadas jerárquico: `main` → high-level functions → mid-level functions → low-level functions
- Dependencias del código fuente bajan verticalmente en paralelo al flujo de control
- El arquitecto tiene **cero opciones** en dirección de dependencias; están dictadas por el flujo necesario del sistema
- Cada nivel debe importar/incluir el módulo del nivel siguiente (dependencia descendente obligatoria)

**Figura 5.2 — Dependency inversion (con polimorfismo)**:
- Módulo `HL1` (high-level) contiene función que llama `F()` en módulo `ML1` (mid-level)
- Existe una **interface `I`** entre ellos (artilugio del código fuente; desaparece en runtime)
- **INVERSIÓN CRÍTICA**: La relación de herencia/dependencia (`ML1` implementa `I`, `HL1` depende de `I`) apunta en dirección OPUESTA al flujo de control
- `HL1` llama a través de la interface; `ML1` la implementa; la dependencia del código fuente apunta hacia arriba (de MI hacia HL)

**Figura 5.3 — The database and the user interface depend on the business rules**:
- Diagrama rectangular tripartito:
  - Centro: **Business Rules** (módulo core)
  - Izquierda: **Database** (módulo plugin)
  - Derecha: **UI** (módulo plugin)
- Flechas de dependencia: DB → interface ← BR, UI → interface ← BR
- BR **no depende** de DB ni UI; DB y UI **dependen** de BR mediante interfaces
- Implicación: Tres componentes compilables independientes; business rules puede existir en su propio jar/DLL sin referencias a DB o UI

---

### 7. Firmas Exactas de Métodos Mencionadas

**C++ Point class signature completa**:
```c++
class Point {  
public:  
  Point(double x, double y);                  // Constructor
  double distance(const Point& p) const;      // Método const
   
private:  
  double x;  
  double y;  
};
```

**C++ Point implementation signatures**:
```c++
Point::Point(double x, double y) : x(x), y(y) {}
double Point::distance(const Point& p) const { ... }
```

**UNIX FILE interface (5 standard functions)**:
- `open(char* name, int mode)` → `void`
- `close()` → `void`
- `read()` → `int`
- `write(char)` → `void`
- `seek(long index, int mode)` → `void`

---

### Nota Importante
El capítulo **no contiene ejemplos de código complejos ni patrones GoF formalizados**. Su enfoque es conceptual-histórico: deconstruye los mitos de OO mediante ejemplos comparativos C vs C++ vs C# vs Java, mostrando que las características supuestamente "inventadas" por OO (encapsulación, herencia, polimorfismo) existían antes. El verdadero aporte de OO fue **hacer polimorfismo seguro y conveniente**, lo que permite **dependency inversion** a escala arquitectónica. Los ejemplos concretos son principalmente narrativos y comparativos, no implementaciones de complejos patrones de diseño.


## 6 Functional Programming

## Ejemplos, Firmas y Estructuras Exactas

**1. Implementación Imperativa Java (Problema: Squares of Integers)**
```java
public class Squint {
  public static void main(String args[]) {
    for (int i=0; i<25; i++)
      System.out.println(i*i);
  }
}
```
Utiliza variable mutable `i` como control de bucle que varía durante la ejecución.

**2. Implementación Funcional Clojure**
```clojure
(println (take 25 (map (fn [x] (* x x)) (range))))
```

Con estructura desagregada:
```clojure
(println                          ;______ Print
  (take 25                        ;______ the first 25
    (map (fn [x] (* x x))        ;______ squares
      (range))))                 ;______ of Integers
```

**Flujo de evaluación** (de adentro hacia afuera):
- `(range)`: Retorna una lista infinita de enteros comenzando en 0
- `(map (fn [x] (* x x)) ...)`: Aplica función anónima `(fn [x] (* x x))` a cada elemento, produciendo lista infinita de cuadrados
- `(take 25 ...)`: Retorna nueva lista con solo los primeros 25 elementos
- `(println ...)`: Imprime la lista de los primeros 25 cuadrados

Nota: Solo los primeros 25 elementos son realmente evaluados debido a lazy evaluation (ningún elemento de lista infinita se evalúa hasta ser accedido).

**3. Clojure Atom con Compare-and-Swap**
```clojure
(def counter (atom 0))  ; initialize counter to 0
(swap! counter inc)     ; safely increment counter
```

**Mecanismo de `swap!`:**
- Firma: `swap! atom function` 
- Algoritmo internamente ejecuta compare-and-swap:
  1. Lee valor de `counter` (ej: 0) y lo pasa a `inc`
  2. `inc` retorna nuevo valor (1)
  3. Bloquea `counter` y compara si todavía es 0
  4. Si sí: almacena 1 y libera lock
  5. Si no: libera lock y reintenta desde paso 1

**4. Conceptos de Arquitectura Descritos**

**Figura 6.1: Mutating State and Transactional Memory** (descrita en prosa)
Diagrama que muestra segregación de componentes:
- Zona superior: Componentes inmutables que realizan procesamiento puro
- Zona inferior: Componentes mutables con transactional memory
- Conexión entre zonas: Componentes inmutables se comunican con componentes mutables para cambios de estado

**5. Event Sourcing - Caso de Uso Bancario**
Contraste en modelo de datos:
- **Enfoque tradicional (mutable)**: Almacenar balance actual de cuenta que se actualiza con cada transacción
- **Event Sourcing (inmutable)**: Almacenar solo transacciones históricas; calcular balance sumando todas las transacciones desde el inicio

Ejemplo conceptual (no código, descrito en prosa):
```
Banking Account State Calculation:
Final Balance = SUM(all transactions from beginning of time)
                = deposit(500) + withdrawal(100) + deposit(250) + ...
                = 650 (en ejemplo simple)
```

Optimización posible:
```
Checkpoint Strategy:
- 01/01/2025, 00:00: Snapshot de balance = 10,000
- 01/02/2025, 10:30: Query requiere balance actual
- Cálculo: balance = 10,000 + SUM(transactions since 01/01/2025, 00:00)
```

**6. Conceptos de Persistencia sin Mutación**
- **CRUD vs CR**: Aplicaciones con event sourcing son CR (Create-Read) no CRUD porque no hay Updates ni Deletes
- **Inmunidad a Concurrency Issues**: Sin actualización ni borrado, zero concurrent update issues posibles
- **Almacenamiento Permanente e Inmutable**: Análogo a `.git` (sistema de control de versiones), donde cada commit es inmutable


## III Design Principles

Este capítulo es puramente introductorio y expositivo. NO contiene ejemplos de código, firmas de métodos, clases específicas con nombres concretos, casos de uso implementados, ni diagramas de secuencia o de clase. Su propósito es: (1) establecer la razón de ser de los principios SOLID; (2) definir su alcance y nivel de aplicación; (3) proporcionar el contexto histórico de su evolución; (4) presentar un resumen ejecutivo de cada uno de los cinco principios.

Todas las definiciones de los principios se expresan únicamente en prosa conceptual. Por ejemplo, SRP se expresa como "cada módulo debe tener una y solo una razón para cambiar", OCP como "agregar código nuevo, no cambiar código existente", LSP como "adhieren a un contrato que permite sustitución", ISP como "evitar depender de cosas que no se usan", DIP como "detalles deben depender de políticas, no al revés". No hay implementaciones, pseudocódigo, ni ejemplos concretos.

El capítulo referencia una imagen (media/Images/PA-UN03.jpg) sin describir su contenido textualmente en el archivo markdown crudo. Las referencias a documentación externa son: "Agile Software Development, Principles, Patterns, and Practices" (Robert C. Martin, Prentice Hall, 2002), el artículo de Bob Martin en butunclebob.com, y la entrada de Wikipedia sobre SOLID. No se proporcionan fragmentos de código ejecutable.

## 7 SRP: The Single Responsibility Principle

## Ejemplos de Código y Estructuras

### Ejemplo 1: Violación de SRP - Clase Employee Original

```
class Employee {
  // Responsabilidad al CFO (Contabilidad)
  calculatePay(): double
  
  // Responsabilidad al COO (RRHH)
  reportHours(): void
  
  // Responsabilidad al CTO (DBAs)
  save(): void
}
```

Problema: Cuando CFO y COO requieren cambios conflictivos en `regularHours()` (método privado/protegido compartido), el código de un actor corrompe al otro.

### Ejemplo 2: Solución 1 - Separación Data-Functions

```
// Estructura de datos pura - sin métodos de negocio
class EmployeeData {
  name: String
  salary: Money
  hoursWorked: integer
  // ... otros datos
}

// Responsable SOLO a CFO
class PayCalculator {
  calculatePay(employeeData: EmployeeData): Money {
    // Lógica de pago
    regularHours = calculateRegularHours(employeeData)
    return regularHours * employeeData.salary
  }
  
  private calculateRegularHours(employeeData: EmployeeData): double
}

// Responsable SOLO a COO  
class HourReporter {
  reportHours(employeeData: EmployeeData): String {
    // Lógica de reporte de horas (diferentes cálculos de horas regulares)
    regularHours = calculateRegularHours(employeeData)
    return generateReport(regularHours)
  }
  
  private calculateRegularHours(employeeData: EmployeeData): double
  private generateReport(hours: double): String
}

// Responsable SOLO a CTO
class EmployeeRepository {
  save(employeeData: EmployeeData): void {
    // Lógica de persistencia
  }
}
```

Ventaja: Cada clase tiene su propia implementación de `calculateRegularHours()`. Cambios en CFO no afectan COO y viceversa. Sin acoplamiento entre actores.

### Ejemplo 3: Solución 2 - Facade Pattern

```
class EmployeeFacade {
  private payCalculator: PayCalculator
  private hourReporter: HourReporter
  private repository: EmployeeRepository
  private employeeData: EmployeeData
  
  constructor(employeeData: EmployeeData) {
    this.employeeData = employeeData
    this.payCalculator = new PayCalculator()
    this.hourReporter = new HourReporter()
    this.repository = new EmployeeRepository()
  }
  
  // Delegar a responsabilidades específicas por actor
  calculatePay(): Money {
    return payCalculator.calculatePay(employeeData)
  }
  
  reportHours(): String {
    return hourReporter.reportHours(employeeData)
  }
  
  save(): void {
    repository.save(employeeData)
  }
}
```

Uso: `facade = new EmployeeFacade(employeeData); facade.calculatePay(); facade.reportHours(); facade.save();`

### Ejemplo 4: Solución 3 - Facade Inverso

```
class Employee {  // Core business rule (CFO - más importante)
  calculatePay(): Money {
    // Lógica principal
    return this.payCalculator.calculatePay(this.data)
  }
  
  // Delega a otras responsabilidades (actores secundarios)
  reportHours(): String {
    return this.hourReporter.reportHours(this.data)
  }
  
  save(): void {
    this.repository.save(this.data)
  }
  
  private payCalculator: PayCalculator
  private hourReporter: HourReporter
  private repository: EmployeeRepository
  private data: EmployeeData
}
```

### Diagrama de Clases Descrito - Solución 1

```
┌─────────────┐
│ EmployeeData│  (Pura estructura, sin métodos)
│ - name      │
│ - salary    │
│ - hours     │
└──────┬──────┘
       │ (usa)
       ├─────────────────┬──────────────┐
       │                 │              │
┌──────▼────────┐ ┌──────▼────────┐ ┌──▼────────────┐
│PayCalculator  │ │HourReporter   │ │EmployeeRepo   │
│calculatePay() │ │reportHours()  │ │save()         │
│(CFO)          │ │(COO)          │ │(CTO)          │
└───────────────┘ └───────────────┘ └───────────────┘

Independientes - no se conocen entre sí
```

### Diagrama de Clases Descrito - Solución 2 (Facade)

```
              ┌─────────────────┐
              │EmployeeFacade   │
              │ calculatePay()  │
              │ reportHours()   │  (Cliente único ve interfaz unificada)
              │ save()          │
              └────────┬────────┘
                       │
       ┌───────────────┼───────────────┐
       │               │               │
    (instancia y delega a:)
       │               │               │
   Pay        Hour      Employee
Calc      Reporter    Repository
```

### Escenario de Merge Evitado

**SIN SRP** (Violación):
- Dos ramas editan `Employee.java` simultáneamente
- Rama 1 (CTO): Modifica `save()` para nuevo schema
- Rama 2 (COO): Modifica `reportHours()` para nuevo formato
- Resultado: Merge conflict en `Employee.java`

**CON SRP** (Solución 1):
- Rama 1 (CTO): Edita `EmployeeRepository.java`
- Rama 2 (COO): Edita `HourReporter.java`
- Resultado: Sin conflictos, cambios independientes

---

**Nota**: El capítulo no incluye código fuente completo, sino referencias a diagramas UML. Las estructuras de código anterior están inferidas del texto descriptivo. El énfasis del capítulo es conceptual (identificar actores, síntomas de violación) más que implementacional.

## 8 OCP: The Open-Closed Principle

CLASES E INTERFACES DEL DISEÑO DE EJEMPLO:

1. FinancialReportController - clase Controller que maneja entrada del usuario
2. FinancialReportRequester - interfaz que protege Controller de Interactor internals
3. FinancialReportGenerator - clase Interactor que contiene business rules
4. FinancialDataGateway - interfaz que invierte dependencia hacia Database
5. FinancialDataMapper - clase que implementa FinancialDataGateway (implementa relación)
6. FinancialReportPresenter - interfaz que invierte dependencia hacia Presenters
7. FinancialEntities - data structures del dominio
8. Interfaces View (2 adicionales) - para presentación web y printer

ESTRUCTURA DE RELACIONES DE CÓDIGO FUENTE:

FinancialDataMapper implements FinancialDataGateway
  → FinancialDataMapper conoce FinancialDataGateway
  → FinancialDataGateway no conoce FinancialDataMapper

FinancialReportController depends on FinancialReportRequester (using relationship)
  → FinancialReportController knows FinancialReportRequester
  → FinancialReportRequester protege de FinancialEntities knowledge

GRAFO DE COMPONENTES (Figura 8.3 - Relaciones Unidireccionales):

Controller → Interactor
Presenters → Controller
Views → Presenters
Database → Interactor

Dirección: todas las flechas apuntan HACIA componentes a proteger

FLUJO DE DATOS ORIGINAL (Figura 8.1):

Financial Data → Analysis Procedure → Reportable Data → [Reporter Process para Web | Reporter Process para Printer]

CASO DE USO:
- Input: Sistema financiero web mostrando números negativos en rojo, datos desplazables
- Extension requirement: Mismo sistema debe generar reporte imprimible en B&W con:
  * Paginación
  * Page headers/footers
  * Column labels
  * Números negativos entre paréntesis
- Expected result: Cambios de código = cero (mediante arquitectura OCP)

NOTA: Este capítulo es arquitectónico conceptual. No contiene código ejecutable, pseudocódigo, o firmas de métodos detalladas. Su valor está en la diagramación de flujos de datos, separación de responsabilidades, y dirección de dependencias. Las figuras (8.1, 8.2, 8.3) son diagramas sin notación UML completa sino representaciones de flujos y componentes con flechas direccionales y clasificaciones de interfaces/data structures.

## 9 LSP: The Liskov Substitution Principle

### Ejemplos de Código y Estructuras de Datos

**1. Patrón Correcto — License/Billing (líneas 3493-3495)**
```java
class License {
    public void calcFee() { /* abstract */ }
}

class PersonalLicense extends License {
    @Override
    public void calcFee() { /* personal-specific algorithm */ }
}

class BusinessLicense extends License {
    @Override
    public void calcFee() { /* business-specific algorithm */ }
}

class Billing {
    public void bill(License license) {
        license.calcFee();  // substitutable, no type guard needed
    }
}
```

**2. Antipatrón — Square/Rectangle (líneas 3537-3552)**
```java
class Rectangle {
    private int height;
    private int width;
    
    public void setW(int w) { this.width = w; }
    public void setH(int h) { this.height = h; }
    public int area() { return width * height; }
}

class Square extends Rectangle {
    @Override
    public void setW(int w) { this.width = w; this.height = w; }
    @Override
    public void setH(int h) { this.width = h; this.height = h; }
}

// Client code violates LSP:
Rectangle r = new Square();  // polymorphic assignment
r.setW(5);   // Square: w=5, h=5
r.setH(2);   // Square: w=2, h=2 (invariant maintained)
assert(r.area() == 10);  // FAILS! area() == 4, not 10
```

**3. REST API Dispatch URI — Original Specification**
```
Base URI:
  purplecab.com/driver/Bob

Complete dispatch request (PUT):
  purplecab.com/driver/Bob/pickupAddress/24 Maple St./pickupTime/153/destination/ORD
```

**4. Anti-pattern — Hardcoded Type Check (línea 3635)**
```java
if (driver.getDispatchUri().startsWith("acme.com")) {
    // special Acme dispatch format: /dest/%s instead of /destination/%s
    dispatchUrl = formatAcmeDispatch(driver, pickup, time, dest);
} else {
    // standard dispatch format
    dispatchUrl = formatStandardDispatch(driver, pickup, time, dest);
}
```

**5. Architectural Solution — Configuration-Driven Dispatch Formatting (líneas 3649-3661)**

Configuration Table (keyed by dispatch URI pattern):
```
| URI_PATTERN | DISPATCH_FORMAT_TEMPLATE        |
|---|---|
| acme.com    | /pickupAddress/%s/pickupTime/%s/dest/%s |
| *.*         | /pickupAddress/%s/pickupTime/%s/destination/%s |
```

Dispatch command builder (pseudocode):
```java
class DispatchCommandBuilder {
    private ConfigurationDatabase configDb;
    
    public String buildDispatchUrl(Driver driver, String pickup, 
                                    int time, String destination) {
        String dispatchUri = driver.getDispatchUri();
        String formatTemplate = configDb.lookupTemplate(dispatchUri);
        return String.format(formatTemplate, pickup, time, destination);
    }
}
```

**Figuras del capítulo (descritas en prosa)**:

- **Figura 9.1**: Diagrama de clases mostrando `License` como clase base con método `calcFee()`. Dos flechas de herencia desciendo de `License` a `PersonalLicense` y `BusinessLicense`. Módulo `Billing` hace referencia a la clase `License` con línea punteada de dependencia, sin visibilidad de los subtipos. Este diagrama representa composición segura y substitutable.

- **Figura 9.2**: Diagrama de clases similar mostrando `Rectangle` como clase base. `Square` extiende `Rectangle` con flecha de herencia. Clase `User` hace referencia a `Rectangle`. El diagrama visualiza la jerarquía problemática donde `Square` intenta heredar de `Rectangle` pero viola contratos de mutabilidad independiente.

## 10 ISP: The Interface Segregation Principle

**ESTRUCTURAS Y DIAGRAMAS EN PROSA**

1. **Figura 10.1 - Problema de Dependencia No Intencional:**
   ```
   Diagrama: Una clase OPS en el centro expone tres operaciones: op1, op2, op3.
   Tres usuarios acceden a ella: User1 consume op1, User2 consume op2, User3 consume op3.
   Aunque cada usuario usa solo su operación, en lenguajes estáticos todos dependen de OPS completo.
   Cambios a op2 o op3 fuerzan recompilación de User1 aunque no use esas operaciones.
   ```

2. **Figura 10.2 - Segregación de Operaciones en Interfaces:**
   ```
   Diagrama: La clase OPS se mantiene pero ahora está mediada por tres interfaces segregadas:
   - User1 depende de interfaz U1Ops (expone op1)
   - User2 depende de interfaz U2Ops (expone op2)
   - User3 depende de interfaz U3Ops (expone op3)
   La clase OPS implementa las tres interfaces: class OPS implements U1Ops, U2Ops, U3Ops
   Resultado: cambios internos en OPS no fuerzan recompilación de usuarios si no afectan su interfaz específica.
   ```

3. **Figura 10.3 - Problema Arquitectónico de Baggage Innecesario:**
   ```
   Diagrama de dependencia en cadena: Sistema S -> Framework F -> Base de Datos D
   La base de datos D contiene características que F no utiliza, y por tanto S tampoco necesita.
   Cambios a esas características no utilizadas en D fuerzan redeployment de F y S.
   Una falla en características no usadas de D puede propagar fallos a F y S.
   ```

4. **Mecanismo de Recompilación en Lenguajes Estáticos:**
   Cuando el código fuente de User1 contiene una declaración como `import OPS` o `using OPS;`, se crea una dependencia de compilación. El compilador debe verificar el contrato completo de OPS. Cualquier cambio a op2 o op3 altera la definición de OPS, invalidando el bytecode compilado de User1. Con interfaces segregadas como `import U1Ops;`, solo cambios a U1Ops invalidarían el bytecode de User1.

5. **Contraste Lenguajes Dinámicos vs Estáticos:**
   En Ruby/Python: `user1.op1()` es una llamada de método dinámica. No hay declaración en tiempo de compilación. El intérprete resuelve `op1` en runtime. Cambios a op2 en la clase OPS no afectan el bytecode de user1 porque no hay bytecode precompilado. La flexibilidad proviene de la ausencia de dependencias de código fuente explícitas.

6. **No hay código literal en este capítulo**, pero la estructura conceptual es clara: interfaces segregadas como patrones, dependencias inversas entre usuarios e interfaces, e implementación múltiple de interfaces por parte de la clase concreta OPS.

## 11 DIP: The Dependency Inversion Principle

### Estructuras y Firmas Exactas del Patrón Abstract Factory (Figure 11.1)

**Interfaz Service (abstracta)**:
- Interfaz base que `Application` utiliza para interactuar con la implementación concreta

**Clase ConcreteImpl**:
- Implementación concreta de `Service`
- Contiene la lógica de negocio específica

**Interfaz ServiceFactory (abstracta)**:
- Método: `makeSvc()` - retorna un objeto de tipo `Service`

**Clase ServiceFactoryImpl**:
- Hereda de `ServiceFactory`
- Implementa `makeSvc()` para instanciar `ConcreteImpl` y retornarla como tipo `Service`

**Clase Application**:
- Depende de:
  - Interfaz `Service` (para usar la implementación)
  - Interfaz `ServiceFactory` (para crear instancias)
- Accede a `ServiceFactory` a través de una variable global

**Diagrama de Dependencias (Prosa)**:
- Límite arquitectónico (línea curva) separa el componente abstracto del concreto
- Lado abstracto: `Application`, `Service` (interfaz), `ServiceFactory` (interfaz)
- Lado concreto: `ServiceFactoryImpl`, `ConcreteImpl`
- Las flechas de dependencia de código fuente apuntan todas hacia el lado abstracto (arriba)
- El flujo de control va en dirección opuesta: desde `Application` a través de la interfaz `Service` hacia `ConcreteImpl`, atravesando la línea curva en la dirección opuesta

**Inicialización en main()**:
```
main() {
    ServiceFactory factory = new ServiceFactoryImpl();
    // Colocar factory en variable global de tipo ServiceFactory
    globalServiceFactory = factory;
}

Application.getInstance() {
    // Acceder a la factory a través de la variable global
    Service service = globalServiceFactory.makeSvc();
}
```

El capítulo enfatiza que esta estructura elimina la dependencia de código fuente directo de `Application` hacia `ConcreteImpl`, manteniendo una dependencia solo en abstracciones (`Service` y `ServiceFactory`), mientras el flujo de control en tiempo de ejecución sigue fluyendo hacia la implementación concreta.

## IV Component Principles

Este capítulo introductorio no contiene ejemplos de código concretos, firmas de métodos específicas, nombres de clases implementadas, ni fragmentos de código. Tampoco describe diagramas de secuencia o de estructura de clases con detalles operacionales. Su propósito es estrictamente introductorio: establecer la metáfora conceptual (bricks → walls/rooms → buildings) que sirve como marco mental para los capítulos subsecuentes de la Parte IV, que sí contienen especificaciones de componentes, patrones de acoplamiento, y principios concretos de composición de componentes. El capítulo actúa como puerta de entrada conceptual antes de abordar Component Cohesion Principles (REP, CCP, CRP) y Component Coupling Principles (ADP, SDP, SAP) en los capítulos siguientes.

## 12 Components

**Código PDP-8 Assembly - Subrutina GETSTR con Test**
```
    *200
    TLS
START,     CLA
          TAD BUFR
          JMS GETSTR
          CLA
          TAD BUFR
          JMS PUTSTR
          JMP START

BUFR,      3000

GETSTR,    0
          DCA PTR
NXTCH,    KSF
          JMP -1
          KRB
          DCA I PTR
          TAD I PTR
          AND K177
          ISZ PTR
          TAD MCR
          SZA
          JMP NXTCH

K177,      177
MCR,       -15
```
**Explicación:** `*200` origin statement declara dirección de carga 200₈. `GETSTR` es subrutina que ingresa strings del teclado usando `KSF` (teclado flag skip), `KRB` (teclado read buffer), `DCA I PTR` (deposit in accumulator, indirect via pointer) almacena carácter. `AND K177` máscara a 7 bits. `K177` (octal 177 = decimal 127) es máscara ASCII. `MCR` (octal -15 = decimal -13) es carriage return. `JMS` (jump to subroutine) retorna.

**Ningún código adicional es mencionado en el capítulo.** El capítulo es primariamente histórico y conceptual, cubriendo evolución de mecanismos de linking y relocation desde era manual de memoria (1950s) a plugin architecture moderna (1990s-presente). No contiene patrones de diseño de componentes, firmas de métodos Java/C#/Ruby, ni casos de uso aplicados. El único artefacto de código es el programa assembly PDP-8 ilustrando la era pre-modular, cuando bibliotecas se compilaban inline.

## 13 Component Cohesion

Este capítulo es conceptual y teórico, dedicado a presentar y justificar tres principios arquitectónicos fundamentales (REP, CCP, CRP) y sus interacciones. NO contiene ejemplos de código específico, firmas de métodos, declaraciones de clases o implementaciones concretas.

El único artefacto visual referenciado es:
- **Figure 13.1: Cohesion Principles Tension Diagram** - Un diagrama triangular con vértices en REP, CCP y CRP, mostrando las interacciones tensionales entre estos principios (fuente: media/Images/13fig01.jpg)
- **Chapter Header Image** - Imagen decorativa (media/Images/CH-UN13.jpg)

**Única Referencia Conceptual a Estructuras Concretas**:
- Container class con sus iteradores asociados - mencionado como ejemplo de clases que se reutilizan juntas y deben estar en el mismo componente, pero sin especificación de código.

El capítulo se enfoca exclusivamente en la teoría de partición de componentes, principios de diseño arquitectónico, y trade-offs de decisión, prescindir de ejemplos de código compilable o pseudocódigo ejecutable. La densidad es conceptual-didáctica, no implementacional.

## 14 Component Coupling


Este capítulo es fundamentalmente conceptual y no contiene fragmentos de código ejecutable. Sin embargo, contiene descripciones precisas de diagramas arquitectónicos en prosa:

## DESCRIPCIONES DE DIAGRAMAS EN PROSA

**Figure 14.1 (Typical component diagram)**
- Componentes (nodos): Entities, Database, Interactors, Authorizer, Presenters, Controllers, View, Main
- Estructura: DAG acíclico donde es imposible seguir flechas de dependencia y volver al punto de partida
- Implicación: Cada componente tiene clear dependents upstream

**Figure 14.2 (A dependency cycle)**
- Ciclo: User (en Entities) → Permissions (en Authorizer) → Interactors → [back to Entities]
- Causa: New requirement fuerza a User usar Permissions
- Efecto: Entities, Authorizer, Interactors se convierten en mega-componente acoplado

**Figure 14.3 (Inverting dependency via DIP)**
- Antes: Entities --> Authorizer (dependencia directa entre componentes)
- Solución: Crear interfaz en Entities que Permissions implementa desde Authorizer
- Después: Dependencia invertida; ciclo roto

**Figure 14.4 (New component extraction)**
- Crear componente neutral (Common/Shared)
- Ambos Entities y Authorizer dependen de Common
- Clase/interfaz compartida movida a Common
- Resultado: DAG restaurado

**Figure 14.5 (Stable component X)**
- Componente X: 3 componentes dependen de él (Fan-in = 3)
- Componente X: No depende de nada (Fan-out = 0)
- I = 0 / (3 + 0) = 0 (maximally stable)
- Clasificación: Responsible (muchos dependents), Independent (cero dependencias)

**Figure 14.6 (Unstable component Y)**
- Componente Y: Nadie depende (Fan-in = 0)
- Componente Y: 3 componentes que depende (Fan-out = 3)
- I = 3 / (0 + 3) = 1 (maximally unstable)
- Clasificación: Irresponsible (cero dependents), Dependent (múltiples dependencias externas)

**Figure 14.7 (Fan-in/Fan-out calculation example)**
- Componente Cc: 3 clases externas dependen de él (Fan-in = 3)
- Componente Cc: 1 clase externa que clases en Cc dependen (Fan-out = 1)
- Cálculo: I = 1 / (3 + 1) = 1/4 = 0.25 (bastante stable)

**Figure 14.8 (Ideal configuration)**
- Top tier: Flexible, Changeable components (I ≈ 1)
- Bottom tier: Stable component (I ≈ 0)
- Dependencies: Todos fluyen downward (hacia estable)
- Convention: Arrows pointing UP = violación de SDP

**Figure 14.9 (SDP violation)**
- Stable (I ≈ 0) depende en Flexible (I ≈ 1)
- Violación: Arrow pointing upward violates SDP
- Consecuencia: Flexible becomes difficult to change despite design intent

**Figure 14.10 (Class-level dependency causing component cycle)**
- Within Stable: Clase U usa Clase C
- Where C is: Dentro componente Flexible
- Problem: Stable --> Flexible creates violation

**Figure 14.11 (DIP solution at component level)**
- Crear componente UServer (abstract, interface-only)
- Crear interfaz US en UServer declarando métodos que U necesita
- C implementa interfaz US (hereda desde Flexible)
- Resultado: Stable --> UServer (maximally stable, I=0), Flexible --> UServer
- Flow: Todas dependencias en dirección de decreasing I

**Figure 14.12 (I/A graph)**
- Axis: X=I (0 a 1, unstable to stable), Y=A (0 a 1, concrete to abstract)
- Good corners: (0,1) stable-abstract, (1,0) unstable-concrete
- Main Sequence: Línea diagonal conectando (1,0) a (0,1)

**Figure 14.13 (Zones of Exclusion)**
- Zone of Pain: Esquina (0,0) — stable pero concreto = rigid, inflexible
- Zone of Uselessness: Esquina (1,1) — unstable y abstract = irrellevant, unused
- Main Sequence: Zona donde componentes deben vivir

**Figure 14.14 (Scatterplot of I/A positions)**
- Axis: I horizontal, A vertical
- Bulk: Componentes dispersos a lo largo Main Sequence
- Outliers: Puntos más de 1 sigma away identifican aberrancies
- Inspect: Por qué ciertos componentes están tan far from ideal

**Figure 14.15 (D metric temporal plot)**
- X-axis: Release versions (R1, R2, R2.1, etc.)
- Y-axis: D metric value para componente Payroll
- Control line: D = 0.1 threshold
- Alert: R2.1 exceeds threshold; strange dependencies han estado creeping in

## FÓRMULAS Y MÉTRICAS EXACTAS

```
Fan-in = número de clases externas que dependen de clases en este componente
Fan-out = número de clases internas que dependen de clases externas
I (Instability) = Fan-out / (Fan-in + Fan-out)  [rango: 0 a 1]

Nc = número total de clases en componente
Na = número de abstract classes e interfaces en componente  
A (Abstractness) = Na ÷ Nc  [rango: 0 a 1]

D (Distance from Main Sequence) = |A + I - 1|  [rango: 0 a 1]
D = 0 → on Main Sequence (ideal)
D = 1 → maximally far from Main Sequence
```

## COMPONENTES Y CLASES MENCIONADOS

**Ejemplos de componentes reales en capítulo**:
- Entities (con clase User)
- Database
- Interactors
- Authorizer (con clase Permissions)
- Presenters
- Controllers
- View
- Main
- Common/Shared (propuesto)
- UServer (abstract component con interfaz US)
- String (utility component example)

**Interfaces y abstractiones mencionadas**:
- Interfaz con métodos que User necesita (DIP example)
- Interfaz US que declara métodos que U necesita
- Abstract classes en general

**No existen en el capítulo**:
- Métodos específicos con firmas completas
- Atributos de clases
- Implementaciones concretas
- Código ejecutable en lenguaje específico

El capítulo es puramente arquitectónico y conceptual, enfocado en principios, patrones, métricas y sus trade-offs.


## V Architecture

No hay ejemplos de código en este rango; se trata únicamente de marcado de sección.

## 15 What Is Architecture?

### Ejemplo 1: Subroutine PRTCHR en Assembly del PDP-8 (circa 1960s)
Código machine que imprime un carácter en el teleprinter del PDP-8:

```
PRTCHR, 0  
        TSF  
        JMP .-1  
        TLS  
        JMP I PRTCHR
```

**Desglose del flujo de control**:
- `PRTCHR, 0`: Label de subroutina; el cero inicial se usaba como almacenamiento para la dirección de retorno (peculiar del PDP-8)
- `TSF`: "Test Status Flag"—salta la siguiente instrucción si el teleprinter está listo para imprimir un carácter
- `JMP .-1`: Si el teleprinter está ocupado, salta atrás a `TSF` (loop de espera busy)
- `TLS`: "Transmit Line Start"—envía el carácter en el registro `A` al teleprinter (solo se ejecuta si teleprinter está listo)
- `JMP I PRTCHR`: "Jump Indirect"—retorna a la dirección almacenada en `PRTCHR` (la dirección del llamador)

Este código es **device-dependent**: está acoplado específicamente a las instrucciones IO del teleprinter del PDP-8.

### Ejemplo 2: Estructuras de Datos del Sistema Contable de Truck Union (circa 1970s)
Sistema de almacenamiento en disco de 25MB con tres tipos de records: `Agents`, `Employers`, `Members`.

**Arreglo físico original (device-dependent)**:
```
Disco de 25MB (200 cilindros × 10 heads)
├─ Cilindros 0-X: Formatted sectors = [Agent record size]
│   └─ Índice: {agent_id, cylinder, head, sector} lookup
├─ Cilindros X+1-Y: Formatted sectors = [Employer record size]
│   └─ Índice: {employer_id, cylinder, head, sector} lookup
└─ Cilindros Y+1-199: Formatted sectors = [Member record size]
    └─ Doubly Linked List on disk:
       Member Record = {
           member_id,
           data...,
           next_cylinder, next_head, next_sector,
           prev_cylinder, prev_head, prev_sector
       }
```

**Problema**: Todo el business logic estaba hard-wired con cilindro/head/sector addressing:
- Rutas de acceso a datos: `fetch(agent_id) -> lookup_table -> (cylinder, head, sector) -> disk_read(cylinder, head, sector)`
- Navegación de linked list: cada traversal requería calcular direcciones físicas

**Solución arquitectónica—Relative Addressing (device-independent)**:
```
Disco abstracto como arreglo linear
Linear Address Space: [0, 1, 2, ..., N-1] 
    (donde N = total sectors)

Conversion Layer (Device Abstraction):
    relative_address → (cylinder, head, sector)
    
Policy-level code:
    fetch(agent_id) -> lookup_table -> relative_address -> 
    conversion_layer(relative_address) -> 
    disk_read_physical(cylinder, head, sector)
```

El negocio lógico ahora solo comprende direcciones relativas. Una rutina de conversión pequeña maneja la traducción a coordenadas físicas. El cambio a un drive con diferente geometría solo requiere actualizar la rutina de conversión, no el código de negocio.

### Ejemplo 3: Junk Mail Processing (circa late 1960s)—Flujo de Datos
**Flujo sin abstracción device-independent (problemático)**:
```
Input: Magnetic tape unit records (customer names/addresses)
    ↓
Read directly from tape device → application policy
    ↓
Format personalized letters
    ↓
Print directly to IBM 360 line printer
    ↓
Output: ~few thousand letters per shift (machine heavily occupied)
```

**Flujo con abstracción device-independent (escalable)**:
```
Input: Magnetic tape unit records
    ↓
Application policy (device-agnostic):
    read_abstract_unit_records()
    format_personalized_output()
    write_abstract_unit_records()
    ↓
Operating System Abstraction Layer:
    Input device:  configure to read from physical tape drive
    Output device: configure to write to physical magnetic tape (not line printer)
    ↓
Runtime Configuration Change (no code modification):
    OS device mapping: [output] → [offline magnetic tape] (not line printer)
    ↓
Output: Write one full tape per ~10 minutes
    ↓
Offline Processing:
    Take tape to separate room
    Mount on 5 different offline printers
    Run 24/7 printing hundreds of thousands of junk mail pieces per week
```

El mismo código de aplicación funciona con cualquier dispositivo porque la decisión sobre dispositivos fue diferida al nivel del SO, demostrando el poder de separar policy (formatting logic) de details (device I/O).

### Resumen de Principios Arquitectónicos Demostrados

| Concepto | Definición | Implicación |
|----------|-----------|------------|
| **Policy** | Business rules y procedures—núcleo de valor del sistema | Debe ser device-agnostic e independent |
| **Details** | IO devices, databases, frameworks, protocols—no impactan behavior | Deben ser reversibles/reemplazables |
| **Separation of Concerns** | Desacoplar policy de details mediante abstracción | Decisions sobre details pueden ser deferred |
| **Device Independence** | No vincular código directamente a hardware específico | Permite cambiar dispositivos sin reescribir business logic |
| **Open-Closed Principle** | Cerrado para modificación, abierto para extensión | Abstracciones permiten nuevos devices sin cambiar policy |
| **Delaying Decisions** | No elegir framework/database/protocol temprano | Mayor información disponible cuando la decisión no puede deferred más |



## 16 Independence

El capítulo "Independence" de Clean Architecture no contiene ejemplos de código, firmas de métodos, o casos de uso concretos con implementación. Es un capítulo de principios y directrices arquitectónicas que establece conceptos fundamentales de desacoplamiento y flexibilidad.

Sin embargo, el capítulo refiere a entidades conceptuales específicas mencionadas como ejemplos ilustrativos:

**Casos de Uso Nombrados (Como Ejemplos Ilustrativos, No Implementaciones):**
- `addOrder` - use case para agregar una orden a un sistema de entrada de órdenes
- `deleteOrder` - use case para eliminar una orden del sistema
- Validación de campos de entrada - regla de negocio específica de aplicación
- Cálculo de interés en cuentas - regla de negocio independiente de aplicación
- Conteo de inventario - regla de negocio independiente de aplicación

**Tipos de Sistemas Mencionados como Contextos:**
- Sistema de carrito de compras
- Sistema de entrada de órdenes (order entry system)
- Sistema de bill of materials
- Sistemas que deben manejar 100,000 clientes por segundo
- Sistemas que deben consultar big data cubes en milisegundos

**Tecnologías de Desacoplamiento Mencionadas (No Código, Sino Conceptos):**
- Ruby Gems (para source-level decoupling)
- jar files, DLLs, shared libraries (para deployment-level decoupling)
- Servicios/microservicios (para service-level decoupling)
- Comunicación por network packets
- Function calls (comunicación en monolitos)
- Interprocess communications, sockets, shared memory (para deployment-level)

**Principios Enunciados (No Código):**
- Single Responsibility Principle (SRP)
- Common Closure Principle (CCP)
- Conway's Law: "Any organization that designs a system will produce a design whose structure is a copy of the organization's communication structure."
- Principios de team organization: feature teams, component teams, layer teams

El capítulo es enteramente conceptual y arquitectónico, enfocado en guiar decisiones de diseño sin proporcionar implementaciones concretas. Su valor radica en los patrones de pensamiento y criterios de decisión para estructurar sistemas grandes de manera flexible y mantenible.

## 17 Boundaries: Drawing Lines

### 1. Patrón DatabaseInterface-DatabaseAccess (FitNesse y Arquitectura General)

**Interfaz Core (vive en BusinessRules component)**:
```java
public interface WikiPage {
    // Data access methods
    WikiPage findPage(String pageName);
    WikiPage fetchPage(String pageId);
    void savePage(WikiPage page);
    // Additional query methods as needed
}
```

**Implementaciones Concretas (viven en Database component)**:
```java
// Primera implementación - 3 meses, desarrollo sin persistencia
public class MockWikiPage implements WikiPage {
    public WikiPage findPage(String pageName) { /* stubbed */ }
    public WikiPage fetchPage(String pageId) { /* stubbed */ }
    public void savePage(WikiPage page) { /* stubbed */ }
}

// Segunda implementación - 1 año completo en memoria
public class InMemoryPage implements WikiPage {
    private static Map<String, WikiPage> pageMap = new HashMap<>();
    
    public WikiPage findPage(String pageName) {
        return pageMap.get(pageName);
    }
    
    public WikiPage fetchPage(String pageId) {
        return pageMap.get(pageId);
    }
    
    public void savePage(WikiPage page) {
        pageMap.put(page.getId(), page);
    }
}

// Tercera implementación - archivo plano
public class FileSystemWikiPage implements WikiPage {
    public WikiPage findPage(String pageName) { /* filesystem operations */ }
    public WikiPage fetchPage(String pageId) { /* filesystem operations */ }
    public void savePage(WikiPage page) { /* filesystem operations */ }
}

// Cuarta implementación - cliente escribió en UN DÍA
public class MySqlWikiPage implements WikiPage {
    public WikiPage findPage(String pageName) { /* SQL queries */ }
    public WikiPage fetchPage(String pageId) { /* SQL queries */ }
    public void savePage(WikiPage page) { /* SQL operations */ }
}
```

**Consumidor (BusinessRules component)**:
```java
public class WikiPageManager {
    private WikiPage wikiPageRepository;  // Dependency injection
    
    public void publishPage(String pageName, String content) {
        WikiPage page = wikiPageRepository.findPage(pageName);
        page.updateContent(content);
        wikiPageRepository.savePage(page);
    }
    
    public String renderPage(String pageName) {
        WikiPage page = wikiPageRepository.fetchPage(pageName);
        return page.renderAsHtml();
    }
}
```

### 2. Diagrama Conceptual: Boundary y Dirección de Dependencias

**Figura 17.1 - Database Behind an Interface**:
```
┌─────────────────────────────────────────────────────┐
│ BusinessRules                                       │
│  ┌─────────────┐                                    │
│  │  UseCase    │                                    │
│  │  (business  │──uses──┐                           │
│  │   logic)    │        │                           │
│  └─────────────┘        │                           │
│                         ▼                           │
│              ┌──────────────────┐                   │
│              │ DatabaseInterface│ (Abstract)        │
│              │  +findPage()     │                   │
│              │  +fetchPage()    │                   │
│              │  +savePage()     │                   │
│              └──────────────────┘                   │
└────────────────────────▲──────────────────────────┘
                         │
                    [BOUNDARY]
                         │
┌────────────────────────┴──────────────────────────┐
│ Database Component                                 │
│              ┌──────────────────┐                  │
│              │  DatabaseAccess  │                  │
│              │  implements      │                  │
│              │  DatabaseInterface                 │
│              │ +findPage()      │                  │
│              │ +fetchPage()     │                  │
│              │ +savePage()      │                  │
│              └────────┬─────────┘                  │
│                       │                            │
│                       ▼                            │
│              ┌──────────────────┐                  │
│              │    Database      │                  │
│              │  (MySQL/Oracle   │                  │
│              │   /Filesystem)   │                  │
│              └──────────────────┘                  │
└───────────────────────────────────────────────────┘

Direction of arrows: AWAY from DatabaseAccess (nothing knows it exists)
Cross-boundary: Database knows BusinessRules; BusinessRules does NOT know Database
```

**Figura 17.3 - Business Rules and Database Components**:
```
┌────────────────────────────┐
│  BusinessRules Component   │
│  - Core domain logic       │
│  - Use cases               │
│  - Entities                │
│                            │
│  DatabaseInterface defined │
│  (interfaces/contracts)    │
└───────────────┬────────────┘
                │
                │ (Database knows about BusinessRules)
                │ (BusinessRules does NOT know about Database)
                │
                ▼
┌────────────────────────────┐
│   Database Component       │
│  - DatabaseAccess impls    │
│  - Query builders          │
│  - Schema mappings         │
│  - Connection management   │
└────────────────────────────┘
```

**Figura 17.4 - Boundary Between GUI and BusinessRules**:
```
┌────────────────────────────┐
│  GUI Component             │
│  - Web UI/Desktop/CLI      │
│  - Controllers             │
│  - Presenters              │
│                            │
│  Depends on BusinessRules  │
└───────────────┬────────────┘
                │
                │ (GUI knows about BusinessRules)
                │ (BusinessRules does NOT know about GUI)
                │
                ▼
┌────────────────────────────┐
│  BusinessRules Component   │
│  - Core business logic     │
│  - Entities & value objects
│  - Use case interactors    │
└────────────────────────────┘
```

### 3. Casos de Uso: Company P vs. Company W - Trade-offs

**Company P Three-Tiered Anti-Pattern**:
```
Adding single field to existing record requires:
- Modify: GuiTierClass, MiddlewareTierClass, DatabaseTierClass (3 changes)
- Update: 4 inter-tier message protocols bidirectionally
- Create: 8 protocol handlers (send and receive sides)
- Build: 3 executables with updates

Overhead even on local single machine:
- Object instantiation across tiers
- Serialization/Deserialization
- Marshaling/De-marshaling
- Message building/parsing
- Socket communications (even localhost)
- Timeout managers
- Retry scenarios

Result: Server farm never deployed; 18+ months of unnecessary complexity
```

**Company W SOA Prematura Anti-Pattern**:
```
Adding contact info (name, address, phone) to sales record:

1. lookup: ServiceRegistry.getServiceId(ContactService)
2. call: SendMessage(CreateContact) 
   - Requires: dozens of fields with valid data (but programmer only has 3)
   - Must fake: all other required fields
3. receive: Contact ID from response
4. update: SaleRecord.setContactId(contactId)
5. call: SendMessage(UpdateContact) to SaleRecordService
6. propagate: through message bus with queues and delays

Testing overhead:
- Startup all required services sequentially
- Fire up message bus
- Fire up BPEL server
- Wait for propagation through queues
- Manage deployment cascades when WSDLs change
```

### 4. Plugin Argument: ReSharper/Visual Studio Asymmetry

**Dependency Structure**:
```
ReSharper Source Code ──depends on──> Visual Studio Source Code

Immunity analysis:
- ReSharper team changes: CANNOT affect Visual Studio team (immune)
- Visual Studio team changes: CAN completely disable ReSharper (power asymmetry)

Desired system property:
- Core business rules component: IMMUNE to GUI/Database changes
- GUI/Database: can depend on business rules
- Changes isolated by boundaries prevent cascade failures
```

### 5. Axes of Change: Where Boundaries Live

**Example 1: GUI vs. BusinessRules**
```
GUI axis of change:
- Changes at different times (UI updates, framework updates)
- Changes for different reasons (user experience, accessibility, browser compatibility)
- Technology volatility: web→desktop→mobile→voice

BusinessRules axis of change:
- Changes driven by business logic evolution
- Rate of change: much slower than UI
- Reason for change: business domain shifts, not technology fashion

Boundary required between them to prevent fragility
```

**Example 2: BusinessRules vs. DI Framework**
```
DI Framework axis of change:
- Framework updates
- New container features
- Alternative frameworks (Spring→Guice→manual)

BusinessRules axis of change:
- Business domain logic
- Use case implementations
- Entity state rules

Boundary isolates business logic from DI technology choices
```

### 6. Explicit Principle Application: SRP, DIP, SAP

**Single Responsibility Principle**: Each component has one reason to change
```
- Database component: changes when data storage strategy changes
- GUI component: changes when presentation requirements change
- BusinessRules component: changes when business rules evolve
```

**Dependency Inversion Principle**: High-level modules (BusinessRules) do NOT depend on low-level modules (Database, GUI)
```
Both depend on abstractions:
BusinessRules → DatabaseInterface ← DatabaseAccess
BusinessRules ← (not), GUI → BusinessRules (asymmetric dependency)
```

**Stable Abstractions Principle**: Depend on stable (abstract) things, not volatile (concrete) things
```
DatabaseInterface (stable): defined by business needs
DatabaseAccess (volatile): implementation details change
BusinessRules (stable): core logic
GUI (volatile): technology changes rapidly
```

---

**Nota**: El capítulo NO contiene ejemplos de código fuente reales. Los ejemplos anteriores son reconstructiones conceptuales basadas en las descripciones narrativas del texto. Las Figuras 17.1-17.6 son diagramas referenciados (en media/Images/) pero descritos como diagr componentes con arrows de dependencia; se han renderizado aquí en formato texto ASCII siguiendo las descripciones prosa del capítulo.

## 18 Boundary Anatomy

### Boundary Crossing Simple (Figura 18.1) - Flow of Control Hacia Nivel Superior
```
Cliente → Service.f(Data)

Pseudostructura de dependencias:
┌─────────────────────────────────────┐
│ Lower-Level Client                  │
│  - calls Service.f()                │
│  - passes Data                      │
│ (Compile-time dep: →)               │
└────────────┬────────────────────────┘
             │ (Control flow →)
             │
┌────────────▼────────────────────────┐
│ Higher-Level Service                │
│ - method f()                        │
│ - Data definition                   │
│ (Compile-time dep: ←)               │
└─────────────────────────────────────┘

Características:
- Flow de control: izquierda → derecha
- Dependencia runtime: → (hacia Service)
- Dependencia compile-time: → (hacia Service)
- Data definida: en lado LLAMADO
```

### Boundary Crossing Invertido (Figura 18.2) - Polimorfismo Dinámico
```
Cliente Alto Nivel → Service (interfaz) ← ServiceImpl

Pseudostructura de dependencias:
┌─────────────────────────────────────┐
│ High-Level Client                   │
│ - calls Service.f()                 │
│ - Data definition                   │
│ (Compile-time dep: ←)               │
└────────────┬────────────────────────┘
             │ (Control flow →)
             │ (through interface)
             ▼
┌────────────────────────────────────┐
│ <<interface>> Service              │
│ + f(): void                        │
└────────────▲──────────────────────┘
             │ (Compile-time dep: ←)
             │
┌────────────┴──────────────────────┐
│ ServiceImpl (Low-Level)             │
│ - implements Service               │
│ - f(): void                        │
│ (Compile-time dep: ←)              │
└─────────────────────────────────────┘

Características:
- Flow de control: izquierda → derecha
- Dependencia runtime: → (al objeto concreto)
- Dependencia compile-time: ← (hacia interfaz)
- Data definida: en lado LLAMANTE
- Inversión: runtime ≠ compile-time
```

### Estratificación en Monolith Threaded
```
Statically-linked executable:
┌──────────────────────────────────────┐
│ Single Address Space                 │
│ Single Processor                     │
├──────────────────────────────────────┤
│ │ Thread 1 │ Thread 2 │ Thread 3 │  │
│ ├──────────────────────────────┤    │
│ │ Component A                  │    │
│ ├──────────────────────────────┤    │
│ │ Component B (via polymorphism)   │
│ ├──────────────────────────────┤    │
│ │ Component C                  │    │
│ └──────────────────────────────┘    │
└──────────────────────────────────────┘

Communication: Function calls (very fast)
Chattiness: Permitted
Deployment: Compilation + Static linking
Delivery: Source code
```

### Deployment Components (Dinámicamente Vinculados)
```
.NET DLL / Java .jar / Ruby Gem / UNIX .so

┌──────────────────────────────────────┐
│ Runtime Process (same processor)     │
├──────────────────────────────────────┤
│ Loaded Component A.dll               │
├──────────────────────────────────────┤
│ Loaded Component B.dll               │
├──────────────────────────────────────┤
│ Loaded Component C.dll               │
└──────────────────────────────────────┘

Diferencia vs Monolith:
- Entrega: Binary/Deployable form (no source)
- Deployment: No compilation necesaria
- Packaging: WAR file, directorio
- Communication: Function calls (fast)
- Initial cost: Dynamic linking / runtime loading
```

### Local Process Boundary
```
┌──────────────────────┐    Socket/IPC    ┌──────────────────────┐
│ Process A            │◄─────────────────►│ Process B            │
│ Address Space A      │   Marshaling      │ Address Space B      │
│ ┌──────────────────┐ │   Decoding       │ ┌──────────────────┐ │
│ │ Component A1     │ │                   │ │ Component B1     │ │
│ ├──────────────────┤ │   Memory          │ ├──────────────────┤ │
│ │ Component A2     │ │   Protection      │ │ Component B2     │ │
│ └──────────────────┘ │   enforced        │ └──────────────────┘ │
└──────────────────────┘                   └──────────────────────┘
  (Higher-level "plugin" caller)             (Lower-level "plugin")
  ← Dependency direction

Communication cost: OS calls + marshaling/decoding + context switches
Chattiness: Must carefully limit
Latency: Moderate
```

### Service Boundary
```
┌──────────────────────┐    Network        ┌──────────────────────┐
│ Service A            │◄───────────────────│ Service B            │
│ (High-level)         │   HTTP/gRPC/TCP   │ (Low-level)          │
│ Machine X            │   Serialization   │ Machine Y (or same)  │
│ ┌──────────────────┐ │   Deserialization│ ┌──────────────────┐ │
│ │ Monolith or      │ │   Network I/O    │ │ Monolith or      │ │
│ │ Deployment       │ │   Packets travel │ │ Deployment       │ │
│ │ Components       │ │                   │ │ Components       │ │
│ └──────────────────┘ │   URI-agnostic   │ └──────────────────┘ │
└──────────────────────┘   (no hardcoding) └──────────────────────┘
  No conocimiento de ubicación física

Communication cost: Very slow (10ms-seconds)
Chattiness: Avoid aggressively
Latency: High (must handle)
```

### Restricciones de Dependencia (Aplicables a todos los tipos)

**NO en código fuente de componente de nivel superior:**
```
// PROHIBIDO en ServiceA (alto nivel) si B es bajo nivel:

// Monolith/Deployment Components:
#include "ComponentB.h"  // ✗ Dependency violates boundary

// Local Processes:
string processPath = "/usr/bin/process-b";  // ✗ Physical address
string registryKey = "HKLM\\ProcessRegistry\\B";  // ✗ Registry lookup

// Services:
string serviceBUri = "http://192.168.1.100:8080/service-b";  // ✗ Hardcoded URI
```

**SÍ: Plugin architecture (bidirectional dependencies contramedida):**
```
// CORRECTO: ComponentA (alto) vs ComponentB (bajo)
// A declara interfaz, B la implementa

// In ComponentA (high-level):
class ServiceA {
    private IComponentB dependency;  // Depends on abstraction
    public ServiceA(IComponentB impl) { 
        dependency = impl;  // Injected
    }
}

// In ComponentB (low-level):
class ComponentB : IComponentB {  // Implements interface defined in A
    public void doWork() { }
}

// Dependency flow: B → A (compila hacia lo abstracto en A)
```

### Síntesis: Mezcla de Boundaries en Sistema Real

```
┌─────────────────────────────────────────────────────────┐
│ Service Boundary (Slowest, Network)                     │
│ ┌───────────────────────────────────────────────────────┤
│ │ Local Process A (Moderate, Marshaling)                │
│ │ ┌─────────────────────────────────────────────────────┤
│ │ │ Monolith/Deployment Components (Fastest, Calls)     │
│ │ │ ┌──────────────────────────────────────────────────┐│
│ │ │ │ Threads (Scheduling, not boundary)              ││
│ │ │ └──────────────────────────────────────────────────┘│
│ │ └─────────────────────────────────────────────────────┘
│ └───────────────────────────────────────────────────────┘
└─────────────────────────────────────────────────────────┘

Trade-off matriz:
┌────────────────┬─────────────┬─────────────┬──────────────┐
│ Boundary Type  │ Speed       │ Chattiness  │ Latency      │
├────────────────┼─────────────┼─────────────┼──────────────┤
│ Monolith       │ Very fast   │ Permitted   │ Microseconds │
│ Deployment     │ Very fast   │ Permitted   │ Microseconds │
│ Local Process  │ Moderate    │ Limited     │ Milliseconds │
│ Service        │ Very slow   │ Restricted  │ Seconds      │
└────────────────┴─────────────┴─────────────┴──────────────┘
```

El capítulo no contiene ejemplos de código explícitos sino descripciones architectónicas abstractas. Las estructuras anteriores son reconstrucciones en prosa de los conceptos presentados, particularmente las Figuras 18.1 y 18.2, que Martin describe mediante dependencias y flujos de control pero no como código ejecutable.

## 19 Policy and Level

## Ejemplos de Código y Diagramas

### Ejemplo 1: Implementación Incorrecta (Violación de DIP)
```
function encrypt() {
  while(true)
    writeChar(translate(readChar()));
}
```
**Problema arquitectónico**: La función `encrypt()` de nivel alto depende directamente de funciones de nivel bajo `readChar()` y `writeChar()`. Las dependencias de código van en dirección opuesta a la abstracción.

### Ejemplo 2: Arquitectura Correcta (Inversión de Dependencias)

**Estructura de clases (Class Diagram - Figure 19.2)**:
- Clase `Encrypt`: Política de alto nivel (rodeada por dashed border indicando límite de componente de nivel más alto)
  - Depende de: `CharReader` (interfaz abstracta)
  - Depende de: `CharWriter` (interfaz abstracta)
- Clase `ConsoleReader`: Implementa `CharReader`, nivel bajo (cercano a inputs)
- Clase `ConsoleWriter`: Implementa `CharWriter`, nivel bajo (cercano a outputs)

**Firmas de interfaz implícitas**:
```
interface CharReader {
  char readChar()
}

interface CharWriter {
  void writeChar(char c)
}

class Encrypt {
  constructor(reader: CharReader, writer: CharWriter)
  void encryptLoop() {
    while(true)
      writer.writeChar(translate(reader.readChar()))
  }
}

class ConsoleReader implements CharReader {
  char readChar() { /* lee del dispositivo */ }
}

class ConsoleWriter implements CharWriter {
  void writeChar(char c) { /* escribe al dispositivo */ }
}
```

**Dirección de dependencias correcta**: `ConsoleReader` → `CharReader`, `ConsoleWriter` → `CharWriter`, `Encrypt` → ambas interfaces. Todas las dependencias de bajo nivel apuntan HACIA adentro del componente de alto nivel.

### Ejemplo 3: Data Flow Diagram (Figure 19.1 - Descripción en Prosa)

El diagrama muestra un programa de encriptación simple con:
- **Flujo de datos** (curvas sólidas): `Input Device` → `Read` → `Translate` → `Write` → `Output Device`
- **Dependencias de código fuente** (líneas rectas punteadas): Cruzan los flujos de datos, indicando que la dirección de dependencias NO sigue el flujo de datos, sino la jerarquía de nivel
- El componente `Translate` es el más alejado de inputs/outputs, por lo tanto el de nivel más alto

### Ejemplo 4: Component Diagram (Figure 19.3 - Descripción en Prosa)

Muestra la relación de plugin entre componentes:
- **Componente `Encryption`**: Núcleo de nivel alto que contiene la política de encriptación
- **Componente `IODevices`**: Contiene las implementaciones concretas de lectura/escritura
- **Dependencia**: El componente `IODevices` tiene una flecha apuntando HACIA el componente `Encryption`
- **Conocimiento**: El componente `Encryption` no conoce la existencia de `IODevices`; es un plugin intercambiable

### Cambio en Encriptación vs Cambio en I/O (Comparación Empírica)

Este no es código, sino la justificación de decisiones arquitectónicas:

**Escenario de cambio en políticas de nivel bajo (I/O)**:
- Cambio: Pasar de consola a lectura/escritura de archivo
- Costo arquitectónico: Crear nuevas implementaciones `FileReader` y `FileWriter` que implementen las interfaces `CharReader` y `CharWriter`
- Impacto en `Encrypt`: NINGUNO. No requiere cambio ni recompilación
- Razón del cambio: Requisito operacional menor

**Escenario de cambio en políticas de nivel alto (Encriptación)**:
- Cambio: Reemplazar algoritmo Caesar por AES
- Costo arquitectónico: Modificar la política dentro de `Encrypt`
- Impacto en `ConsoleReader`/`ConsoleWriter`: NINGUNO
- Razón del cambio: Fortaleza criptográfica mejorada (razón sustancial)

## 20 Business Rules

**Diagrama UML: Loan Entity (Figure 20.1)**
Descrito como una clase UML con:
- Tres datos críticos de negocio (Critical Business Data)
- Tres métodos relacionados (Critical Business Rules implementadas como funciones que operan sobre los datos)
Aunque el texto no proporciona sintaxis de código específica, la clase modelaría algo como:
```
class Loan {
  // Critical Business Data
  private BigDecimal balance
  private double interestRate
  private PaymentSchedule paymentSchedule
  
  // Critical Business Rules (métodos que implementan reglas)
  calculateInterest()
  determinePaymentAmount()
  applyPayment()
}
```

**Diagrama Use Case: Ejemplo de Creación de Préstamo (Figure 20.2)**
El diagrama referencia el flujo de un sistema usado por bank officers para crear nuevos préstamos. El use case especifica:
- Input: contact information y credit score validation
- Processing: validación de información de contacto, verificación credit score >= 500
- Output: acceso permitido a payment estimation screen solo tras cumplir precondiciones
- Interacción con Entity: referencia explícita a Customer entity que contiene Critical Business Rules que gobiernan la relación entre banco y clientes

**Patrón de Datos: Request/Response Model Structure (no código específico en el texto)**
El capítulo ilustra la separación mediante descripción:
- Request Model: estructura simple con datos de entrada del usuario, sin dependencias framework
- Response Model: estructura simple con datos de salida, sin derivación de HttpResponse o similares
- Trade-off ejemplo: aunque Request/Response y Entity comparten datos (p.ej., loan information), DEBEN ser estructuras separadas para evitar cambios acoplados
- Antipatrón: NO incluir `Entity entity` dentro del Request/Response

**Principios SOLID Aplicados:**
- Dependency Inversion Principle: Entities (high-level) no conocen Use Cases (low-level); inversión de dependencias
- Single Responsibility Principle: Request/Response models y Entities tienen responsabilidades distintas, no deben combinarse
- Common Closure Principle: cambios a reglas de negocio vs cambios a interfaz de usuario son razones diferentes de cambio

Este capítulo NO contiene fragmentos de código ejecutable en lenguajes específicos (Java, C#, etc.), sino descripciones conceptuales de estructura y patrones. Los diagramas son referencias a imágenes en media/Images/ cuyos detalles se infieren del texto circundante.

## 21 Screaming Architecture

El capítulo 21 "Screaming Architecture" es fundamentalmente teórico y de principios arquitectónicos, sin incluir ejemplos de código concretos, firmas de métodos o diagramas de secuencia/clase.

Sin embargo, contiene las siguientes referencias estructurales y ejemplos conceptuales importantes:

1. **Referencia bibliográfica clave**:
   - Ivar Jacobson's "Object Oriented Software Engineering: A Use Case Driven Approach" (se cita como fundamento del enfoque de arquitectura basada en casos de uso)

2. **Analogías de estructura arquitectónica mencionadas**:
   - **Casa unifamiliar**: Entrada frontal → foyer → sala de estar → comedor ← cocina ← dinette ← family room
   - **Biblioteca**: Entrada grandiosa → área de check-in/out ↔ áreas de lectura ↔ salas de conferencias ↔ galerías de almacenamiento de libros

3. **Preguntas arquitectónicas reflexivas** (no código, sino heurística):
   - "What does the architecture of your application scream?"
   - "Do [the top-level directories] scream 'Health Care System' or 'Accounting System' or 'Inventory Management System'? Or do they scream 'Rails' or 'Spring/Hibernate' or 'ASP'?"

4. **Estructura de objetos mencionada** (conceptual, sin implementación):
   - Entity objects = plain old objects (POJOs/POCOs) sin dependencias
   - Use case objects = coordinadores de Entity objects
   - Ambos testables juntos in situ sin frameworks

5. **Diálogo esperado con nuevos desarrolladores**:
   ```
   Pregunta: "We see some things that look like models—but where are the views and controllers?"
   
   Respuesta: "Oh, those are details that needn't concern us at the moment. We'll decide about them later."
   ```

6. **Mecanismos de entrega mencionados como detalles intercambiables**:
   - Console app
   - Web app
   - Thick client app
   - Web service app

No hay fragmentos de código, pseudocódigo, o diagramas formales en este capítulo. Es una argumentación arquitectónica pura centrada en principios y metáforas conceptuales sobre cómo la arquitectura debe comunicar propósito funcional antes que decisiones tecnológicas.


## 22 The Clean Architecture

El capítulo contiene dos diagramas de arquitectura referenciados en el texto, pero NO proporciona código ejecutable explícito (clases Java, método implementations, etc.). Sin embargo, proporciona descriptores precisos de componentes y su interacción:

**COMPONENTES MENCIONADOS EXPLÍCITAMENTE** (del Typical Scenario - Figura 22.2):

- Controller: Clase/componente que recibe input del usuario
- InputBoundary: Interfaz que el Controller usa para comunicarse con UseCaseInteractor
- UseCaseInteractor: Clase/componente que orquesta entities y acceso a datos
- DataAccessInterface: Interfaz para acceso a persistencia
- Database: Capa de persistencia
- Entities: Objetos que encapsulan reglas de negocio
- OutputData: Plain old Java object que contiene resultado del use case
- OutputBoundary: Interfaz que UseCaseInteractor implementa/usa para comunicarse con Presenter
- Presenter: Componente que transforma OutputData
- ViewModel: Plain old Java object con Strings y flags
- View: Componente que renderiza ViewModel a HTML

**FIRMAS CONCEPTUALES RECONSTRUIDAS DEL TEXTO**:

```java
// Interfaz de entrada (círculo interior, implementada por controller en exterior)
interface InputBoundary {
  void execute(InputData input);
}

// Datos de entrada simples
class InputData {
  // plain old Java object con datos de usuario
}

// Use case interactor (círculo interior)
class UseCaseInteractor {
  void execute(InputData input) {
    // Interpreta data
    // Controla entities
    // Accede datos via DataAccessInterface
    // Construye OutputData
    // Pasa a presenter via OutputBoundary
  }
}

// Interfaz de acceso a datos (círculo interior, implementada por adapter externo)
interface DataAccessInterface {
  Entity fetchEntity(id);
}

// Interfaz de salida (círculo interior, implementada por presenter en exterior)
interface OutputBoundary {
  void present(OutputData output);
}

// Datos de salida simples
class OutputData {
  // plain old Java object con resultados del use case
  Date date;
  Currency currency;
  // otros business data
}

// ViewModel para presentación
class ViewModel {
  String dateString;
  String currencyString;
  String buttonName;
  boolean buttonGrayed;
  // Strings y flags pre-formateados
}

// Presenter en capa externa
class Presenter implements OutputBoundary {
  void present(OutputData output) {
    ViewModel vm = new ViewModel();
    vm.dateString = formatDate(output.date);
    vm.currencyString = formatCurrency(output.currency);
    // ... prepara flags visuales
    view.update(vm);
  }
}

// View en capa externa
class View {
  void update(ViewModel vm) {
    // Move data from ViewModel to HTML page
  }
}
```

**RESTRICCIONES DE DEPENDENCIA** (descrito en prosa del texto):

- Controller (exterior) NO puede importar/usar clases de UseCaseInteractor (interior)
- UseCaseInteractor (interior) NO puede importar/usar clases de Presenter (exterior)
- Ambas capas comunican SOLO a través de interfaces definidas en la capa interior
- DataAccessInterface (interior) es implementada por adapters (exterior)
- OutputBoundary (interior) es implementada por Presenter (exterior)

El capítulo enfatiza que los datos que cruzan boundaries deben ser "simple data structures" y nunca incluir dependencias hacia el exterior; describe el mecanismo conceptual pero no proporciona implementación Java completa ni casos de uso de código específico más allá de esta prosa arquitectónica.

## 23 Presenters and Humble Objects

**Firmas de Métodos y Estructuras:**

1. Database Gateway Interface - Método parametrizado:
   ```
   UserGateway.getLastNamesOfUsersWhoLoggedInAfter(Date date) → List<String>
   ```

2. ViewModel Structure - Tipos de datos:
   - String fields: button names, menu item names, formatted dates, formatted currency
   - Boolean flags: visual states (e.g., isNegative for red color, isGrayedOut for button disabled)
   - Enum values: categorical UI states
   - Example: View expects to find formatted currency as `String` with appropriate decimal places and currency markers in ViewModel

3. Date Transformation Example (described conceptually):
   - Input: `Date` object from application
   - Presenter processing: Format the Date to appropriate locale/timezone
   - Output in ViewModel: `String` representation ready to display

4. Currency Display Example (described conceptually):
   - Input: `Currency` object from application
   - Presenter processing: Format with decimal places and currency markers; evaluate if negative
   - Output in ViewModel: 
     - `String` with formatted currency value
     - `Boolean isNegative` flag (true if Currency value < 0, controls red color rendering)

5. Generic UI Element Population Pattern:
   - Button/menu/radio/checkbox names: Presenter loads into `String` fields in ViewModel
   - Enable/disable state: Presenter sets `Boolean` flag in ViewModel (e.g., isDisabled)
   - Table display: Presenter converts `Table<Domain Objects>` to `Table<String[]>` of formatted strings

**Límites Arquitectónicos donde el patrón se aplica:**
- Presenter ↔ View boundary: Presenter (testeable) | ViewModel (data) | View (humilde)
- Interactor ↔ Database boundary: Interactor (testeable) | Gateway interface (abstraction) | Database implementation (humilde) | Data mapper (humilde)
- Application ↔ External Service boundary: Application (testeable) | Service listener (formatter, humilde) | Service structures (data)

**Nota importante:** Este capítulo NO contiene ejemplos de código fuente ejecutable completo, pseudocódigo o diagramas de secuencia con sintaxis formal. Su valor reside en los patrones arquitectónicos conceptuales, las firmas de métodos ilustrativas y la progresión de principios aplicados a diferentes límites architectónicos. La imagen referenciada (media/Images/CH-UN23.jpg) aparece en el encabezado pero su contenido no se describe textualmente en el markdown.

## 24 Partial Boundaries

**Interfaces y Clases Exactas Mencionadas:**

1. **Límites Completos:**
   - Interfaz `Boundary` (genérica)
   - Estructuras `Input`, `Output`

2. **Skip the Last Step:**
   - Componentes con reciprocal polymorphic interfaces, input/output data structures
   - Despliegue: archivo único (ej: FitNesse.jar compilando componente web + wiki)

3. **One-Dimensional Boundaries (Strategy Pattern):**
   ```
   Interfaz: ServiceBoundary
   Implementaciones: ServiceImpl (múltiples clases concretas)
   Cliente: Client (depende de ServiceBoundary, no directamente de ServiceImpl)
   Vulnerabilidad: backchannel Client→ServiceImpl sin protección técnica
   ```

4. **Facades:**
   ```
   Clase: Facade (expone métodos públicos)
   Métodos: todos los servicios como métodos de Facade
   Clases Internas: Service1, Service2, ..., ServiceN
   Cliente: Client (depende transitivamente de Facade y todas las Service*)
   Impacto en compilación estática: cambio en Service → recompilación forzada de Client
   ```

**Diagramas (descritos en prosa del texto):**

Figura 24.1 (Strategy Pattern):
- Eje X: Cliente a la izquierda, ServiceImpl a la derecha
- ServiceBoundary como interfaz en el medio
- Línea sólida: Client→ServiceBoundary (implementada por ServiceImpl)
- Línea punteada desagradable: Client→ServiceImpl (backchannel sin protección técnica)

Figura 24.2 (Facade Pattern):
- Cliente a la izquierda, Facade en el medio
- Múltiples clases Service (Service1, Service2, ..., ServiceN) a la derecha
- Línea sólida: Client→Facade
- Líneas: Facade→Service* (canalización)
- Dependencia transitiva: Client expuesto transitivamente a todas las Service*

**No hay código fuente concreto** — el capítulo es puramente arquitectónico, enfocado en mecanismos de aislamiento y patrones de diseño (Strategy, Facade) no implementación de sintaxis.

## 25 Layers and Boundaries

### Componentes Mencionados (Nombres Exactos de Clases y Estructuras)

**Componentes Principales:**
- `GameRules` - Componente central que contiene la política del juego (alta y baja nivel)
- `Language` - Abstracción para traducción entre lenguaje humano y comandos internos
- `TextDelivery` - API para mecanismo de comunicación (shell, SMS, chat, etc.)
- `DataStorage` - API abstracta para persistencia de estado del juego
- `MoveManagement` - Componente de política de mecanismo (movimiento, eventos de mapa)
- `PlayerManagement` - Componente de política de aplicación (salud, puntuación, condición de victoria)
- `Network` - Componente para sincronización en arquitectura distribuida

**Implementaciones Concretas:**
- `English`, `Spanish` - Implementaciones de `Language` API
- `SMS`, `CloudData` - Ejemplos de implementaciones específicas mencionadas
- `FileSystemData`, `CloudData` - Implementaciones de `DataStorage` (inferidas del texto)

**Interfaces Polimórficas (Boundary Interfaces):**
El texto define estructuralmente pero no da nombres de interfaces específicas. Las interfaces existen como:
- Interfaces definidas por `GameRules` e implementadas por `Language`
- Interfaces definidas por `Language` e implementadas por `TextDelivery`
- Interfaces definidas por `Language` e implementadas por implementaciones concretas (English, Spanish)
- Interfaces definidas por `GameRules` e implementadas por `DataStorage`
- Interfaces para eventos entre `MoveManagement` y `PlayerManagement`

**Eventos del Juego Mencionados:**
- `FoundFood` - Evento cuando el jugador encuentra comida
- `FellInPit` - Evento cuando el jugador cae en un pozo
- `EncounteredWumpus` - (Inferido) Evento cuando se encuentra el Wumpus

**Comandos del Usuario:**
- `GO EAST` - Comando de movimiento hacia el este
- `SHOOT WEST` - Comando para disparar hacia el oeste

### Diagramas Descritos en Prosa

**Figura 25.1 - Reutilización de GameRules por Múltiples UIs:**
```
┌──────────┐
│   UI_1   │
└────┬─────┘
     │
     ├──────────┐
     │          │
┌────▼──────┬──▼────┐
│            │       │
│ GameRules  │ (UI_2, UI_3, ... UI_N)
│            │
└────────────┘
```
Cada componente UI depende de `GameRules`, pero `GameRules` no conoce ni depende de ninguna UI específica. Las dependencias apuntan hacia arriba (hacia `GameRules`).

**Figura 25.2 - Dependency Rule con DataStorage:**
```
┌──────────────┐
│  GameRules   │
└──────┬───────┘
       │ (dependencia)
       │
┌──────▼──────┐
│ DataStorage  │ (API abstracta)
└──────┬───────┘
       │
    ┌──┴────┬──────┐
    │        │      │
 [Flash] [Cloud] [RAM]
```
`GameRules` define la interfaz de `DataStorage`; las implementaciones concretas dependen de esa interfaz. `GameRules` permanece independiente del mecanismo específico.

**Figura 25.3 - Arquitectura Multicapa Detallada:**
```
         ┌─────────────┐
         │  GameRules  │ (Central Transform)
         └──────┬──────┘
                │
    ┌───────────┴──────────────┐
    │                          │
┌───▼────────────┐    ┌────────▼──────────┐
│   Language     │    │   DataStorage     │
│   (API)        │    │   (API)           │
└───┬────────────┘    └────────┬──────────┘
    │                          │
┌───┴─────────┐          ┌─────▼────────┐
│ ┌─────────┐ │          │ ┌──────────┐ │
│ │ English │ │          │ │CloudData │ │
│ │ Spanish │ │          │ │FileSystem│ │
│ └─────────┘ │          │ └──────────┘ │
└─────────────┘          └──────────────┘
    │
┌───▼────────────┐
│ TextDelivery   │
│ (API)          │
└───┬────────────┘
    │
┌───┴──────┐
│ ┌─────┐  │
│ │Shell│  │ (Implementaciones)
│ │ SMS │  │
│ │Chat │  │
│ └─────┘  │
└──────────┘
```

**Figura 25.4 - Diagrama Simplificado (Solo APIs, Orientación Ascendente):**
```
        ┌────────────┐
        │ GameRules  │ ◄─ Políticas de nivel más alto
        └─────┬──────┘
              │ (dependencias apuntan arriba)
        ┌─────▼──────┐
        │  Language  │ ◄─ Traducción texto ↔ comandos
        └─────┬──────┘
        ┌─────┴──────┐
   ┌────▼─────┐  ┌───▼──────────┐
   │DataStorage│  │ TextDelivery │ ◄─ Canales de I/O
   └──────────┘  └──────────────┘
```
Todas las flechas apuntan hacia `GameRules`, indicando dirección de dependencias (no flujo de datos).

**Figura 25.5 - Tres Streams de Datos (Sistema Multijugador en Red):**
```
                ┌────────────┐
         ┌──────│ GameRules  │◄──────┐
         │      └────┬───────┘       │
         │           │               │
    ┌────▼────┐  ┌───▼────┐  ┌──────▼────┐
    │Language/│  │Data     │  │  Network  │
    │Text Del.│  │Storage  │  │(otros jug)│
    └──────────┘ └────────┘  └───────────┘
    │(Local UI)  (Persistencia) (Remotos)
```
`GameRules` orquesta tres streams independientes; todos convergen en `GameRules` como Central Transform.

**Figura 25.6 - Jerarquía de Políticas dentro de GameRules:**
```
┌────────────────────────┐
│  PlayerManagement      │ ◄─ Política alta: salud, puntuación, victoria
│  (Health, Scoring)     │
└────────┬───────────────┘
         │ (eventos desde)
         │
┌────────▼──────────────┐
│  MoveManagement        │ ◄─ Política baja: mapa, movimiento
│  (Map, Movement)       │
│  (genera FoundFood,    │
│   FellInPit, etc.)     │
└────────────────────────┘
```

**Figura 25.7 - Arquitectura Microservicios (Límite Arquitectónico Plenamente Implementado):**
```
┌─────────────────────────────┐       ┌──────────────────────┐
│    Player 1's Computer      │       │   Central Server     │
│  ┌───────────────────────┐  │       │ ┌──────────────────┐ │
│  │  MoveManagement       │  │◄─────▶│ │PlayerManagement  │ │
│  │  (local, low latency) │  │ Micro-│ │(centralized)     │ │
│  │                       │  │service│ │                  │ │
│  │ Events:              │  │ API   │ │ Single source of │ │
│  │  FoundFood           │  │       │ │ truth for health/│ │
│  │  FellInPit           │  │       │ │ points           │ │
│  └───────────────────────┘  │       │ └──────────────────┘ │
└─────────────────────────────┘       └──────────────────────┘
             │                                    ▲
             └────────────────────────────────────┘
                   (Network serialization)

[Repeated for Players 2, 3, ..., N with separate MoveManagement instances]
```

Cada jugador tiene su propio `MoveManagement` local. Todos se comunican con el servidor central `PlayerManagement` vía API de red (serialización/deserialización en componentes `Network`).

### Principios y Patrones de Diseño (Sin código explícito, pero estructuralmente presente)

**Dependency Inversion Principle (DIP):**
- `GameRules` define las interfaces; implementadores (Language, DataStorage) las implementan.
- Las dependencias nunca apuntan hacia detalles de bajo nivel; siempre hacia abstracciones.

**Separation of Concerns:**
- `MoveManagement` maneja solo lógica de mapa y movimiento.
- `PlayerManagement` maneja solo salud y puntuación.
- `Language` maneja solo traducción.
- `TextDelivery` maneja solo el canal de comunicación.

**Plugin Architecture Pattern:**
- `GameRules` es el plugin invariante.
- `Language`, `TextDelivery`, `DataStorage` son plugins intercambiables.
- Nuevas implementaciones (Spanish, SMS, CloudData) se conectan sin modificar `GameRules`.

**Layered Architecture:**
- Capas de abstracción creciente hacia arriba (GameRules → Language → TextDelivery).
- Cada capa es una frontera potencial.

**Central Transform Pattern:**
- `GameRules` es el transform central que recibe entrada, la procesa, y genera salida.
- Todos los datos fluyen a través de él (aunque las dependencias apunten hacia él).

**Microservices Architecture:**
- Frontera arquitectónica completamente implementada entre `MoveManagement` (local) y `PlayerManagement` (remoto).
- Sincronización vía API de red.

## 26 The Main Component

### Fragmentos de Código y Firmas Completas

**Declaración de Clase Main:**
```java
public class Main implements HtwMessageReceiver {  
  private static HuntTheWumpus game;  
  private static int hitPoints = 10;  
  private static final List<String> caverns = new ArrayList<>();  
  private static final String[] environments = new String[]{  
    "bright", "humid", "dry", "creepy", "ugly", "foggy", "hot",
    "cold", "drafty", "dreadful"  
  };  
  private static final String[] shapes = new String[] {  
    "round", "square", "oval", "irregular", "long", "craggy", "rough", "tall", "narrow"  
  };  
  private static final String[] cavernTypes = new String[] {  
    "cavern", "room", "chamber", "catacomb", "crevasse",
    "cell", "tunnel", "passageway", "hall", "expanse"  
  };  
  private static final String[] adornments = new String[] {  
    "smelling of sulfur", "with engravings on the walls", "with a bumpy floor", "",
    "littered with garbage", "spattered with guano", "with piles of Wumpus droppings",
    "with bones scattered around", "with a corpse on the floor", "that seems to vibrate",
    "that feels stuffy", "that fills you with dread"  
  };
}
```

**Método main(String[] args):**
```java
public static void main(String[] args) throws IOException {  
   game = HtwFactory.makeGame("htw.game.HuntTheWumpusFacade", new Main());  
   createMap();  
   BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  
   game.makeRestCommand().execute();  
   while (true) {  
     System.out.println(game.getPlayerCavern());  
     System.out.println("Health: " + hitPoints + " arrows: " + game.getQuiver());  
     HuntTheWumpus.Command c = game.makeRestCommand();  
     System.out.println(">");  
     String command = br.readLine();  
     if (command.equalsIgnoreCase("e"))  
       c = game.makeMoveCommand(EAST);  
     else if (command.equalsIgnoreCase("w"))  
       c = game.makeMoveCommand(WEST);  
     else if (command.equalsIgnoreCase("n"))  
       c = game.makeMoveCommand(NORTH);  
     else if (command.equalsIgnoreCase("s"))  
       c = game.makeMoveCommand(SOUTH);  
     else if (command.equalsIgnoreCase("r"))  
       c = game.makeRestCommand();  
     else if (command.equalsIgnoreCase("sw"))  
       c = game.makeShootCommand(WEST);  
     else if (command.equalsIgnoreCase("se"))  
       c = game.makeShootCommand(EAST);  
     else if (command.equalsIgnoreCase("sn"))  
       c = game.makeShootCommand(NORTH);  
     else if (command.equalsIgnoreCase("ss"))  
       c = game.makeShootCommand(SOUTH);  
     else if (command.equalsIgnoreCase("q"))  
       return;  
     c.execute();  
   }  
}
```

**Método createMap():**
```java
private static void createMap() {  
   int nCaverns = (int) (Math.random() * 30.0 + 10.0);  
   while (nCaverns-- > 0)  
     caverns.add(makeName());  
   
   for (String cavern : caverns) {  
     maybeConnectCavern(cavern, NORTH);  
     maybeConnectCavern(cavern, SOUTH);  
     maybeConnectCavern(cavern, EAST);  
     maybeConnectCavern(cavern, WEST);  
   }  
   
   String playerCavern = anyCavern();  
   game.setPlayerCavern(playerCavern);  
   game.setWumpusCavern(anyOther(playerCavern));  
   game.addBatCavern(anyOther(playerCavern));  
   game.addBatCavern(anyOther(playerCavern));  
   game.addBatCavern(anyOther(playerCavern));  
   game.addPitCavern(anyOther(playerCavern));  
   game.addPitCavern(anyOther(playerCavern));  
   game.addPitCavern(anyOther(playerCavern));  
   game.setQuiver(5);  
}
```

**Patrón de Factory Usage:**
```
HtwFactory.makeGame("htw.game.HuntTheWumpusFacade", new Main())
```
El nombre de clase se pasa como String para evitar acoplamiento de compilación.

**Patrón de Dependency Injection:**
El framework inyecta dependencias en Main, y Main luego las distribuye normalmente sin usar el framework, manteniéndolas fuera del sistema de alto nivel.

**Casos de Uso de Configuración Múltiple:**
- `Main_Dev` con configuración de desarrollo
- `Main_Test` con configuración de pruebas
- `Main_Prod` con configuración de producción
- `Main_US`, `Main_EU`, `Main_LATAM` para diferentes regiones
- `Main_Customer_A`, `Main_Customer_B` para diferentes clientes

## 27 Services: Great and Small

## Ejemplos, Diagramas y Estructuras

### Figura 27.1: Servicios Arranged para el Sistema de Taxi
**Descripción prosa del diagrama:**
El sistema original se divide en 5 servicios principais que fluyen horizontalmente:
```
TaxiUI → TaxiFinder → TaxiSuppliers (repositorio) → TaxiSelector → TaxiDispatcher
```

Detalles operacionales:
- `TaxiUI`: Interfaz con clientes en dispositivos móviles
- `TaxiFinder`: Lee inventarios de múltiples `TaxiSuppliers`, devuelve candidatos
- `TaxiSelector`: Evalúa criterios de usuario (pickup time, cost, luxury, driver experience) contra candidatos
- `TaxiDispatcher`: Ordena el taxi final

**Problema identificado:** Cuando se añade el feature de entrega de gatitos (kitten delivery), TODOS estos servicios requieren cambios:
- `TaxiUI`: Debe permitir ordenar gatitos
- `TaxiFinder`: Debe filtrar taxis con alergia a gatos
- `TaxiSelector`: Debe aplicar criterios de alergia de clientes y vehículos (no usado en últimos 3 días)
- `TaxiDispatcher`: Debe marcar vehículos después de entrega de gatitos

### Figura 27.2: Enfoque Object-Oriented con Componentes Rides y Kittens
**Descripción prosa de la arquitectura:**
```
Abstract Base Classes (con Templates)
    ↓
    ├─ Rides Component [implementa Template Method/Strategy]
    └─ Kittens Component [implementa Template Method/Strategy]
       
Dependencies follow Dependency Rule → pointing inward toward abstract base classes
```

**Patrones utilizados:**
- **Template Method Pattern**: Define esqueleto del algoritmo en clase base, delegando pasos específicos a subclases
- **Strategy Pattern**: Encapsula familia de algoritmos, haciéndolos intercambiables

**Implicación:** UI (TaxiUI) crea instancias a través de factories que seleccionan la clase derivada correcta (Rides o Kittens) en tiempo de ejecución.

### Figura 27.3: Component-Based Services with Internal Component Architecture
**Descripción prosa de la estructura de servicios:**
```
Service Instance (e.g., TaxiDispatcher Service)
    ├─ Abstract Base Component
    ├─ Rides Derivative Component (jar/Gem/DLL)
    └─ Kittens Derivative Component (jar/Gem/DLL)

Service Instance (e.g., TaxiSelector Service)
    ├─ Abstract Base Component
    ├─ Rides Derivative Component (jar/Gem/DLL)
    └─ Kittens Derivative Component (jar/Gem/DLL)
```

**Mecanismo de extensión:**
- Base component en jar file principal
- Nuevos features como jar files adicionales en load path
- No requiere recompilación de servicio base
- Sigue Open-Closed Principle explícitamente

**Ejemplo Java explícito (inferido del texto):**
```java
// Service define abstract base
public abstract class TaxiSelector {
    public abstract Taxi selectTaxi(List<Taxi> candidates, SelectionCriteria criteria);
}

// Rides component implements for typical rides
public class RidesTaxiSelector extends TaxiSelector {
    @Override
    public Taxi selectTaxi(List<Taxi> candidates, SelectionCriteria criteria) {
        // Filter by cost, time, luxury, driver experience
        return candidates.stream()
            .filter(t -> t.getCost() <= criteria.getMaxCost())
            .filter(t -> t.getPickupTime() <= criteria.getMaxPickupTime())
            // ... additional filters
            .findFirst()
            .orElse(null);
    }
}

// Kittens component - new jar file, extends with new logic
public class KittensTaxiSelector extends TaxiSelector {
    @Override
    public Taxi selectTaxi(List<Taxi> candidates, SelectionCriteria criteria) {
        // Original logic from Rides
        Taxi selected = rideLogic.selectTaxi(candidates, criteria);
        
        // Additional kitten-specific logic
        if (criteria.hasKittyOrder()) {
            selected = candidates.stream()
                .filter(t -> !t.getDriver().hasAllergyToCats())
                .filter(t -> !t.wasUsedForKittyDeliveryInLast3Days())
                .filter(t -> !criteria.getCustomer().hasAllergyToCats())
                // ... apply customer allergy filters
                .findFirst()
                .orElse(null);
        }
        return selected;
    }
}
```

### Figura 27.4: Services with Internal Component Architecture Following Dependency Rule
**Descripción prosa de arquitectura:**
```
                     ┌─────────────────────────────┐
                     │  Dependency Rule            │
                     │  (pointing inward)          │
                     └─────────────────────────────┘
                            ↓
Service Boundary (conceptual)
    ├─ High-Level Policy Components
    ├─ Mid-Level Components
    └─ Low-Level Detail Components
    
    Architectural boundaries run THROUGH service
    NOT BETWEEN services
```

**Estructura de dependencias correcta:**
- Componentes internos de servicio siguen Dependency Rule
- Componentes dependen de abstracciones, no inversamente
- Nuevas características (Kittens) no requieren modificar componentes existentes (Rides)

### Case Study: Kitten Delivery Feature - Coordenadas de Cambio Requeridas

**Criterios de negocio:**
```
1. Driver Allergy: driver.hasAllergyToCats() = true → excluir de kitty orders
2. Vehicle History: vehicle.lastKittyDelivery + 3 days < now() → 
   excluir si customer.hasAllergyToCats()
3. Customer Preference: customer.allergies.contains(CATS) → 
   filter vehicles por 3-day rule
4. Collection Point: location.isKittyCollectionPoint() → incluir en TaxiFinder
5. Delivery Address: order.isKittyDelivery() → incluir en delivery logic
```

**Cambios requeridos en arquitectura de servicios (acoplamiento implícito):**
- TaxiUI: Nueva UI workflow para kitty orders
- TaxiFinder: Filtrar por collection points de gatos + alergia de conductores
- TaxiSelector: Aplicar lógica de alergia de clientes y vehículos
- TaxiDispatcher: Marcar vehículo con timestamp de última entrega de gatos

**Cambios NO requeridos en arquitectura OO con componentes:**
Solo TaxiUI necesita cambiar (para inicializar KittensTaxiSelector en lugar de RidesTaxiSelector). Nuevos jar files se añaden sin tocar servicios existentes.

### Resumen de Principios Clave Implementados

1. **Dependency Rule**: Dependencias siempre apuntan hacia políticas de alto nivel; servicios deben aplicarlo internamente
2. **Open-Closed Principle**: Componentes abiertos a extensión (Kittens extends base), cerrados a modificación (Rides no cambia)
3. **SOLID Principles**: Especialmente Liskov Substitution Principle (Rides y Kittens intercambiables polimórficamente)
4. **Template Method / Strategy**: Mecanismos para implementar variaciones sin modificar base
5. **Separation of Concerns**: Lógica de Rides vs. Kittens separada en componentes distintos, cross-cutting concerns (driver/customer allergies) implementados como filtros transversales

## 28 The Test Boundary

El capítulo "The Test Boundary" no contiene ejemplos de código explícitos ni firmas de métodos específicas. Martin enfatiza conceptos arquitectónicos y patrones de anti-coupling a través de narrativa y argumentación.

Sin embargo, los principios descritos se ilustran mediante ESCENARIOS CONCRETOS:

1. **GUI Testing Anti-Pattern (línea 9106-9111):**
   - Tests que inician en login screen
   - Navegan a través de page structure
   - Verifican particular business rules
   - Resultado: cualquier cambio a login page o navigation structure rompe enorme número de tests

2. **Structural Coupling Anti-Pattern Ilustrado (línea 9145-9150):**
   - Test class por cada production class
   - Test methods por cada production method
   - Consecuencia: cuando production methods/classes cambian, large number de tests deben cambiar
   - Resultado: fragile tests, rigid production code

3. **Testing API Concept (línea 9129-9135):**
   - API superset de: interactors + interface adapters
   - Debe permitir: avoid security constraints, bypass databases, force system into testable states
   - Implementación implica crear nuevas abstracciones que no espejean la estructura productiva

4. **Deployment Topology (línea 9168-9170):**
   - Testing API + dangerous implementation parts en separate, independently deployable component
   - Asegura que superpowers nunca alcanzen producción

El capítulo es fundamentalmente arquitectónico y prescriptivo, no prescriptivo con código. Los "ejemplos" son anti-patterns a evitar y principios de diseño a aplicar.

## 29 Clean Embedded Architecture

## FRAGMENTOS DE CÓDIGO, FIRMAS Y ESTRUCTURAS

### 1. LISTA DE FUNCIONES SIN ESTRUCTURA (ANTI-PATRÓN)

```c
ISR(TIMER1_vect) { ... }  
ISR(INT2_vect) { ... }  
void btn_Handler(void) { ... }  
float calc_RPM(void) { ... }  
static char Read_RawData(void) { ... }  
void Do_Average(void) { ... }  
void Get_Next_Measurement(void) { ... }  
void Zero_Sensor_1(void) { ... }  
void Zero_Sensor_2(void) { ... }  
void Dev_Control(char Activation) { ... }  
char Load_FLASH_Setup(void) { ... }  
void Save_FLASH_Setup(void) { ... }  
void Store_DataSet(void) { ... }  
float bytes2float(char bytes[4]) { ... }  
void Recall_DataSet(void) { ... }  
void Sensor_init(void) { ... }  
void uC_Sleep(void) { ... }
```

### 2. HEADER FILE ACMETYPES.H (ACME DSP - ESPECÍFICO DE PROCESADOR)

```c
#ifndef _ACME_STD_TYPES  
#define _ACME_STD_TYPES  

#if defined(_ACME_X42)  
    typedef unsigned int        Uint_32;  
    typedef unsigned short      Uint_16;  
    typedef unsigned char       Uint_8;  
    typedef int                 Int_32;  
    typedef short               Int_16;  
    typedef char                Int_8;  

#elif defined(_ACME_A42)  
    typedef unsigned long       Uint_32;  
    typedef unsigned int        Uint_16;  
    typedef unsigned char       Uint_8;  
    typedef long                Int_32;  
    typedef int                 Int_16;  
    typedef char                Int_8;  
#else  
    #error <acmetypes.h> is not supported for this environment  
#endif  

#endif
```

### 3. ADAPTADOR STDINT.H (SOLUCIÓN PORTÁTIL)

```c
#ifndef _STDINT_H_  
#define _STDINT_H_  

#include <acmetypes.h>  

typedef Uint_32 uint32_t;  
typedef Uint_16 uint16_t;  
typedef Uint_8  uint8_t;  

typedef Int_32  int32_t;  
typedef Int_16  int16_t;  
typedef Int_8   int8_t;  

#endif
```

### 4. FUNCIÓN SAY_HI() - FIRMWARE DE BAJO NIVEL (ACOPLADO A PROCESADOR)

```c
void say_hi()  
{  
    IE = 0b11000000;           // Interrupt enable bits (no es C estándar)
    SBUF0 = (0x68);            // 'h' a Serial output buffer (registro directo)
    while(TI_0 == 0);          // Esperar bandera transmit empty interrupt
    TI_0 = 0;                  // Limpiar bandera
    SBUF0 = (0x69);            // 'i' a buffer
    while(TI_0 == 0);  
    TI_0 = 0;  
    SBUF0 = (0x0a);            // '\n' (line feed)
    while(TI_0 == 0);  
    TI_0 = 0;  
    SBUF0 = (0x0d);            // '\r' (carriage return)
    while(TI_0 == 0);  
    TI_0 = 0;  
    IE = 0b11010000;           // Restaurar interrupt bits
}
```

**Nota sobre sintaxis**: 0b11000000 es notación binaria que NO es C estándar. Variables en mayúsculas (IE, SBUF0, TI_0) acceden directamente a periféricos embebidos del micro-controlador. Esto hace la función FIRMWARE, no software.

### 5. DIAGRAMAS DE ARQUITECTURA DESCRITOS EN PROSA

**Figura 29.1 — Three Layers (Tres Capas Básicas)**:
Representación vertical con tres rectángulos apilados:
- Superior: "Software" / Application Logic
- Medio: "Firmware" / OS, Drivers
- Inferior: "Hardware" / Processors, Memory, Peripherals

Contexto: El capítulo explica que hardware está en la base y cambará inevitablemente. Las capas superiores deben estar protegidas de estos cambios.

**Figura 29.2 — Hardware Must Be Separated from Rest of System**:
Similar a 29.1 pero el enfoque es la barrera entre Hardware y todo lo demás. Se muestra una línea gruesa separando claramente Hardware (abajo) de Firmware+Software (arriba). El mensaje: evitar que conocimiento de hardware permee hacia arriba.

**Figura 29.3 — The Line Between Software and Firmware is Fuzzier**:
Diagrama mostrando que mientras la línea Hardware/Código es clara, la línea entre Software (lógica de negocio) y Firmware (lógica hardware-dependiente) es difusa/punteada. Esto ilustra el problema: sin cuidado, software y firmware se mezclan. Es trabajo del arquitecto "firmar" esta línea (hacerla clara).

**Figura 29.4 — The Hardware Abstraction Layer**:
Estructura de cuatro capas de abajo hacia arriba:
- Hardware (bottom)
- HAL (Hardware Abstraction Layer) — interfaz clara
- Firmware (encima de HAL)
- Software/Application (top)

El HAL representa el "boundary" definido entre lo que es firmware (depende de detalles hardware) y software (independiente de hardware). Arrows típicamente muestran software llamando servicios HAL, que internamente usan firmware, que a su vez controla hardware.

**Figura 29.5 — Adding in an Operating System**:
Extensión de arquitectura que inserta capa OS entre software y capas inferiores. Estructura (de arriba a abajo):
- Software/Application
- OS (Real-Time OS o embedded Linux/Windows)
- Firmware + HAL
- Hardware

Contexto: Muestra cómo OS se convierte en una capa adicional que software usa para servicios.

**Figura 29.6 — The Operating System Abstraction Layer**:
Refinamiento que introduce OSAL como interfaz entre Software y OS específico:
- Software/Application
- OSAL (Operating System Abstraction Layer) — interfaz agnóstica de OS
- OS Real (RTOS específico o Linux)
- Firmware + HAL
- Hardware

El beneficio: si se cambia de RTOS, solo hay que reimplementar OSAL, no reescribir Software que ya depende de interfaz OSAL estable.

### 6. CONVECIÓN PROBLÉMATICA - DIRECTIVA CONDICIONAL REPETIDA

```c
// VIOLACIÓN DE DRY - Antipatrón encontrado 6,000+ veces en una aplicación:
#ifdef BOARD_V2
    // código específico para Board Version 2
#else
    // código específico para versión anterior
#endif
```

**Problema**: Cuando aparece 6,000 veces, cada mencion crea acoplamiento directo entre código y versión de hardware. Refactoring para nuevo hardware requiere buscar y modificar todas las 6,000 menciones.

**Solución Correcta**: Una única vez en HAL:
```c
// En hal_board.h - interfaz agnóstica
void hal_initialize_board(void);

// En hal_board_v2.c - implementación para Board V2
void hal_initialize_board(void) {
    // Setup específico Board V2
}

// En hal_board_v1.c - implementación para versión anterior  
void hal_initialize_board(void) {
    // Setup versión anterior
}

// Linker selecciona implementación correcta
```

Ahora `#ifdef BOARD_V2` aparece UNA vez en HAL, no 6,000 en codebase. Software puede compilar para cualquier versión de board sin modificación.

## VI Details

Ninguno. El rango especificado no contiene fragmentos de código, firmas de métodos, casos de uso, ejemplos concretos ni diagramas descritos en prosa. Contiene únicamente metadatos y estructura de documento en formato Markdown/HTML procesado por Pandoc.

## 30 The Database Is a Detail

El capítulo 30 es fundamentalmente conceptual y principios arquitectónicos; **no contiene ejemplos de código ni firmas de métodos**. Sin embargo, contiene:

1. **Referencias a imágenes**: media/Images/CH-UN30.jpg (imagen descriptiva del capítulo, probablemente ilustración conceptual de la relación entre arquitectura y BD)

2. **Categorización de sistemas de persistencia** (sin código):
   - File Systems: document-based, óptimos para almacenamiento/recuperación "login.c"
   - RDBMS: content-based, óptimos para "encontrar todos .c con variable x"

3. **Mecánica técnica de acceso a disco** (descripción de proceso, no código):
   - Mover cabeza a pista correcta → esperar rotación → leer sector 4K → indexar byte
   - Latencia: milisegundos vs nanosegundos en RAM

4. **Anécdota como caso de estudio**: Estructura de datos alternativa vs BD relacional
   - Arquitectura original: trees + linked lists en archivos random access
   - Presión comercial: implementar RDBMS sin justificación técnica
   - Solución recomendada: "bolt RDBMS on the side" con channel de acceso seguro/estrecho

5. **Diagrama conceptual en prosa** (sin código):
   - Modelos de datos naturales en RAM: linked lists, trees, hash tables, stacks, queues
   - Acceso: punteros/referencias (no SQL)

El capítulo deliberadamente evita código para enfatizar que el debate es arquitectónico/principios, no de implementación técnica.

## 31 The Web Is a Detail

El capítulo 31 "The Web Is a Detail" es principalmente conceptual y arquitectónico, sin contener ejemplos de código, firmas de métodos, o pseudocódigo explícito. 

**Ausencia de Artefactos Concretos de Código:** El capítulo no incluye:
- Implementaciones de clases o interfaces
- Firmas de métodos específicas
- Ejemplos de pseudocódigo o código fuente
- Diagramas UML o diagramas de secuencia renderizados (hay una referencia a una imagen CH-UN31.jpg, pero su contenido no se describe en el texto de markdown)

**Representación Textual de Conceptos:**
Los únicos artefactos cercanos a estructuras concretas son descripciones textuales de patrones mentales:

1. **El Patrón del Use Case Device-Independent:**
   ```
   Input Data → [Complete] → Use Case Execution → Output Data → UI Feedback
   ```
   Conceptualmente: Los datos de entrada se encapsulan en estructuras de datos, se pasan al proceso de use case que opera independientemente del dispositivo, y los datos de salida se extraen para realimentar el UI.

2. **El Antipatrón Histórico - Oscillation Cycle:**
   ```
   Centralized (Mainframes) ↔ Distributed (Terminals) ↔ Centralized (Servers) ↔ 
   Distributed (Browsers) ↔ Centralized (Dynamic Content) ↔ Distributed (AJAX) ↔ 
   Centralized (SPAs on Browsers) ↔ Distributed (Node.js)
   ```

3. **Ejemplos Mencionados de Interacción UI "Chatty":**
   - JavaScript validation (validación en cliente)
   - Drag-and-drop AJAX calls (múltiples round-trips interactivos)
   - Plethora of widgets and gadgets (componentes complejos)

**Imagen Referenciada:** El capítulo incluye una referencia a `media/Images/CH-UN31.jpg` que aparentemente ilustra conceptos visuales, pero su descripción no está en el texto.

**Conclusión:** Este es un capítulo de principios y patrones arquitectónicos sin ejemplos de implementación concretos. Su valor reside en la justificación conceptual del aislamiento de capas, no en demostraciones de código.

## 32 Frameworks Are Details

**Anotación de Spring Framework (Uso Incorrecto - NO hacer):**
```java
@autowired
private FrameworkService service;
```
Esta anotación NO debe aparecer en business objects. Los objetos de entidades de negocio no deben contener conocimiento de Spring.

**Patrón correcto - Inyección en Main Component (Uso Correcto):**
```java
// Main es el único componente donde es aceptable usar @autowired
@Configuration
@ComponentScan("com.myapp")
public class Main {
    @Bean
    public ApplicationContext createApplicationContext() {
        // Spring auto-wires dependencies here
        // This is the "dirtiest, lowest-level component"
    }
}
```

**Patrón de Proxy/Adapter (Aislamiento de Framework):**
El capítulo describe conceptualmente (sin código literal) que cuando un framework pide herencia, crear proxies en su lugar:
- Rehúsa heredar desde base classes del framework en business objects
- Crea clases proxy que implementan las interfaces del framework
- Mantén esas proxies en componentes plugin separados
- El componente plugin actúa como boundary/adapter entre el framework y el core

**Principio de Arquitectura mencionado pero no con código literal:**
Dependency Rule: Las dependencias siempre apuntan hacia adentro (innermost circles). Los frameworks (outer circles) nunca deben ser importados en Entities o Use Cases (inner circles).

**Nota**: El capítulo NO contiene ejemplos de código compilable ni implementaciones concretas. Es un capítulo principalista y estratégico que describe la filosofía arquitectónica mediante prosa, no código de demostración. La única sintaxis específica mencionada es la anotación `@autowired` de Spring como ejemplo de QUÉ NO HACER.

## 33 Case Study: Video Sales

## Diagramas Arquitectónicos Descritos en Prosa

### Figure 33.1: Análisis de Casos de Uso (Use-Case Analysis)

**Estructura del diagrama**:
- Centro: Abstract use case "View Catalog" (representado con línea discontinua/dashed)
- Herencia: "View Catalog as Viewer" y "View Catalog as Purchaser" heredan del abstract
- Cuatro actores periféricos conectados a sus respectivos casos de uso:
  1. **Viewer**: accede a "View Catalog as Viewer", visualiza videos
  2. **Purchaser**: accede a "View Catalog as Purchaser", "Purchase License", compra licencias individuales o empresariales
  3. **Business Administrator**: "Manage Business Account", gestiona compras en lote, usuarios
  4. **Video Author**: "Maintain Video", "Maintain Ancillary Files", suministra contenido

El texto omite deliberadamente casos de uso como login/logout para mantener la complejidad manejable en el caso de estudio.

### Figure 33.2: Arquitectura Preliminar de Componentes (Component Architecture)

**Estructura jerárquica de componentes**:

```
[Views Layer]
├── Catalog View (Abstract base component)
├── Viewer Catalog View (inherits from Catalog View)
├── Purchaser Catalog View (inherits from Catalog View)
├── Purchase View
└── [Views for each actor]

[Presenters Layer]
├── Catalog Presenter (Abstract base component)
├── Viewer Catalog Presenter (inherits from Catalog Presenter)
├── Purchaser Catalog Presenter (inherits from Catalog Presenter)
├── Purchase Presenter
└── [Presenters for each actor]

[Interactors Layer]
├── View Catalog Interactor
├── Purchase License Interactor
├── Maintain Video Interactor
└── Manage Business Account Interactor

[Controllers Layer]
├── View Catalog Controller
├── Purchase Controller
└── [Controllers for each actor]

[Utilities]
└── Shared services & entities
```

**Límites arquitectónicos** (doble línea):
- Separación vertical entre Views/Presenters/Interactors/Controllers
- Separación horizontal por actor (Viewer, Purchaser, Business, Author)

**Patrón de dependencias**:
- Arrows de *using* (abiertas): Controllers→Interactors→Presenters→Views (con flujo)
- Arrows de *inheritance* (cerradas): Viewer/Purchaser Catalog View/Presenter → Abstract bases (contra flujo)
- Dirección general: derecha a izquierda desde Controllers; izquierda a derecha en componentes de presentación hacia utilidades compartidas

**Opciones de empaquetado mencionadas**:
- 5 `.jar` files: Views.jar, Presenters.jar, Interactors.jar, Controllers.jar, Utilities.jar
- 3 `.jar` files: ViewsPresenters.jar, BusinessLogic.jar, Utilities.jar  
- 2 `.jar` files: UI.jar (Views+Presenters), Domain.jar (todo lo demás)

Cada agrupamiento es válido; la estructura de compilación preserva independencia interna permitiendo decisión de despliegue posterior.

## 34 The Missing Chapter

## Firmas, Estructuras y Ejemplos de Código

### 1. TIPOS JAVA CORE DEL CASO DE USO (View Orders)

```java
// Package by Layer - estructura
// Web Layer:
class OrdersController {
  // Handles HTTP requests
}

// Business Logic Layer:
interface OrdersService {
  // Defines business contracts
}

class OrdersServiceImpl implements OrdersService {
  // Implementation of business logic
}

// Persistence Layer:
interface OrdersRepository {
  // Defines data access contracts
}

class JdbcOrdersRepository implements OrdersRepository {
  // JDBC-based persistence implementation
}
```

### 2. PACKAGE BY FEATURE - AGRUPACIÓN ÚNICA

```
com.mycompany.myapp.orders/
  ├── OrdersController.java
  ├── OrdersService.java
  ├── OrdersServiceImpl.java
  ├── OrdersRepository.java
  └── JdbcOrdersRepository.java
```
Mismo código Java, diferente localización y accesoría.

### 3. PORTS AND ADAPTERS - RENOMBRADO DE CONCEPTOS

```java
// Domain (Inside):
package com.mycompany.myapp.domain;

interface OrdersService {
  // Business logic interface
}

class OrdersServiceImpl implements OrdersService {
  // Implements business rules
}

interface Orders {
  // NOT "OrdersRepository" - uses ubiquitous language
}

// Infrastructure (Outside):
package com.mycompany.myapp.web;
class OrdersController {
  // Depends on domain interfaces
}

package com.mycompany.myapp.persistence;
class JdbcOrders implements Orders {
  // JDBC implementation
}
```

**Nota de Arquitectura:** El diagrama incluiría objetos para marshaling de datos a través de límites de dependencia (interactors, boundary objects), aunque el texto no los detalla explícitamente.

### 4. PACKAGE BY COMPONENT - INTERFAZ ÚNICA

```java
// Component Package:
package com.mycompany.myapp.component.orders;

// Single public entry point:
public interface OrdersComponent {
  // Public API of the component
}

public class OrdersComponentImpl implements OrdersComponent {
  // Implementation, delegates internally
}

// Internal (package-protected) types:
interface OrdersService {
  // Package-protected - hidden from outside
}

class OrdersServiceImpl implements OrdersService {
  // Hidden implementation
}

interface Orders {
  // Internal domain concept - package-protected
}

class JdbcOrders implements Orders {
  // Hidden persistence - package-protected
}

// Only this is visible externally:
// OrdersComponent component = new OrdersComponentImpl();
```

### 5. MODIFICADORES DE ACCESO POR ESTRATEGIA (Pseudocódigo Conceptual)

#### Strict Layered Approach:
```
[public] OrdersController
  ↓ (depends on)
[public] OrdersService (interface)
  ↓ (depends on)
[package-protected] OrdersServiceImpl
  ↓ (depends on)
[public] OrdersRepository (interface)
  ↓ (depends on)
[package-protected] JdbcOrdersRepository
```

#### Package by Feature:
```
public OrdersController {
  private OrdersService service;  // package-protected reference
  private OrdersRepository repo;  // package-protected reference
}

[package-protected] OrdersService, OrdersServiceImpl, OrdersRepository, JdbcOrdersRepository
```

#### Package by Component:
```
public OrdersComponent {
  // Single public interface
}

[package-protected] everything else
// No external access to OrdersRepository or OrdersService
```

### 6. MULTI-SOURCE-TREE PORTS AND ADAPTERS

```
Source Tree 1 (Domain - the "inside"):
- OrdersService.java
- OrdersServiceImpl.java
- Orders.java  (interface, replaces OrdersRepository concept)

Source Tree 2 (Web - the "outside"):
- OrdersController.java
- Depends on: Tree 1 (compile-time dependency)

Source Tree 3 (Persistence - the "outside"):
- JdbcOrders.java (implements Orders interface from Tree 1)
- Depends on: Tree 1 (compile-time dependency)

Build Configuration (Maven/Gradle/MSBuild):
Tree1: no dependencies
Tree2: depends on Tree1
Tree3: depends on Tree1
Tree2 and Tree3 are independent of each other
```

### 7. JAVA 9 MODULE SYSTEM DISTINCTION

```java
// module-info.java
module orders.domain {
  exports com.mycompany.orders.domain;  // published types
  // Many more internal 'public' types not exported
}

module orders.web {
  requires orders.domain;
  exports com.mycompany.orders.web;
}
```

En este modelo, todos los tipos pueden ser `public` internamente, pero solo aquellos en `exports` son accesibles desde otros módulos.

### 8. RELAXED LAYERED ARCHITECTURE - VIOLACIÓN INDETECTADA

```java
// Intended Architecture (Strict):
OrdersController → OrdersService → OrdersRepository

// Actual Architecture (Relaxed - Violation):
OrdersController ⇉ OrdersRepository  // Direct bypass!
       ↓           ↓
OrdersService  (unused for this use case)

// If all types are public and no static analysis, compiler allows this.
// If static analysis catches it: "types in package **/web should not access types in **/data"
// But this is post-compilation and fallible.
```

### 9. C4 ARCHITECTURE MODEL HIERARCHY (Conceptual)

```
System (Online Book Store)
├── Container 1: Web Application
│   └── Component 1: OrdersComponent
│       ├── Class: OrdersController
│       ├── Class: OrdersService
│       ├── Class: OrdersServiceImpl
│       ├── Class: Orders (interface)
│       └── Class: JdbcOrders
├── Container 2: Database
└── Container 3: Third-party Services
```

### 10. NO EXAMPLE SCENARIO (as stated in text)

El capítulo **no proporciona ejemplos de código ejecutable completo o casos de uso con datos concretos**. Es un capítulo de principios arquitectónicos aplicados a código Java preexistente, con enfoque en decisiones estructurales (paquetes, modificadores de acceso, dependencias), no en lógica de negocio funcional.

Los ejemplos mostrados son:
- Diagramas UML de clases (Figure 34.1-34.8)
- Estructuras de paquetes y dependencias conceptuales
- Firmas de tipos (interfaces e implementaciones)
- Pseudocódigo de acceso (qui tiene dependencia en quién)

No hay métodos con lógica de negocio, sin data de ejemplo, sin assertions de test, sin workflow ejecutable.


## Afterword

No hay fragmentos de código, firmas de métodos, clases específicas, o ejemplos técnicos concretos en este capítulo. El Afterword es un epílogo reflexivo y motivacional que sintetiza la filosofía del libro mediante narrativa autobiográfica y principios arquitectónicos generales.

Las únicas "estructuras" mencionadas son metafóricas:
- **Metáfora del pool**: "Like playing pool, each shot isn't just about sinking that ball; it's also about lining up the next shot"—ilustra que cada decisión de diseño debe considerar futuras adaptaciones
- **Metáfora de montar bicicleta**: "Like riding a bicycle, you can't master software design just by reading about it"—enfatiza la necesidad de práctica práctica, no solo teoría
- **Referencia a Big Process vs. Agile**: Descripción de evolución desde arquitectura de arriba-hacia-abajo con documentos masivos a diseño ágil Just-Enough-Design-Up-Front-with-Plenty-of-Refactoring

El capítulo no incluye diagramas, secuencias de clases, o implementaciones de patrones; es principalmente un argumento retórico sobre la filosofía y práctica de arquitectura de software limpia.

## VII Appendix

Las líneas especificadas (11411-11418) no contienen ejemplos de código, firmas de métodos, diagramas en prosa, o casos de uso concretos. El rango solicitado consiste únicamente en marcadores estructurales de Pandoc sin payload técnico. Estructura observada:\n\nLínea 11411: `## <span id="part7.xhtml_page_323" class="pagebreak"></span><span class="gray">VII</span> Appendix <span id="part7.xhtml_page_324" class="pagebreak"></span>`\n\nLínea 11413: `</div>` (cierre de contenedor anterior)\n\nLínea 11415: `<span id="appendixa.xhtml"></span>` (marcador de navegación sin contenido)\n\nLínea 11417: `<div id="appendixa.xhtml_sbo-rt-content">` (apertura de contenedor para contenido)\n\nPara acceder al contenido técnico del Apéndice A, se requiere leer desde la línea 11419 en adelante, donde comienza "A ARCHITECTURE ARCHAEOLOGY" con la narrativa sobre la Union Accounting System y arquitecturas históricas.

## A Architecture Archaeology


## EJEMPLOS, FIRMAS Y ESTRUCTURAS TÉCNICAS

### 1. BOSS - Block Function
```c
block(eventCheckFunction);
```
Signature: Suspendía current task, colocaba `eventCheckFunction` en polling list, asociándolo con newly blocked task. Esperaba en polling loop, llamando cada función en polling list hasta que una retornara `true`, permitiendo entonces que task asociada ejecute.

### 2. Vectorization Project - Chip Memory Layout y Vector Table

**Archivo Fuente Example (cada chip <1K)**:
```
ORG C400          // Address para chip C4
                  
// Vector table fixed-size, 40 bytes (max 20 addresses)
VECTOR_TABLE:
  .word SUBROUTINE_A
  .word SUBROUTINE_B
  .word SUBROUTINE_C
  ... (máximo 20)
  
// Subroutines
SUBROUTINE_A:
  ; code aqui
  
SUBROUTINE_B:
  ; code aqui
```

**RAM Vector Array**:
```
32 tables de 40 bytes = 1280 bytes RAM
Tabla[0] = Punteros chip 0
Tabla[1] = Punteros chip 1
...
Tabla[31] = Punteros chip 31
```

**Boot Sequence**:
1. Scan cada chip
2. Carga vector table al inicio de cada chip en RAM vectors
3. Jump al programa principal
4. Todas las llamadas subroutine: indirect call through appropriate RAM vector

**Indirect Call Example**:
```
; Viejo: direct call a SUBROUTINE_A
CALL SUBROUTINE_A

; Nuevo: indirect call via vector
LEA RAX, [VECTORS + CHIP_ID*40 + OFFSET_A]
CALL [RAX]
```

### 3. 4-TEL COLT/SAC DSL Packets

Simple comando DSL entre SAC y COLT:
```
DIAL XXXX         // Dial phone number
MEASURE           // Measure line characteristics
OPEN CABLE        // Open cable (physical operation)
SHORT CABLE       // Short cable (physical operation)
FAULT_DISTANCE    // Return fault distance in feet
```

Ejemplo secuencia:
1. SAC: `DIAL 5551212`
2. COLT: Dial line, return success/fail
3. SAC: `MEASURE`
4. COLT: Measure electronic characteristics
5. SAC: `OPEN CABLE`
6. COLT: Request craftsman open cable
7. COLT: `MEASUREMENT_RESULT: 450 FEET`

### 4. Electronic Receptionist - Service-Oriented State Machine

**Service Process Types** (initiated por eventos, pass control, exit/wait):
```
ListenerProcess       // Monitor single phone line
InitialHandlerProcess // Handle incoming call
VoicePromptService    // Prompt user for input
DirectoryLookupService // Look up phone numbers
CallForwardingService  // Forward call to destinations
MessageRecordingService // Record voicemail
```

**Inter-Service Communication (Disk Files)**:
```
/tmp/service_state_CALL_ID.txt

// Contents:
state: RECORDING_MESSAGE
caller_id: 5551212
recorded_data: /tmp/message_CALL_ID.wav
next_service: MessageDeliveryService
parameters:
  recipient_code: RMART
  message_path: /tmp/message_CALL_ID.wav
```

**Service Transition**:
```
CurrentService (ej InitialHandlerProcess):
  1. Determines next service needed
  2. Writes state info to disk file
  3. Issues command line: 
     /bin/start_service MessageRecordingService /tmp/service_state_CALL123.txt
  4. Exits
  
MessageRecordingService:
  1. Reads state from file
  2. Continues from previous state
  3. Records message to WAV file
  4. Writes new state to file
  5. Starts MessageDeliveryService
  6. Exits
```

### 5. CDS - 3DBB (Three-Dimensional Black Board) Shared Memory

**3DBB API Conceptual**:
```c
3DBB_SET(name, value)           // Set named string value
value = 3DBB_GET(name)          // Get named string value
3DBB_DELETE(name)               // Delete named entry
exists = 3DBB_EXISTS(name)      // Check existence
```

**Example State Machine Instance Data**:
```
// Names associated con state machine instance TROUBLE_TICKET_42:
3DBB_SET("TROUBLE_TICKET_42:pno", "8475551212")
3DBB_SET("TROUBLE_TICKET_42:noise", "true")
3DBB_SET("TROUBLE_TICKET_42:dropped_calls", "true")
3DBB_SET("TROUBLE_TICKET_42:assigned_craftsman", "TECH_001")
3DBB_SET("TROUBLE_TICKET_42:dispatch_type", "CABLE")
```

**Limitation**: No pointers allowed
```
// VÁLIDO:
3DBB_SET("DATA:name", "John")           // String OK
3DBB_SET("DATA:count", "42")            // Constant OK

// INVÁLIDO - No pointers:
// Can't store linked list head pointer
// Can't store tree root pointer
// Each process live en own memory partition; pointers meaningless across partitions
```

### 6. FLD (Field Labeled Data) - XML/JSON Precursor

**Conceptual Structure** (Binary tree):
```
FLD: Hierarchical name-value associations
     queryable por API
     translatable to/from string format ideal para 3DBB

Example Tree:
ROOT
├── pno: "8475551212"
├── noise: true
├── dropped_calls: true
└── dispatch
    ├── type: "CABLE"
    ├── priority: "HIGH"
    └── location
        └── address: "123 Main St"
```

**String Representation para 3DBB**:
```
/pno 8475551212
/noise
/dropped-calls
/dispatch /type CABLE /priority HIGH
/dispatch /location /address 123 Main St
```

**Query API** (conceptual):
```c
value = FLD_GET(fld_tree, "/pno")
// Returns: "8475551212"

value = FLD_GET(fld_tree, "/dispatch/type")
// Returns: "CABLE"

exists = FLD_EXISTS(fld_tree, "/dropped-calls")
// Returns: true
```

### 7. Architects Registry Exam - Plugin Architecture with Dependency Rule

**Framework Structure** (45,000 lines):
```
FrameworkBase
├── Common GUI Components
├── State Management
├── Event Dispatching
├── Rendering Engine
└── Input Handling
```

**Vignette Plugin Structure** (3,000-6,000 lines each):
```
VignettePlugin
├── Domain Logic (specific to vignette)
├── Data Model (vignette-specific)
└── GUI Customization
    └── Extends CommonGUIComponents
```

**Dependency Direction**:
```
// CORRECT (Dependency Rule):
Vignette ──depends on──> Framework
                         (high-level policy)

// INCORRECT (what failed initially):
Vignette <──depends on── Framework
(would create circular/complex dependencies)
```

**Scoring Application Variant**:
```
VignetteScoringLogic (high-level policy)
    ↓
ScoringFramework (low-level detail/algorithm)
(Framework plugged INTO vignette, not vice-versa)
```

### 8. ROSE Architecture - Layered Dependency Flow (Problematic)

**ROSE Layer Stack**:
```
GUI Layer
    ↓ depends on
Representation Layer (internal model of Booch diagrams)
    ↓ depends on
Manipulation Layer (rules, algorithms)
    ↓ depends on
OO Database Layer
    ↓
Storage
```

**Problem**: Dependencies pointed con flow of control direction, no toward high-level policies.

**Correct Pattern Should Be**:
```
High-Level Business Policies
    ↑ dependencies point UP
Low-Level Database Details
```

### 9. Clear Communications - `gi()` Function

```c
// Infamous 3000-line "Graphic Interpreter" function
int gi() {
  // Masterpiece of goo
  // Mixed GUI rendering logic, device control, state management
  // No separation of concerns
  // Impossible to test, debug, or maintain independently
  
  // This monolithic approach was typical of startup under pressure
  // No architecture = spaghetti code
}
```

### 10. BOSS - Task Management Context Switch Scenario

**Conceptual Implementation**:
```
TASK_CONTROL_BLOCK = {
  task_id: integer
  program_counter: address
  local_ram_area: pointer
  status: (RUNNING, BLOCKED, READY)
  event_check_function: function_pointer
}

// Task 1 blocking on I/O
block(check_modem_ready)  // block() suspends Task 1
                          // adds check_modem_ready to polling list

// Polling loop (in supervisor)
while (true) {
  for each blocked_task in polling_list:
    if blocked_task.event_check_function() == true:
      swap blocked_task.local_ram from disk
      jump to blocked_task.program_counter
      // Task runs until it fills its output buffer
      // Then gets swapped out again
}
```

### 11. Craft Dispatch System - Externalized State Machine File

**state_machine.txt** (text file defining FSM):
```
STATE: WAITING_FOR_REPAIRMAN
  EVENT: repairman_calls
    ACTION: start RepairmanGreetingService
    NEXT_STATE: GREETING

STATE: GREETING
  EVENT: menu_selection_received
    ACTION: start TroubleTicketLookupService
    NEXT_STATE: ASSIGNING_TICKET

STATE: ASSIGNING_TICKET
  EVENT: ticket_ready
    ACTION: start TicketReadingService
    NEXT_STATE: TICKET_READING

STATE: TICKET_READING
  EVENT: ticket_complete
    ACTION: start StatusUpdateService
    NEXT_STATE: UPDATING_STATUS
```

**Runtime FSM Processing**:
```
current_state = read_state_machine_file()

while (system_running):
  event = wait_for_event()  // Phone line event
  
  next_service = lookup_service(current_state, event)
  write_state_to_3DBB(state_info)
  start_service_process(next_service, state_file_path)
  
  current_state = next_state  // Advance FSM
```

**Hot-swapping Example**:
```
// Modify state_machine.txt mientras system running:
// Add new state transition sin stopping system
STATE: TICKET_READING
  EVENT: priority_escalation
    ACTION: start EscalationService       // NEW LINE
    NEXT_STATE: ESCALATING               // NEW LINE
```

System lee changes en next state machine file transitions sin necesidad de recompilación o restart.

### 12. VRS Architecture - Embedded SQL Problem

**Problem Code (Anti-pattern)**:
```c
// VRS.c - scattered everywhere
void process_voice_input(char *input) {
  char query[256];
  
  // SQL smeared throughout code
  sprintf(query, "SELECT * FROM craftsmen WHERE skills LIKE '%s'", input);
  EXEC SQL EXECUTE :query;
  // UNIFY-specific API calls
  UNIFY_fetch_result(&result);
  
  // More SQL elsewhere
  sprintf(query2, "UPDATE assignments SET status='ASSIGNED' WHERE id=%d", ticket_id);
  EXEC SQL EXECUTE :query2;
  
  // Vendor-specific quirks all over
  if (UNIFY_get_error() == UNIFY_ERR_DEADLOCK) {
    UNIFY_retry_transaction();
  }
}

void update_ticket_status(int ticket_id, char *status) {
  // More embedded SQL
  sprintf(query, "INSERT INTO ticket_history ...");
  EXEC SQL EXECUTE :query;
}

// 100s de places like this
```

**Problem**: Cuando UNIFY cancelled, no possible migration path. Database layer completamente entangled con business logic. No abstraction layer.

**What Should Have Been Done** (Database Abstraction):
```c
typedef struct {
  void (*init)(void);
  Craftsman* (*find_craftsman_by_skills)(char *skills);
  void (*assign_ticket)(int ticket_id, int craftsman_id);
  void (*update_ticket_status)(int ticket_id, char *status);
} DatabaseAdapter;

// Implementation pode cambiar (UNIFY, SyBase, Ingress, etc.)
// Pero business logic unchanged
```

---

**Nota**: El capítulo no contiene ejemplos de código formal sino descripciones arquitectónicas derivadas de experiencias de 45 años. Los ejemplos aquí están construidos basados en la prosa del capítulo reconstruyendo structures conceptuales, APIs de función, layouts de memoria, y ejemplos de state machines. El capítulo es fundamentalmente narrativo y de lecciones arquitectónicas más que código literal.


## Index

_Es el índice alfabético del libro (términos y referencias de página), no prosa técnica. No se resumió._

## Code Snippets

_Nueve secciones (líneas 16590-16973) que son galerías de imágenes de código fuente sin texto extraíble (ver raw/media/Images/05pro*.jpg y similares, ligadas a los capítulos 5, 14, 17, 25, 27, 29, 33). No se resumieron por no tener texto que resumir._
