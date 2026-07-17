# Design Patterns: Elements of Reusable Object-Oriented Software — Resúmenes Profundos por Capítulo


## Índice de capítulos
- [Chapter 1: Introduction](#chapter-1-introduction)
- [Chapter 2. A Case Study: Designing a Document Editor](#chapter-2-a-case-study-designing-a-document-editor)
- [Chapter 3: Creational Patterns](#chapter-3-creational-patterns)
- [Chapter 4: Structural Patterns](#chapter-4-structural-patterns)
- [Chapter 5: Behavioral Patterns](#chapter-5-behavioral-patterns)
- [Chapter 6. Conclusion](#chapter-6-conclusion)
- [Appendices](#appendices)

## Chapter 1: Introduction

### Designing Reusable OO Software
Designing object-oriented (OO) software is challenging; designing *reusable* OO software is even more difficult. The designer must identify pertinent objects, factor them into classes at the correct granularity, define class interfaces and inheritance hierarchies, and establish key relationships. The resulting design should be specific to the problem at hand yet general enough to accommodate future modifications and requirements while avoiding or minimizing subsequent redesigns. Experienced designers rely heavily on prior design experience, reusing patterns of classes and communicating objects that have proven successful. Design patterns systematically name, explain, and evaluate these recurring designs in OO systems.

### 1.1 What Is a Design Pattern?
A design pattern is a solution to a recurring design problem within a specific context. According to Christopher Alexander (addressing architectural patterns in buildings and towns, which translates directly to software design), each pattern describes a recurring problem and the core of its solution in a way that allows the solution to be applied countless times without being done the exact same way twice. In OO design, patterns are expressed in terms of objects and interfaces.

A design pattern consists of four essential elements:
1. **Pattern Name:** A short, one- or two-word handle used to describe a design problem, its solution, and its consequences. It increases design vocabulary, allowing developers to design and communicate at a higher level of abstraction.
2. **Problem:** Describes the context and conditions under which the pattern should be applied. It explains the specific design issues (e.g., how to represent algorithms as objects) or structures symptomatic of inflexible design.
3. **Solution:** Describes the elements (classes and objects), their relationships, responsibilities, and collaborations. It is abstract, acting as a template rather than a concrete implementation.
4. **Consequences:** The results, trade-offs, and impacts of applying the pattern. These include space and time trade-offs, implementation/language issues, and the pattern's impact on flexibility, extensibility, and portability.

*Design Patterns versus Primitives/Whole Architectures:* Design patterns occupy a middle ground of abstraction. They are not low-level, reusable data structures like linked lists or hash tables. Neither are they complex, domain-specific designs for entire applications or subsystems. Instead, they are descriptions of communicating objects and classes customized to solve a general design problem in a particular context.

*Language Influences:* The patterns in this book assume features comparable to C++ and Smalltalk. In procedural languages (e.g., C, Pascal, Ada), basic concepts like "Inheritance," "Encapsulation," and "Polymorphism" might themselves be considered patterns. Conversely, dynamic OO languages with advanced built-in features may lessen the need for certain patterns (for example, the presence of multi-methods in CLOS reduces the necessity of the Visitor pattern).

### 1.2 Design Patterns in Smalltalk MVC
The Model/View/Controller (MVC) triad in Smalltalk-80 is an illustrative example of design patterns in action. MVC decouples the application logic from its visual presentation and user interaction:
* **Model:** The application object containing data and core logic.
* **View:** The screen presentation of the model's data.
* **Controller:** Defines the way the user interface reacts to user input (keyboard, mouse).

#### Key Design Patterns inside MVC:
1. **Observer Pattern:** MVC decouples views and models via a subscribe/notify protocol. The model manages its data and, when it changes, notifies all dependent views. The views then query the model to update their visual representations. This allows multiple views (e.g., spreadsheet, histogram, pie chart) to be attached to a single model simultaneously without the model knowing their concrete classes.
2. **Composite Pattern:** MVC supports nested views using the `CompositeView` class, a subclass of `View`. A `CompositeView` object can contain and manage nested views (such as sub-buttons in a panel), yet it behaves exactly like a single `View` object, allowing uniform treatment of individual and composite objects.
3. **Strategy Pattern:** MVC encapsulates user response mechanisms in a `Controller` object. A `View` uses an instance of a `Controller` subclass to implement a particular input strategy (e.g., handling keyboard inputs or displaying pop-up menus). Replacing the controller instance changes the view's response behavior statically or dynamically at run-time (for example, disabling input by assigning a controller that ignores all input events).
4. **Other Patterns in MVC:** `Factory Method` is used to specify the default controller class for a view, and `Decorator` is used to add scrolling capabilities to a view.

### 1.3 Describing Design Patterns
Design patterns are documented using a consistent 13-section template to facilitate comparison, learning, and usage:
1. **Pattern Name and Classification:** A succinct name and its category based on purpose and scope.
2. **Intent:** A short statement of what the pattern does, its rationale, and the specific design issue it addresses.
3. **Also Known As:** Alternative names.
4. **Motivation:** A concrete scenario showing the design problem and how the pattern's class/object structures resolve it.
5. **Applicability:** Situations where the pattern is appropriate, including poor designs it can remedy.
6. **Structure:** Graphical class diagrams using Object Modeling Technique (OMT) notation, along with interaction diagrams showing sequence of requests.
7. **Participants:** The classes and objects involved and their specific responsibilities.
8. **Collaborations:** How the participants interact to execute their responsibilities.
9. **Consequences:** The trade-offs, results, and structural variations enabled by the pattern.
10. **Implementation:** Pitfalls, hints, techniques, and language-specific details (e.g., C++ or Smalltalk).
11. **Sample Code:** Code fragments illustrating implementation.
12. **Known Uses:** Real-world examples of the pattern across different domains.
13. **Related Patterns:** Comparisons and structural relationships with other patterns.

### 1.4 The Catalog of Design Patterns
The catalog details 23 design patterns:
1. **Abstract Factory:** Interface for creating families of related products.
2. **Adapter:** Converts one interface into another that clients expect.
3. **Bridge:** Decouples an abstraction from its implementation.
4. **Builder:** Separates construction of complex objects from their representation.
5. **Chain of Responsibility:** Avoids coupling sender to receiver by chaining handlers.
6. **Command:** Encapsulates requests as objects.
7. **Composite:** Tree structures for uniform leaf and composite treatment.
8. **Decorator:** Dynamically attaches additional responsibilities.
9. **Facade:** Single, simplified interface to a complex subsystem.
10. **Factory Method:** Defines creation interface, defers instantiation to subclasses.
11. **Flyweight:** Shared fine-grained objects to optimize storage.
12. **Interpreter:** Represent a grammar and evaluate sentences.
13. **Iterator:** Sequential access without exposing representation.
14. **Mediator:** Encapsulates and coordinates object interactions.
15. **Memento:** Captures and restores object state without breaking encapsulation.
16. **Observer:** Pub-sub synchronization mechanism.
17. **Prototype:** Clones prototypical template instances.
18. **Proxy:** Surrogate placeholder to control access.
19. **Singleton:** Ensures exactly one instance.
20. **State:** Dynamic subclass switching based on internal state.
21. **Strategy:** Interchangeable, encapsulated algorithms.
22. **Template Method:** Fixed algorithm skeleton, hook overrides.
23. **Visitor:** Adds operations to a stable hierarchy via double-dispatch.

### 1.5 Organizing the Catalog
The 23 patterns are classified based on two main criteria:
1. **Purpose (Creational, Structural, or Behavioral):**
   * **Creational:** Concerns the process of object creation.
   * **Structural:** Deals with the composition of classes or objects.
   * **Behavioral:** Characterizes how classes or objects interact and distribute responsibility.
2. **Scope (Class or Object):**
   * **Class Patterns:** Focus on static relationships established through inheritance at compile-time.
   * **Object Patterns:** Focus on dynamic relationships between objects that can be changed at run-time.

### 1.6 How Design Patterns Solve Design Problems

#### Finding Appropriate Objects
Decomposing a system into objects is difficult due to competing factors: encapsulation, granularity, dependency, flexibility, performance, and evolution.
Strict real-world modeling often fails to produce flexible systems because the resulting classes reflect today's realities but not tomorrow's changes. Design patterns introduce abstractions that do not exist in the physical world (e.g., algorithms as objects via `Strategy`, or states as objects via `State`).

#### Determining Object Granularity
Objects vary in scale. Design patterns provide strategies for managing granularity:
* `Facade` represents entire subsystems as single objects.
* `Flyweight` manages huge numbers of fine-grained objects via sharing.
* `Abstract Factory` and `Builder` create objects whose sole job is to construct other objects.
* `Visitor` and `Command` encapsulate operations or requests as objects.

#### Specifying Object Interfaces
An object's **signature** is defined by its name, parameters, and return value. The **interface** is the set of all signatures defined by its operations. A **type** is a name for a specific interface.
* **Subtype / Supertype:** A subtype's interface contains the interface of its supertype (inherits the interface).
* **Dynamic Binding:** The run-time association of a request to an object and one of its operations.
* **Polymorphism:** The ability to substitute objects with identical interfaces at run-time. It simplifies clients, decouples objects, and dynamically alters relationships.
* **Interface Specification in Patterns:** Patterns define key interface elements and what *not* to expose. For instance, `Memento` specifies a double interface: a narrow one for clients (to hold/copy mementos) and a wide, privileged one for the originator (to access internal state). `Decorator` and `Proxy` require interfaces identical to the objects they wrap. `Visitor` interfaces must reflect all classes of elements they can visit.

#### Specifying Object Implementations
An object's implementation is defined by its **class**.
* **Instantiation:** Allocates storage for internal data (**instance variables**) and associates operations.
* **Abstract Class:** Defines a common interface; it cannot be instantiated. It contains **abstract operations** (declared but not implemented).
* **Concrete Class:** An instantiable class with full implementations.
* **Mixin Class:** Provides optional interfaces/functionality via multiple inheritance; not intended for direct instantiation.

##### Class versus Interface Inheritance
* **Class (Implementation) Inheritance:** A mechanism for code and representation sharing. A subclass inherits the parent's data and operation implementations.
* **Interface Inheritance (Subtyping):** Describes when an object can be used in place of another.
* *Language Differences:* C++ uses public inheritance for both, using pure virtual functions/pure abstract classes for interface inheritance and private inheritance for pure class inheritance. Smalltalk inheritance is strictly implementation inheritance; type conformance is implicit.
* *Design Pattern Dependency:* Many patterns rely on this distinction. For example, `Chain of Responsibility` participants share a type but rarely an implementation. In `Composite`, `Component` defines the interface while `Composite` provides the implementation. `Command`, `Observer`, `State`, and `Strategy` are often implemented via pure interface abstract classes.

##### Design Principle 1: Program to an interface, not an implementation.
Do not declare variables as instances of concrete classes. Declare them using abstract classes that define interfaces. This eliminates client dependencies on concrete classes and enables dynamic substitution. Creational patterns facilitate this by abstracting the instantiation process.

#### Putting Reuse Mechanisms to Work

##### Inheritance versus Composition
* **White-Box Reuse (Class Inheritance):** Reuse by subclassing. The internals of the parent class are visible to the subclass.
  * *Advantages:* Static, compile-time definition; easy to use; simple to override and modify parent behavior.
  * *Disadvantages:* Cannot be changed at run-time; breaks encapsulation by exposing parent internals; subclass becomes dependent on parent implementation details (fragile base class problem).
* **Black-Box Reuse (Object Composition):** Assembling objects at run-time to achieve complex functionality.
  * *Advantages:* Does not break encapsulation (objects accessed solely through interfaces); objects can be substituted dynamically at run-time; fewer implementation dependencies; keeps classes small and focused on single tasks.
  * *Disadvantages:* System behavior depends on run-time relationships; more objects and fewer classes, making the design harder to understand statically.

##### Design Principle 2: Favor object composition over class inheritance.
Object composition keeps the system dynamic and modular. Inheritance is used to build new components that can then be composed.

##### Delegation
Delegation makes composition as powerful for reuse as inheritance. A receiving object forwards (delegates) operations to its delegate.
* *The Self Reference Problem:* In class inheritance, an inherited operation refers to the receiver via `this` (C++) or `self` (Smalltalk). In delegation, the receiver must explicitly pass itself to the delegate so that the delegated operation can refer back to the receiver.
* *Example:* Instead of `Window` subclassing `Rectangle`, `Window` contains an instance of `Rectangle` and delegates its `Area()` request by calling `rectangle->Area()`.
* *Trade-offs:* Allows dynamic behavior modifications (e.g., swapping a `Rectangle` delegate with a `Circle` delegate at run-time). However, highly parameterized, dynamic software is harder to read, maintain, and debug than static hierarchies, and it introduces slight run-time call overhead.
* *Usage:* Central to `State`, `Strategy`, `Visitor`, and (to a lesser degree) `Mediator`, `Chain of Responsibility`, and `Bridge`.

##### Inheritance versus Parameterized Types (Generics/Templates)
Parameterized types (C++ templates, Ada/Eiffel generics) define a type without specifying all types it uses.
* *Comparison of reuse options (e.g., sorting comparison operations):*
  1. Subclassing: Overriding comparison operations (Template Method).
  2. Composition: Passing a comparison object to the sorting routine (Strategy).
  3. Parameterized Types: Specifying the comparison function as a template argument.
* *Trade-offs:* Parameterized types are static (resolved at compile-time) and cannot change at run-time, unlike composition. They do not require run-time indirection, making them highly efficient. They are unnecessary in dynamically typed languages like Smalltalk.

#### Relating Run-Time and Compile-Time Structures
Compile-time structures (classes and inheritance hierarchies) are static. Run-time structures consist of dynamic networks of communicating objects.
* **Aggregation:** An object owns or is responsible for another (part-whole relationship). Aggregated objects share the lifetime of their owner.
* **Acquaintance (Association / Using):** An object merely knows of another object. They request operations but have independent lifetimes and are loosely coupled.
* *Implementation:* Both are often implemented using pointers or references in C++ and Smalltalk. The difference is determined by *intent*. Acquaintance is dynamic, short-lived (sometimes lasting only for a single operation), and hard to discern from static code. Many patterns (e.g., `Composite`, `Decorator`, `Observer`, `Chain of Responsibility`) explicitly construct these run-time structures.

#### Designing for Change
Anticipating change is crucial to avoiding expensive redesigns. Design patterns allow specific aspects of a system to vary independently:
1. **Creating an object by specifying a class explicitly:** Commits to an implementation. *Remedy:* `Abstract Factory`, `Factory Method`, `Prototype`.
2. **Dependence on specific operations:** Commits to one way of satisfying a request. *Remedy:* `Chain of Responsibility`, `Command`.
3. **Dependence on hardware and software platform:** Impedes portability. *Remedy:* `Abstract Factory`, `Bridge`.
4. **Dependence on object representations or implementations:** Changes cascade when implementations alter. *Remedy:* `Abstract Factory`, `Bridge`, `Memento`, `Proxy`.
5. **Algorithmic dependencies:** Changing algorithms forces client updates. *Remedy:* `Builder`, `Iterator`, `Strategy`, `Template Method`, `Visitor`.
6. **Tight coupling:** Monolithic systems, classes hard to reuse in isolation. *Remedy:* `Abstract Factory`, `Bridge`, `Chain of Responsibility`, `Command`, `Facade`, `Mediator`, `Observer`.
7. **Extending functionality by subclassing:** Class explosion and high inheritance overhead. *Remedy:* `Bridge`, `Chain of Responsibility`, `Composite`, `Decorator`, `Observer`, `Strategy`.
8. **Inability to alter classes conveniently:** Modifying closed libraries or complex hierarchies. *Remedy:* `Adapter`, `Decorator`, `Visitor`.

##### Software Categories and Reuse:
* **Application Programs:** Focus on internal reuse, maintainability, and extension. Reduced coupling ensures classes can be reused across different internal contexts.
* **Toolkits:** Collections of general-purpose classes (e.g., C++ I/O stream, collection libraries). Toolkits focus on *code reuse* and do not impose an architecture.
* **Frameworks:** Cooperating classes forming a reusable design for a specific domain (e.g., graphical editors, financial simulators). Applications are built by subclassing framework classes. Frameworks implement *design reuse* and feature **inversion of control** (the framework calls the application code, not vice versa).

##### Differences between Design Patterns and Frameworks:
1. **Abstraction:** Design patterns are more abstract; they cannot be directly executed in code, whereas frameworks are concrete implementations.
2. **Scale:** Frameworks are larger; a single framework typically contains multiple design patterns, but a pattern never contains a framework.
3. **Specialization:** Frameworks are domain-specific; design patterns can be applied across virtually any application domain.

---

## Chapter 2. A Case Study: Designing a Document Editor

### 2.1 DOCUMENT STRUCTURE (DESIGN PROBLEM 1)
The first design problem in Lexi is the internal representation of the document. A document consists of text characters, shapes, lines, polygons, and images. While the user views a document in terms of physical substructures (such as columns, rows, tables, figures, pages, and margins), the editor must map these physical hierarchies to an internal data structure.

#### Design Goals:
- Maintain the document's physical structure (the nested arrangement of columns, lines, tables, pages, etc.).
- Render and visually present the document on the screen.
- Map screen coordinates to logical elements in the internal representation. This hit detection determines which element a user is pointing to or clicking on.

#### Constraints:
- **Uniformity of Text and Graphics:** Avoid treating graphics as special cases of text or text as special cases of graphics. Treating them separately leads to redundant layout, formatting, rendering, and interaction engines.
- **Single vs. Group Element Transparency:** Client code must not need to distinguish between single characters and complex groups of elements. The layout system should treat a complex diagram containing thousands of lines and shapes as a single unit, just as it would treat a single character, as long as it knows how to draw itself and specify its bounding dimensions.
- **Conflicting Analytical Requirements:** The representation must accommodate analytical operations (like spell-checking and hyphenation) that apply only to characters and text, not to graphics like polygons.

#### Solution: Recursive Composition & The Composite Pattern
- Lexi represents hierarchically structured documents by building complex components out of simpler ones recursively.
- A sequence of character and image glyphs is aggregated into rows. Multiple rows are grouped into columns. Columns are grouped into pages, and pages constitute the document.
- To implement this structure, an abstract base class `Glyph` is introduced. It provides a compatible interface for both leaf nodes (e.g., characters, images) and composite nodes (e.g., rows, columns, tables).

#### The Glyph Interface and Operations:
- **`Draw(Window* w)`**: Abstract rendering operation. Passed a reference to a `Window` object which encapsulates graphics primitives. For instance, a `Rectangle` subclass implements `Draw` by calling `w->DrawRect(_x0, _y0, _x1, _y1)` where `_x0, _y0, _x1, _y1` represent opposing corners.
- **`Bounds(Rect& r)`**: Returns the minimum bounding box enclosing the glyph. Composite glyphs (like rows) query their children's bounds to format and layout elements without overlapping them.
- **`Intersects(Point& p)`**: Checks if the given screen coordinate intersects the glyph's bounds, allowing Lexi to perform hit detection.
- **Composite Child Management Operations:**
  - `Insert(Glyph* g, int index)`: Adds a child glyph at a specified index.
  - `Remove(Glyph* g)`: Removes a child glyph.
  - `Child(int index)`: Retrieves a child glyph at a given index.
  - `Parent()`: Returns a pointer to the parent glyph.

#### Mechanics of the Composite Pattern in Lexi:
- The `Glyph` base class represents the Component interface.
- Leaf classes (such as `Character`, `Image`, `Rectangle`, `Polygon`) represent primitive objects that cannot have children. They implement rendering and layout query operations but define child operations to do nothing or return default values.
- Composite classes (such as `Row`, `Column`, `Table`, `Page`) represent nodes containing child glyphs. They implement the child management operations and override rendering operations to iterate through their child list, calling `Draw` on each child.

### 2.2 FORMATTING (DESIGN PROBLEM 2)
Having defined how to represent the physical structure, Lexi must construct specific layouts. "Formatting" is defined as breaking a collection of glyphs into lines, columns, and pages.

#### Design Goals:
- Format text and graphics into rows, columns, and pages.
- Support diverse formatting policies (margins, line-spacing, justifications, tabs).

#### Constraints:
- **Performance vs. Quality Trade-offs:** WYSIWYG editing requires high responsiveness. Simple line-breaking algorithms are fast but yield uneven margins and "loose" lines. High-quality typesetting (such as the Knuth-Plass global optimization algorithm used in TeX) yields balanced whitespace but requires more processing and memory.
- **Decoupling Algorithms from Structures:** The physical layout logic must be separated from the document representation. Changing formatting algorithms must not affect `Glyph` implementations, and adding new `Glyph` subclasses (e.g. math symbols) must not require rewriting the formatting engine.

#### Encapsulating Formatting & The Strategy Pattern:
- The solution is to separate the formatting algorithm from the document structure by encapsulating it in a strategy object.
- The `Composition` class (a subclass of `Glyph`) represents the context. It contains a sequence of unformatted content glyphs (leaf elements like characters and images) without formatting structure.
- The `Compositor` abstract class represents the Strategy. It defines the interface for line-breaking. Concrete subclasses implement specific line-breaking algorithms.

#### The Compositor Interface and Subclasses:
- **`Compositor::Compose(Composition* context)`**: Triggers the formatting process. The compositor iterates through the content glyphs of the `Composition` object, calculates line boundaries, creates structural composite glyphs (such as `Row` and `Column` instances), and inserts the content glyphs as children of these structural glyphs.
- **Concrete Subclasses:**
  - `SimpleCompositor`: Implements a fast, single-pass line-breaking algorithm that breaks lines at margins on a character-by-character basis.
  - `TeXCompositor`: Implements Knuth's line-breaking algorithm, which evaluates a paragraph globally to optimize the distribution of whitespace (minimizing badness and rivers of white space).
  - `ArrayCompositor`: Formats glyphs into fixed-size grid matrices (e.g., for tables).

#### Dynamic Formatting Control:
- The `Composition` object contains a pointer to a `Compositor` object. By calling `Composition::SetCompositor(Compositor*)` at runtime, the application can switch formatting engines dynamically (e.g., switching to `SimpleCompositor` during rapid typing, and switching to `TeXCompositor` when the document is idle or ready for printing).

### 2.3 EMBELLISHING THE USER INTERFACE (DESIGN PROBLEM 3)
Lexi needs visual additions like borders, drop shadows, and scroll bars surrounding the main document editing view.

#### Design Goals:
- Wrap the document editing area with visual embellishments, such as borders, drop shadows, and scroll bars.
- Users must be able to add or remove these embellishments easily (including at runtime).

#### Constraints:
- **Subclass Explosion:** Using standard inheritance to add features like borders or scrolling to `Composition` causes a combinatorial explosion of subclasses: `BorderedComposition`, `ScrollableComposition`, `BorderedScrollableComposition`, etc. Adding new kinds of borders or scroll controls multiplies the classes, creating a maintenance nightmare.
- **Client Ignorance:** Other user interface elements (like layout managers or parents) must remain completely unaware of the presence of these embellishments, treating embellished components exactly like standard components.

#### Transparent Enclosure & The Decorator Pattern:
- Transparent enclosure solves this by using object composition combined with interface compatibility.
- We create an enclosure class that wraps a single component. The enclosure implements the same interface as the component. Clients make calls on the enclosure, which delegates them to the component. The enclosure can execute additional behavior before or after delegation.

#### The MonoGlyph Class and Embellishment Subclasses:
- **`MonoGlyph`**: An abstract subclass of `Glyph`. It acts as the decorator base class. It stores a pointer to a single child `Glyph` (`_component`). By default, it implements all `Glyph` operations (like `Draw`, `Bounds`, `Intersects`) by forwarding them directly to `_component`.
- **`Border`**: A subclass of `MonoGlyph`. It overrides `Draw` to first call `MonoGlyph::Draw(w)` (rendering the wrapped content) and then call a private helper `DrawBorder(w)` to draw a boundary outline. It overrides `Bounds` to extend the inner component's bounding box by the width of the border.
- **`Scroller`**: A subclass of `MonoGlyph`. It adds scroll bars and coordinates layout positions. It overrides `Draw` to set a clipping region in the graphics subsystem before calling `MonoGlyph::Draw(w)`, preventing text that is scrolled out of bounds from rendering on screen.

#### Dynamically Nesting Decorators:
- Because `Border` and `Scroller` inherit from `Glyph`, they can wrap any other glyph. To create a bordered, scrollable document area, the application instantiates a `Composition`, wraps it inside a `Scroller`, and wraps that `Scroller` inside a `Border`. The client interacts with the outer `Border` object as a generic `Glyph`. The order of decoration can be swapped at runtime to test different layout combinations.

### 2.4 SUPPORTING MULTIPLE LOOK-AND-FEEL STANDARDS (DESIGN PROBLEM 4)
Lexi must adapt to multiple look-and-feel style guides (such as Motif, Presentation Manager (PM), Macintosh, Windows) to ensure usability across host systems.

#### Design Goals:
- Conform to multiple existing and future look-and-feel standards.
- Support style switching dynamically at runtime.

#### Constraints:
- **No Direct Constructors:** Lexi must avoid explicit constructor calls (e.g. `new MotifButton`) in the client code. Hard-coding widget instantiations creates tight coupling, making porting difficult and style switching impossible.
- **Consistency across Families:** A user interface style relies on consistent widgets. Mixing a Motif Scrollbar inside a Macintosh-themed window must be prevented.

#### Abstracting Object Creation & The Abstract Factory Pattern:
- Lexi achieves style independence by abstracting the creation of widget objects.
- We introduce a factory hierarchy that groups widget creation operations.

#### The GUIFactory and Product hierarchies:
- **`GUIFactory`**: An abstract base class defining factory methods: `CreateScrollBar()`, `CreateButton()`, `CreateMenu()`, etc.
- **Concrete Factories:**
  - `MotifFactory`: Overrides factory methods to return Motif-compliant widget instances.
  - `PMFactory`: Overrides factory methods to return PM-compliant widget instances.
- **Abstract Products:** Widget classes are structured under abstract interfaces that extend the `Glyph` class: `ScrollBar`, `Button`, `Menu`.
- **Concrete Products:** Platform-specific classes that implement the look and feel: `MotifScrollBar`, `PMScrollBar`, `MotifButton`, `PMButton`.

#### Client Configuration and Runtime Swapping:
- The client editor code creates widgets using a global or static factory pointer `guiFactory` (type `GUIFactory*`).
- To instantiate a button, the code calls `guiFactory->CreateButton()`.
- At startup, the system initializes `guiFactory` based on configurations (e.g., if Motif is selected: `guiFactory = new MotifFactory;`). The rest of the application remains decoupled from specific widget classes.

### 2.5 SUPPORTING MULTIPLE WINDOW SYSTEMS (DESIGN PROBLEM 5)
Different look-and-feel standards are usually implemented on top of different host windowing systems (such as X Windows, Win32, PM, Mac OS). Lexi's core editing code must run on these systems without modification.

#### Design Goals:
- Operate on diverse underlying window platforms.
- Shield the core application logic from platform-specific APIs.

#### Constraints:
- **Incompatible Vendor Class Libraries:** Unlike widgets, which Lexi defines, window system APIs are external and don't share a common interface or root class.
- **Impossible Re-implementation:** Implementing a custom window manager is not feasible; Lexi must use the host system's native window API.
- **Subclass Explosion and Maintenance:** Subclassing each window type (e.g., `ApplicationWindow`, `IconWindow`, `DialogWindow`) for every platform (`X11ApplicationWindow`, `PMApplicationWindow`) creates duplicate hierarchies and limits run-time flexibility.

#### Encapsulating Window Implementations & The Bridge Pattern:
- The Bridge pattern separates the logical window concepts (used by developers) from the window system implementations (which interface with the OS) into independent hierarchies.

#### The Abstraction and Implementation Hierarchies:
- **Logical Abstraction (`Window` hierarchy)**:
  - `Window` is the abstract base class for client-facing windows. It provides operations like `DrawRect()`, `Resize()`, `Iconify()`.
  - Concrete subclasses reflect window functions: `ApplicationWindow` (adds menus/toolbars), `IconWindow` (renders document icons), `DialogWindow` (manages prompt input).
- **Implementation (`WindowImp` hierarchy)**:
  - `WindowImp` is the abstract base class for window system-dependent code. It provides low-level graphics functions: `DeviceRect()`, `DeviceLine()`, `DeviceText()`.
  - Subclasses wrap platform window APIs: `XWindowImp` (translates `DeviceRect` to `XDrawRectangle` calls), `PMWindowImp` (translates to PM path creation APIs).

#### Abstractions Delegating to Implementations:
- The `Window` class holds a reference to a `WindowImp` instance (`_imp`).
- When Lexi calls `Window::DrawRect(x0, y0, x1, y1)`, the method delegates the task to the implementation: `_imp->DeviceRect(x0, y0, x1, y1)`.
- The `Window` abstraction constructor initializes `_imp` using a `WindowSystemFactory` (an abstract factory that maps to `XWindowSystemFactory` or `PMWindowSystemFactory`).

### 2.6 USER OPERATIONS (DESIGN PROBLEM 6)
Lexi must execute operations (New, Open, Save, Print, Cut, Paste, style modifications) triggered by various UI widgets (menus, buttons, keyboard shortcuts).

#### Design Goals:
- Support user commands.
- Support execution of commands through different user interfaces (menu items, buttons, keyboard shortcuts).
- Support multi-level, arbitrary-depth Undo and Redo operations.

#### Constraints:
- **Decoupling Widgets from Implementations:** MenuItem and Button classes must not hard-code target functionality. This prevents class explosion and allows reusing commands across different triggers.
- **Undo State Management:** Commands must capture and store the document's state before execution. Only document-modifying commands (e.g., Delete, Format) should participate in the undo history; actions like Print or Quit should not.

#### Encapsulating Requests & The Command Pattern:
- The Command pattern addresses these issues by encapsulating requests as objects.

#### The Command Hierarchy and MenuItem Integration:
- **`Command`**: An abstract base class defining the command interface.
  - `Execute()`: Runs the request behavior.
  - `Unexecute()`: Reverses the actions performed by `Execute()`.
  - `Reversible()`: Returns a Boolean indicating if the command can be undone.
- **Concrete Subclasses:**
  - `PasteCommand`: Modifies document text. In `Execute()`, it inserts clipboard content and saves insertion location. In `Unexecute()`, it deletes inserted text.
  - `FontCommand`: Modifies text styles. `Execute()` applies a new font to a selection and caches previous styles. `Unexecute()` reapplies cached styles.
  - `OpenCommand`: Prompts for file name, creates a new document, and opens it.
- **Widget Integration**:
  - `MenuItem` contains a pointer to a `Command` object. When selected, the menu item calls `Execute()` on its command pointer.

#### Command History Mechanics (Undo/Redo):
- The application maintains a command history list of executed commands.
- A "present" cursor points to the last executed command.
- **Undo**: When the user triggers Undo, the system calls `Unexecute()` on the command at the "present" cursor and moves the cursor one step to the left.
- **Redo**: When the user triggers Redo, the system moves the cursor one step to the right and calls `Execute()` on that command.

### 2.7 SPELLING CHECKING AND HYPHENATION (DESIGN PROBLEM 7)
Lexi needs analytical capabilities to check for misspellings and insert hyphenation points for line formatting.

#### Design Goals:
- Support textual analyses like spell-checking, hyphenation, and word counts.
- Allow adding new analyses easily without modifying the `Glyph` classes.

#### Constraints:
- **Hiding Storage Layouts:** The layout representation must hide whether children are stored in arrays, lists, or trees.
- **Multiple Traversal Orders:** System must support traversing glyph structures in preorder, postorder, or inorder, sometimes skipping non-textual nodes.
- **Avoiding Type Downcasts:** The analyzer must distinguish between glyph types (e.g. `Character` vs. `Polygon`) without using unsafe type-checking.
- **Stable Glyph Interface:** Adding new analyses must not bloat the `Glyph` base class with new analytical methods.

#### Decoupling Traversal & The Iterator Pattern:
- The Iterator pattern encapsulates the traversal algorithm in a separate iterator object, decoupling it from the glyph container.
- **`Iterator`**: Abstract base class defining traversal control (`First()`, `Next()`, `IsDone()`, `CurrentItem()`).
- **Subclasses**:
  - `ListIterator` & `ArrayIterator`: Wrap list and array structures.
  - `NullIterator`: Returned by leaf glyphs. Its `IsDone()` always returns true.
  - `PreorderIterator`: Traverses a composite tree structure recursively using a stack to keep track of iterators.
- **Glyph Integration**: `Glyph` declares `CreateIterator()`. Composite classes override it to return list/array iterators, while leaf classes return `NullIterator`.

#### Decoupling Analysis Actions & The Visitor Pattern:
- The Visitor pattern separates the traversal from the actions performed on the nodes.
- **Double Dispatch Mechanics:**
  - The `Glyph` base class declares `Accept(Visitor&)`.
  - Every subclass overrides `Accept` to call back the visitor: `void Character::Accept(Visitor& v) { v.VisitCharacter(this); }`.
  - When the client traverses glyphs and calls `glyph->Accept(visitor)`, the system resolves the concrete glyph type and invokes the matching visitor method (e.g., `VisitCharacter` or `VisitPolygon`).
- **The Visitor Hierarchy**:
  - `Visitor` declares abstract methods for each glyph subclass: `VisitCharacter(Character*)`, `VisitRow(Row*)`, etc.
  - `SpellingCheckingVisitor`: Accumulates text from character nodes into a word buffer. On non-alphabetic boundaries, it checks the spelling and stores misspellings.
  - `HyphenationVisitor`: Assembles words, calculates hyphenation points, and inserts `Discretionary` glyphs.

#### The Discretionary Glyph:
- `Discretionary` is a subclass of `Glyph` inserted at hyphenation points.
- It checks its parent `Row` to determine if it is the last child.
- If it is at the end of a line, it renders as a hyphen; otherwise, it is invisible and takes up no space.

---

## Chapter 3: Creational Patterns

### I. INTRODUCTION TO CREATIONAL PATTERNS
Creational design patterns abstract the instantiation process, decoupling a system from how its constituent objects are created, composed, and represented. These patterns are divided into class-creational patterns, which utilize inheritance to vary the class that is instantiated, and object-creational patterns, which delegate the instantiation responsibilities to another object through composition.

#### A. The Shift from Inheritance to Composition
As software architectures evolve, they shift from rigid class inheritance hierarchies toward flexible object composition. Hardcoded instantiation binds code to concrete classes, making it difficult to introduce new behaviors or configurations. Creational patterns address this by defining a small set of fundamental behaviors that can be composed dynamically. They encapsulate all knowledge of concrete product classes and obscure the precise mechanics of object creation. As a result, the system interacts with products solely through their abstract interfaces, granting substantial flexibility in *what* is created, *who* creates it, *how* it is created, and *when*.

#### B. Relationships and Core Themes
Creational patterns frequently compete or complement one another. For instance, Prototype and Abstract Factory are often viable alternatives, whereas Builder can use other creational patterns to configure component instantiation, and Prototype can incorporate the Singleton pattern. The choice of pattern involves trade-offs between simplicity, subclass proliferation, runtime flexibility, and type safety.

### II. THE MAZE GAME COMMON RUNNING EXAMPLE
To illustrate and compare the creational patterns, a shared domain model—a maze game—is established. The core classes and their relations are defined as follows:

1. **MapSite (Abstract Base)**:
   - Represents any physical location or boundary in the maze.
   - Declares a single abstract operation: `virtual void Enter() = 0;`.
   - Behavioral semantics: Entering a room changes the player's location. Entering a door transfers the player to the adjoining room if open, or results in a collision ("hurting their nose") if closed.

2. **Direction (Enumeration)**:
   - Defines cardinal directions used for room boundaries: `enum Direction { North, South, East, West };`.

3. **Room (Concrete Subclass of MapSite)**:
   - Maintains a unique integer identifier: `_roomNumber`.
   - Stores four references to `MapSite` objects representing its north, south, east, and west boundaries: `MapSite* _sides[4]`.
   - Operations: `MapSite* GetSide(Direction) const;` and `void SetSide(Direction, MapSite*);`.

4. **Wall (Concrete Subclass of MapSite)**:
   - Represents a solid boundary that blocks movement.
   - Overrides `Enter()` to represent a collision.

5. **Door (Concrete Subclass of MapSite)**:
   - Connects two rooms: `Room* _room1;` and `Room* _room2;`.
   - Tracks its open/closed state: `bool _isOpen;`.
   - Operations: `Room* OtherSideFrom(Room*);` to determine the destination.

6. **Maze (Aggregate Container)**:
   - Represents a collection of rooms.
   - Operations: `void AddRoom(Room*);` and `Room* RoomNo(int) const;` to look up a room.

7. **MazeGame (Director/Client Context)**:
   - Contains the construction algorithm.
   - The naive, hardcoded implementation of `CreateMaze()` is highly inflexible because it directly instantiates concrete classes (`Maze`, `Room`, `Wall`, `Door`), locking layout and component types.

### III. DEEP PATTERN BREAKDOWNS

### 1. ABSTRACT FACTORY (Object Creational)
*   **Intent:** Provide an interface for creating families of related or dependent objects without specifying their concrete classes. It is also known as a **Kit**.
*   **Motivation:** In user interface toolkits supporting multiple look-and-feel standards (e.g., Motif and PM), widgets like scrollbars, windows, and buttons must exhibit coordinate behaviors and styles. Hardcoding look-and-feel-specific classes throughout client code prevents switching styles. By declaring an abstract `WidgetFactory` with operations for creating each widget type, clients retrieve widget instances through abstract interfaces, decoupling them from concrete implementation classes.
*   **Applicability:** Use when:
    *   The system must remain independent of how its products are created, composed, and represented.
    *   The system needs configuration with one of multiple product families.
    *   A family of related products must be used together, and this consistency constraint must be programmatically enforced.
    *   You want to distribute a class library of products, exposing only their interfaces rather than their implementations.
*   **Structure:**
    *   `AbstractFactory` defines widget instantiation operations.
    *   `ConcreteFactory` overrides operations to return platform-specific widgets.
    *   `AbstractProduct` represents abstract interfaces for widgets.
    *   `ConcreteProduct` implements platform-specific look and feel.
*   **Participants:** AbstractFactory, ConcreteFactory, AbstractProduct, ConcreteProduct, Client.
*   **Collaborations:**
    *   A single instance of a `ConcreteFactory` is typically instantiated at runtime.
    *   The `AbstractFactory` delegates product instantiation to its `ConcreteFactory` subclasses.
    *   To change product configurations, the client must be configured with a different `ConcreteFactory`.
*   **Consequences:**
    *   *Concrete Class Isolation:* Clients remain oblivious to concrete class names. The factory encapsulates the instantiation process, making product class names invisible.
    *   *Easy Product Family Exchange:* Exchanging the concrete factory class changes the entire product family at once. The system can switch look-and-feels or behaviors by instantiating a different factory.
    *   *Consistency Enforcement:* Prevents clients from mixing incompatible products (e.g., mixing Motif scrollbars with PM buttons).
    *   *Difficult Product Extension:* Supporting new product types requires updating the `AbstractFactory` interface, which cascades changes to all subclasses and client code.
*   **Implementation Mechanics:**
    1.  *Factories as Singletons:* Because an application typically requires only one factory instance per product family, concrete factories are best implemented as Singletons.
    2.  *Product Instantiation Methods:*
        - *Factory Method:* Simple but requires a new factory subclass for every product family, even for minor variations.
        - *Prototype-Based Factory:* The factory stores prototypical instances of products in a catalog and clones them to create new products. This eliminates the need for concrete factory subclasses.
        - *Class-Based Factory:* In dynamic languages (Smalltalk, Objective-C), factories can store the *class objects* of products in a registry. The factory instantiates products directly from these class objects, avoiding subclassing.
    3.  *Extensible Factories (Parameterized Creators):*
        - Instead of separate methods for each product type, the factory defines a single `Make(Identifier)` method.
        - This approach is highly flexible but reduces compile-time type safety. In statically typed languages like C++, all products must share a common base class or be coerced using `dynamic_cast`, which can fail at runtime.

### 2. BUILDER (Object Creational)
*   **Intent:** Separate the construction of a complex object from its representation so that the same construction process can create different representations.
*   **Motivation:** An RTF document reader must convert RTF into multiple target formats (e.g., ASCII text, TeX, or an interactive TextWidget). Adding new conversions should not require modifying the parsing algorithm. By routing parsed tokens through an abstract `TextConverter` interface, the reader (Director) is decoupled from the specific format construction (Builder). Each `TextConverter` subclass implements formatting logic independently.
*   **Applicability:** Use when:
    *   The algorithm for creating a complex object must be independent of its parts and how they are assembled.
    *   The construction process must allow different representations for the object under construction.
*   **Structure:**
    *   `Director` parses components and calls Builder operations.
    *   `Builder` declares interfaces for creating parts of a product.
    *   `ConcreteBuilder` implements creation interface and returns final product.
*   **Participants:** Builder, ConcreteBuilder, Director, Product.
*   **Collaborations:**
    *   The client instantiates a `ConcreteBuilder` and passes it to the `Director`.
    *   The `Director` notifies the builder step-by-step as it parses components.
    *   The builder handles assembly internally, appending parts to the product.
    *   The client retrieves the completed product from the `ConcreteBuilder`.
*   **Consequences:**
    *   *Internal Representation Encapsulation:* The director only interacts with an abstract builder interface. The concrete builder hides the internal structure and assembly details of the product.
    *   *Separation of Concerns:* Decouples parsing/assembly logic from the underlying representation. The same builder can be reused across different directors.
    *   *Fine-Grained Construction Control:* Unlike other creational patterns that construct objects in a single call, Builder operates step-by-step under the director's control. The product is retrieved only at the end.
*   **Implementation Mechanics:**
    1.  *Assembly Interface:* The Builder's interface must be generic enough to accommodate diverse target formats. Bottom-up construction is used for complex trees.
    2.  *Product Hierarchy:* Because products constructed by different builders can vary wildly (e.g., a plain string vs. a GUI widget), they rarely share a common abstract base class.
    3.  *Empty Default Methods:* The abstract Builder class should provide empty inline methods so subclasses only override the build steps they require.

### 3. FACTORY METHOD (Class Creational)
*   **Intent:** Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses. It is also known as a **Virtual Constructor**.
*   **Motivation:** An application framework manages documents using abstract classes like `Application` and `Document`. The framework is responsible for instantiating documents (e.g., when the user selects "New"), but it cannot predict which specific document subclass will be used by client applications. The framework resolves this by defining an abstract factory method `CreateDocument()` on `Application`. Subclasses of `Application` override this method to return the correct document subclass.
*   **Applicability:** Use when:
    *   A class cannot anticipate the concrete class of objects it must instantiate.
    *   A class wants its subclasses to specify the objects it creates.
    *   Classes delegate responsibility to one of several helper subclasses, and you want to localize the knowledge of which helper is the delegate.
*   **Structure:**
    *   `Creator` declares the factory method returning an abstract `Product`.
    *   `ConcreteCreator` overrides the factory method to return a `ConcreteProduct`.
*   **Participants:** Product, ConcreteProduct, Creator, ConcreteCreator.
*   **Collaborations:**
    *   The `Creator` relies on its subclasses to define the factory method, returning the appropriate `ConcreteProduct`.
*   **Consequences:**
    *   *Decoupling:* Eliminates the need to bind application-specific classes into client code. The creator interacts solely with the abstract Product interface.
    *   *Subclass Hooking:* Provides a hook for subclasses to extend or customize default objects.
    *   *Parallel Hierarchy Connection:* Localizes knowledge of which classes belong together when a class delegates part of its responsibilities to a helper class.
*   **Implementation Mechanics:**
    1.  *Abstract vs. Concrete Creator:* The creator can be an abstract class, forcing subclasses to implement the factory method, or concrete, providing a default implementation.
    2.  *Parameterized Factory Methods:* The factory method accepts an identifier specifying the product type.
    3.  *Lazy Initialization:* To avoid constructor issues, access products through accessors that instantiate the product on demand if it is null.

### 4. PROTOTYPE (Object Creational)
*   **Intent:** Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.
*   **Motivation:** A music score editor framework provides a `GraphicTool` for creating graphical elements (notes, staves). Subclassing `GraphicTool` for each musical note creates a bloated class hierarchy. Instead, `GraphicTool` can be initialized with a prototypical instance of a `Graphic` subclass (e.g., a quarter note). When the tool is activated, it clones its prototype and adds the copy to the document. This replaces subclassing with object composition.
*   **Applicability:** Use when:
    *   The system must remain independent of how its products are created, composed, and represented.
    *   The classes to instantiate are specified at runtime (e.g., via dynamic loading).
    *   You want to avoid building a factory class hierarchy that parallels the product class hierarchy.
    *   Instances of a class can have only a few different combinations of state, and cloning pre-configured prototypes is more convenient than manual instantiation.
*   **Structure:**
    *   `Prototype` declares a `Clone()` interface.
    *   `ConcretePrototype` implements `Clone()` by duplicating itself.
    *   `Client` requests the prototype to clone itself.
*   **Participants:** Prototype, ConcretePrototype, Client.
*   **Collaborations:** The client asks the prototype to clone itself.
*   **Consequences:**
    *   *Dynamic Registration:* Prototypes can be registered or unregistered at runtime.
    *   *Reduced Subclassing:* Eliminates parallel creator hierarchies.
    *   *State-Based Behavior:* Allows defining new "classes" by composing objects and assigning state values to prototypes.
    *   *Clone Implementation Liability:* Implementing `Clone()` can be difficult, particularly when handling circular references, pointer sharing, or classes that do not natively support copying.
*   **Implementation Mechanics:**
    1.  *Prototype Manager:* In dynamic systems, prototypes are managed using a registry (associative map) accessed by key at runtime.
    2.  *Deep vs. Shallow Copying:* Shallow copy shares pointers; deep copy clones all nested elements recursively.
    3.  *Clone Initialization:* Call a separate `Initialize(arguments)` method on the clone immediately after creation, or use setter operations.

### 5. SINGLETON (Object Creational)
*   **Intent:** Ensure a class only has one instance, and provide a global point of access to it.
*   **Motivation:** Certain system components must have exactly one instance (e.g., a printer spooler, a file system, or a window manager). Global variables provide global access but do not prevent multiple instantiations. A cleaner approach is to make the class itself responsible for tracking its sole instance, intercepting instantiation requests and returning the unique instance.
*   **Applicability:** Use when:
    *   There must be exactly one instance of a class, and it must be accessible to clients from a well-known access point.
    *   The sole instance should be extensible by subclassing, allowing clients to use an extended instance without code modification.
*   **Structure:**
    *   `Singleton` class declares a static `Instance()` method and protects its constructor.
*   **Participants:** Singleton.
*   **Collaborations:** Clients access the singleton instance exclusively through the class operation `Instance()`.
*   **Consequences:**
    *   *Controlled Access:* Strictly controls how and when clients interact with the instance.
    *   *Name Space Protection:* Replaces global variables, preventing name space pollution.
    *   *Subclass Refinement:* The singleton can be subclassed, and the application configured with the subclass instance at runtime.
    *   *Variable Instance Counts:* The instantiation logic can be modified to allow a specific number of instances (e.g., thread pools) by updating only the access operation.
*   **Implementation Mechanics:**
    1.  *Ensuring Uniqueness:* Constructor is protected/private; static `Instance()` manages lifecycle via lazy initialization.
    2.  *Issues with Static/Global Objects:* Automatic global initialization is problematic because it does not prevent multiple instantiations, lacks runtime parameters, has undefined initialization order, and forces instantiation even if unused.
    3.  *Registry of Singletons:* Subclasses register their name and instance in a registry. The base class looks up the desired name (e.g., from an environment variable) to retrieve the correct instance.

---

## Chapter 4: Structural Patterns

### 1. Architectural Overview of Structural Patterns
Structural patterns deal with how classes and objects are composed to form larger, more complex structures. They help ensure that if one part of a system changes, the entire structure does not need to change. These patterns are divided into two main categories:
1. **Class Structural Patterns**: Use inheritance to compose interfaces or implementations. An example is the class form of the Adapter pattern, which uses multiple inheritance to make one interface conform to another. This is a static composition established at compile-time.
2. **Object Structural Patterns**: Describe ways to compose objects to realize new, dynamic functionality. The primary advantage of object composition is the ability to change the composition at run-time, which is impossible with static class composition. Examples include Composite, Bridge, Decorator, Flyweight, Facade, and Proxy.

### 2. The Adapter Pattern (Wrapper)
*   **Intent**: Convert the interface of an existing class into another interface that clients expect. Adapter lets classes work together that could not otherwise due to incompatible interfaces.
*   **Also Known As**: Wrapper.
*   **Motivation**: Reusable toolkit classes (like a specialized text view) often cannot be reused directly because their interfaces do not match the domain-specific interfaces that an application requires. For example, a drawing editor defines a `Shape` abstract class with subclasses like `LineShape` and `PolygonShape`. Implementing a complex `TextShape` from scratch is difficult, but a toolkit already provides a sophisticated `TextView` class. An adapter subclass `TextShape` can inherit from `Shape` and wrap a `TextView` instance, converting shape-oriented requests (e.g., `BoundingBox`) into text-oriented requests (e.g., `GetExtent`).
*   **Applicability**:
  - You want to use an existing class, but its interface does not match the one you need.
  - You want to create a reusable class that cooperates with unrelated or unforeseen classes.
  - *(Object Adapter only)* You need to use several existing subclasses, but adapting their interface by subclassing every one is impractical.
*   **Structure**:
  - **Class Adapter**: Uses multiple inheritance. `Adapter` inherits publicly from the `Target` interface and privately from the `Adaptee` implementation.
  - **Object Adapter**: Uses object composition. `Adapter` inherits from the `Target` interface and maintains a reference to an `Adaptee` instance.
*   **Participants**: Target, Client, Adaptee, Adapter.
*   **Collaborations**: Clients call operations on an `Adapter` instance. The adapter in turn calls `Adaptee` operations to carry out the request.
*   **Consequences & Trade-offs**:
  - **Class Adapter**:
    - Commits to a concrete `Adaptee` class; it cannot adapt a class and all its subclasses.
    - Lets the `Adapter` override some of `Adaptee`'s behavior.
    - Introduces only one object (no pointer indirection to access the adaptee).
  - **Object Adapter**:
    - Allows a single `Adapter` to work with many `Adaptees`.
    - Makes it harder to override `Adaptee` behavior; it requires subclassing the `Adaptee` first.

### 3. The Bridge Pattern (Handle/Body)
*   **Intent**: Decouple an abstraction from its implementation so that the two can vary independently.
*   **Also Known As**: Handle/Body.
*   **Motivation**: When an abstraction can have several implementations, using inheritance binds them permanently. For instance, a portable `Window` abstraction should work on both the X Window System and Presentation Manager (PM). Subclassing `Window` to create `XWindow` and `PMWindow` creates issues:
  1. Extending the window abstraction (e.g., `IconWindow`, `TransientWindow`) requires implementing platform-specific versions of every new window type (e.g., `XIconWindow`, `PMIconWindow`).
  2. It couples client code to specific implementations, preventing portability.
  The Bridge pattern addresses this by putting window abstractions and platform-specific window implementations (`WindowImp` hierarchy) in separate class hierarchies.
*   **Applicability**:
  - You want to avoid a permanent binding between an abstraction and its implementation.
  - Both abstractions and implementations should be extensible by subclassing.
  - Changes in implementation should have no impact on clients (no recompilation).
  - (C++) You want to hide the representation of a class completely from clients.
  - You want to share an implementation among multiple objects.
*   **Structure**: An `Abstraction` class maintains a pointer to an `Implementor` instance. `RefinedAbstraction` extends the interface. `ConcreteImplementor` implements the `Implementor` primitives.
*   **Participants**: Abstraction, RefinedAbstraction, Implementor, ConcreteImplementor.
*   **Collaborations**: `Abstraction` forwards client requests to its `Implementor` object.
*   **Consequences**:
  - Decoupling of interface and implementation allows run-time configuration and runtime switching of implementations.
  - Eliminates compile-time dependencies (ensures binary compatibility).
  - Independent extensibility of both hierarchies.
  - Hidden implementation details (like sharing and reference counting).

### 4. The Composite Pattern
*   **Intent**: Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.
*   **Motivation**: Graphics applications let users build complex diagrams out of simple components (primitives like lines, text) and containers (pictures). A naive implementation treats primitives and containers differently, leading to complex client code with conditional type checking. The Composite pattern introduces an abstract base class (`Graphic`) that represents both primitives and containers. Primitives implement drawing operations directly, while containers (`Picture`) implement them by forwarding the calls to their children, allowing recursive composition.
*   **Applicability**:
  - You want to represent part-whole hierarchies of objects.
  - You want clients to be able to ignore the differences between compositions of objects and individual objects, treating all elements in the structure uniformly.
*   **Structure**: `Component` defines the common interface. `Leaf` represents primitives. `Composite` maintains a child list of components.
*   **Participants**: Component, Leaf, Composite, Client.
*   **Collaborations**: Clients interact through the `Component` interface. Leaves handle requests directly; composites forward requests to children.
*   **Consequences**:
  - Defines class hierarchies representing primitive and composite objects recursively.
  - Simplifies client code by avoiding type-conditional statements.
  - Makes it easy to add new components.
  - *Disadvantage*: Can make the design overly general, making it difficult to restrict component types inside a composite using the static type system.

### 5. The Decorator Pattern (Wrapper)
*   **Intent**: Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
*   **Also Known As**: Wrapper.
*   **Motivation**: Adding responsibilities to objects via inheritance is static and inflexible. Enclosing the component in another object—a decorator—is a more flexible alternative. The decorator conforms to the interface of the component it decorates, making it transparent to clients. It forwards requests to the component and performs additional actions (e.g., drawing a border or rendering scrollbars) before or after forwarding. Because of interface conformance, decorators can be nested recursively.
*   **Applicability**:
  - To add responsibilities to individual objects dynamically and transparently.
  - For responsibilities that can be withdrawn.
  - When extension by subclassing is impractical due to an explosion of subclasses, or when class definition is hidden.
*   **Structure**: `Decorator` inherits from `Component` and maintains a reference to a `Component` instance. `ConcreteDecorator` overrides methods to add responsibilities.
*   **Participants**: Component, ConcreteComponent, Decorator, ConcreteDecorator.
*   **Collaborations**: `Decorator` forwards requests to its `Component` object, optionally performing actions before/after.
*   **Consequences**:
  - More flexible than static inheritance (mix-and-match properties).
  - Avoids feature-laden classes high up in the hierarchy.
  - *Liability*: A decorated component is not identical to the component itself (breaks object identity tests).
  - *Liability*: Results in systems composed of "lots of little objects," making debugging difficult.

### 6. The Facade Pattern
*   **Intent**: Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
*   **Motivation**: Subsystem partitioning reduces complexity, but dependencies between subsystems can become complex. Introducing a facade object provides a single, simplified interface. For example, a compiler subsystem contains low-level classes (`Scanner`, `Parser`, `ProgramNodeBuilder`, `BytecodeStream`). Most clients do not need to deal with parser tokens or AST nodes; they just want to compile a source file. The `Compiler` class acts as a facade, providing a simple `Compile` interface that orchestrates the low-level classes.
*   **Applicability**:
  - You want to provide a simple interface to a complex subsystem.
  - There are many dependencies between clients and implementation classes. Decouple them using a facade.
  - You want to layer your subsystems, using facades as entry points.
*   **Structure**: Clients interact with the `Facade` class. The `Facade` delegates requests to internal subsystem classes.
*   **Participants**: Facade, Subsystem classes.
*   **Collaborations**: Clients send requests to the `Facade`, which translates them and forwards them to subsystem objects.
*   **Consequences**:
  - Shields clients from subsystem components, reducing the number of objects they interact with.
  - Promotes weak coupling, allowing subsystem components to vary without affecting clients.
  - Does not prevent power users from bypassing the facade to access low-level classes.

### 7. The Flyweight Pattern
*   **Intent**: Use sharing to support large numbers of fine-grained objects efficiently.
*   **Motivation**: A document editor could represent every character in a document as an object to promote formatting flexibility, but storing hundreds of thousands of character objects is prohibitively expensive. The Flyweight pattern addresses this by sharing objects. A flyweight is a shared object that can be used in multiple contexts simultaneously. State is divided into:
  1. **Intrinsic State**: Independent of context, stored within the flyweight, and sharable.
  2. **Extrinsic State**: Context-dependent, stored/computed externally, and passed to the flyweight during operation invocations.
*   **Applicability**: Use when:
  - An application uses a large number of objects.
  - Storage costs are high due to the quantity of objects.
  - Most object state can be made extrinsic.
  - Many groups of objects can be replaced by a few shared objects once extrinsic state is removed.
  - The application does not depend on object identity.
*   **Structure**: `FlyweightFactory` manages shared flyweights. `ConcreteFlyweight` stores intrinsic state. `UnsharedConcreteFlyweight` represents composite elements containing flyweights.
*   **Participants**: Flyweight, ConcreteFlyweight, UnsharedConcreteFlyweight, FlyweightFactory, Client.
*   **Collaborations**: Clients pass extrinsic state to flyweights during operation invocations. Clients must obtain flyweights exclusively from the factory.
*   **Consequences**:
  - Introduces run-time overhead for transferring/computing extrinsic state.
  - Generates major storage savings by reducing instance count.
  - *Composite Integration*: Combined with Composite to represent trees as directed-acyclic graphs with shared leaves (which cannot store parent pointers).

### 8. The Proxy Pattern (Surrogate)
*   **Intent**: Provide a surrogate or placeholder for another object to control access to it.
*   **Also Known As**: Surrogate.
*   **Motivation**: Controlling access to a heavyweight object allows deferring the cost of its creation and initialization. For example, opening a text document with large raster images should be fast. Images should be loaded on demand. An image proxy acts as a stand-in for the real image. It conforms to the same interface (`Graphic`) and caches the image's bounding box extent so the formatter can lay out the document without instantiating the real image. The proxy instantiates the real image and forwards requests only when `Draw` is called.
*   **Applicability**:
  1. **Remote Proxy (Ambassador)**: Local representative for an object in a different address space.
  2. **Virtual Proxy**: Creates expensive objects on demand.
  3. **Protection Proxy**: Controls access rights.
  4. **Smart Reference (Smart Pointer)**: Replaces bare pointers to perform housekeeping (reference counting, locking).
*   **Structure**: `Proxy` maintains a reference to `RealSubject` and conforms to the `Subject` interface.
*   **Participants**: Proxy, Subject, RealSubject.
*   **Collaborations**: `Proxy` forwards requests to `RealSubject` when appropriate.
*   **Consequences**:
  - Indirection enables remote communication hiding, demand loading optimization, and access control.
  - *Copy-on-Write*: Copying a large object is deferred. The real object is copied only when a client attempts to modify it.

---

## Chapter 5: Behavioral Patterns

### SECTION 1: Introduction to Behavioral Patterns
Behavioral design patterns are concerned with algorithms and the assignment of responsibilities between objects. Unlike creational or structural patterns, behavioral patterns focus on patterns of communication and the complex, dynamic control flow that occurs at run-time. These control flows are often difficult to trace statically; by encapsulating these behaviors within objects and decoupling their interactions, behavioral patterns shift the focus from execution flow control to object interconnection and topological design.

Behavioral patterns are categorized into two primary forms:
1. **Behavioral Class Patterns**: These patterns use class inheritance to distribute behavior:
   - **Template Method**: Defines the invariant skeleton of an algorithm in a parent class, delegating variant primitive steps to subclasses.
   - **Interpreter**: Represents a grammar of a language as a class hierarchy, representing sentences as abstract syntax trees (ASTs).
2. **Behavioral Object Patterns**: These patterns leverage object composition and delegation rather than inheritance to distribute responsibilities. They describe how peer groups of objects cooperate to execute tasks that no single object can manage alone.

### SECTION 2: Comprehensive Breakdown of Behavioral Patterns

### 1. Chain of Responsibility (Object Behavioral)
*   **Intent**: Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.
*   **Motivation**: In context-sensitive help systems, a user interface widget (like a "Print" button inside a print dialog box) needs to show help. If the button has no help topic defined, the request must flow up to the Dialog Box. If the Dialog Box has no help, it flows up to the Application object. Decoupling the sender (the click handler) from the receiver (the object containing the help content) is achieved by passing the request along an implicit chain. The sender has no explicit knowledge of which object handles the request (an "implicit receiver").
*   **Applicability**:
    *   More than one object may handle a request, and the actual handler is not known a priori but must be determined automatically at runtime.
    *   You want to issue a request to one of several objects without specifying the receiver explicitly.
    *   The set of candidate objects that can handle a request should be specified dynamically.
*   **Structure:** `Client` calls a handler on a chain of `Handlers` (`ConcreteHandler1`, `ConcreteHandler2`), which hold a reference to their `successor`.
*   **Participants**: Handler, ConcreteHandler, Client.
*   **Collaborations**: When a client issues a request, the request propagates along the chain of ConcreteHandlers until an object takes responsibility for handling it.
*   **Consequences**:
    *   *Reduced Coupling:* Senders and receivers remain completely decoupled. Objects only keep a single reference to their successor.
    *   *Flexibility in Assigning Responsibilities:* You can dynamically add, remove, or reorder handlers in the chain at runtime.
    *   *No Guarantee of Receipt:* A request can fall off the end of the chain if no handler is configured to catch it.
*   **Implementation Details**:
    *   *Successor Chain Representation:* Can use existing links in a part-whole hierarchy (e.g., parent pointers in a composite widget tree).
    *   *Request Representation:* Can use hard-coded operations (e.g., `HandleHelp()`), request codes with a single handler dispatcher, or encapsulate requests as Request Objects containing parameters.

### 2. Command (Object Behavioral)
*   **Intent**: Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.
*   **Also Known As**: Action, Transaction.
*   **Motivation**: User interface toolkits provide buttons and menus that trigger actions when clicked. However, the toolkit design cannot hard-wire the action directly into the button class since only the application developer knows what should happen. The Command pattern solves this by wrapping the request itself inside an object (a `Command`). The button (the invoker) only needs to know how to call `Execute()` on the command interface. Concrete subclasses of Command store a reference to the receiver (e.g., a `Document` object) and call specific methods on that receiver.
*   **Applicability**:
    *   Parameterize objects by an action to perform (commands are the object-oriented equivalent of callback functions).
    *   Specify, queue, and execute requests at different times.
    *   Support undo/redo operations.
    *   Support logging changes to persistent storage to recover state after a crash.
    *   Structure a system around high-level transactional operations built from primitive operations.
*   **Structure:** `Invoker` holds a pointer to an abstract `Command`. `ConcreteCommand` implements `Execute()` and holds a pointer to `Receiver`.
*   **Participants**: Command, ConcreteCommand, Client, Invoker, Receiver.
*   **Collaborations**:
    1.  The client instantiates a `ConcreteCommand` and configures it with a `Receiver`.
    2.  The invoker stores this command object.
    3.  The invoker triggers the command by calling `Execute()`.
    4.  The `ConcreteCommand` calls methods on the `Receiver` to execute the action.
*   **Consequences**:
    *   *Decouples Invoker and Receiver:* The object invoking the operation is isolated from the object performing the work.
    *   *First-Class Objects:* Commands can be manipulated, subclassed, passed as arguments, and composed.
    *   *Composite Commands:* Multiple commands can be chained into a single transaction (e.g., `MacroCommand`).
*   **Implementation Details**:
    *   *Undo/Redo State:* Commands must store the receiver, arguments, and original values of changed properties.
    *   *Avoiding Error Accumulation:* Repetitive undo/redo cycles can accumulate errors. Mementos are used to store exact snapshots.
    *   *C++ Templates:* For simple, non-undoable commands, templates can bind a receiver instance and member function pointer, avoiding class explosion.

### 3. Interpreter (Class Behavioral)
*   **Intent**: Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.
*   **Motivation**: If a specific type of problem occurs frequently, it can be modeled as sentences in a simple, structured language. An interpreter then solves instances of the problem by parsing and evaluating these sentences. For example, regular expressions represent a language of string patterns. Instead of building unique string-matching logic for each pattern, a system can represent a regular expression as an abstract syntax tree (AST) where each grammar rule is mapped to a class, and an `Interpret()` method evaluates input strings against the tree nodes.
*   **Applicability**:
    *   The grammar of the language is simple.
    *   Efficiency is not the primary concern.
*   **Structure:** `AbstractExpression` defines `Interpret(Context)`. `TerminalExpression` and `NonterminalExpression` implement this for grammar symbols and syntax structures.
*   **Participants**: AbstractExpression, TerminalExpression, NonterminalExpression, Context, Client.
*   **Collaborations**:
    1.  The client constructs the sentence as an AST.
    2.  The client invokes `Interpret(Context)`.
    3.  Each `NonterminalExpression` defines its `Interpret` method in terms of recursive calls on subexpressions.
    4.  The `Interpret` methods use the shared `Context` to store and access state.
*   **Consequences**:
    *   *Extending the Grammar is Easy:* Grammar rules are represented by classes.
    *   *Simple Implementation:* Node classes share similar, clean structures that are easy to code.
    *   *Maintenance Overhead for Complex Grammars:* A grammar with many rules requires at least one class per rule, leading to class explosion.

### 4. Iterator (Object Behavioral)
*   **Intent**: Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
*   **Also Known As**: Cursor.
*   **Motivation**: An aggregate structure (like a list) must allow clients to traverse its elements. However, adding different traversal methods directly to the List interface bloats the class. Furthermore, supporting multiple concurrent traversals requires separating the traversal state from the aggregate container. The Iterator pattern solves this by moving traversal logic and state tracking into a dedicated `Iterator` object. Generalizing both lists and iterators via abstract base classes enables polymorphic iteration.
*   **Applicability**:
    *   Access the contents of an aggregate object without exposing its internal data structures.
    *   Support multiple concurrent traversals over the same aggregate.
    *   Provide a uniform, polymorphic interface for traversing different aggregate structures.
*   **Structure:** `Aggregate` defines `CreateIterator()`. `Iterator` defines traversal operations (`First()`, `Next()`, `IsDone()`, `CurrentItem()`). `ConcreteIterator` implements these for `ConcreteAggregate`.
*   **Participants**: Iterator, ConcreteIterator, Aggregate, ConcreteAggregate.
*   **Collaborations**: A `ConcreteIterator` maintains the traversal state (such as the current index) and accesses the `ConcreteAggregate` to retrieve elements and calculate the next item.
*   **Consequences**:
    *   *Supports Traversal Variations:* Different iteration algorithms can be swapped in simply by instantiating different ConcreteIterator classes.
    *   *Simplifies the Aggregate Interface:* The container does not need to declare traversal methods.
    *   *Concurrent Traversals:* A client can maintain multiple active iterations over a single aggregate without interference.
*   **Implementation Details**:
    *   *Iteration Control:* External iterators leave loop control to clients. Internal iterators loop automatically, applying a passed callback to every element.
    *   *Robustness:* Modifying an aggregate during traversal can cause errors. Robust iterators register with the aggregate to automatically update indexes when elements are added or deleted.
    *   *C++ Memory Management:* Stack-allocated proxy classes (`IteratorPtr`) wrap heap-allocated iterators to ensure deletion.

### 5. Mediator (Object Behavioral)
*   **Intent**: Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.
*   **Motivation**: In complex graphical user interfaces (e.g., font dialogs), widgets have intricate dependencies. Selecting an item in a list box updates an entry field, which then enables button options. Having widgets directly reference and call each other creates a highly coupled, monolithic grid of dependencies. Reusing a widget class becomes impossible because it is tied to specific peer classes. A Mediator object (`DialogDirector`) coordinates interaction. Widgets only reference their director, which acts as a central hub.
*   **Applicability**:
    *   A set of objects communicate in well-defined but highly complex ways, creating unstructured, tangled dependencies.
    *   Reusing an object is difficult because it refers to and communicates with many other objects.
    *   A behavior distributed across several classes should be customizable without extensive subclassing.
*   **Structure:** `Mediator` defines change notifications. `Colleague` objects maintain a reference to `Mediator` and communicate through it instead of referencing each other.
*   **Participants**: Mediator, ConcreteMediator, Colleague classes.
*   **Collaborations**: Colleagues send notifications of changes to the Mediator. The Mediator receives these notifications and propagates the appropriate updates to the other colleagues.
*   **Consequences**:
    *   *Limits Subclassing:* Centralizing coordination logic in the Mediator means only the Mediator needs subclassing to alter system behavior.
    *   *Decouples Colleagues:* Colleagues are independent.
    *   *Centralized Monolithic Risk:* The mediator can grow into a massive, complex, and unmaintainable monolith ("god object").

### 6. Memento (Object Behavioral)
*   **Intent**: Without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later.
*   **Also Known As**: Token.
*   **Motivation**: Checkpoint and undo mechanisms require recording the internal state of an object. However, simply exposing internal attributes via public accessors violates object encapsulation, exposing private implementation details. The Memento pattern solves this by introducing a passive `Memento` object. The `Originator` creates the memento, initializing it with its current state. The `Caretaker` holds the memento but cannot see inside it (it has a narrow interface to the caretaker). When restoring, the caretaker passes the memento back to the originator, which unpacks the data using its wide interface.
*   **Applicability**:
    *   A snapshot of an object's state must be saved so that it can be restored to that exact state later.
    *   A direct interface to obtain the state would expose implementation details and break the object's encapsulation.
*   **Structure:** `Originator` creates `Memento` and restores from it. `Caretaker` manages mementos but cannot view or modify their contents.
*   **Participants**: Memento, Originator, Caretaker.
*   **Collaborations**: Caretaker requests mementos from Originator, stores them, and passes them back to trigger state restoration.
*   **Consequences**:
    *   *Preserves Encapsulation:* Caretakers cannot access the originator's internal fields.
    *   *Simplifies Originator:* Frees the originator from managing the storage of previous states.
    *   *Potential Performance Costs:* Copying large amounts of state into mementos can introduce substantial memory and CPU overhead.
*   **Implementation Details**:
    *   *Static Protection:* In C++, the wide interface is kept private on the Memento, and the Originator is declared a `friend` of the Memento class. The public interface is empty.

### 7. Observer (Object Behavioral)
*   **Intent**: Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
*   **Also Known As**: Dependents, Publish-Subscribe.
*   **Motivation**: When partitioning a system into collaborating classes, you must maintain consistency without creating tight coupling. For example, a graphical spreadsheet and a bar chart both display the same underlying database object. When the database updates, both views must change immediately. The spreadsheet and chart do not need to know about each other, but they must be notified when the data changes. The database (the Subject) publishes notifications, and the views (the Observers) subscribe to them.
*   **Applicability**:
    *   An abstraction has two aspects, one dependent on the other. Encapsulating these aspects in separate objects lets you vary and reuse them independently.
    *   A change to one object requires changing others, and you do not know how many objects need to change.
    *   An object must be able to notify other objects without making assumptions about their concrete class types.
*   **Structure:** `Subject` manages dynamic observers. `Observer` defines `Update()`. `ConcreteObserver` queries `ConcreteSubject` for state synchronization upon notification.
*   **Participants**: Subject, Observer, ConcreteSubject, ConcreteObserver.
*   **Collaborations**:
    1.  `ConcreteSubject` triggers `Notify()` when its state changes.
    2.  `Notify()` loops through the attached observers, calling `Update()` on each.
    3.  `ConcreteObserver` queries the `ConcreteSubject` using its public accessors to synchronize state.
*   **Consequences**:
    *   *Abstract Coupling:* The subject only knows that it has a list of objects conforming to the simple `Observer` interface.
    *   *Broadcast Communication:* Notifications are automatically broadcast to all subscribers.
    *   *Unexpected Updates:* Because observers are blind to each other, a small change can trigger cascading updates.
*   **Implementation Details**:
    *   *Self-Consistency Before Notification:* Observers query the subject during `Update()`. If the subject is not fully consistent when `Notify()` runs, observers read stale state. Call `Notify()` from within a base-class template method after all subclass mutation steps finish.
    *   *Push vs. Pull Models:* Push sends detailed change info; Pull sends a minimal notification and let observers query.

### 8. State (Object Behavioral)
*   **Intent**: Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
*   **Also Known As**: Objects for States.
*   **Motivation**: A network connection class (`TCPConnection`) can be in several states: Established, Listening, Closed. The connection responds differently depending on this state (e.g., calling `Open()` in the Closed state opens a socket, while calling it in Established is an error). Instead of using massive conditional blocks in every method, the State pattern introduces a `TCPState` base class. Subclasses like `TCPEstablished` and `TCPClosed` implement state-specific behaviors. The `TCPConnection` delegates all state-specific operations to a current state object, which is swapped dynamically.
*   **Applicability**:
    *   An object's behavior depends on its state, and it must change its behavior at runtime depending on that state.
    *   Operations have large, multipart conditional statements that depend on the object's state (typically represented by enumerated constants).
*   **Structure:** `Context` delegates state-specific requests to a `State` object pointer, which is swapped dynamically with different `ConcreteState` subclasses.
*   **Participants**: Context, State, ConcreteState subclasses.
*   **Collaborations**:
    1.  `Context` delegates state-specific requests to its current `ConcreteState` object.
    2.  `Context` passes itself as an argument to the State object, allowing the State to access context data or trigger state changes.
*   **Consequences**:
    *   *Localizes State Behavior:* State-specific logic is isolated within individual classes.
    *   *Explicit Transitions:* Replaces implicit state transitions (mutating data variables) with atomic transitions (changing a single state object reference), preventing inconsistencies.
    *   *State Sharing:* If state objects have no instance variables, contexts can share them as Flyweights.

### 9. Strategy (Object Behavioral)
*   **Intent**: Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
*   **Also Known As**: Policy.
*   **Motivation**: Line-breaking algorithms process streams of text. Hard-wiring all these variations into a text-formatting client class is undesirable: it complicates the client, makes it unnecessarily large, and makes adding new algorithms difficult. The Strategy pattern extracts these algorithms into separate subclasses of a `Compositor` base class. The client (`Composition`) retains a reference to a `Compositor` object and delegates formatting to it.
*   **Applicability**:
    *   Many related classes differ only in their execution behavior.
    *   You need different variants of an algorithm (e.g., space vs. time optimizations).
    *   An algorithm uses internal data structures that should remain hidden from clients.
    *   A class defines many behaviors that appear as complex conditional blocks.
*   **Structure:** `Context` maintains reference to abstract `Strategy` and delegates operations. `ConcreteStrategy` implements the algorithm.
*   **Participants**: Strategy, ConcreteStrategy, Context.
*   **Collaborations**:
    1.  The Strategy and Context interact. Data is passed as parameters, or the Context passes a reference to itself.
    2.  The Context forwards client requests to the Strategy.
*   **Consequences**:
    *   *Families of Algorithms:* Defines reuse-friendly hierarchies of algorithms.
    *   *Alternative to Subclassing:* Decouples algorithmic logic from the Context, avoiding subclassing Context directly and making it easy to swap algorithms at runtime.
    *   *Eliminates Conditionals:* Replaces massive conditional blocks with polymorphism.
    *   *Client Awareness:* Clients must understand how strategies differ to choose the right one, exposing implementation details.

### 10. Template Method (Class Behavioral)
*   **Intent**: Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
*   **Motivation**: Application frameworks must coordinate opening document files. The basic steps are invariant: check if the file can open, create a document instance, add it to the application, and read the file contents. However, creating the document object and reading its content are application-specific actions. The base `Application` class defines the sequence of these steps in a non-virtual template method (`OpenDocument`). Subclasses override virtual hook and abstract methods (like `DoCreateDocument` or `CanOpenDocument`) to inject specific behaviors into the fixed execution sequence.
*   **Applicability**:
    *   Implement the invariant portions of an algorithm once, leaving variant steps to subclasses.
    *   Factor and localize common behaviors among subclasses to prevent code duplication.
    *   Control subclass extensions by defining hooks at specific execution points.
*   **Structure:** `AbstractClass` defines a non-virtual `TemplateMethod()` which calls virtual `PrimitiveOperation1()` and `PrimitiveOperation2()`.
*   **Participants**: AbstractClass, ConcreteClass.
*   **Collaborations**: The `ConcreteClass` relies on the `AbstractClass` to execute the structural skeleton of the algorithm.
*   **Consequences**:
    *   *Code Reuse:* Centralizes common logic in the base class.
    *   *Inverted Control Flow:* The parent class calls subclass methods rather than the subclass invoking parent behavior (the "Hollywood principle": "Don't call us, we'll call you").
    *   *Hook vs. Abstract Distinction:* Essential to distinguish between hook operations (which provide default behavior that subclasses *may* override) and abstract operations (which subclasses *must* override).
*   **Implementation Details**:
    *   *C++ Access Control:* Template methods themselves should be non-virtual (to prevent subclasses from altering the skeleton structure) and can be public. Primitive operations called by the template method can be declared protected to prevent external access. Operations that must be overridden are declared as pure virtuals.

### 11. Visitor (Object Behavioral)
*   **Intent**: Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.
*   **Motivation**: Compilers represent source code as abstract syntax trees (ASTs) containing nodes like `AssignmentNode`, `VariableRefNode`, etc. Multiple operations (type-checking, code generation, pretty-printing) must process these nodes. Spreading this logic across all node classes pollutes them with unrelated dependencies and makes the codebase hard to maintain. Adding a new compiler phase requires modifying and recompiling all node classes. The Visitor pattern extracts these operations. An abstract `NodeVisitor` defines a visit method for each node type. Nodes implement an `Accept(NodeVisitor*)` method that calls the matching visitor method, implementing run-time double dispatch.
*   **Applicability**:
    *   An object structure contains many classes with different interfaces, and you need to perform operations that depend on their concrete classes.
    *   Many distinct, unrelated operations must run across a structured hierarchy of objects, and you want to avoid polluting their classes.
    *   The classes defining the object structure rarely change, but you frequently add new operations over the structure.
*   **Structure:** `Element` defines `Accept(Visitor)`. `Visitor` defines `VisitConcreteElement(ConcreteElement)`.
*   **Participants**: Visitor, ConcreteVisitor, Element, ConcreteElement, ObjectStructure.
*   **Collaborations**: Each element calls the visitor method matching its class, passing itself as an argument. The visitor accesses the element's state to execute the operation.
*   **Consequences**:
    *   *Easy to Add Operations:* New operations are added by writing new Visitor subclasses without changing element classes.
    *   *Consolidates Related Logic:* Gathers related operations in a single class.
    *   *Adding Concrete Elements is Hard:* Adding a new Element subclass requires updating all Visitor interfaces and implementations, causing a cascading refactor.
    *   *Double Dispatch:* The operation executed depends on *both* the Visitor type and the Element type.

---

## Chapter 6. Conclusion

### The Role of Patterns in Software Design
1. Conventional language studies of expert developers show that knowledge is organized around large conceptual structures like algorithms, data structures, idioms, and plans to satisfy goals, rather than syntax.
2. When designing, developers rarely focus on design notation itself; instead, they attempt to map the current scenario against these learned plans and conceptual structures.
3. While computer scientists have historically named and cataloged algorithms and data structures, other design patterns remained unnamed and uncataloged before the pattern movement.
4. Design patterns address this gap by establishing a shared vocabulary for designers to communicate, document, and analyze alternative approaches.
5. They reduce the apparent complexity of a system by enabling discussions at a higher abstraction level than diagrams, notation, or programming syntax.
6. Internalizing these patterns shifts discussions from raw implementation details to direct references like "Let's use an Observer here" or "Make a Strategy out of these classes."
7. Understanding design patterns makes it much easier to comprehend existing large-scale systems, which almost always employ these structures.
8. Beginners in object-oriented programming often struggle to understand complex control flows and deep inheritance hierarchies in existing systems.
9. This struggle typically stems from a lack of understanding of the design patterns embedded within the architecture.
10. Learning patterns accelerates a designer's growth, helping a novice developer reason and act more like an experienced expert.
11. Documenting a system using patterns prevents future maintainers from having to reverse-engineer the codebase to discover the design decisions.
12. A pattern name provides a dense summary of a design choice, allowing readers to look up the pattern rather than dissecting the class relationships from scratch.
13. Patterns help developers pick appropriate class names, reason about good design principles, and describe architectures as sequences of applied patterns.
14. Traditional object-oriented design methodologies standardize notations and propose rules, but they fail to capture the hard-earned experience of expert designers.
15. Design patterns supplement these methodologies by showing how to compose primitive constructs (objects, classes, inheritance, polymorphism) to achieve flexibility.
16. They record the "why" of a design decision (via applicability, implementation guidelines, and trade-offs) instead of just documenting the structural "what."
17. Patterns are highly effective in navigating the transition from Object-Oriented Analysis (OOA) to Object-Oriented Design (OOD).
18. OOA models rarely translate smoothly into flexible, reusable systems; OOD requires introducing objects that do not correspond to domain entities, influenced by libraries and language limits.

### Targets and Drivers for Refactoring
19. Reusable software is not built in a single pass; it must be continually reorganized and refactored over its lifecycle.
20. Design patterns help developers determine how to reorganize code and minimize the amount of refactoring needed in later stages.
21. Brian Foote outlines three primary phases in the lifecycle of object-oriented software: prototyping, expansionary, and consolidation.
22. The prototyping phase is characterized by rapid development and incremental adjustments to meet initial requirements.
23. Structures in the prototyping phase closely mirror problem domain entities, relying heavily on inheritance (white-box reuse).
24. The expansionary phase is driven by two competing forces: the need for new features and the need for greater reusability.
25. Adding new classes and hierarchies to meet requirements eventually makes the system "arthritic" and inflexible.
26. Class hierarchies cease to represent a single domain, instead reflecting multiple domains, with classes accumulating unrelated operations and instance variables.
27. To continue evolving, the system must undergo refactoring in the consolidation phase.
28. During consolidation, frameworks emerge as developers decompose large classes into special- and general-purpose components.
29. Interfaces are rationalized, operations are moved within class hierarchies, and object composition (black-box reuse) replaces inheritance (white-box reuse).
30. The cycle of expansion and consolidation is inevitable in software evolution.
31. Experienced designers anticipate changes that prompt refactoring and design structures that are robust against these requirements shifts.
32. Design patterns capture the target structures that naturally result from the consolidation phase.
33. Applying design patterns early in development avoids future refactoring, while applying them post-hoc provides clear targets for refactoring.

### The History and Evolution of Design Patterns
34. The pattern catalog originated in Erich Gamma's Ph.D. thesis (1991–1992), which contained approximately half of the final 23 patterns.
35. At OOPSLA '91, the catalog became an independent project when Richard Helm joined Erich Gamma to collaborate on it.
36. John Vlissides joined the effort shortly thereafter, followed by Ralph Johnson at OOPSLA '92, completing the "Gang of Four" (GoF).
37. The group targeted publication at ECOOP '93, but their 90-page paper was rejected as too long, prompting them to submit a summary paper instead.
38. Following the acceptance of the summary paper, they committed to transforming the catalog into a full-length book.
39. Over time, several pattern names evolved: "Wrapper" became "Decorator," "Glue" became "Facade," "Solitaire" became "Singleton," and "Walker" became "Visitor."
40. Noticing a pattern is relatively easy when reviewing multiple systems; describing it so others can learn and apply it is the real challenge.
41. Early drafts were only understood by experts who had already implemented the patterns in their own designs.
42. To serve as an effective learning tool for novices, the average pattern description was expanded from under two pages to over ten pages.
43. Descriptions were enriched with motivating examples, sample code, detailed trade-offs, and implementation strategies.
44. The authors increased emphasis on the specific problem a pattern solves (the "why"), which is harder to identify than the structural solution (the "what").

### Christopher Alexander and the Pattern Community
45. Christopher Alexander, an architect who studied patterns in towns and buildings, inspired the software pattern movement.
46. Similarities between Alexander's work and GoF include: observing existing systems, using structured templates, relying on natural language, and providing design rationales.
47. Differences between architectural and software patterns are significant:
48. First, architecture has thousands of years of history and classic structures, whereas software engineering is a young discipline with few classic systems.
49. Second, Alexander defines a strict sequential order in which patterns should be applied; GoF does not impose an order.
50. Third, Alexander's patterns emphasize the problem context, whereas GoF patterns focus heavily on detailing the structural solution.
51. Fourth, Alexander claims his patterns can generate complete structures (buildings); GoF makes no claim that patterns generate complete programs.
52. The GoF catalog is a collection of related patterns, not a complete pattern language.
53. The software pattern community grew from an OOPSLA '91 workshop on a "software architect's handbook" led by Bruce Anderson.
54. This workshop led to the Pattern Languages of Programs (PLoP) conference in August 1994, formalizing the community of pattern catalogers.
55. James Coplien's *Advanced C++: Programming Styles and Idioms* influenced GoF and pioneered patterns describing organizational roles.
56. Kent Beck was an early advocate of Alexander's work, writing Smalltalk patterns columns, and Peter Coad collected analysis patterns.

### Conclusions and Key Takeaways
57. Developers are encouraged to use patterns, adopt them in daily communication, and identify new patterns from their practical experience.
58. Patterns move design decisions out of vague intuition, making trade-offs explicit and allowing constructive debates.
59. Finding patterns requires practical experience; writing them down should be a collaborative process with peer feedback.
60. **Alexander's Concept of Density**: Loose assemblies of patterns do not produce profound designs. High-quality designs overlap and intertwine multiple patterns within the same design space, creating a dense and profound structure.

---

## Appendices

### 1. Glossary Terms & OOD Context (Appendix A)
The glossary defines foundational terminology that establishes the conceptual framework for object-oriented design (OOD), reuse, and pattern relationships:

*   **Abstract Class & Concrete Class**: An *abstract class* defines an interface but defers implementation of its operations to subclasses; it cannot be instantiated. A *concrete class* implements all inherited operations and can be instantiated. In OOD, designing to abstract classes decouples clients from concrete implementations.
*   **Abstract Operation**: An operation that declares a signature without providing an implementation (in C++, a pure virtual member function). This defines the contract that subclasses must fulfill.
*   **Abstract Coupling**: Occurs when class $A$ maintains a reference to abstract class $B$. Because $A$ refers to a *type* (interface) rather than a concrete instantiation, the coupling is abstract. This is a core mechanism of patterns (e.g., Bridge, Strategy) to isolate dependencies.
*   **Relationships: Aggregation vs. Acquaintance**: 
    *   *Aggregation* represents a whole-part relationship where the aggregate object is composed of subobjects (parts) and is responsible for their lifecycle.
    *   *Acquaintance* is a looser, dynamic relationship where one class refers to another without ownership (e.g., holding a reference or pointer). Aggregation is static and structural, while acquaintance is dynamic and behavioral.
*   **Black-box Reuse vs. White-box Reuse**:
    *   *Black-box reuse* is based on object composition. Composed objects hide their internal representation from each other, behaving as black boxes. This maintains encapsulation and allows runtime changes.
    *   *White-box reuse* relies on class inheritance. The subclass reuses the parent class's interface and implementation, but inheritance breaks encapsulation because parent class internals are often exposed to subclasses.
*   **Delegation**: An implementation mechanism where an object forwards a request to another object (the delegate) to perform it. In OOD, delegation acts as an alternative to inheritance, allowing dynamic, run-time behavior composition.
*   **Interface, Type, Subtype, and Protocol**:
    *   *Interface* is the set of all signatures defined by an object's operations.
    *   *Type* is the name associated with a specific interface.
    *   *Subtype* is a type whose interface contains (and extends) another type's interface, allowing substitutability.
    *   *Protocol* extends the interface concept by specifying the allowable *sequence* of requests an object can handle.
*   **Dynamic Binding & Polymorphism**:
    *   *Dynamic binding* is the run-time association of a request to an object and its operation.
    *   *Polymorphism* is the ability to substitute objects with matching interfaces at run-time, allowing dynamic binding to invoke correct behaviors.
*   **Parameterized Type**: A type that leaves constituent types unspecified until instantiation (C++ Templates). It provides compile-time polymorphism.
*   **Mixin Class**: A class (typically abstract) designed to be combined with other classes via inheritance to supply optional, shared behavior.
*   **Framework vs. Toolkit**:
    *   A *toolkit* is a collection of utility classes (like lists or strings) providing functionality without defining the application's design or flow of control.
    *   A *framework* is a reusable design for a specific class of software, consisting of cooperating abstract classes that define the application's control flow (Inversion of Control).

### 2. Foundation Classes (Appendix C)
Appendix C documents five minimal foundation classes used in the book's C++ sample code to demonstrate structural and behavioral design patterns:

1.  **`List`**: Parameterized container template class (`template <class Item> class List`) that stores elements by value. In the patterns book, it is heavily used to store pointers to objects (e.g., `List<Glyph*>`) to implement heterogeneous (polymorphic) collections. It also provides stack interface synonyms (`Top`, `Push`, `Pop`).
2.  **`Iterator`**: Abstract interface class template (`template <class Item> class Iterator`) defining operations to traverse any aggregate collection sequentially without exposing its internal structure (`First()`, `Next()`, `IsDone()`, `CurrentItem()`).
3.  **`ListIterator`**: Concrete iterator implementing the `Iterator` interface specifically for traversing `List` aggregates. It holds a pointer to a `List` and a tracking index representing the current traversal index.
4.  **`Point`**: Represents a point in two-dimensional Cartesian space, providing basic vector arithmetic. Relies on type alias `typedef float Coord;`. Holds internal coordinates and exposes arithmetic operator overloads (`+`, `-`, `*`, `/`).
5.  **`Rect`**: Represents an axis-aligned rectangle defined by an origin point and an extent (width and height). Composed of two `Point` objects representing origin and extent.

### 3. Bibliography Analysis & Thematic Mapping
The bibliography reflects the theoretical and practical foundations of object-oriented design and the patterns movement:

*   **Theme 1: The Pattern Movement & Architecture Roots**: The term "Pattern Language" is directly imported from Christopher Alexander’s architectural work, *A Pattern Language* `[AIS+77]`. Kent Beck and Ralph Johnson’s "Patterns generate architectures" `[BJ94]` and Peter Coad's early work `[Coa92]` represent the translation of these concepts to software design. Coplien's *Advanced C++ Programming Styles and Idioms* `[Cop92]` contributed concrete idioms.
*   **Theme 2: Object-Oriented Analysis, Design, and Notation**: Books like Booch’s OOD `[Boo94]` and Rumbaugh et al.'s OMT `[RBP+91]` provided the diagrammatic notation used by the GoF. Wirfs-Brock et al. `[WBWW90]` introduced Responsibility-Driven Design (RDD), which heavily influenced how behavioral patterns allocate roles.
*   **Theme 3: Frameworks and UI Toolkits (Practical Incubators)**: Erich Gamma’s PhD thesis on ET++ `[Gam91, Gam92]` and papers on it `[WGM88]` were primary source material. Linton, Vlissides, and Calder’s work on InterViews `[LVC89, CL90]` (especially the Flyweight/Glyph concept) provided the basis for structural patterns.
*   **Theme 4: Theoretical Software Engineering Foundations**: Johnson and Foote's "Designing reusable classes" `[JF88]` formulated early rules for designing abstract classes and frameworks. Snyder's "Encapsulation and inheritance" `[Sny86]` explored base class fragility. Liskov and Guttag's work on data abstraction `[LG86]` formed the basis for subtype substitutability. Opdyke and Johnson's papers on refactoring `[OJ90, OJ93]` laid the groundwork for class hierarchy evolution.
*   **Theme 5: Historical Roots of Graphic Systems & Interactive Environments**: Ivan Sutherland's Sketchpad `[Sut63]` and Alan Borning’s constraint-based ThingLab `[Bor81]` represent the historical lineage of interactive object systems. Adele Goldberg and David Robson’s *Smalltalk-80* `[GR83]` provided dynamic typing foundations and early implementations of MVC.

---

Fuentes: *GoF Design Patterns*, Caps. 1-6, Glosario y Apéndices — el resto es criterio general.
