# Patterns of Enterprise Application Architecture

## Índice de capítulos
- [Preface](#preface)
- [Introduction](#introduction)
- [Chapter 1. Layering](#chapter-1-layering)
- [Chapter 2. Organizing Domain Logic](#chapter-2-organizing-domain-logic)
- [Chapter 3. Mapping to Relational Databases](#chapter-3-mapping-to-relational-databases)
- [Chapter 4. Web Presentation](#chapter-4-web-presentation)
- [Chapter 5. Concurrency](#chapter-5-concurrency)
- [Chapter 6. Session State](#chapter-6-session-state)
- [Chapter 7. Distribution Strategies](#chapter-7-distribution-strategies)
- [Chapter 8. Putting It All Together](#chapter-8-putting-it-all-together)
- [Chapter 9. Domain Logic Patterns](#chapter-9-domain-logic-patterns)
- [Chapter 10. Data Source Architectural Patterns](#chapter-10-data-source-architectural-patterns)
- [Chapter 11. Object-Relational Behavioral Patterns](#chapter-11-object-relational-behavioral-patterns)
- [Chapter 12. Object-Relational Structural Patterns](#chapter-12-object-relational-structural-patterns)
- [Chapter 13. Object-Relational Metadata Mapping Patterns](#chapter-13-object-relational-metadata-mapping-patterns)
- [Chapter 14. Web Presentation Patterns](#chapter-14-web-presentation-patterns)
- [Chapter 15. Distribution Patterns](#chapter-15-distribution-patterns)
- [Chapter 16. Offline Concurrency Patterns](#chapter-16-offline-concurrency-patterns)
- [Chapter 17. Session State Patterns](#chapter-17-session-state-patterns)
- [Chapter 18. Base Patterns](#chapter-18-base-patterns)
- [References](#references)

## Preface

This is Martin Fowler's preface to "Patterns of Enterprise Application Architecture," offering contextual framing rather than substantive technical content. It narrates the author's motivating project at ThoughtWorks—a complex leasing system—and establishes the book's goals: capturing proven architectural patterns applicable across enterprise applications. The preface explains the book's dual structure (narrative chapters plus reference patterns) and intended audience (programmers, designers, architects), but does not present patterns, principles, or design solutions themselves. It concludes with extensive acknowledgments and publication details.

## Introduction

Martin Fowler introduces the book's scope by establishing that enterprise applications face distinct and fundamental challenges—persistent data at scale, concurrent access patterns, complex business rules, and integration with heterogeneous systems—that demand architectural decisions rooted in understanding your specific problem space rather than applying one universal solution. He argues that architecture is ultimately a subjective, shared understanding among expert developers of the important decisions that are hard to change, and presents patterns as discovered (not invented) reusable chunks of design advice that require contextual adaptation. The introduction defines core performance terminology (response time, throughput, latency, scalability) to enable measurement-based optimization, and emphasizes that patterns serve as a design vocabulary for communication among teams, not as rigid rules or ready-made implementations.

## Chapter 1. Layering

Layering is a fundamental architectural technique for decomposing complex systems by organizing principal subsystems into layers where higher layers use services of lower layers without being aware of them, and lower layers remain unaware of upper layers. Fowler presents three principal layers (presentation, domain, data source) as the standard pattern for enterprise applications, explaining the evolution from client-server two-tier systems to three-layer architectures driven by web technology and object-oriented programming. The chapter examines the critical trade-offs: while layering provides understandability, substitutability, and standardization, it introduces cascading changes and potential performance penalties. Fowler emphasizes that the hardest task in layered architecture is deciding which layers to have and how to distribute them physically across clients and servers.

## Chapter 2. Organizing Domain Logic

Chapter 2 introduces three foundational patterns for organizing domain logic in enterprise applications: Transaction Script, Domain Model, and Table Module. Each pattern represents a different approach to structuring business logic, with distinct trade-offs regarding complexity, code duplication, developer learning curve, and alignment with database architecture. Fowler presents these as viable choices rather than absolute prescriptions, guided by domain complexity levels and team expertise. The chapter includes a decision framework for pattern selection, discussion of the Service Layer as an additional architectural consideration, and analysis of when to refactor between approaches.

## Chapter 3. Mapping to Relational Databases

Chapter 3 establishes that mapping between objects and relational databases requires careful architectural choices at the data source layer. Fowler presents five primary architectural patterns—Row Data Gateway, Table Data Gateway, Active Record, Data Mapper, and Gateway—arguing that the selection depends critically on domain logic complexity. The chapter emphasizes that as domain models become richer and more decoupled from database schemas, architects must progress from simple gateway patterns toward Data Mapper to achieve proper isolation and testability, while addressing behavioral challenges like identity tracking and transaction management through Unit of Work and Identity Map patterns.

## Chapter 4. Web Presentation

Chapter 4 introduces Web Presentation by analyzing how to structure Web applications using the Model-View-Controller (MVC) pattern to cleanly separate request handling, business logic, and response rendering. Fowler contrasts two fundamental approaches—scripts (CGI, Java servlets) that excel at interpreting HTTP requests, and server pages (PHP, ASP, JSP) that excel at formatting output—arguing that combining both through MVC provides optimal architecture. The author emphasizes that models must be completely isolated from Web presentation, and he clarifies terminology by introducing "input controller" to distinguish MVC's controller from Application Controllers, which manage complex navigation flows. The chapter concludes with three view patterns (Transform View, Template View, Two Step View) and two input controller patterns (Page Controller, Front Controller), each suited to different contexts.

## Chapter 5. Concurrency

Fowler and Rice examine concurrency—one of the most challenging aspects of enterprise application development. While transaction managers protect data manipulated within single transactions, developers must manage "offline concurrency" when interactions span multiple database transactions. The chapter covers fundamental concurrency problems (lost updates, inconsistent reads), the tension between correctness and liveness, execution contexts (requests, sessions, processes, threads, transactions), and two primary control strategies: isolation and immutability. It then contrasts optimistic locking (conflict detection at commit time) with pessimistic locking (conflict prevention by holding locks), discussing trade-offs in isolation levels, deadlock prevention, and the distinction between system transactions and business transactions. The authors present patterns for offline concurrency control and address application server concurrency, concluding that while concurrency is inherently difficult to test and verify, disciplined architectural choices and pattern application make it manageable.

## Chapter 6. Session State

Chapter 6 addresses the fundamental debate between stateless and stateful server architectures in enterprise applications, grounded in the distinction between business transactions (which span multiple system-level interactions) and system transactions. Fowler argues that while stateless servers offer significant resource efficiency benefits—particularly object pooling and scalability on high-traffic systems—many real-world applications are inherently stateful by nature (e.g., shopping carts, multi-step workflows). The chapter's core insight is that the technical choice of statelessness versus statefulness must follow from recognizing whether a business process truly requires persisting state; the architectural question isn't whether to be stateless, but how to manage the state that must exist. Three complementary patterns for storing session state are presented with extensive trade-off analysis across bandwidth, security, isolation, clustering, performance, fault tolerance, and development complexity.

## Chapter 7. Distribution Strategies

This chapter addresses the fundamental problem of distributed object design in enterprise systems. Fowler articulates his "First Law of Distributed Object Design: Don't distribute your objects!" He explains why the common practice of placing different object classes on separate processing nodes for performance reasons actually cripples performance and maintainability. The core tension is that procedure calls across processes are orders of magnitude slower than local calls, forcing remote interfaces to be coarse-grained and awkward to program against. Fowler advocates clustering (running multiple identical process copies) as the primary scalability strategy and recommends the Remote Facade and Data Transfer Object patterns to manage the unavoidable distribution boundaries that must exist between clients and servers, applications and databases.

## Chapter 8. Putting It All Together

Chapter 8 synthesizes the entire catalog of patterns discussed in the book into practical architectural guidance for enterprise applications. Fowler establishes domain logic complexity as the central decision point, using it to drive choices across three domain layer patterns (Transaction Script, Table Module, and Domain Model), then cascades those decisions through data source and presentation layers. His stance is pragmatic and anti-dogmatic: he acknowledges the limitations of advice without seeing actual projects, emphasizes that tools often constrain architecture, and recommends three practices (continuous integration, TDD, refactoring) to reduce the cost of architectural changes. The chapter concludes by comparing his three-layer model against alternative layering schemes from other architects, showing multiple valid approaches to organization.

## Chapter 9. Domain Logic Patterns

Chapter 9 presents four fundamental patterns for organizing domain logic in enterprise applications, arranged on a spectrum of complexity and object orientation. Transaction Script organizes logic as procedures handling single requests, suitable for simple applications but vulnerable to duplication as complexity grows. Domain Model creates a web of interconnected objects modeling both behavior and business rules, ideal for complex logic but demanding careful design. Table Module organizes behavior per database table with single instances handling all rows, balancing object benefits with relational database strengths. Service Layer establishes an application boundary with coarse-grained operations coordinating domain and application logic. Fowler advocates selecting the pattern based on business logic complexity and team familiarity, emphasizing that each pattern addresses different trade-offs between simplicity, extensibility, and maintainability in enterprise systems.

## Chapter 10. Data Source Architectural Patterns

Chapter 10 presents four complementary architectural patterns for accessing relational databases from object-oriented code: Table Data Gateway (encapsulates all SQL operations for a single table), Row Data Gateway (one gateway object per database row, containing only data access logic), Active Record (combines gateway logic with domain business logic in the same class), and Data Mapper (a separate architectural layer isolating domain objects from the database entirely). These patterns form a spectrum from tight database coupling (gateways) to complete separation of concerns (Data Mapper), each with distinct trade-offs. The author argues that the choice depends primarily on domain complexity: simple CRUD applications suit Table/Row Data Gateway or Active Record, while complex business logic benefits from Data Mapper's architectural independence despite its additional layering cost.

## Chapter 11. Object-Relational Behavioral Patterns

Chapter 11 addresses three foundational object-relational behavioral patterns that manage the synchronization between in-memory domain objects and persistent database state. Unit of Work maintains a registry of object changes to batch database operations and handle concurrency, Identity Map ensures each database record loads into exactly one object instance to prevent inconsistency, and Lazy Load defers loading related object data until explicitly accessed to optimize performance. The chapter treats each pattern with multiple implementation strategies, design trade-offs, and concrete code examples showing how to balance developer convenience, correctness, and performance in object-oriented systems that persist to relational databases.

## Chapter 12. Object-Relational Structural Patterns

Chapter 12 addresses the foundational challenge of mapping object-oriented domain models to relational database schemas through ten key structural patterns. The chapter explores how to represent object identity, associations (one-to-one, one-to-many, many-to-many), complex value objects, and inheritance hierarchies in a relational database context. Fowler's approach emphasizes that the relational and object paradigms have fundamental mismatches—relational databases use keys and foreign keys while objects use references; databases have no built-in inheritance support; and relational databases enforce first normal form (single-valued fields only). The patterns provide practical solutions ranging from simple field mappings (Identity Field, Embedded Value) through association handling (Foreign Key Mapping, Association Table Mapping), dependent objects (Dependent Mapping, Serialized LOB), and three distinct inheritance mapping strategies (Single Table, Class Table, and Concrete Table Inheritance), all coordinated through the Inheritance Mappers pattern. The overarching principle is to minimize database accesses and maintain clear separation between object identity/structure and relational persistence while preserving queryability where appropriate.

Key design tensions include: avoiding query impedance through joins vs. normalizing the schema; handling collection mappings when databases support only single-valued fields; managing inheritance without native database support; and deciding when to serialize complex object graphs versus maintaining relational structure for SQL querying. Fowler advocates pragmatic solutions rather than purist approaches, recognizing that no single pattern fits all situations and that mixing strategies within a single domain model is often necessary.

## Chapter 13. Object-Relational Metadata Mapping Patterns

Chapter 13 presents three complementary patterns for object-relational mapping: Metadata Mapping, which eliminates tedious repetitive mapping code through tabular metadata processed by generic code; Query Object, which lets developers construct database queries using object and field names rather than table and column names via the Interpreter pattern; and Repository, which acts as a collection-like interface mediating between domain and persistence layers, encapsulating query logic and supporting multiple data sources. These patterns work together to reduce coupling between domain logic and data access while maintaining flexibility for special cases through subclass overrides. Fowler advocates for starting with simple metadata schemes and evolving them as needs grow rather than building overly complex frameworks upfront.

## Chapter 14. Web Presentation Patterns

Chapter 14 presents the foundational and practical patterns for building Web presentation layers in enterprise applications. It begins with Model View Controller (MVC), emphasizing the critical separation of presentation from domain logic as a fundamental design principle, then addresses the input controller problem through Page Controller (one per logical page) and Front Controller (centralized handler for all requests). The chapter then explores three patterns for the view layer—Template View (embedding markers in static HTML), Transform View (programmatic transformation via XSLT), and Two Step View (separating logical screen construction from HTML rendering)—highlighting the trade-offs between simplicity and constraint in each approach. Finally, Application Controller addresses cross-cutting concerns of navigation flow and screen sequencing, allowing centralized management of which domain commands and views to invoke based on application state. Throughout, Fowler emphasizes keeping presentation logic separate from domain logic and choosing patterns based on application complexity and team preferences.

## Chapter 15. Distribution Patterns

Chapter 15, "Distribution Patterns," addresses the fundamental problem of designing object-oriented systems that must span process and network boundaries. Fowler's central thesis is that fine-grained object interfaces are expensive and awkward across a network, so systems should be designed as if they were local, then a distribution boundary layered on top using two complementary patterns. Remote Facade wraps fine-grained domain objects in a coarse-grained interface to minimize the number of network calls, while Data Transfer Object (DTO) carries batches of data across that boundary in a single call, avoiding chatty multi-call interactions. The chapter's stance is pragmatic and slightly reluctant: these are patterns you need only when a real process/network boundary exists, and they add complexity (duplication of structure, serialization concerns, synchronization risk) that should not be introduced into a non-distributed design. (Nota: la máxima "First Law of Distributed Object Design — don't distribute your objects" que a veces se asocia con este tema aparece en el Capítulo 7, "Distribution Strategies", no en este capítulo.)

## Chapter 16. Offline Concurrency Patterns

Chapter 16 addresses offline concurrency management—preventing conflicts in business transactions that span multiple system transactions where database-level transaction control is insufficient. Fowler presents four complementary patterns: Optimistic Offline Lock (detects conflicts at commit via version checks), Pessimistic Offline Lock (prevents conflicts by acquiring locks before data access), Coarse-Grained Lock (groups related objects under single lock to reduce contention), and Implicit Lock (automates lock mechanics via framework). The overarching principle is that validation and database updates must occur atomically within a single system transaction to guarantee data consistency across distributed business logic.

## Chapter 17. Session State Patterns

Chapter 17 introduces three mutually exclusive patterns for managing session state in enterprise applications: Client Session State (storing data on the client), Server Session State (storing in application server memory or persistent storage), and Database Session State (storing as committed data in the database). Each pattern makes fundamentally different trade-offs between server resource consumption, network bandwidth, security, clustering support, and programming complexity. Fowler argues against a universal best practice, instead providing detailed analysis of when each pattern succeeds or fails based on data volume, architectural requirements, failure tolerance needs, and implementation effort—with specific guidance for Java and .NET platforms.

## Chapter 18. Base Patterns

Chapter 18 presents eleven foundational patterns for enterprise application architecture: Gateway, Mapper, Layer Supertype, Separated Interface, Registry, Value Object, Money, Special Case, Plugin, Service Stub, and Record Set. These patterns address critical design challenges in multi-layered systems, such as encapsulating external resource access, decoupling subsystems, managing common behavior across layers, and enabling runtime configuration. Fowler emphasizes practical trade-offs between simplicity and flexibility, with Gateway being the most frequently used solution for isolating external resource access and Service Stub being essential for testable development when external services are unreliable or unavailable.

## References

This References chapter is Martin Fowler's curated bibliography for "Patterns of Enterprise Application Architecture." It provides 42 annotated citations spanning foundational pattern works (Gang of Four, Alexander), platform-specific pattern collections (J2EE, EJB, .NET), enterprise architecture resources (POSA, OOSE), object-relational mapping materials, transaction processing, domain modeling, process methodologies (XP, TDD), and concurrent/distributed systems patterns. Fowler's annotations are brief evaluative statements positioning each work's relevance and merit within the broader landscape of enterprise application development, designed as a navigational guide for readers seeking deeper understanding of concepts discussed throughout the main text.
