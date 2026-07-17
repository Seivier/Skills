# Clean Architecture: A Craftsman's Guide to Software Structure and Design

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
- [III Design Principles](#iii-design-principles)
- [7 SRP: The Single Responsibility Principle](#7-srp-the-single-responsibility-principle)
- [8 OCP: The Open-Closed Principle](#8-ocp-the-open-closed-principle)
- [9 LSP: The Liskov Substitution Principle](#9-lsp-the-liskov-substitution-principle)
- [10 ISP: The Interface Segregation Principle](#10-isp-the-interface-segregation-principle)
- [11 DIP: The Dependency Inversion Principle](#11-dip-the-dependency-inversion-principle)
- [IV Component Principles](#iv-component-principles)
- [12 Components](#12-components)
- [13 Component Cohesion](#13-component-cohesion)
- [14 Component Coupling](#14-component-coupling)
- [1. THE ACYCLIC DEPENDENCIES PRINCIPLE (ADP)](#1-the-acyclic-dependencies-principle-adp)
- [2. TOP-DOWN DESIGN](#2-top-down-design)
- [3. THE STABLE DEPENDENCIES PRINCIPLE (SDP)](#3-the-stable-dependencies-principle-sdp)
- [4. THE STABLE ABSTRACTIONS PRINCIPLE (SAP)](#4-the-stable-abstractions-principle-sap)
- [5. MEASURING ABSTRACTION: THE A METRIC](#5-measuring-abstraction-the-a-metric)
- [6. THE MAIN SEQUENCE: I/A RELATIONSHIP](#6-the-main-sequence-ia-relationship)
- [7. DISTANCE FROM THE MAIN SEQUENCE: D METRIC](#7-distance-from-the-main-sequence-d-metric)
- [8. CONCLUSION](#8-conclusion)
- [V Architecture](#v-architecture)
- [15 What Is Architecture?](#15-what-is-architecture)
- [16 Independence](#16-independence)
- [17 Boundaries: Drawing Lines](#17-boundaries-drawing-lines)
- [18 Boundary Anatomy](#18-boundary-anatomy)
- [19 Policy and Level](#19-policy-and-level)
- [20 Business Rules](#20-business-rules)
- [21 Screaming Architecture](#21-screaming-architecture)
- [22 The Clean Architecture](#22-the-clean-architecture)
- [23 Presenters and Humble Objects](#23-presenters-and-humble-objects)
- [24 Partial Boundaries](#24-partial-boundaries)
- [25 Layers and Boundaries](#25-layers-and-boundaries)
- [Notas Técnicas Adicionales (del texto original)](#notas-técnicas-adicionales-del-texto-original)
- [26 The Main Component](#26-the-main-component)
- [27 Services: Great and Small](#27-services-great-and-small)
- [28 The Test Boundary](#28-the-test-boundary)
- [29 Clean Embedded Architecture](#29-clean-embedded-architecture)
- [VI Details](#vi-details)
- [30 The Database Is a Detail](#30-the-database-is-a-detail)
- [31 The Web Is a Detail](#31-the-web-is-a-detail)
- [32 Frameworks Are Details](#32-frameworks-are-details)
- [33 Case Study: Video Sales](#33-case-study-video-sales)
- [34 The Missing Chapter](#34-the-missing-chapter)
- [Afterword](#afterword)
- [VII Appendix](#vii-appendix)
- [A Architecture Archaeology](#a-architecture-archaeology)
- [SÍNTESIS DE PRINCIPIOS ARQUITECTÓNICOS TRANSVERSALES](#síntesis-de-principios-arquitectónicos-transversales)
- [LECCIONES CLAVE DE CARRERA](#lecciones-clave-de-carrera)
- [Index](#index)
- [Code Snippets](#code-snippets)

## About This E-Book

This is editorial material regarding licensing and ebook format with no author content.
Sin contenido sustantivo.

## Contents

This section presents the table of contents listing titles and pages.
Sin contenido sustantivo.

## Foreword

The foreword introduces the software architecture metaphor, highlighting its non-physical and fractal nature.
It defines architecture operationally based on the cost of change over time, contrasting bad architecture with clean design.
Kevlin Henney outlines three paths—rigidity, generalized speculation, and clean design—recommending the latter.
The chapter frames architecture as an empirical, testable hypothesis where quality directly enables development velocity.

## Preface

Drawing on over fifty years of programming experience, Robert C. Martin argues that architectural rules are invariant.
Despite exponential increases in computational power, software building blocks have not changed since Alan Turing's era.
The preface asserts that this stability makes the rules of ordering programming blocks universal and timeless.
It warns that modern developer failure stems from failing to learn and apply these historic, stable principles.

## Acknowledgments

This section contains the author's acknowledgments to contributors and a brief reflection on Jim Weirich.
Sin contenido sustantivo.

## About the Author

This section presents the professional biography of the author, Robert C. Martin, listing his career milestones.
Sin contenido sustantivo.

## I Introduction

This introductory section outlines the critical dichotomy between making a software system function and making it correct.
While getting a program to run is accessible, structuring it correctly demands discipline and professional passion.
The author shows how clean design minimizes team size and maintenance overhead while preventing technical debt.
It warns that rotten architecture leads to high coupling, team burnout, and potential organizational collapse.

## 1 What Is Design and Architecture?

This chapter refutes the artificial separation between software design and architecture, treating them as an indivisible continuum.
The primary goal of architecture is defined as minimizing the lifetime cost and human resources needed to maintain a system.
Through empirical data, the author exposes the fallacy that messy code allows for faster short-term development.
It asserts that clean practices like Test-Driven Development are consistently faster at any timescale.

## 2 A Tale of Two Values

Software provides two distinct values to stakeholders: behavior (functional requirements) and structure (ease of change).
The author argues that structure is the more critical value, as a system that is easy to change is far more valuable.
Using Eisenhower's urgent-versus-important matrix, developers are urged to advocate for architectural integrity.
It explains that failing to fight for structure leads to compounding maintenance costs and unchangeable software.

## II Starting with the Bricks: Programming Paradigms

This introductory chapter to programming paradigms reviews the history of computing from Turing to modern compilers.
It defines paradigms as language-independent philosophies of code organization that prescribe structure and limit options.
The author establishes that only three programming paradigms exist, and no others are likely to be discovered.
This is because the three paradigms completely restrict control flow transfer, indirect control, and data mutation.

## 3 Paradigm Overview

This chapter surveys the three main programming paradigms—structured, object-oriented, and functional.
It explains how each paradigm restricts programming capabilities rather than adding new features to the language.
Structured programming limits control transfer, object-oriented limits indirect control, and functional limits assignment.
These constraints align with the architectural concerns of function, component separation, and data management.

## 4 Structured Programming

Detailing the origins of structured programming, this chapter explores Dijkstra's goal to make code mathematically verifiable.
While formal Euclidian-style proofs proved too tedious, the resulting paradigm enabled disciplined functional decomposition.
The author explains that structured programming makes code testable by allowing developers to falsify incorrect behavior.
It establishes testing as a scientific method of showing the presence of bugs rather than proving their absence.

## 5 Object-Oriented Programming

This chapter deconstructs common myths surrounding Object-Oriented programming, specifically encapsulation and inheritance.
The author argues that these capabilities were already achievable in C, making polymorphism the true value of OO.
Through polymorphism, developers gain the ability to invert source code dependencies against the flow of control.
This dependency inversion allows the creation of pluggable architectures where high-level policies are protected.

## 6 Functional Programming

Exploring the principles of functional programming, this chapter focuses on the architectural benefits of immutability.
The author highlights how removing mutable variables entirely eliminates concurrent updates, race conditions, and deadlocks.
To make immutability practical, the chapter proposes segregating applications into mutable and immutable components.
It also presents event sourcing as a strategy that records transactions rather than mutable state changes.

## III Design Principles

This introductory section for the Design Principles part of the book frames the SOLID principles.
It explains that while clean code blocks are necessary, they are insufficient without modular composition principles.
Applying SOLID to groups of functions and data across programming paradigms creates software that is easy to understand.
This section serves as a bridge, preparing readers to apply class-level concepts to component-level architectures.

## 7 SRP: The Single Responsibility Principle

Clarifying a common misconception, this chapter defines the Single Responsibility Principle in terms of business actors.
It states that each software module should be responsible to only one user, stakeholder, or business actor.
The author illustrates the dangers of violating this principle through examples of accidental duplication and merge conflicts.
To solve these issues, architectural strategies are proposed, such as separating data from functions and using Facades.

## 8 OCP: The Open-Closed Principle

This chapter examines the Open-Closed Principle, which asserts that software should be open for extension but closed for modification.
Through a case study of a financial reporting system, the author demonstrates how to partition software into components.
By ensuring that dependencies flow unidirectionally toward high-level policies, developers can extend behavior without changes.
Ultimately, this principle forms the foundation of modern, flexible software architectures.

## 9 LSP: The Liskov Substitution Principle

Based on Barbara Liskov's definition of subtypes, this chapter explores the Liskov Substitution Principle.
Using the square-versus-rectangle problem and a taxi aggregator case study, the author shows the cost of violations.
Violating subtype substitutability forces client code to implement complex, fragile exception-handling logic.
The chapter extends this principle to architectural interfaces like REST APIs, ensuring components remain interchangeable.

## 10 ISP: The Interface Segregation Principle

This chapter details the Interface Segregation Principle, advising developers to avoid depending on elements they do not use.
Through the example of a shared class, the author shows how unsegregated interfaces force unnecessary recompilation.
The principle is then elevated to the architectural level, illustrating the risks of importing heavy frameworks.
It warns that framework-level baggage can cause system instability and unexpected dependencies on third-party libraries.

## 11 DIP: The Dependency Inversion Principle

The Dependency Inversion Principle states that flexible software architectures should depend on abstractions, not concretions.
The author explains that because interfaces are inherently more stable than volatile realization modules, they are preferred.
The chapter utilizes the Abstract Factory pattern to demonstrate how to draw boundaries that separate logic from details.
This unidirectional alignment of dependencies toward abstract layers forms the core of the Dependency Rule.

## IV Component Principles

Introducing the Component Principles section, this chapter outlines how to organize software components.
The author uses a construction metaphor, contrasting SOLID principles with component-level arrangement principles.
This transition marks a shift from class-level design to systemic architecture, addressing build and deployment issues.
The chapter serves as an overview of the cohesion and coupling principles explored in the subsequent sections.

## 12 Components

This chapter defines software components as the basic units of deployment and independent developability.
The author traces the history of component design from manual memory management to modern dynamic linking.
Through the historical battle between Moore's law and Murphy's law, the text explains the evolution of linkers.
Today, this history enables plugin-based architectures where packages act as interchangeable, deployable assets.

## 13 Component Cohesion

This chapter examines component cohesion by introducing three core principles of class grouping.
It details the Reuse/Release Equivalence, the Common Closure, and the Common Reuse principles.
The author describes a natural tension between these rules, where inclusive rules expand and exclusive rules shrink components.
To resolve this, a tension diagram is introduced, showing that architects must find a dynamic balance.

## 14 Component Coupling

This introductory section on component coupling sets the stage for the principles governing component relationships.
It introduces the fundamental tension between technical developability and logical system design that architects must manage.
The author prepares the reader to balance these forces to create a viable, integrated component structure.

## 1. THE ACYCLIC DEPENDENCIES PRINCIPLE (ADP)

This section explores the Acyclic Dependencies Principle, which dictates that component dependency graphs must contain no cycles.
The author critiques the weekly build process as an integration nightmare that degrades geometrically as teams grow.
Instead, the text advocates for partitioning development into independently releaseable, versioned components.
When cycles form, they must be broken using the Dependency Inversion Principle or by extracting shared classes.

## 2. TOP-DOWN DESIGN

This chapter explains why software component structures cannot be successfully designed from the top down.
Rather than representing functional decomposition, component dependency diagrams serve as maps of buildability and maintainability.
The author argues that component structures must grow and evolve organically alongside the logical design of classes.
As modules accumulate, principles like Single Responsibility and Common Closure guide the grouping of classes.

## 3. THE STABLE DEPENDENCIES PRINCIPLE (SDP)

Focusing on component volatility, this chapter introduces the Stable Dependencies Principle.
It states that dependencies must always run in the direction of stability, which is calculated using Fan-in and Fan-out.
The author explains that volatile components should be placed at the top and depend on stable components below.
When this flow is violated, the Dependency Inversion Principle is used to insert interfaces that restore correct direction.

## 4. THE STABLE ABSTRACTIONS PRINCIPLE (SAP)

The Stable Abstractions Principle asserts that a component should be as abstract as it is stable.
This principle establishes that high-level policies must reside in stable, abstract components to remain flexible.
By using interfaces and abstract classes, stable components conform to the Open-Closed Principle, permitting extension.
The chapter demonstrates that combining stable dependencies and stable abstractions is equivalent to component-level DIP.

## 5. MEASURING ABSTRACTION: THE A METRIC

This chapter defines a quantitative metric to measure the abstraction level of a software component.
The abstraction score, denoted as A, is calculated as the ratio of abstract classes to the total number of classes.
This metric allows developers to mathematically evaluate where a component lies on the concrete-to-abstract spectrum.
It serves as a vital input for graphing relationship dynamics and analyzing design health.

## 6. THE MAIN SEQUENCE: I/A RELATIONSHIP

This chapter introduces the Instability-Abstraction relationship graph, plotting components to identify zones of pain and uselessness.
The Zone of Pain represents highly stable, highly concrete components that are rigid and difficult to extend.
The Zone of Uselessness contains abstract components with no dependents, representing unused detritus in the codebase.
To prevent these states, the author defines the Main Sequence line where instability and abstraction balance perfectly.

## 7. DISTANCE FROM THE MAIN SEQUENCE: D METRIC

To assess how well a system conforms to the Main Sequence, this chapter introduces the D metric.
The D metric measures a component's absolute distance from the ideal Main Sequence line.
The author explains how calculating the mean and variance of this metric helps identify poorly structured components.
Furthermore, tracking the D metric over time allows teams to monitor progressive architectural degradation.

## 8. CONCLUSION

Concluding the discussion on component coupling, this chapter reflects on the nature and limitations of software metrics.
The author stresses that these measurements are imperfect, standard-based tools rather than absolute rules.
However, they remain invaluable for guiding decisions and assessing design quality throughout a project's lifecycle.
They represent distilled experience on which dependency and abstraction patterns are beneficial or harmful.

## V Architecture

This section contains Pandoc structural markers dividing the Parts of the book.
Sin contenido sustantivo.

## 15 What Is Architecture?

Defining the fundamental role of software architecture, this chapter asserts that architecture is the shape given to a system.
This shape is designed to facilitate the development, deployment, operation, and maintenance of the application.
The central strategy is to defer low-level detail decisions—such as databases and frameworks—by keeping options open.
Through case studies, the author shows how isolating core business policies from concrete devices reduces life-cycle costs.

## 16 Independence

This chapter explores how a good architecture supports the system's use cases, operational needs, and deployment processes.
To achieve independence, the author recommends decoupling the system horizontally into layers and vertically into use cases.
Decoupling can be applied at the source, deployment, or service level based on team size and complexity.
A flexible design allows a system to start as a monolith, transition to services, and scale back as needs change.

## 17 Boundaries: Drawing Lines

Exploring the boundary lines that separate software elements, this chapter details how to isolate core business rules.
The author provides case studies of failed, premature distributed architectures, contrasted with the success of FitNesse.
By ensuring that dependency arrows point only from concrete plugins to stable core abstractions, a pluggable design is created.
This design prevents local modifications from propagating throughout the codebase, safeguarding architectural integrity.

## 18 Boundary Anatomy

This chapter examines the physical and logical structure of software boundaries, explaining runtime boundary crossings.
The author analyzes three decoupling modes: threaded monoliths, dynamic shared libraries, and local or network services.
While monoliths communicate rapidly via function calls, services suffer from network latency and require careful design.
Regardless of the communication mechanism, the same rules apply, requiring low-level plugins to depend inward.

## 19 Policy and Level

This chapter defines a software system as a collection of policies transforming inputs into outputs.
The author introduces the concept of 'level' to measure a policy's distance from physical inputs and outputs.
To prevent change propagation, the architecture is structured as a DAG where dependencies run toward high-level policies.
By employing Dependency Inversion, low-level details are treated as plugins, protecting high-value business logic.

## 20 Business Rules

This chapter identifies business rules as the core functionality that justifies a software system's existence.
It distinguishes between Critical Business Rules and Data, and application-specific rules that reside in Use Cases.
To isolate these rules, the chapter details the structure of Entities, which bind critical data and general rules.
Use Cases act as orchestrators of these Entities, interacting via independent request and response models.

## 21 Screaming Architecture

Drawing on the metaphor of building plans, this chapter argues that architecture should loudly declare its functional domain.
The author highlights the importance of a use-case-driven approach, urging architects to treat frameworks as details.
By keeping frameworks at arm's length, the core business logic remains clean and fully testable in isolation.
Tens of decisions regarding delivery mechanisms can be deferred, keeping the system flexible.

## 22 The Clean Architecture

This chapter integrates various layered design patterns into a unified approach known as Clean Architecture.
Organized as concentric circles, the architecture enforces the Dependency Rule, pointing dependencies only inward.
The author demonstrates how boundary crossings are managed using the Dependency Inversion Principle with interfaces.
It stresses that only simple, framework-agnostic data structures should cross boundaries to prevent dependency contamination.

## 23 Presenters and Humble Objects

Introducing the Humble Object pattern, this chapter explains how to separate behaviors that are difficult to test.
The author applies this pattern to the user interface by dividing it into a simple View and a formatting Presenter.
This pattern is shown to be universal across boundaries, including database gateways, data mappers, and service listeners.
By encapsulating volatile dependencies behind these boundaries, the testability and maintainability of the system are improved.

## 24 Partial Boundaries

This chapter explores the pragmatics of implementing partial boundaries to defer the high costs of full boundaries.
The author details three strategies: skipping the deployment separation, using one-dimensional boundaries, and employing Facades.
While these options keep the architecture flexible, they are vulnerable to decay if developers bypass the boundaries.
It concludes that the architect must carefully evaluate the cost and trade-offs of each partial boundary.

## 25 Layers and Boundaries

Using the classic game 'Hunt the Wumpus' as a case study, this chapter demonstrates boundary multiplicity.
The author illustrates the gradual refinement of the game's architecture by separating rules from languages and storage.
As the system scales, logical boundaries are physicalized into microservices and network APIs.
The chapter details the tension between over-engineering and the high cost of refactoring late-discovered boundaries.

## Notas Técnicas Adicionales (del texto original)

This section contains additional technical footnotes from the original text clarifying arrow directions.
Sin contenido sustantivo.

## 26 The Main Component

This chapter examines the Main component, which serves as the system's entry point and ultimate detail.
Located in the outermost layer, Main is responsible for instantiating factories and executing dependency injection.
Through the Hunt the Wumpus example, the author shows how treating Main as a plugin allows easy configuration swapping.
This separation preserves the pure architecture of the core by keeping configuration details on the periphery.

## 27 Services: Great and Small

This chapter critiques the architectural claims of Service-Oriented (SOA) and microservice architectures.
The author refutes the common assumptions of strong decoupling, showing that services remain coupled by shared data.
Through a taxi aggregator case study, the text demonstrates how cross-cutting concerns force coordinated service changes.
The solution is to design services internally using SOLID component principles so that new features are pluggable.

## 28 The Test Boundary

Positioning tests as integral, outer-circle components of software architecture, this chapter outlines testability strategies.
The author addresses the problem of fragile tests, where changes in volatile elements like the GUI break test suites.
To prevent this, the chapter advocates for a dedicated Testing API that acts as a superset of the application's interactors.
By avoiding structural coupling, developers can safely refactor code without breaking the test suite.

## 29 Clean Embedded Architecture

This chapter examines software development in the embedded systems domain, distinguishing software from firmware.
The author critiques the tendency to stop at Kent Beck's 'make it work' stage and optimize code prematurely.
To solve the target-hardware bottleneck where testing is restricted to physical targets, a three-layer architecture is proposed.
Key abstraction layers—including the HAL, PAL, and OSAL—are detailed as critical boundaries that isolate hardware specifics.

## VI Details

This section contains Pandoc structural markers dividing the Parts of the book.
Sin contenido sustantivo.

## 30 The Database Is a Detail

This chapter establishes that databases are low-level implementation details rather than core architectural concerns.
The author traces the rise of relational databases to the latency limitations of rotating magnetic disks.
Without this bottleneck, developers would naturally organize data using standard memory structures like trees.
The text warns against letting database table schemas and SQL query structures contaminate the core application logic.

## 31 The Web Is a Detail

Framing the web as a volatile input-output device, this chapter outlines the endless pendulum of software architecture.
The author argues that because the user interface is an implementation detail, the core must remain independent of GUIs.
To handle chatty user interactions, the system should encapsulate inputs and outputs into simple data structures.
This strategy isolates business rules from marketing changes and technological shifts in GUI delivery.

## 32 Frameworks Are Details

This chapter cautions developers against deeply coupling their core application logic to third-party frameworks.
The author highlights the asymmetric relationship between users and framework authors who design for their own needs.
To combat this risk, a defensive architecture is proposed where frameworks are relegated to the system's outer circles.
Using the Spring Framework as an example, the text demonstrates that frameworks should be contained in the Main component.

## 33 Case Study: Video Sales

Synthesizing the book's architectural principles, this chapter presents a comprehensive case study for a video sales website.
The design partitions the system vertically by business actors (SRP) and horizontally by layers of policy level.
The resulting component architecture ensures that all code dependencies run unidirectionally toward high-level business rules.
This separation allows the team to defer deployment decisions and package components into jar files dynamically.

## 34 The Missing Chapter

Written by Simon Brown, this chapter explores the critical gap between conceptual design and concrete code implementation.
It compares four methods of organizing code: package by layer, package by feature, ports and adapters, and package by component.
Brown warns that if developers make all classes public, packages act only as folders rather than encapsulation boundaries.
The chapter advises using language-level access modifiers, module systems, and separate source trees to enforce boundaries.

## Afterword

The afterword reflects on the history of software architecture, contrasting the rigid 'Big Architecture' with Agile revolutions.
While Agile successfully prioritized delivering business value, it often neglected structural design, leading to fragile codebases.
The text urges developers to integrate lightweight design reviews and refactoring into their daily TDD workflows.
It concludes with a call to action for experienced developers to mentor younger programmers to pass down clean design.

## VII Appendix

This section contains Pandoc structural markers dividing the Parts of the book.
Sin contenido sustantivo.

## A Architecture Archaeology

Drawing on forty years of software history, this appendix documents fifteen real-world projects that shaped the author's philosophy.
It details early systems using memory overlays and explores failures like the Voice Response System's database lock-in.
From inventing polymorphic dispatch on an Intel 8085 to designing precursor microservice architectures, the author shows key patterns.
These challenges in device coupling and code organization birthed the modern principles of clean boundaries.

## SÍNTESIS DE PRINCIPIOS ARQUITECTÓNICOS TRANSVERSALES

This section synthesizes the transversal architectural principles derived from the career archaeology in the appendix.
It consolidates key patterns including boundary design, hardware and database isolation, and domain-specific languages.
Additionally, it highlights lessons on avoiding tight coupling to third-party vendors and managing over-engineering risks.
The summary reinforces that there is no single best architecture, and that design flexibility must match problem scale.

## LECCIONES CLAVE DE CARRERA

Concluding the historical appendix, this section highlights seven critical career lessons for software engineers.
It emphasizes the importance of code readability, architectural flexibility in matching scale, and proper dependency direction.
The author underscores that databases, user interfaces, and device controls must always be isolated from business rules.
Ultimately, the section notes that while clean architectures can be implemented differently, they all share boundary discipline.

## Index

This section contains the alphabetical index of terms and page numbers for the book.
Sin contenido sustantivo.

## Code Snippets

This section contains source code image galleries linked to various chapters with no extractable text.
Sin contenido sustantivo.
