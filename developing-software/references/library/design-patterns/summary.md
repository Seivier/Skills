# Design Patterns: Elements of Reusable Object-Oriented Software

## Índice de capítulos
- [Chapter 1: Introduction](#chapter-1-introduction)
- [Chapter 2. A Case Study: Designing a Document Editor](#chapter-2-a-case-study-designing-a-document-editor)
- [Chapter 3: Creational Patterns](#chapter-3-creational-patterns)
- [Chapter 4: Structural Patterns](#chapter-4-structural-patterns)
- [Chapter 5: Behavioral Patterns](#chapter-5-behavioral-patterns)
- [Chapter 6. Conclusion](#chapter-6-conclusion)
- [Appendices](#appendices)

## Chapter 1: Introduction

This chapter introduces the concepts of object-oriented design patterns, defining them as reusable solutions to recurring design problems in a specific context.
It highlights the Model-View-Controller (MVC) architecture in Smalltalk-80 as a primary case study demonstrating several patterns working in unison.
The author establishes key design principles, notably urging developers to program to interfaces rather than concrete implementations and to favor object composition over class inheritance.
By examining how patterns manage object granularity, interfaces, and run-time relationships, this chapter provides a foundational framework for understanding how to design highly flexible, maintainable, and reusable software.

## Chapter 2. A Case Study: Designing a Document Editor

This case study outlines the step-by-step design of a WYSIWYG document editor named Lexi to illustrate how multiple design patterns collaborate in a real-world application.
It covers seven distinct design problems, including document representation using the Composite pattern, page formatting via Strategy, and UI embellishments using Decorator.
Additionally, it demonstrates Abstract Factory for look-and-feel style guides, Bridge for window system independence, Command for undoable operations, and Iterator and Visitor for text analysis.
The author shows that complex software design is an iterative process where patterns naturally overlap to handle competing constraints of flexibility, performance, and platform independence.

## Chapter 3: Creational Patterns

This chapter focuses on creational design patterns, which abstract the instantiation process to decouple a system from how its constituent objects are created and composed.
Through the common example of building a maze game, it provides in-depth analyses of five patterns: Abstract Factory, Builder, Factory Method, Prototype, and Singleton.
The author emphasizes the architectural shift from static class inheritance to dynamic object composition, demonstrating how these patterns hide concrete product classes.
By utilizing these techniques, developers can write systems that interact with products solely through abstract interfaces, enhancing runtime configuration and reusability.

## Chapter 4: Structural Patterns

This chapter details structural design patterns, which examine how classes and objects are composed to form larger, more complex systems without sacrificing flexibility.
It contrasts static class structural patterns that use inheritance with dynamic object structural patterns that rely on object composition at run-time.
Seven patterns are thoroughly analyzed: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, and Proxy, each detailing trade-offs regarding storage, performance, and coupling.
The author argues that proper structural composition shields clients from changes in subsystems, ensuring binary compatibility and enabling run-time configuration changes.

## Chapter 5: Behavioral Patterns

This chapter covers behavioral design patterns, focusing on how algorithms are structured and how responsibilities are distributed among communicating objects at runtime.
It distinguishes class behavioral patterns like Template Method and Interpreter, which use inheritance, from object behavioral patterns that utilize composition.
Detailed breakdowns are provided for eleven patterns: Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, and Visitor.
The author highlights how these patterns shift design focus from hardcoded execution control flows to flexible, topological networks of loosely coupled objects.
These patterns are crucial for managing complex, dynamic interactions without exposing internal structures or violating object encapsulation boundaries.

## Chapter 6. Conclusion

The concluding chapter summarizes the broader role of design patterns in establishing a shared design vocabulary and documenting software architecture decisions.
It outlines the lifecycle of object-oriented software through three phases—prototyping, expansion, and consolidation—demonstrating how refactoring leads to pattern-dense designs.
The authors trace the history of the design patterns movement, the collaboration of the Gang of Four, and the influence of architect Christopher Alexander.
Ultimately, the chapter advocates for design density, where multiple overlapping patterns are woven together to build profound, robust, and highly maintainable software systems.

## Appendices

The appendices provide a comprehensive glossary of object-oriented design terms, details on the C++ foundation classes used throughout the book, and a thematic bibliography analysis.
Key concepts are defined, such as abstract coupling, white-box versus black-box reuse, delegation, dynamic binding, and the distinction between toolkits and frameworks.
It documents minimal implementation structures for standard collections and coordinates, which are essential for understanding the book's concrete design pattern examples.
Furthermore, the bibliographical mapping connects the design pattern catalog to historical software engineering research, UI toolkits, and refactoring methodologies.
