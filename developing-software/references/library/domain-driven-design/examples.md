# Domain-Driven Design: Tackling Complexity in the Heart of Software — Ejemplos


## Índice de capítulos
- [Praise for *Domain-Driven Design*](#praise-for-domain-driven-design)
- [Contents](#contents)
- [Foreword](#foreword)
- [Preface](#preface)
- [Acknowledgments](#acknowledgments)
- [One. Crunching Knowledge](#one-crunching-knowledge)
- [Two. Communication and the Use of Language](#two-communication-and-the-use-of-language)
- [Three. Binding Model and Implementation](#three-binding-model-and-implementation)
- [Four. Isolating the Domain](#four-isolating-the-domain)
- [Five. A Model Expressed in Software](#five-a-model-expressed-in-software)
- [Six. The Life Cycle of a Domain Object](#six-the-life-cycle-of-a-domain-object)
- [Seven. Using the Language: An Extended Example](#seven-using-the-language-an-extended-example)
- [Eight. Breakthrough](#eight-breakthrough)
- [Nine. Making Implicit Concepts Explicit](#nine-making-implicit-concepts-explicit)
- [Ten. Supple Design](#ten-supple-design)
- [Eleven. Applying Analysis Patterns](#eleven-applying-analysis-patterns)
- [Twelve. Relating Design Patterns to the Model](#twelve-relating-design-patterns-to-the-model)
- [Thirteen. Refactoring Toward Deeper Insight](#thirteen-refactoring-toward-deeper-insight)
- [Fourteen. Maintaining Model Integrity](#fourteen-maintaining-model-integrity)
- [Fifteen. Distillation](#fifteen-distillation)
- [Sixteen. Large-Scale Structure](#sixteen-large-scale-structure)
- [Seventeen. Bringing the Strategy Together](#seventeen-bringing-the-strategy-together)
- [Conclusion](#conclusion)
- [Appendix. The Use of Patterns in This Book](#appendix-the-use-of-patterns-in-this-book)
- [Glossary](#glossary)
- [References](#references)
- [Photo Credits](#photo-credits)
- [Index](#index)
- [Footnotes](#footnotes)

## Praise for *Domain-Driven Design*

Sin contenido sustantivo de diseño — sección de portada/agradecimientos/referencia bibliográfica del libro impreso, omitida deliberadamente de la ingesta (ver todo.md).

## Contents

Sin contenido sustantivo de diseño — sección de portada/agradecimientos/referencia bibliográfica del libro impreso, omitida deliberadamente de la ingesta (ver todo.md).

## Foreword

Este capítulo es un prólogo introductorio y no contiene ejemplos concretos de código, diagramas UML, o casos de estudio específicos. Es una exposición conceptual y motivacional de Martin Fowler acerca de la importancia del domain modeling y el trabajo de Eric Evans, sin código ejecutable ni ilustraciones técnicas detalladas. Los conceptos DDD específicos mencionados son: domain model (modelo de dominio) y ubiquitous language (lenguaje ubicuo), ambos nombrados pero sin ejemplificación concreta en este segmento.

## Preface

Este capítulo es exclusivamente discurso introductorio sin ejemplos concretos de código Java, UML, diagramas de patrones o casos de estudio detallados. Evans explícitamente señala que ejemplos concretos y patterns aparecerán en secciones posteriores del libro—menciona que el material será ilustrado "con ejemplos realistas adaptados de proyectos actuales" y que la mayoría del libro está escrito como un conjunto de "patterns", cuyos detalles de estilo y formato se explican en el apéndice. Los tres proyectos contrastados (trading system simple sin domain model, trading system con emphasis en domain design, y enterprise system global que fracasó) son anécdotas narrativas sin código o diagramas específicos adjuntos.

## Acknowledgments

Sin contenido sustantivo de diseño — sección de portada/agradecimientos/referencia bibliográfica del libro impreso, omitida deliberadamente de la ingesta (ver todo.md).

## One. Crunching Knowledge

Concepto clave del PCB: "Net" es un conductor eléctrico que conecta múltiples componentes en un PCB y transmite señales eléctricas. Component Instance es la instancia de un componente en el circuito. Pin es el punto de conexión específico en una Component Instance. Topology es el arreglo que determina cómo elementos de la red se conectan. La probe simulation rastrea propagación de señal detectando sitios problemáticos, contando "hops" (cada vez que la señal atraviesa un Net es un hop).

Método original sin overbooking:
```
public int makeBooking(Cargo cargo, Voyage voyage) {
   int confirmation = orderConfirmationSequence.next();
   voyage.addCargo(cargo, confirmation);
   return confirmation;
}
```

Implementación con overbooking como guard clause (problema: conocimiento oculto):
```
public int makeBooking(Cargo cargo, Voyage voyage) {
   double maxBooking = voyage.capacity() * 1.1;
   if ((voyage.bookedCargoSize() + cargo.size()) > maxBooking)
       return -1;
   int confirmation = orderConfirmationSequence.next();
   voyage.addCargo(cargo, confirmation);
   return confirmation;
}
```

Solución con patrón Policy (Overbooking Policy como concepto explícito):
```
public int makeBooking(Cargo cargo, Voyage voyage) {
   if (!overbookingPolicy.isAllowed(cargo, voyage)) return -1;
   int confirmation = orderConfirmationSequence.next();
   voyage.addCargo(cargo, confirmation);
   return confirmation;
}

// En clase OverbookingPolicy:
public boolean isAllowed(Cargo cargo, Voyage voyage) {
   return (cargo.size() + voyage.bookedCargoSize()) <= (voyage.capacity() * 1.1);
}
```

Escenario de conversación entre developer y expertos PCB: cuando developers usan notación de diagramas, expertos corrigen terminología. "Component instances" (instancias reutilizables, múltiples del mismo componente), distintos de "ref-des" (designación de referencia en herramientas). Un Net conecta pin particular de una instance a pin particular de otra. Topology determina el arreglo de conexiones. Componentes "empujan" señales a través, modelado como lista de pushes desde ciertos Pins a otros. El modelo evoluciona de estos ajustes iterativos de lenguaje.

## Two. Communication and the Use of Language

EJEMPLO 1 - Diálogo del Cargo Router (Scenario 1: Minimal Abstraction):
Usuario: Así que cuando cambiamos el punto de despacho aduanal, necesitamos rehacer todo el plan de enrutamiento.
Desarrollador: Correcto. Eliminaremos todas las filas en la tabla de envío con ese cargo id, luego pasaremos el origen, destino y el nuevo punto de despacho aduanal al Routing Service, y repoblará la tabla. Tendremos que tener un Boolean en el Cargo para saber si hay datos en la tabla de envío.
Usuario: ¿Eliminar las filas? OK, lo que sea. De todos modos, si no tuviéramos un punto de despacho aduanal antes, tendríamos que hacer lo mismo.
Desarrollador: Claro, siempre que cambies el origen, destino o punto de despacho aduanal (o ingreses uno por primera vez), verificaremos si tenemos datos de envío y luego los eliminaremos y dejaremos que el Routing Service los regenere.

EJEMPLO 2 - Diálogo del Cargo Router (Scenario 2: Domain Model Enriched):
Usuario: Así que cuando cambiamos el punto de despacho aduanal, necesitamos rehacer todo el plan de enrutamiento.
Desarrollador: Correcto. Cuando cambies cualquiera de los atributos en la Route Specification, eliminaremos el Itinerary antiguo y le pediremos al Routing Service que genere uno nuevo basado en la nueva Route Specification.
Usuario: Si no hubiéramos especificado un punto de despacho aduanal antes, tendríamos que hacerlo al mismo tiempo.
Desarrollador: Claro, siempre que cambies algo en la Route Spec, regeneraremos el Itinerary. Eso incluye ingresar algo por primera vez.
El texto señala que el segundo diálogo transmite mucho más la intención del experto de dominio, permitiendo discusión precisa y concreta sobre objetos del modelo (Itinerary, Route Specification) en lugar de atributos y procedimientos.

EJEMPLO 3 - Variaciones de lenguaje para describir la Routing Service:
"Si le damos al Routing Service un origen, destino y tiempo de llegada, puede buscar las paradas que el cargo tendrá que hacer y, bueno... meter los datos en la base de datos." (vago y técnico)
"El origen, destino, etcétera... todo se alimenta al Routing Service, y obtenemos un Itinerary que tiene todo lo que necesitamos." (más completo, pero verboso)
"Un Routing Service encuentra un Itinerary que satisface una Route Specification." (conciso)
Este ejemplo demuestra cómo el lenguaje hablado puede refinarse hacia expresiones más precisas y expresivas.

EJEMPLO 4 - Figura 2.3 (Ubiquitous Language en la intersección de jergas):
El texto describe un diagrama que muestra cómo el UBIQUITOUS LANGUAGE se cultiva en la intersección entre la jerga técnica de desarrolladores y la jerga del dominio de expertos, con ambos grupos contribuyendo términos pero compartiendo un vocabulario central.

EJEMPLO 5 - Figura 2.4 y 2.5 (Shipping Operations):
Un diagrama de clases riguroso para un sistema de seguimiento de cargas en una empresa de envíos muestra relaciones entre operaciones portuarias, viajes de buques y planes operacionales. La Figura 2.5 (modelo explicativo) redibuja estos mismos conceptos como líneas que representan operaciones de puerto (cargar/descargar), almacenamiento en tierra o carga en buque en tránsito. Este modelo explicativo, junto con explicaciones en lenguaje natural, ayuda a desarrolladores y expertos a comprender el diagrama de clases más riguroso sin crear confusión sobre qué modelo impulsa realmente el software.

## Three. Binding Model and Implementation

Ejemplo central: PCB Layout Tool con Buses y Nets. La aplicación maneja placas de circuito impreso (PCB) como colecciones de conductores eléctricos (nets) conectando pines de componentes. En el dominio, los ingenieros ven muchos nets como pertenecientes a agrupamientos naturales llamados buses (ejemplo: 8, 16 o 256 nets en un bus). El enfoque mecanístico original involucraba scripts procedurales que parseaban archivos, usaban sorting alfabético y pattern matching para inferir buses, y luego insertaban reglas directamente en archivos—todo basado en manipulación de strings y archivos sin modelo explícito de la clase Bus.

El modelo-driven redesign introduce explícitamente una clase Bus con una asociación uno-a-muchos a Net. La clase abstracta AbstractNet encapsula el comportamiento común:

```
abstract class AbstractNet {
    private Set rules;
    
    void assignRule(LayoutRule rule) {
        rules.add(rule);
    }
    
    Set assignedRules() {
        return rules;
    }
}

class Net extends AbstractNet {
    private Bus bus;
    
    Set assignedRules() {
        Set result = new HashSet();
        result.addAll(super.assignedRules());
        result.addAll(bus.assignedRules());
        return result;
    }
}
```

El método assignedRules() en Net retorna tanto sus propias reglas como las reglas de su Bus. Este diseño escala a 20+ operaciones sin reescribir, permite unit testing directo (los tests no dependían de names o sorting), y expresa directamente el concepto del dominio de que nets heredan reglas de sus buses.

Inicialización y uso:
```
Collection nets = NetListImportService.read(aFile);
NetRepository.addAll(nets);
Collection buses = InferredBusFactory.groupIntoBuses(nets);
BusRepository.addAll(buses);
```

Test unitario (JUnit) demostrando la corrección del modelo sin dependencias de formato:
```
public void testBusRuleAssignment() {
    Net a0 = new Net("a0");
    Net a1 = new Net("a1");
    Bus a = new Bus("a"); //Bus is not conceptually dependent
    a.addNet(a0);         //on name-based recognition, and so
    a.addNet(a1);         //its tests should not be either.
    
    NetRule minWidth4 = NetRule.create(MIN_WIDTH, 4);
    a.assignRule(minWidth4);
    
    assertTrue(a0.assignedRules().contains(minWidth4));
    assertEquals(minWidth4, a0.getRule(MIN_WIDTH));
    assertEquals(minWidth4, a1.getRule(MIN_WIDTH));
}
```

Ejemplo secundario: Internet Explorer Favorites. El usuario concibe Favorites como una lista de nombres de sitios web que persisten entre sesiones. La implementación los almacena como archivos cuyos nombres van en la lista de Favorites. Cuando un usuario intenta crear un Favorite con nombre "Laziness: The Secret to Happiness", recibe un error diciendo que los filenames no pueden contener ciertos caracteres (incluido el ":"). Inversamente, si la URL ya contiene caracteres ilegales para Windows, Internet Explorer silenciosamente los elimina. Este mismatch entre el modelo conceptual del usuario y el modelo de implementación causa confusión y corrupción silenciosa de datos—dos modelos diferentes para el mismo concepto.

## Four. Isolating the Domain

Evans proporciona un ejemplo detallado de Online Banking para ilustrar LAYERED ARCHITECTURE aplicada a funcionalidad de transferencia de fondos. En este ejemplo, un usuario selecciona dos números de cuenta y un monto de dinero para transferir. La responsabilidad de la UI layer es dibujar widgets en pantalla y capturar entrada del usuario. La application layer coordina la solicitud de transferencia sin asumir la fuente (podría ser UI con campos de entrada y botones, o una solicitud XML por red). La domain layer contiene la regla de negocio fundamental: "Every credit has a matching debit" (cada crédito tiene un débito coincidente), y es responsable de validar que este invariante se mantenga. La infrastructure layer maneja persistencia en base de datos y transacciones técnicas. Evans dibuja Figure 4.1 mostrando cómo los objetos llevan responsabilidades consistentes con su capa y están más acoplados a otros objetos en su propia capa. El ejemplo enfatiza que la lógica de débito y crédito debe residir en la domain layer, no en la application o UI layer, permitiendo que esta regla sea aplicada consistentemente sin importar el origen de la solicitud. Otro aspecto tratado es cómo el J2EE framework historicamente fue usado implementando todos los objetos de dominio como "entity beans", bloqueando performance y desarrollo. La práctica actual mejor es usar J2EE framework solo para objetos de grano más grueso, implementando la mayoría de la lógica de negocio con objetos Java genéricos. Esto ilustra el trade-off entre usar frameworks comprehensivos versus aplicarlos selectivamente. El texto también menciona TRANSACTION SCRIPT como solución intermedia (mencionado como patrón de Fowler) que separa UI de aplicación pero no provee un modelo orientado a objetos, posicionándose entre SMART UI y LAYERED ARCHITECTURE completa.

## Five. A Model Expressed in Software

Ejemplo de Brokerage Account con Asociaciones: El modelo muestra una relación entre BrokerageAccount, Customer, e Investments. Una implementación Java directa encapsula customer y investments como atributos de instancia. Una implementación SQL-basada usa BrokerageAccount con customerSocialSecurityNumber y consultas de base de datos: public class BrokerageAccount { String accountNumber; String customerSocialSecurityNumber; public Customer getCustomer() { String sqlQuery = "SELECT * FROM CUSTOMER WHERE SS_NUMBER='"+customerSocialSecurityNumber+"'"; return QueryService.findSingleCustomerFor(sqlQuery); } public Set getInvestments() { String sqlQuery = "SELECT * FROM INVESTMENT WHERE BROKERAGE_ACCOUNT='"+accountNumber+"'"; return QueryService.findInvestmentsFor(sqlQuery); } }. Cuando se refina el modelo para cualificar la asociación (un investment por stock symbol), la multiplicidad se reduce y el método getInvestment toma un parámetro: public Investment getInvestment(String stockSymbol) { String sqlQuery = "SELECT * FROM INVESTMENT WHERE BROKERAGE_ACCOUNT='" + accountNumber + "' AND STOCK_SYMBOL='" + stockSymbol +"'"; return QueryService.findInvestmentFor(sqlQuery); }. Ambas implementaciones reflejan el mismo modelo pero con mecanismos de traversal diferentes.

Ejemplo de Identidad en Transacciones Bancarias: Dos depósitos del mismo monto a la misma cuenta el mismo día son ENTITIES distintas porque tienen identidad separada (un número de cheque es el identificador único). Sin embargo, los montos en sí (los valores) son instances de un objeto dinero sin identidad. Cuando el cliente bancario reconcilia los extractos bancarios con el registro de cheques, busca transacciones con la misma identidad a pesar de que fueron registradas por diferentes personas en fechas diferentes (la fecha de clearing del banco es más tarde). El mismo principio aplica a depósitos y retiros en efectivo sin número identificador: cada uno es una ENTITY que aparece en al menos dos formas.

Ejemplo de Asientos de Estadio: En asientos asignados, cada asiento es una ENTITY identificada por número de asiento (único dentro del estadio). El asiento puede tener atributos como ubicación, vista obstruida, precio, pero solo el número de asiento lo identifica. En admisión general, los asientos específicos no necesitan ser distinguidos; solo el número total importa. Aquí, los asientos no son ENTITIES y no se necesita un identificador, aunque los números estén grabados físicamente. Esta decisión es contextual: el usuario de la aplicación determina si necesita distinguir identidades específicas.

Ejemplo de Dirección como VALUE OBJECT o ENTITY: En software de correo, una dirección es un VALUE OBJECT porque solo importa lo que es (la ubicación), no cuál instancia. Si dos compañeros de cuarto ordenan del mismo lugar, no importa que compartan ubicación. En software de servicios postales que organiza rutas de entrega, Address es una ENTITY en una jerarquía (región, ciudad, zona postal, bloques), donde los códigos postales se derivan del padre y cambios de asignación postal afectan toda la jerarquía. En una compañía de servicios eléctricos, Address es una ENTITY porque cada llamada de compañeros de cuarto requiere que la compañía realice cambios separados de servicio.

Ejemplo de Métodos equals para VALUE OBJECTS: En programas de diseño de casas, si cada outlet eléctrico es un VALUE OBJECT separado pero todos son interchangeable, se puede compartir una sola instancia sin cambio en comportamiento o identidad hasta que se realice un cambio. Si se cambia el nombre de una persona, el otro person que compartía el mismo name object también cambiaría (corrupción de invariante). La solución es: hacer el VALUE OBJECT inmutable (no se puede cambiar excepto por reemplazo completo) o pasar una copia.

Ejemplo de Paradigma de Reglas: Un dominio financiero rico contiene reglas explícitas, pero el paradigma orientado a objetos carece de semántica específica para expresarlas. Aunque las reglas pueden modelarse como objetos, la encapsulación de objetos hace incómodo aplicar reglas globales que cruzan todo el sistema. Un rules engine promete una forma más natural y declarativa de definir reglas. Sin embargo, si el engine no permite una vista sin costuras que muestre la relatedness de conceptos del modelo entre ambos ambientes de implementación, el resultado es una aplicación fracturada: un sistema de almacenamiento de datos estático usando objetos, y una aplicación ad-hoc de procesamiento de reglas que ha perdido casi toda conexión con el modelo de objetos.

## Six. The Life Cycle of a Domain Object

Ejemplo de AGGREGATE de auto en taller de reparación: El automóvil es una ENTITY con identidad global (VIN único), con llantas como ENTITIES locales cuya identidad se distingue solo dentro del AGGREGATE del auto. Los bloques de motor pueden ser AGGREGATE roots separados si el negocio los rastrea independientemente. Consultas: nunca se busca directamente una llanta; se busca el auto y se accede a sus llantas por traversal desde el auto.

Ejemplo de Purchase Order: Una PO con líneas de orden es un AGGREGATE donde la PO es la raíz. El invariante es que la suma de líneas no puede exceder el límite de aprobación. Problema de locking ingenuo: George bloquea línea 001, Amanda bloquea línea 002 de la misma PO en transacciones concurrentes, y después de ambos commits, la PO viola el invariante sin que nadie lo sepa. Solución: bloquear la PO completa. Problema refinado: Si parts (componentes) pueden cambiar precio, ¿debe reflejarse inmediatamente en POs existentes? No. Solución de dominio: copiar precio al momento de crear la línea de orden, rompiendo la dependencia directa a parts. Ahora el AGGREGATE PO+LineItems es aislable, y cambios a parts no crean contención.

Ejemplo de FACTORY en compra: Una FACTORY METHOD en BrokageAccount crea TradeOrders (que no son parte del mismo AGGREGATE, porque interactuarán con sistemas de ejecución). La FACTORY encapsula que puede haber subclases Buy/SellOrder, manteniendo el cliente desacoplado de la jerarquía. Parámetros: la FACTORY toma la BROKERAGE_ACCOUNT misma (que contiene el ID y reglas), manteniendo bajo acoplamiento porque ya estaba relacionada en el modelo.

Ejemplo de reconstitución: Recuperar una ENTITY de BD relacional requiere: SELECT * FROM customer WHERE id=123 → resultado de filas → FACTORY toma {id: 123, name: "John", created_date: "2020-01-01"} → retorna instancia Customer con identidad preservada (no se asigna nuevo ID). Si hay violación de invariante en datos históricos (ej. precio negativo en línea archivada), la FACTORY puede ser más permisiva que durante creación nueva, porque la alternativa es perder datos existentes.

Ejemplo de REPOSITORY: En vez de customerDAO.findBySqlQuery("SELECT * FROM customers WHERE salary > 50000 AND department_id = 5"), el cliente usa customerRepository.findByMinSalaryAndDepartment(50000, dept). La interfaz habla de dominio, no SQL. Internamente el REPOSITORY puede usar SPECIFICATION: salarySpec = Salary.greaterThan(50000); deptSpec = Department.equals(dept); specification = salarySpec.and(deptSpec); customers = repository.findMatching(specification). Esto es flexible sin exponer mecanismos técnicos.

Ejemplo de anti-patrón: Una aplicación WebSphere para manufacturación llamaba repository.allObjects() para resumir información global, lo que instanciaba cada objeto en la BD entera en memoria, causando OutOfMemoryError en producción porque el dataset de prueba era pequeño. El problema es que los developers no entendían las implicaciones de performance de la implementación encapsulada del REPOSITORY, subrayando por qué debe haber feedback bidireccional entre el uso y la implementación.

## Seven. Using the Language: An Extended Example

Código Java de constructores:

public Cargo(String id) {
    trackingID = id;
    deliveryHistory = new DeliveryHistory(this);
    customerRoles = new HashMap();
}

public HandlingEvent(Cargo c, String eventType, Date timeStamp) {
    handled = c;
    type = eventType;
    completionTime = timeStamp;
}

FACTORY METHOD especializado:
public static HandlingEvent newLoading(
    Cargo c, CarrierMovement loadedOnto, Date timeStamp) {
    HandlingEvent result = 
        new HandlingEvent(c, LOADING_EVENT, timeStamp);
    result.setCarrierMovement(loadedOnto);
    return result;
}

FACTORY methods para Cargo:
public Cargo copyPrototype(String newTrackingID)
public Cargo newCargo(Cargo prototype, String newTrackingID)
public Cargo newCargo(Cargo prototype)

Diagrama de asociaciones (Figura 7.2): Traversal direction especificado con Customer sin referencia directa a Cargos, Handling Event→Carrier Movement unidireccional, Cargo→Delivery History bidireccional, Delivery History→Handling Events (inicialmente collection, posteriormente query).

Diagrama de AGGREGATE Boundaries (Figura 7.3): Customer, Location, Carrier Movement como raíces de AGGREGATES independientes. Cargo AGGREGATE abarcando Delivery History y Delivery Specification internamente. Handling Event como raíz de AGGREGATE independiente.

Diagrama de REPOSITORIES (Figura 7.4): Customer Repository, Location Repository, Cargo Repository, Carrier Movement Repository accediendo a sus raíces AGGREGATE respectivas.

Escenario "Changing Destination": Delivery Specification VALUE OBJECT simplemente descartado y reemplazado mediante setter en Cargo.

Escenario "Repeat Business": Cargo se copia usando PROTOTYPE pattern:
- Delivery History: nueva y vacía
- Customer Roles: Map copiado con keys idénticas pero referencias al mismo Customer objects
- Tracking ID: nuevo del mismo source
Sin afectar nada fuera del AGGREGATE boundary.

Patrón Circular Reference (Figura 7.5): Añadir Handling Event requiere inserción en Delivery History como parte de transacción. Refactoring (Figura 7.6): collection reemplazada por query, eliminando contention.

Modularización (Figuras 7.7, 7.8): Contraste entre particionamiento erróneo por patrón (ENTITIES, VALUES, FACTORIES) versus correcto por conceptos de dominio (Shipping, Customers, Billing).

Allocation Checking Integration (Figuras 7.9, 7.10, 7.11): Booking Application consulta Sales Management System e información de REPOSITORIES. Allocation Checker como ANTICORRUPTION LAYER traduciendo Enterprise Segments. Shift de responsabilidades: Booking Application originalmente aplicaba regla de negocio; refactorizado para que Allocation Checker maneje derivación de Enterprise Segment y validación.

## Eight. Breakthrough

El capítulo no contiene fragmentos reales de código (Java, pseudocódigo, o configuraciones técnicas). En su lugar, usa una serie de nueve diagramas visuales descritos en prosa para ilustrar la evolución conceptual del modelo.

Modelo inicial (Figura 8.1): Loan Investment como objeto derivado representando participación de un inversor en un Loan, proporcional a su share en la Facility.

Modelo iterado (Figura 8.2): Incorpora Loan Adjustments para rastrear desviaciones de la share original que un lender acordó en la Facility.

Escenario de primer drawdown (Figura 8.3): Borrower dibuja $50MM de $100MM committed bajo Facility. Los tres lenders participan proporcionalmente a sus Facility shares, resultando en $50MM Loan dividido según esas proporciones.

Escenario de segundo drawdown (Figura 8.4): Borrower dibuja $30MM adicionales ($80MM total Loan outstanding). Company B elige no participar; Company A toma share extra. Las shares del drawdown reflejan estas decisiones de inversión. Cuando se suma al Loan, las Loan shares ya no son proporcionales a Facility shares.

Pagos de principal (Figura 8.5): El dinero se divide entre lenders según Loan shares, no Facility shares.

Pagos de fee (Figura 8.6): Divididos según Facility shares, independiente de quién realmente ha prestado dinero.

Modelo abstracto de Shares (Figura 8.7): Captura shares como concepto generalizado aplicable a cualquier valor divisible.

Modelo de Loan con Share Pie (Figura 8.8): Facility y Loan ya no tienen objetos especializados para shares; ambos se desglosan en Share Pie más intuitiva.

Breakthrough posterior (Figura 8.9): Introduce Transactions como ENTITY explícita que captura significativas reglas sobre drawdowns, pagos de fee, etc., simplicando Positions (abstracción que incluye Facility y Loan).

## Nine. Making Implicit Concepts Explicit

Ejemplo 1 - Shipping Model / Itinerary: El equipo ya tenía una aplicación de booking de cargo con un routing engine. Cuando comenzó a construir operaciones support, el experto de envíos enfatizaba que el "itinerary" —la secuencia completa de legs con fechas de operación— era lo fundamental. El desarrollador descubrió que todos los datos ya existían (ID de vessel voyage, puerto de carga, puerto de descarga por leg), pero no como objeto unificado. El diálogo reveló que el itinerary era el puente entre booking, operaciones y relaciones con clientes. Se refactorizó para crear un objeto Itinerary que encapsulaba colecciones de Leg, donde cada Leg contenía vessel voyage, puertos y derivaba fechas del schedule. El Routing Service ahora retornaba Itinerary en lugar de escribir a tablas de base de datos. El objeto Itinerary reemplazó el report anterior, moviendo lógica de dominio hacia el domain layer. Beneficios: interfaz de Routing Service más expresiva, decoupling de tablas de base de datos, relación clarificada entre aplicaciones, reducción de duplicación de cálculos de tiempo, expansión de UBIQUITOUS LANGUAGE.

Ejemplo 2 - Interest Calculation / Accrual: Un sistema de seguimiento de inversiones en préstamos comerciales tenía un componente nightly batch que llamaba calculateInterestForDate() en cada Asset y pasaba montos a un SERVICE de contabilidad. A través del diálogo entre desarrollador y experto bancario, surgió que el diseño era incómodo porque especialmente los casos de impago impredecible generaban complejidad creciente. El experto explicó que "accrual basis accounting" es el estándar: el interés devengado se registra en un ledger en la fecha de accrual, SEPARADO de los pagos que se registran de otra forma. Se refactorizó para crear un objeto Accrual (VALUE OBJECT) con fecha, monto y ledger target. Assets.calculateAccrualsThroughDate() retorna una colección de Accruals que el batch script luego registra individualmente. Fees se modelaron paralelo a Interest bajo el mismo patrón. Beneficios: enriquecimiento de UBIQUITOUS LANGUAGE con "accrual", decoupling de accrual y payment, movimiento de knowledge de dominio (qué ledger usar) desde script a domain layer, unificación de fees e interest eliminando duplicación, path clara para nuevas variaciones vía Accrual Schedules.

Ejemplo 3 - Bucket Constraint: Un objeto Bucket debe garantizar que no exceda capacity. La versión inicial tenía:
```
class Bucket {
   private float capacity;
   private float contents;
   public void pourIn(float addedVolume) {
      if (contents + addedVolume > capacity) {
         contents = capacity;
      } else {
         contents = contents + addedVolume;
      }
   }
}
```
Se refactorizó para hacer explícito el constraint:
```
class Bucket {
   private float capacity;
   private float contents;
   public void pourIn(float addedVolume) {
      float volumePresent = contents + addedVolume;
      contents = constrainedToCapacity(volumePresent);
   }
   private float constrainedToCapacity(float volumePlacedIn) {
      if (volumePlacedIn > capacity) return capacity;
      return volumePlacedIn;
   }
}
```
El método constrainedToCapacity() con nombre revelador explicitiza el constraint y le da espacio para crecer en complejidad sin obscurecer pourIn().

Ejemplo 4 - Delinquent Invoice Specification: Una DelinquentInvoiceSpecification es un VALUE OBJECT que encapsula la lógica de qué hace que una Invoice sea delinquent (no solo overdue, sino además considerando grace period del cliente, status de cuenta, y políticas corporativas):
```
public class DelinquentInvoiceSpecification extends InvoiceSpecification {
   private Date currentDate;
   public DelinquentInvoiceSpecification(Date currentDate) {
      this.currentDate = currentDate;
   }
   public boolean isSatisfiedBy(Invoice candidate) {
      int gracePeriod = candidate.customer().getPaymentGracePeriod();
      Date firmDeadline = DateUtility.addDaysToDate(candidate.dueDate(), gracePeriod);
      return currentDate.after(firmDeadline);
   }
}
```
Para validar si una Invoice es delinquent:
```
public boolean accountIsDelinquent(Customer customer) {
   Date today = new Date();
   Specification delinquentSpec = new DelinquentInvoiceSpecification(today);
   Iterator it = customer.getInvoices().iterator();
   while (it.hasNext()) {
      Invoice candidate = (Invoice) it.next();
      if (delinquentSpec.isSatisfiedBy(candidate)) return true;
   }
   return false;
}
```
Para querying/selección desde Repository:
```
public Set selectSatisfying(InvoiceSpecification spec) {
   Set results = new HashSet();
   Iterator it = invoices.iterator();
   while (it.hasNext()) {
      Invoice candidate = (Invoice) it.next();
      if (spec.isSatisfiedBy(candidate)) results.add(candidate);
   }
   return results;
}
Set delinquentInvoices = invoiceRepository.selectSatisfying(
   new DelinquentInvoiceSpecification(currentDate));
```
Para bases de datos grandes, el SPECIFICATION puede proporcionar SQL o delegar a métodos genéricos del Repository y filtrar en memoria:
```
public Set satisfyingElementsFrom(InvoiceRepository repository) {
   Collection pastDueInvoices = 
      repository.selectWhereDueDateIsBefore(currentDate);
   Set delinquentInvoices = new HashSet();
   Iterator it = pastDueInvoices.iterator();
   while (it.hasNext()) {
      Invoice anInvoice = (Invoice) it.next();
      if (this.isSatisfiedBy(anInvoice))
         delinquentInvoices.add(anInvoice);
   }
   return delinquentInvoices;
}
```

Ejemplo 5 - Chemical Warehouse Packer: Cada Chemical debe almacenarse en un Container con características específicas (ARMORED para explosivos, VENTILATED para volátiles):
```
public class ContainerSpecification {
   private ContainerFeature requiredFeature;
   public ContainerSpecification(ContainerFeature required) {
      requiredFeature = required;
   }
   boolean isSatisfiedBy(Container aContainer) {
      return aContainer.getFeatures().contains(requiredFeature);
   }
}
tnt.setContainerSpecification(new ContainerSpecification(ARMORED));
```
Un Container valida si está safely packed:
```
boolean isSafelyPacked() {
   Iterator it = contents.iterator();
   while (it.hasNext()) {
      Drum drum = (Drum) it.next();
      if (!drum.containerSpecification().isSatisfiedBy(this))
         return false;
   }
   return true;
}
```
La interfaz del WarehousePacker SERVICE define:
```
public interface WarehousePacker {
   public void pack(Collection containersToFill, Collection drumsToPack) 
      throws NoAnswerFoundException;
   /* ASSERTION: At end of pack(), the ContainerSpecification of each Drum 
      shall be satisfied by its Container. If no complete solution can be 
      found, an exception shall be thrown. */
}
```
Una protoimplementación simple permite desarrollo paralelo:
```
public class PrototypePacker implements WarehousePacker {
   public void pack(Collection containers, Collection drums) 
      throws NoAnswerFoundException {
      Iterator it = drums.iterator();
      while (it.hasNext()) {
         Drum drum = (Drum) it.next();
         Container container = findContainerFor(containers, drum);
         container.add(drum);
      }
   }
   public Container findContainerFor(Collection containers, Drum drum) 
      throws NoAnswerFoundException {
      Iterator it = containers.iterator();
      while (it.hasNext()) {
         Container container = (Container) it.next();
         if (container.canAccommodate(drum)) return container;
      }
      throw new NoAnswerFoundException();
   }
}
```
Esta implementación es simple y correcta respecto a las reglas explícitas, aunque imperfecta en optimización. Permite a otros equipos iterar en paralelo. Cuando un packer optimizado está listo, se integra sin fricción porque respeta la misma interfaz y ASSERTIONS.

## Ten. Supple Design


Paint-Mixing Application (Intention-Revealing Interfaces and Refactoring):

Initial design with opaque method name:
public void paint(Paint paint) {
   v = v + paint.getV(); // After mixing, volume is summed
   // Omitted many lines of complicated color mixing logic
   // ending with the assignment of new r, b, and y values.
}

Initial test (passes but unclear intent):
public void testPaint() {
   Paint yellow = new Paint(100.0, 0, 50, 0);
   Paint blue = new Paint(100.0, 0, 0, 50);
   yellow.paint(blue);
   assertEquals(200.0, yellow.getV(), 0.01);
   assertEquals(25, yellow.getB());
   assertEquals(25, yellow.getY());
   assertEquals(0, yellow.getR());
}

Refactored with intention-revealing interface (client perspective first):
public void testPaint() {
   Paint ourPaint = new Paint(100.0, 0, 50, 0);
   Paint blue = new Paint(100.0, 0, 0, 50);
   ourPaint.mixIn(blue);
   assertEquals(200.0, ourPaint.getVolume(), 0.01);
   assertEquals(25, ourPaint.getBlue());
   assertEquals(25, ourPaint.getYellow());
   assertEquals(0, ourPaint.getRed());
}

Side-Effect-Free Functions with VALUE OBJECT Refactoring:

PigmentColor as VALUE OBJECT with closed operation:
public class PigmentColor {
   public PigmentColor mixedWith(PigmentColor other, double ratio) {
      // Many lines of complicated color-mixing logic
      // ending with the creation of a new PigmentColor object
      // with appropriate new red, blue, and yellow values.
   }
}

Paint delegating to PigmentColor function:
public class Paint {
   public void mixIn(Paint other) {
      volume = volume + other.getVolume();
      double ratio = other.getVolume() / volume;
      pigmentColor = pigmentColor.mixedWith(other.pigmentColor(), ratio);
   }
}

Assertions in Paint Mixing (Post-Conditions):

Refactored model with clear responsibilities separating StockPaint and MixedPaint:
After p1.mixIn(p2):
- p1.volume is increased by amount of p2.volume
- p2.volume is unchanged
(Original problematic post-condition that didn't match domain intuition)

Improved model (StockPaint as input, MixedPaint as accumulator):
Test confirming assertions:
public void testMixingVolume {
   PigmentColor yellow = new PigmentColor(0, 50, 0);
   PigmentColor blue = new PigmentColor(0, 0, 50);
   StockPaint paint1 = new StockPaint(1.0, yellow);
   StockPaint paint2 = new StockPaint(1.5, blue);
   MixedPaint mix = new MixedPaint();
   mix.mixIn(paint1);
   mix.mixIn(paint2);
   assertEquals(2.5, mix.getVolume(), 0.01);
}

SPECIFICATION with Logical Operators (Container Specifications):

Abstract interface with AND, OR, NOT operations:
public interface Specification {
   boolean isSatisfiedBy(Object candidate);
   Specification and(Specification other);
   Specification or(Specification other);
   Specification not();
}

Composing specifications declaratively:
Specification ventilated = new ContainerSpecification(VENTILATED);
Specification armored = new ContainerSpecification(ARMORED);
Specification both = ventilated.and(armored);

Specification ventilatedType1 = new ContainerSpecification(VENTILATED_TYPE_1);
Specification ventilatedType2 = new ContainerSpecification(VENTILATED_TYPE_2);
Specification either = ventilatedType1.or(ventilatedType2);

Specification cheap = ventilated.not().and(armored.not());

Implementation of composite specifications:
public abstract class AbstractSpecification implements Specification {
   public Specification and(Specification other) {
      return new AndSpecification(this, other);
   }
   public Specification or(Specification other) {
      return new OrSpecification(this, other);
   }
   public Specification not() {
      return new NotSpecification(this);
   }
}

public class AndSpecification extends AbstractSpecification {
   Specification one;
   Specification other;
   public AndSpecification(Specification x, Specification y) {
      one = x;
      other = y;
   }
   public boolean isSatisfiedBy(Object candidate) {
      return one.isSatisfiedBy(candidate) && other.isSatisfiedBy(candidate);
   }
}

public class OrSpecification extends AbstractSpecification {
   Specification one;
   Specification other;
   public OrSpecification(Specification x, Specification y) {
      one = x;
      other = y;
   }
   public boolean isSatisfiedBy(Object candidate) {
      return one.isSatisfiedBy(candidate) || other.isSatisfiedBy(candidate);
   }
}

public class NotSpecification extends AbstractSpecification {
   Specification wrapped;
   public NotSpecification(Specification x) {
      wrapped = x;
   }
   public boolean isSatisfiedBy(Object candidate) {
      return !wrapped.isSatisfiedBy(candidate);
   }
}

SPECIFICATION Subsumption (Logical Implication):

MinimumAgeSpecification with subsumption rule:
public class MinimumAgeSpecification {
   int threshold;
   public boolean isSatisfiedBy(Person candidate) {
      return candidate.getAge() >= threshold;
   }
   public boolean subsumes(MinimumAgeSpecification other) {
      return threshold >= other.getThreshold();
   }
}

Test confirming subsumption:
drivingAge = new MinimumAgeSpecification(16);
votingAge = new MinimumAgeSpecification(18);
assertTrue(votingAge.subsumes(drivingAge));

CompositeSpecification with leaf collection subsumption:
public boolean subsumes(Specification other) {
   if (other instanceof CompositeSpecification) {
      Collection otherLeaves = (CompositeSpecification) other.leafSpecifications();
      Iterator it = otherLeaves.iterator();
      while (it.hasNext()) {
         if (!leafSpecifications().contains(it.next()))
            return false;
      }
   } else {
      if (!leafSpecifications().contains(other))
         return false;
   }
   return true;
}

Java vs. Smalltalk Collection Selection (Closure of Operations):

Java approach (Iterator with accumulated results):
Set employees = (some Set of Employee objects);
Set lowPaidEmployees = new HashSet();
Iterator it = employees.iterator();
while (it.hasNext()) {
   Employee anEmployee = it.next();
   if (anEmployee.salary() < 40000)
      lowPaidEmployees.add(anEmployee);
}

Smalltalk approach (closed operation returning Collection):
employees := (some Set of Employee objects).
lowPaidEmployees := employees select: [:anEmployee | anEmployee salary < 40000].

Shares Math in Syndicated Loan System:

Initial complex design (mixed command and query):
public class Loan {
   private Map shares;
   public Map distributePrincipalPayment(double paymentAmount) {
      Map paymentShares = new HashMap();
      Map loanShares = getShares();
      double total = getAmount();
      Iterator it = loanShares.keySet().iterator();
      while(it.hasNext()) {
         Object owner = it.next();
         double initialLoanShareAmount = getShareAmount(owner);
         double paymentShareAmount = initialLoanShareAmount / total * paymentAmount;
         Share paymentShare = new Share(owner, paymentShareAmount);
         paymentShares.put(owner, paymentShare);
         double newLoanShareAmount = initialLoanShareAmount - paymentShareAmount;
         Share newLoanShare = new Share(owner, newLoanShareAmount);
         loanShares.put(owner, newLoanShare);
      }
      return paymentShares;
   }
   public double getAmount() {
      Map loanShares = getShares();
      double total = 0.0;
      Iterator it = loanShares.keySet().iterator();
      while(it.hasNext()) {
         Share loanShare = (Share) loanShares.get(it.next());
         total = total + loanShare.getAmount();
      }
      return total;
   }
}

Refactored with separated commands and side-effect-free functions:
public void applyPrincipalPaymentShares(Map paymentShares) {
   Map loanShares = getShares();
   Iterator it = paymentShares.keySet().iterator();
   while(it.hasNext()) {
      Object lender = it.next();
      Share paymentShare = (Share) paymentShares.get(lender);
      Share loanShare = (Share) loanShares.get(lender);
      double newLoanShareAmount = loanShare.getAmount() - paymentShare.getAmount();
      Share newLoanShare = new Share(lender, newLoanShareAmount);
      loanShares.put(lender, newLoanShare);
   }
}

public Map calculatePrincipalPaymentShares(double paymentAmount) {
   Map paymentShares = new HashMap();
   Map loanShares = getShares();
   double total = getAmount();
   Iterator it = loanShares.keySet().iterator();
   while(it.hasNext()) {
      Object lender = it.next();
      Share loanShare = (Share) loanShares.get(lender);
      double paymentShareAmount = loanShare.getAmount() / total * paymentAmount;
      Share paymentShare = new Share(lender, paymentShareAmount);
      paymentShares.put(lender, paymentShare);
   }
   return paymentShares;
}

Client code:
Map distribution = aLoan.calculatePrincipalPaymentShares(paymentAmount);
aLoan.applyPrincipalPaymentShares(distribution);

SharePie as VALUE OBJECT with closed operations and mathematical formalism:
public class SharePie {
   private Map shares = new HashMap();

   public double getAmount() {
      double total = 0.0;
      Iterator it = shares.keySet().iterator();
      while(it.hasNext()) {
         Share loanShare = getShare(it.next());
         total = total + loanShare.getAmount();
      }
      return total;
   }

   public SharePie minus(SharePie otherShares) {
      SharePie result = new SharePie();
      Set owners = new HashSet();
      owners.addAll(getOwners());
      owners.addAll(otherShares.getOwners());
      Iterator it = owners.iterator();
      while(it.hasNext()) {
         Object owner = it.next();
         double resultShareAmount = getShareAmount(owner) - otherShares.getShareAmount(owner);
         result.add(owner, resultShareAmount);
      }
      return result;
   }

   public SharePie plus(SharePie otherShares) {
      // Similar to implementation of minus()
   }

   public SharePie prorated(double amountToProrate) {
      SharePie proration = new SharePie();
      double basis = getAmount();
      Iterator it = shares.keySet().iterator();
      while(it.hasNext()) {
         Object owner = it.next();
         Share share = getShare(owner);
         double proratedShareAmount = share.getAmount() / basis * amountToProrate;
         proration.add(owner, proratedShareAmount);
      }
      return proration;
   }
}

Supple Loan and Facility classes using SharePie:
public class Loan {
   private SharePie shares;

   public SharePie calculatePrincipalPaymentDistribution(double paymentAmount) {
      return shares.prorated(paymentAmount);
   }

   public void applyPrincipalPayment(SharePie paymentShares) {
      setShares(shares.minus(paymentShares));
   }
}

public class Facility {
   private SharePie shares;

   public SharePie calculateDrawdownDefaultDistribution(double drawdownAmount) {
      return shares.prorated(drawdownAmount);
   }
}

public class Loan {
   public void applyDrawdown(SharePie drawdownShares) {
      setShares(shares.plus(drawdownShares));
   }
}

Analytical capability using declarative style:
SharePie originalAgreement = aFacility.getShares().prorated(aLoan.getAmount());
SharePie actual = aLoan.getShares();
SharePie deviation = actual.minus(originalAgreement);


## Eleven. Applying Analysis Patterns

Ejemplo 1 - Modelo básico de contabilidad (Fowler, Analysis Patterns cap. 6): Una Account con múltiples Entries (nunca removidas). Cada Entry agrega o resta valor. El balance es el efecto combinado. Una Entry en salary Account podría ser 1000. Una Entry negativa de 300 taxa. El balance resultante es 700. Double-entry bookkeeping: cada crédito tiene un débito coincidente, conservando dinero entre Accounts. Ejemplo: Entry de +1000 en salary Account vinculada a Entry de +1000 en Asset Account (dinero que llega). Diagrama descrito: Account contiene múltiples Entries. Una Entry es una abstracción con monto (positivo o negativo).

Ejemplo 2 - Diálogo Domain-Driven entre desarrolladores y Expert (sintaxis conversacional): Developer 1 propone crear Entry en Interest Account para interés devengado, otra Entry para pago balanceando. Expert pregunta si así verían historial de devengamientos y pagos. Developer 2 objeta que Transaction de Fowler es para mover dinero entre Accounts distintos, no dos entries en la misma. Developer 1 reconoce que interest payments pueden ser varios días después, violando el supuesto de Fowler sobre creación simultánea. Expert clarifica que pagos y devengamientos son postulaciones separadas en el sistema contable, el balance de Account es lo principal. Developer 2 pregunta si no rastrean pagos. Expert: "es más complicado que tu esquema de un-devengamiento/un-pago". Resultado: descartan Transaction, usan solo Account, Entries y el término accrual introducido por Expert.

Ejemplo 3 - Posting Rule modelo de Fowler: Salary Account (input) → Posting Rule calcula 30% → Tax Withholding Account (output). El Rule contiene Method que calcula el porcentaje. Triggers: Entry en salary dispara Rule → Rule calcula amount → Rule inserta Entry en tax account. Tres firing modes: (1) Eager: cada Entry dispara inmediatamente Rules. (2) Account-based: mensaje a Account procesa todas sus Entries nuevas. (3) Posting-Rule-based: agente externo le dice a Rule que dispare.

Ejemplo 4 - Adaptación pragmática al batch nocturno: Asset conoce qué Accounts contiene (fee o interest). Batch itera Assets → envía mensaje auto-explicativo → Asset selecciona Posting Rules apropiadas → Rules buscan Entries nuevas → calcular y postear. Posting Service (FACADE) expone legacy accounting system como SERVICE. Developer 2 usa Posting-Rule-based firing: batch le dice a cada Rule que dispare, Rule busca sus Entries nuevas y actúa. Pragmáticamente Asset selecciona Rules (aunque idealmente Rule estaría asociada directamente a Account, lo cual es una futura refactorización esperada).

## Twelve. Relating Design Patterns to the Model

Ejemplo 1: Route-Finding Policies. Una Route Specification se pasa a una Routing Service cuyo trabajo es construir un detallado Itinerary que satisface la especificación. El servicio es un motor de optimización que encuentra rutas más rápidas o más baratas. Inicialmente, esto introduce condicionales en cada computación (fastest vs cheapest branches everywhere). La solución es separar parámetros de tuning en Strategies: una Leg Magnitude Policy calcula la magnitud de cada leg. El Routing Service entonces maneja todas las requests incondicionalmente, buscando una secuencia de Legs con baja magnitud como computa la policy. Diferentes Leg Magnitude Policy implementations (fastest, cheapest, o combinaciones que balancean ambos) se pasan como parámetro, haciendo la interface clara y extensible: The Routing Service chooses an Itinerary with minimum total magnitude of Legs based on the chosen Strategy.

Ejemplo 2: Shipment Routes Made of Routes. Un shipment complejo requiere múltiples movimientos: trucked a railhead, carried a puerto, transported en ship a otro puerto (posiblemente transferencias entre ships), finalmente transported by ground. El modelo inicial trata una Route como un string arbitrario de Legs. Pero domain experts revelan que routes tienen five logical segments (door-to-door inicial, rail, ship, ship-to-ship transfers, door-to-door final) cada uno distinto conceptualmente. Además, "door legs" (locally hired trucks, customer haulage) son categoricamente diferentes de scheduled rail/ship transports. Sin Composite, el modelo requiere múltiples tipos de objetos a diferentes niveles. Con Composite: se define un Route abstracto donde todo es "movimiento de contenedor de punto A a punto B." Las door legs y otros segment types implementan la interfaz Route uniformemente. Una route puede componerse de subroutes que se pueden planear en diferentes momentos por diferentes personas, y operaciones como "generar operational plan" se simplifican dramáticamente porque recurren uniformemente sin condicionales por tipo.

## Thirteen. Refactoring Toward Deeper Insight

Este capítulo no contiene ejemplos de código concreto ni estudios de caso implementados. El contenido es puramente conceptual y metodológico, presentando principios y procesos de refactoring hacia mayor profundidad en el modelo de dominio. Evans ilustra estas ideas mediante narrativa descriptiva (p.ej., la dinámica de una sesión de brainstorming de 4-5 personas, la metáfora de equilibrio punteado de Darwin) pero no desarrolla fragmentos de código fuente ni diagramas de patrones transcritos textualmente.

## Fourteen. Maintaining Model Integrity

Los ejemplos concretos del capítulo incluyen:

1. **Caso introductorio Charge Objects**: Dos equipos (billing customers vs. paying vendors) ambos llamaban a su objeto "Charge" pero significaba cosas distintas. Billing team asumía "percent deductible" field required, validation aplicaba default. Vendor payments team no requería este field. Cuando código fue combinado sin resolver contradicciones, surgieron "mysterious Charges" sin valor en "percent deductible", causando crashes en month-to-date tax report function que sumaba amount deductible. Solución: crearon separadas Customer Charge y Supplier Charge classes con distintos models, pero sin proceso preventivo futuro.

2. **Booking Application Context (Shipping Company Example)**: Proyecto develop booking application object-driven. BOUNDED CONTEXT incluye: (a) application team (consumer del modelo); (b) modeling team (lifecycle control, database schema driven by model, in bounds); (c) legacy cargotracking system (traducción responsibility legacy team, out of bounds); (d) voyage scheduling team (casual coordination, separate models, NOT same CONTEXT—risk). Ganancia: dos teams en CONTEXT saben stay consistentes; legacy/scheduling teams libertad fuera CONTEXT.

3. **Two Bounded Contexts in Shipping Application (Routing Example)**: Automatic cargo routing en booking time. Inicialmente autor insistió routing operation con extended domain model (vessel voyages directly related Legs in Itinerary). Routing team demandó network model optimizado (matrix con cada voyage leg elemento) para performance y established algorithms. Creó two BOUNDED CONTEXTS: Booking CONTEXT (model elegante entities); Transport Network CONTEXT (optimized network matrix). 

   Route Specification → List de location codes: origen/destino primero/último, customs clearance middlle. Network traversal input permite any intermediate points, reverse translation ambiguous (no problem, direccionality one-way).

   List Node IDs → Itinerary: REPOSITORY lookup Node/Shipping Operation por Node IDs. Nodes (pares departure/arrival por operationType-Code) mapeados a Legs. Attribute mapping:
   - departureNode.shippingOperation.vesselVoyageId → leg.vesselVoyageId
   - departureNode.shippingOperation.date → leg.loadDate
   - departureNode.locationCode → leg.loadLocationCode
   - arrivalNode.shippingOperation.date → leg.unloadDate
   - arrivalNode.locationCode → leg.unloadLocationCode

   Implementación: Booking_TransportNetwork_Translator object (único objeto ambos teams maintain). Routing Service (SIDE-EFFECT-FREE FUNCTIONS): public Itinerary route(RouteSpecification spec) { Booking_TransportNetwork_Translator translator = new Booking_TransportNetwork_Translator(); List constraintLocations = translator.convertConstraints(spec); List pathNodes = traversalService.findPath(constraintLocations); Itinerary result = translator.convert(pathNodes); return result; }

4. **Yield Analysis vs. Booking (Customer/Supplier Example)**: Specialized yield analysis team analiza all bookings to maximize income, usa data warehouse con analytical models, needs información Booking application. Two BOUNDED CONTEXTS: different tools, different domain models. Yield analysis interesada Booking subset; upstream (Booking) no depende downstream (Yield analysis). Downstream needs: (1) datos no needed booking operations; (2) stability database schema o notificación reliable changes. Project managers motivated cooperate, report same VP. CUSTOMER/SUPPLIER relationship applies: Yield team plays customer role planning sessions, negocia tasks iteration plans upstream team.

5. **Insurance Project Scope Reduction**: Team año-stuck integration everything para claims. Nueva PM week ruthless planning: identified algunas features (acceso existing databases) where integration provided little value. Aunque usuarios needed data, ninguna otra proposed system feature usaba. Solutions: HTML export reports intranet, specialized query tool standard software, buttons desktop. Launched small SEPARATE WAYS projects almost overnight. Valuable capabilities delivered. Pero team relapseó old habits; legacy sólo small applications que went SEPARATE WAYS permanecieron.

6. **Chemical Markup Language (CML) as Published Language**: Multiple programs catálogo/analyze/manipulate chemical formulas, historically difficult intercambio data (cada program distinct domain model). CML (dialect XML por Murray-Rust et al.) common interchange language. Describe basics: formulas organic/inorganic molecules, protein sequences, spectra, physical quantities. Published CML permitió tools development nunca worth trouble antes (e.g., JUMBO Browser creates graphical views chemical structures stored CML). Benefited XML published meta-language: learning curve flattened, implementation eased (off-shelf tools parsers), documentation (many books XML). Tiny CML sample: &lt;CML.ARR ID="array3" EL.TYPE=FLOAT NAME="ATOMIC ORBITAL ELECTRON POPULATIONS" SIZE=30 GLO.ENT=CML.THE.AOEPOPS&gt; con números floating point representando electron orbital populations. 

7. **Blind Men and Elephant Allegory**: Poema "The Blind Men and the Elephant" (John Godfrey Saxe, basado Hindu text Udana): seis men touching different parts elephant (wall/tree/snake/rope/fan según what touched) dispute loudly cada en own opinion exceeding stiff, cada partly right, all wrong. Diagrams UML (Figure 14.9): four men contexts, no integration. Figure 14.10: four contexts minimal integration. Figure 14.11: one crude integration context (wall held trunks, rope/snake ends). Trunk como snake vs. fire hose (conflicting models mismo part): need new abstraction (aliveness+water-shooting, sin venomous fangs/rolled-up compartment implications). Figure 14.12: deeper model (elephant animal con trunk/leg/body/tail parts distinto properties relationships). Succeeds hinges minimalism: trunk less water-spewing capability mejor que poison-fang feature incorrect.

## Fifteen. Distillation

Ejemplo 1 — Zonas horarias en dos proyectos (líneas 17369-17465): Proyecto A (envío de carga internacional) necesitaba conversión exacta de zonas horarias para coordinar transportes. Asignó un programador de contrato temporal—no requería conocimiento de envío y no lo cultivaría. El programador investigó implementaciones existentes, adaptó la solución pública BSD Unix (base de datos elaborada en C, reverse-engineered), escribió rutina de importación, entregó código integrado. Proyecto B (procesamiento de reclamaciones de seguros) asignó prematuramente, sin requisitos claros, un desarrollador junior para construir un modelo de zona horaria *a priori* flexible. Necesitó ayuda, entonces involucraron a un desarrollador senior. Escribieron código complejo, pero sin aplicación específica no quedó claro si funcionaba. El proyecto fracasó; el código de zona horaria nunca se usó. Lección: segregar GENERIC SUBDOMAINS del CORE es correcto en ambos; pero en Proyecto B, los mejores desarrolladores deberían haber estado construyendo el CORE DOMAIN de seguros, no anticipando necesidades generales.

Ejemplo 2 — Modelo de organigrama como COHESIVE MECHANISM (líneas 17881-17920): Un equipo modelando organizaciones necesitaba responder "¿Quién en esta cadena de mando tiene autoridad de aprobación?" mediante traversal de árbol organizacional. Reconoció el formalismo de *grafos*: nodos (personas) conectados por arcos (relaciones), con algoritmos estándar de traversal bien documentados. Un subcontratista implementó un framework de traversal de grafos como COHESIVE MECHANISM, no un grafo completamente general, solo el subconjunto para necesidades de organización. Con INTENTION-REVEALING INTERFACE: el modelo ahora declaraba simplemente que cada persona es un nodo, cada relación es una arista; el framework podría encontrar relaciones. Sin esta separación, el modelo de organización habría estado acoplado a un método particular de resolver el problema, complejizando y enturbiando el modelo de negocio. Después, un año más tarde, otros desarrolladores rediseñaron para eliminar la separación, reabsorbiendo el MECHANISM en ENTITIES, pero reteniendo la interfaz pública declarativa y la encapsulación: un "círculo completo" a un modelo más profundo.

Ejemplo 3 — SEGREGATED CORE en modelo de envío de carga (líneas 18183-18294, con figuras): Modelo inicial contiene Customer, Customer Agreement, Cargo, Handling Step, Leg, Transport Schedule, Routing Service, Location, plus Billing-related. DOMAIN VISION STATEMENT: "Aumentar visibilidad de operaciones y proveer herramientas para cumplir requerimientos de clientes más rápido y confiablemente." No para ventas; para operadores de primera línea. Se segrega dinero/facturación en package "Billing" como GENERIC SUBDOMAIN. El SEGREGATED CORE "Delivery" contiene clases más directamente involucradas en cumplir requerimientos de clientes: Cargo, Handling Step, Customer Agreement. Cambios modelo: (1) Handling Step ahora restringido por Customer Agreement (insight durante segregación); (2) Customer Agreement adjuntado directamente a Cargo, no a través de Customer (en delivery, el acuerdo es relevante, el Customer no). Resultado: Customer eliminado del CORE (modelo genérico, no necesario en interacciones de delivery). Leg podría quedar en CORE, pero Evans prefiere minimalismo, manteniendo tightest cohesion. Finalmente, "Shipping" package remanente factoriza en GENERIC SUBDOMAINs significativos (e.g., Location como GENERIC SUBDOMAIN) y packages domain-specific de apoyo.

## Sixteen. Large-Scale Structure

El capítulo contiene múltiples ejemplos significativos:

1. OPENING SCENARIO - Satellite Communications System: Un diseño model-driven que claramente expresaba relaciones intrincadas fue descompuesto en módulos manejables por necesidad, resultando en muchos módulos sin estructura unificadora. El equipo no sabía dónde buscar funcionalidad, dónde colocar clases nuevas, ni cómo las piezas encajaban. La solución fue imponer una estructura de capas: capa física de infraestructura (transmisión de bits nodo a nodo), capa de packet-routing (data stream direction), y otras capas identificando niveles conceptuales del problema. Las capas contaban su historia del sistema. Después refactorización para conformar, los módulos y objetos coevolucionaron hasta el diseño completo seguir contornos de estructura en capas.

2. RESPONSIBILITY LAYERS - IN DEPTH: Layering a Shipping System. Modelo básico: Cargo (focus de actividad diaria de compañía), Route Specification (parte integral de Cargo, indicando requisitos entrega), Itinerary (plan entrega operacional), ambos parte del Cargo Aggregate con ciclos de vida atados a marco temporal de entrega activa. Transit Leg es concepto clásico: barcos programados correr con cierta capacidad carga. Customer es decisión tricada: para servicio parcel delivery consumidor individual, Customer sería solo preocupación operacional (transient), pero para compañía shipping cultivando relaciones largo plazo con mayoría business de repeat, Customer pertenece a capa Potential. Decisión no era técnica sino intento de capturar y comunicar conocimiento de dominio. Inicialmente dos capas (Operations, Capability), luego identificaron tercera (Decision Support) cuando Router y otros elementos ayudaban con planning y decision making. 'is preferred' atributo en Transport Leg (preferencia por naves propias o contratadas favorecidas) tenía propósito bias hacia estos transports favorecidos pero violaría layering al existir en Capability capa — se refactorizó en Route Bias Policy separada en Decision Support capa, haciendo Transport Leg más enfocado en concepto fundamental transportación capability.

3. HAZARDOUS MATERIALS ROUTING EXAMPLE: Sistema requería que restricciones aplicaran a ciertas categorías de materiales peligrosos; algunos no permitidos en algunos transports o puertos. Posible diseño inicial: dar a Cargo la responsabilidad de incorporar routing rules porque Cargo posee Route Specification y código HazMat — dependencia Cargo -> HazMat Route Policy Service. Problema: esta dependencia violaría la estructura (Operational -> Decision Support, dirección inversa prohibida). Solución alternativa consistente: Router recopila políticas apropiadas antes de la búsqueda de ruta, requiriendo un cambio en la interfaz de Router para incluir los objetos de los que dependen las policies.

4. RESPONSIBILITY LAYER TYPES - LAYERING PATTERNS. Potential layer ejemplos: en negocios que explotan activos de capital fijo (transportación, manufactura), Potential layer refleja recursos (personas, cómo están organizados los recursos, contratos con vendors que definen potenciales). Operation layer: ¿qué se está haciendo? ¿qué hemos logrado hacer de esos potenciales? Debería reflejar la realidad de la situación, no lo que quisiéramos que fuese. Los objetos de Operations típicamente referencian/componen objetos de Potential; los objetos de Potential no referencian la capa Operations. Decision Support layer: ¿qué acción debería tomarse o qué política debería fijarse? Para análisis y toma de decisiones, basa su análisis en información de capas inferiores; puede usar datos históricos para buscar oportunidades; a menudo implementado con tecnología de data warehouse. Policy layer: ¿cuáles son las reglas y objetivos? Restringe pasivamente el comportamiento de otras capas, a veces aplicando el patrón STRATEGY. Commitment layer (financial/insurance): ¿qué hemos prometido? Tiene naturaleza de Policy (los objetivos dirigen las operaciones futuras) pero también naturaleza de Operations (los commitments emergen y cambian).

5. KNOWLEDGE LEVEL - EMPLOYEE PAYROLL EXAMPLE PART 1: un departamento de HR con un programa simple que calculaba payroll y contribuciones a pensión. El modelo inicial tenía empleados salaried vs. hourly; salaried podían estar en un defined-benefit retirement plan, hourly en un hourly plan — restrictivo. Management decidió que office administrators fuesen defined-benefit pero son hourly — el modelo no permitía mezclar. Se propuso remover las constraints completamente, permitiendo que cada employee se asociara con cualquier plan — rechazado porque no reflejaba la política de la compañía (algunos administrators podrían cambiar, otros no; un janitor no podría). Solución: Employee Type como objeto explícito, haciendo el 'job title' un concepto de dominio explícito. Cada Employee Type se asigna a un Retirement Plan particular Y a un payroll particular. Ubiquitous Language: 'An Employee Type is assigned to either Retirement Plan or either payroll. Employees are constrained by the Employee Type.'

6. KNOWLEDGE LEVEL PART 2 - AFTER RECOGNITION: el equipo reconoció un Knowledge Level implícito en el modelo existente. Los elementos 'arriba' de la línea (Employee Type, Retirement Plans) eran de edición restringida (solo superusuario, cuando la política cambia); los elementos 'abajo' (Employees específicos) eran de edición diaria (personal del departamento). Ediciones restringidas en el Knowledge Level; ediciones operacionales en el nivel operacional. Otro insight: dos conceptos distintos estaban combinados — 'Employee Type is assigned to either Retirement Plan or either payroll' no era realmente un enunciado de Ubiquitous Language (no había objeto 'payroll'); el concepto payroll estaba implícito, mezclado con Employee Type. La refactorización separó Payroll explícitamente: ahora Employee Type tiene tanto Retirement Plan como Payroll.

7. PLUGGABLE COMPONENT FRAMEWORK - SEMATECH CIM EXAMPLE: una fábrica de semiconductores produce grupos de silicon wafers (lots) movidos de máquina en máquina a través de cientos de pasos de procesamiento. Se necesita software para rastrear cada lot individual, registrar el procesamiento exacto hecho, dirigir workers o equipment al siguiente paso y aplicar el siguiente proceso (Manufacturing Execution System - MES). Cientos de máquinas de diferentes vendors, con recipes customizadas por paso. SEMATECH desarrolló el CIM Framework, que define interfaces abstractas para los conceptos básicos del dominio MES de semiconductores (Core Domain como Abstract Core), incluyendo comportamiento y semántica (Process Machine, Transport, Recipe, etc.). Si un vendor produce una nueva máquina, desarrolla una implementación especializada de la interfaz Process Machine; si se adhiere a la interfaz, el componente de control de la máquina debería conectarse (plug in) a cualquier aplicación basada en el CIM Framework. SEMATECH definió las reglas de interacción vía un protocolo específico: si el protocolo está implementado y la aplicación observa las interfaces abstractas estrictamente, puede contar con los servicios prometidos por las interfaces independientemente de la implementación. La combinación de interfaces y protocolo hace de esta una estructura a gran escala muy restrictiva; los requerimientos de infraestructura son específicos (fuertemente acoplados a CORBA para persistence, transactions, events). Esta definición de Pluggable Component Framework permite que la gente desarrolle software independientemente y lo integre suavemente en sistemas inmensos — nadie conoce todos los detalles, pero todos entienden el overview.

8. AIDS MEMORIAL QUILT AS LARGE-SCALE STRUCTURE: miles de personas trabajaron independientemente para crear un quilt de más de 40,000 paneles. Pocas reglas simples proveen la estructura a gran escala, dejando los detalles a los contribuyentes individuales: reglas enfocadas en la misión general (memorializar a las personas fallecidas por SIDA), características que hacen práctica la integración de componentes, y la capacidad de manejar el quilt en secciones (folding). Diseño del panel: incluir el nombre de la persona recordada, información adicional opcional (fechas de nacimiento/muerte, ciudad natal), limitado a un individuo. Materiales: el quilt se pliega/despliega múltiples veces, la durabilidad es crucial — tela de peso medio no elástica (cotton duck o poplin) es la mejor. Diseño vertical u horizontal permitido, el panel terminado con dobladillo debe medir exactamente 3 por 6 pies (90cm × 180cm) — ni más ni menos, con 2-3 pulgadas extra por lado para el dobladillo. El batting no es necesario pero el backing se recomienda. Técnicas de construcción permitidas: Appliqué (coser letras/recuerdos de tela al fondo, no pegamento), Paint (pintura textil, tinte color-fast, marcador de tinta indeleble, no puffy paint), Stencil (trazar diseño con lápiz, levantar plantilla, pintar/marcar con textil), Collage (materiales que no rasguen la tela, evitar vidrio o lentejuelas, sin objetos voluminosos), Photos (fotocopiar en transferencias de planchado sobre 100% algodón, o vinilo plástico transparente cosido evitando el doblez).

## Seventeen. Bringing the Strategy Together

El capítulo no contiene ejemplos concretos de código. Sin embargo, incluye cinco diagramas descritos en prosa: (1) Figure 17.1 muestra principios básicos de diseño estratégico (contexto, destilación, estructura a gran escala) interactuando; (2) Figure 17.2 ilustra RESPONSIBILITY LAYERS ordenando un modelo dentro de un BOUNDED CONTEXT único; (3) Figure 17.3 muestra estructura impuesta sobre relaciones de componentes en distintos BOUNDED CONTEXTS; (4) Figure 17.4 demuestra una estructura que permite a algunos componentes atravesar capas (ej: acceso a legado vía FACADE); (5) Figure 17.5 muestra la misma estructura aplicada tanto dentro de un CONTEXT como a través del CONTEXT MAP entero. El capítulo también presenta un estudio de caso breve: "the Shipping Coordination application" como ejemplo de subsistema legado presentado como masa indiferenciada, que podría internamente ser ordenado por las mismas LAYERS que organiza el CONTEXT MAP del proyecto.

## Conclusion

El capítulo no contiene ejemplos de código (Java, pseudocódigo, UML diagramas). Son estudios de caso narrativos que ilustran patrones DDD en acción: el UBIQUITOUS LANGUAGE persiste y evoluciona tras handoff en el utility project; el ABSTRACT CORE facilita design supple y cambio continuo; la ausencia de MODEL-DRIVEN DESIGN loop (feedback implementation → model changes) en shipping project debilitó la arquitectura cuando surgieron issues de performance y scaling; en Evant, un deep model y supple design permitieron a cuatro developers escalar a billions de planning elements; el CORE DOMAIN con UBIQUITOUS LANGUAGE actúo como "glue" que helped teams unificar un sistema complejo despite diferentes niveles de habilidad entre equipos. No hay fragmentos de código, diagrama detallado, ni ejemplo concreto de patrones—son anécdotas sobre cómo la presencia o ausencia de principios DDD determinó el destino técnico y comercial del software en el tiempo.

## Appendix. The Use of Patterns in This Book

Este capítulo no contiene ejemplos concretos de código DDD (Entity, Value Object, Aggregate, Repository, etc.) ni diagramas de patrones. El contenido es enteramente conceptual y narrativo: la metáfora del auto Peugeot (idiosyncratic design, fluid leak from "a little box two-thirds of the way back"), la analogía de la casa con kitchen/bedroom/bathroom y sus requisitos de infraestructura, y la estructura genérica de cómo Evans presenta patrones en el libro (problema → solución → consecuencias). No hay fragmentos de código Java, UML, o casos de estudio con patrones DDD específicos aplicados.

## Glossary

Este capítulo no contiene ejemplos concretos de código, diagramas de patrones descritos en prosa, ni casos de estudio. Es exclusivamente un glosario de definiciones alfabéticas de términos, patrones y conceptos de DDD sin ilustraciones de implementación.

## References

Sin contenido sustantivo de diseño — sección de portada/agradecimientos/referencia bibliográfica del libro impreso, omitida deliberadamente de la ingesta (ver todo.md).

## Photo Credits

Sin contenido sustantivo de diseño — sección de portada/agradecimientos/referencia bibliográfica del libro impreso, omitida deliberadamente de la ingesta (ver todo.md).

## Index

Sin contenido sustantivo de diseño — sección de portada/agradecimientos/referencia bibliográfica del libro impreso, omitida deliberadamente de la ingesta (ver todo.md).

## Footnotes

Sin contenido sustantivo de diseño — sección de portada/agradecimientos/referencia bibliográfica del libro impreso, omitida deliberadamente de la ingesta (ver todo.md).
