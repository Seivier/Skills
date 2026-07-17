# Design Patterns: Elements of Reusable Object-Oriented Software — Ejemplos, Casos de Estudio y Diagramas


## Índice de capítulos
- [Chapter 1: Introduction](#chapter-1-introduction)
- [Chapter 2: A Case Study: Designing a Document Editor](#chapter-2-a-case-study-designing-a-document-editor)
- [Chapter 3: Creational Patterns](#chapter-3-creational-patterns)
- [Chapter 4: Structural Patterns](#chapter-4-structural-patterns)
- [Chapter 5: Behavioral Patterns](#chapter-5-behavioral-patterns)
- [Appendices](#appendices)

## Chapter 1: Introduction

No concrete code examples in this chapter. The chapter is entirely conceptual and uses prose-based descriptions, UML/OMT-style diagrams, and one extended case study described in prose:

### 1. Smalltalk-80 MVC Structure
The standard user interface structure in Smalltalk-80 relies on the interactions of three classes:
* `Model`: Manages the data and application state.
* `View`: Manages the visual rendering of the `Model` on screen.
* `Controller`: Intercepts user inputs (key presses, mouse movements) and translates them into requests for the `Model` or updates for the `View`.

```
[View] <----+ (notifies of change)
  |         |
  | (queries)
  v         |
[Model] ----+
  ^
  | (updates state)
  |
[Controller] <--- (user input)
```

#### Prose Description of the MVC Observer Diagram:
A diagram shows a single `Model` block connected to three active views:
1. A **Spreadsheet View** (displaying numerical tables).
2. A **Histogram View** (displaying vertical bar charts).
3. A **Pie Chart View** (displaying circular segments).

The `Model` maintains internal data values (e.g., `x = 5`, `y = 10`, `z = 15`). The diagram uses directed arrows to show the flow of information:
* A notification link points from the `Model` to the three views, indicating that when values change, the model broadcasts an update signal.
* Queries point from each view back to the `Model`, indicating that the views read the model's values to redraw themselves. The controllers are omitted for visual simplicity.

### 2. Class Diagrams and Structural Conventions in OMT
The book uses the Object Modeling Technique (OMT) notation to represent relationships:

#### Class Structure Notation
A class is represented by a 3-part rectangle:
* **Top section:** Class Name (in **bold** for concrete classes, in *slanted* font for abstract classes).
* **Middle section:** Operations (methods) with optional signatures. Abstract operations are written in *slanted* text.
* **Bottom section:** Data (instance variables) with optional types.
Lines separate these three sections.

```
+------------------------------------+
|             ClassName              |
+------------------------------------+
| Operation1(param: Type): ReturnType|
| Operation2()                       |
+------------------------------------+
| instanceVariable1: Type            |
| instanceVariable2                  |
+------------------------------------+
```

#### Instantiation Relationship
A dashed arrow points from the class doing the instantiating to the class being instantiated.
* *Example:* If class `Application` instantiates class `Document`, the dashed arrow starts at `Application` and its arrowhead points to `Document`.
```
[Application] - - - - - > [Document]
```

#### Inheritance (Subclassing) Hierarchy
Inheritance is represented by a vertical line leading to a triangle pointing up to the parent class. Subclasses branch off the base of the triangle.
* *Example:* An abstract parent class `View` has a concrete subclass `CompositeView` and another concrete subclass `Button`.
```
            [View (slanted)]
                   ^
                   | (triangle)
         +---------+---------+
         |                   |
  [CompositeView]        [Button]
```

#### Pseudocode Implementation Note
If the diagram contains pseudocode for a method, it is shown in a dogeared box and connected to the corresponding operation via a dashed line.
* *Example:*
```
  [View] --- (dashed line) --- [ Area() { return rectangle->Area(); } ]
```

#### Mixin Class and Multiple Inheritance
A class that inherits from multiple parents (e.g., a concrete class inheriting from an abstract base and a mixin class) is represented by multiple inheritance lines.
```
  [ParentClass]    [MixinClass (slanted)]
        ^                 ^
        |                 |
        +--------+--------+
                 |
           [DerivedClass]
```

### 3. Concrete Design Examples

#### Window Delegation (Replacing Inheritance with Composition)
Instead of `Window` subclassing `Rectangle`, it uses delegation to achieve reuse.

##### Class Structure:
* **Window Class:** Has a reference to an instance of `Rectangle` named `rectangle` and exposes an `Area()` operation.
* **Rectangle Class:** Exposes an `Area()` operation and defines width and height parameters.

##### Interaction / Method Signature:
When a client calls `Window::Area()`, the `Window` class explicitly forwards the call to its internal `Rectangle` instance.

```cpp
// C++ Implementation of Window Delegation
class Rectangle {
public:
    virtual float Area() {
        return _width * _height;
    }
private:
    float _width;
    float _height;
};

class Window {
public:
    virtual float Area() {
        // Window delegates the Area calculation to its Rectangle member variable
        return _rectangle->Area();
    }
private:
    Rectangle* _rectangle; // Object reference (Composition)
};
```

##### Prose Description of the Delegation Diagram:
The diagram depicts two classes: `Window` and `Rectangle`.
* The `Window` class contains an operation `Area()`.
* The `Rectangle` class contains an operation `Area()`.
* A solid line with a plain arrowhead points from `Window` to `Rectangle`, labeled with the variable name `rectangle`, indicating that `Window` holds a reference to a `Rectangle` instance.
* A dashed line connects the `Area()` operation of `Window` to a dogeared text box containing the pseudocode: `rectangle->Area()`, illustrating the delegation mechanism.

---

## Chapter 2: A Case Study: Designing a Document Editor

### COMPOSITE PATTERN IMPLEMENTATION IN LEXI
`Glyph` serves as the abstract component base, while `Character` is a leaf and `Row` is a composite container.

#### Virtual Class Declaration (C++)
```cpp
class Window;
class Rect;
class Point;
class Iterator;

class Glyph {
public:
    virtual ~Glyph() {}

    // Rendering & Hit Detection
    virtual void Draw(Window*) = 0;
    virtual void Bounds(Rect&) = 0;
    virtual bool Intersects(const Point&) = 0;

    // Structural child management
    virtual void Insert(Glyph*, int index) {}
    virtual void Remove(Glyph*) {}
    virtual Glyph* Child(int index) { return nullptr; }
    virtual Glyph* Parent() { return nullptr; }
    
    // Iterator support
    virtual Iterator* CreateIterator() { return new NullIterator(); }
    virtual void Accept(Visitor&) = 0;
};
```

#### Leaf Class Implementation (C++)
```cpp
class Character : public Glyph {
public:
    Character(char c) : _charcode(c) {}
    virtual void Draw(Window* w) override {
        // Draw character code on window
    }
    virtual void Bounds(Rect& r) override {
        // Calculate dimensions based on character font
    }
    virtual bool Intersects(const Point& p) override {
        // Check intersection with bounds
    }
    char GetCharCode() const { return _charcode; }
    virtual void Accept(Visitor& v) override {
        v.VisitCharacter(this);
    }
private:
    char _charcode;
};
```

#### Composite Class Implementation (C++)
```cpp
class Row : public Glyph {
public:
    virtual void Draw(Window* w) override {
        for (Glyph* child : _children) {
            child->Draw(w);
        }
    }
    virtual void Bounds(Rect& r) override {
        // Compute bounding box containing all children
    }
    virtual bool Intersects(const Point& p) override {
        for (Glyph* child : _children) {
            if (child->Intersects(p)) return true;
        }
        return false;
    }
    virtual void Insert(Glyph* g, int index) override {
        _children.insert(_children.begin() + index, g);
    }
    virtual void Remove(Glyph* g) override {
        auto it = std::find(_children.begin(), _children.end(), g);
        if (it != _children.end()) {
            _children.erase(it);
        }
    }
    virtual Glyph* Child(int index) override {
        return _children.at(index);
    }
    virtual Iterator* CreateIterator() override {
        return new ListIterator(this);
    }
    virtual void Accept(Visitor& v) override {
        v.VisitRow(this);
    }
private:
    std::vector<Glyph*> _children;
};
```

### STRATEGY PATTERN IMPLEMENTATION IN LEXI
The formatting engine separation. `Composition` holds elements and delegates formatting logic to `Compositor`.

```cpp
class Compositor {
public:
    virtual void SetComposition(Composition* c) = 0;
    virtual void Compose() = 0;
protected:
    Compositor() {}
};

class Composition : public Glyph {
public:
    Composition(Compositor* compositor) : _compositor(compositor) {
        _compositor->SetComposition(this);
    }
    void SetCompositor(Compositor* c) {
        _compositor = c;
        _compositor->SetComposition(this);
    }
    virtual void Draw(Window* w) override {
        // Draws the formatted layout (Rows and Columns)
    }
    // ... basic glyph method implementations ...
private:
    Compositor* _compositor;
    std::vector<Glyph*> _content; // raw characters/images
    std::vector<Glyph*> _lines;   // structured Row glyphs
};
```

### DECORATOR PATTERN IMPLEMENTATION IN LEXI
Transparent enclosure implementations for border and scroll embellishments.

```cpp
class MonoGlyph : public Glyph {
public:
    MonoGlyph(Glyph* component) : _component(component) {}
    virtual void Draw(Window* w) override {
        _component->Draw(w);
    }
    virtual void Bounds(Rect& r) override {
        _component->Bounds(r);
    }
    virtual bool Intersects(const Point& p) override {
        return _component->Intersects(p);
    }
private:
    Glyph* _component;
};

class Border : public MonoGlyph {
public:
    Border(Glyph* component, int width) : MonoGlyph(component), _width(width) {}
    virtual void Draw(Window* w) override {
        MonoGlyph::Draw(w);
        DrawBorder(w);
    }
    virtual void Bounds(Rect& r) override {
        MonoGlyph::Bounds(r);
        // Expand bounds by _width
    }
private:
    void DrawBorder(Window* w) {
        // Custom border rendering logic using window graphics
    }
    int _width;
};
```

### ABSTRACT FACTORY PATTERN IMPLEMENTATION IN LEXI
Abstract widget creation factory and concrete look-and-feel subclasses.

```cpp
class ScrollBar : public Glyph { /* abstract widget operations */ };
class Button : public Glyph { /* abstract widget operations */ };

class GUIFactory {
public:
    virtual ScrollBar* CreateScrollBar() = 0;
    virtual Button* CreateButton() = 0;
};

class MotifFactory : public GUIFactory {
public:
    virtual ScrollBar* CreateScrollBar() override {
        return new MotifScrollBar();
    }
    virtual Button* CreateButton() override {
        return new MotifButton();
    }
};

class PMFactory : public GUIFactory {
public:
    virtual ScrollBar* CreateScrollBar() override {
        return new PMScrollBar();
    }
    virtual Button* CreateButton() override {
        return new PMButton();
    }
};
```

### BRIDGE PATTERN IMPLEMENTATION IN LEXI
Separation of window abstraction from window system implementation.

```cpp
class WindowImp {
public:
    virtual void DeviceRect(Coord x0, Coord y0, Coord x1, Coord y1) = 0;
    virtual void DeviceText(const char*, Coord, Coord) = 0;
};

class Window {
public:
    Window(WindowImp* imp) : _imp(imp) {}
    virtual void DrawRect(Coord x0, Coord y0, Coord x1, Coord y1) {
        _imp->DeviceRect(x0, y0, x1, y1);
    }
private:
    WindowImp* _imp;
};

class ApplicationWindow : public Window {
public:
    ApplicationWindow(WindowImp* imp) : Window(imp) {}
    void DrawMenu() {
        // Abstraction level menu drawing logic
    }
};

class XWindowImp : public WindowImp {
public:
    virtual void DeviceRect(Coord x0, Coord y0, Coord x1, Coord y1) override {
        int x = std::min(x0, x1);
        int y = std::min(y0, y1);
        int w = std::abs(x0 - x1);
        int h = std::abs(y0 - y1);
        XDrawRectangle(_display, _win, _gc, x, y, w, h);
    }
private:
    Display* _display;
    ::Window _win;
    GC _gc;
};
```

### COMMAND PATTERN IMPLEMENTATION IN LEXI
Encapsulated user operations with support for execution, unexecution, and undo capabilities.

```cpp
class Command {
public:
    virtual void Execute() = 0;
    virtual void Unexecute() = 0;
    virtual bool Reversible() = 0;
};

class FontCommand : public Command {
public:
    FontCommand(Document* doc, const std::string& fontName) 
        : _doc(doc), _fontName(fontName), _hasExecuted(false) {}

    virtual void Execute() override {
        if (_doc->GetSelectionFont() != _fontName) {
            _prevFont = _doc->GetSelectionFont();
            _selectionRange = _doc->GetSelectionRange();
            _doc->SetSelectionFont(_fontName);
            _hasExecuted = true;
        }
    }

    virtual void Unexecute() override {
        if (_hasExecuted) {
            _doc->SetSelectionFontRange(_prevFont, _selectionRange);
        }
    }

    virtual bool Reversible() override {
        return _hasExecuted;
    }

private:
    Document* _doc;
    std::string _fontName;
    std::string _prevFont;
    Range _selectionRange;
    bool _hasExecuted;
};
```

### ITERATOR AND VISITOR PATTERN IMPLEMENTATION IN LEXI
Decoupling of structure traversal and processing actions.

```cpp
class Iterator {
public:
    virtual void First() = 0;
    virtual void Next() = 0;
    virtual bool IsDone() = 0;
    virtual Glyph* CurrentItem() = 0;
protected:
    Iterator() {}
};

class NullIterator : public Iterator {
public:
    virtual void First() override {}
    virtual void Next() override {}
    virtual bool IsDone() override { return true; }
    virtual Glyph* CurrentItem() override { return nullptr; }
};

class ListIterator : public Iterator {
public:
    ListIterator(const Row* row) : _row(row), _current(0) {}
    virtual void First() override { _current = 0; }
    virtual void Next() override { _current++; }
    virtual bool IsDone() override { return _current >= _row->ChildCount(); }
    virtual Glyph* CurrentItem() override { 
        return IsDone() ? nullptr : _row->Child(_current); 
    }
private:
    const Row* _row;
    int _current;
};

class Visitor {
public:
    virtual void VisitCharacter(Character*) = 0;
    virtual void VisitRow(Row*) = 0;
};

class SpellingCheckingVisitor : public Visitor {
public:
    SpellingCheckingVisitor() : _misspellings() {}
    virtual void VisitCharacter(Character* c) override {
        char ch = c->GetCharCode();
        if (isalpha(ch)) {
            _currentWord += ch;
        } else {
            if (!_currentWord.empty() && IsMisspelled(_currentWord)) {
                _misspellings.push_back(_currentWord);
            }
            _currentWord.clear();
        }
    }
    virtual void VisitRow(Row* r) override {}
    std::vector<std::string> GetMisspellings() { return _misspellings; }
private:
    bool IsMisspelled(const std::string& word) { return true; }
    std::string _currentWord;
    std::vector<std::string> _misspellings;
};
```

---

## Chapter 3: Creational Patterns

### I. COMMON MAZE CLASS DEFINITIONS (C++)
The baseline model classes are defined below, illustrating the starting code:

```cpp
#include <iostream>
#include <vector>
#include <map>

enum Direction { North, South, East, West };

class MapSite {
public:
    virtual ~MapSite() = default;
    virtual void Enter() = 0;
};

class Room : public MapSite {
public:
    Room(int roomNo) : _roomNumber(roomNo) {
        for (int i = 0; i < 4; ++i) {
            _sides[i] = nullptr;
        }
    }

    MapSite* GetSide(Direction direction) const {
        return _sides[direction];
    }

    void SetSide(Direction direction, MapSite* mapSite) {
        _sides[direction] = mapSite;
    }

    int GetRoomNumber() const {
        return _roomNumber;
    }

    void Enter() override {
        std::cout << "Entering Room " << _roomNumber << std::endl;
    }

private:
    MapSite* _sides[4];
    int _roomNumber;
};

class Wall : public MapSite {
public:
    void Enter() override {
        std::cout << "Ouch! You bumped into a wall." << std::endl;
    }
};

class Door : public MapSite {
public:
    Door(Room* room1 = nullptr, Room* room2 = nullptr)
        : _room1(room1), _room2(room2), _isOpen(false) {}

    void Enter() override {
        if (_isOpen) {
            std::cout << "Stepping through the door." << std::endl;
        } else {
            std::cout << "Ouch! The door is closed." << std::endl;
        }
    }

    Room* OtherSideFrom(Room* room) {
        if (room == _room1) return _room2;
        if (room == _room2) return _room1;
        return nullptr;
    }

private:
    Room* _room1;
    Room* _room2;
    bool _isOpen;
};

class Maze {
public:
    void AddRoom(Room* room) {
        _rooms[room->GetRoomNumber()] = room;
    }

    Room* RoomNo(int roomNo) const {
        auto it = _rooms.find(roomNo);
        if (it != _rooms.end()) {
            return it->second;
        }
        return nullptr;
    }

private:
    std::map<int, Room*> _rooms;
};

// Inflexible Client Method
class MazeGame {
public:
    Maze* CreateMaze() {
        Maze* aMaze = new Maze;
        Room* r1 = new Room(1);
        Room* r2 = new Room(2);
        Door* theDoor = new Door(r1, r2);

        aMaze->AddRoom(r1);
        aMaze->AddRoom(r2);

        r1->SetSide(North, new Wall);
        r1->SetSide(East, theDoor);
        r1->SetSide(South, new Wall);
        r1->SetSide(West, new Wall);

        r2->SetSide(North, new Wall);
        r2->SetSide(East, new Wall);
        r2->SetSide(South, new Wall);
        r2->SetSide(West, theDoor);

        return aMaze;
    }
};
```

### II. ABSTRACT FACTORY EXAMPLES

#### A. C++ Maze Abstract Factory Implementation
To make `CreateMaze()` flexible, we introduce `MazeFactory` to instantiate components:

```cpp
class MazeFactory {
public:
    virtual ~MazeFactory() = default;

    virtual Maze* MakeMaze() const {
        return new Maze;
    }

    virtual Wall* MakeWall() const {
        return new Wall;
    }

    virtual Room* MakeRoom(int n) const {
        return new Room(n);
    }

    virtual Door* MakeDoor(Room* r1, Room* r2) const {
        return new Door(r1, r2);
    }
};

// Subclass for Enchanted Mazes
class Spell;
class EnchantedRoom : public Room {
public:
    EnchantedRoom(int n, Spell* spell) : Room(n), _spell(spell) {}
private:
    Spell* _spell;
};

class DoorNeedingSpell : public Door {
public:
    DoorNeedingSpell(Room* r1, Room* r2) : Door(r1, r2) {}
};

class EnchantedMazeFactory : public MazeFactory {
public:
    EnchantedMazeFactory() = default;

    Room* MakeRoom(int n) const override {
        return new EnchantedRoom(n, CastSpell());
    }

    Door* MakeDoor(Room* r1, Room* r2) const override {
        return new DoorNeedingSpell(r1, r2);
    }

protected:
    Spell* CastSpell() const { return nullptr; } // Cast placeholder
};

// Subclass for Bombed Mazes
class BombedWall : public Wall {
public:
    BombedWall() : _isDamaged(false) {}
    bool _isDamaged;
};

class RoomWithABomb : public Room {
public:
    RoomWithABomb(int n) : Room(n), _hasBomb(true) {}
private:
    bool _hasBomb;
};

class BombedMazeFactory : public MazeFactory {
public:
    Wall* MakeWall() const override {
        return new BombedWall;
    }

    Room* MakeRoom(int n) const override {
        return new RoomWithABomb(n);
    }
};

// Client refactored to accept MazeFactory
class FlexibleMazeGame {
public:
    Maze* CreateMaze(const MazeFactory& factory) {
        Maze* aMaze = factory.MakeMaze();
        Room* r1 = factory.MakeRoom(1);
        Room* r2 = factory.MakeRoom(2);
        Door* theDoor = factory.MakeDoor(r1, r2);

        aMaze->AddRoom(r1);
        aMaze->AddRoom(r2);

        r1->SetSide(North, factory.MakeWall());
        r1->SetSide(East, theDoor);
        r1->SetSide(South, factory.MakeWall());
        r1->SetSide(West, factory.MakeWall());

        r2->SetSide(North, factory.MakeWall());
        r2->SetSide(East, factory.MakeWall());
        r2->SetSide(South, factory.MakeWall());
        r2->SetSide(West, theDoor);

        return aMaze;
    }
};
```

#### B. Smalltalk Class-Based Catalog Factory
In Smalltalk, class objects can be stored directly inside the factory instance:

```smalltalk
"Define MazeFactory class with an instance variable 'partCatalog'"
Object subclass: #MazeFactory
    instanceVariableNames: 'partCatalog'
    classVariableNames: ''
    poolDictionaries: ''
    category: 'DesignPatterns-AbstractFactory'

"Initialize dictionary mapping parts to product classes"
initialize
    partCatalog := Dictionary new.
    partCatalog at: #room put: Room.
    partCatalog at: #wall put: Wall.
    partCatalog at: #door put: Door.
    partCatalog at: #maze put: Maze.

"Generic Make operation instantiating classes directly"
make: partName
    ^ (partCatalog at: partName) new

"Enchanted Factory Initialization"
initializeEnchanted
    partCatalog := Dictionary new.
    partCatalog at: #room put: EnchantedRoom.
    partCatalog at: #wall put: Wall.
    partCatalog at: #door put: DoorNeedingSpell.
    partCatalog at: #maze put: Maze.
```

### III. BUILDER EXAMPLES

#### A. C++ Maze Builder Implementation
The construction interface is separated from representation:

```cpp
class MazeBuilder {
public:
    virtual ~MazeBuilder() = default;

    virtual void BuildMaze() {}
    virtual void BuildRoom(int roomNo) {}
    virtual void BuildDoor(int roomFrom, int roomTo) {}

    virtual Maze* GetMaze() { return nullptr; }

protected:
    MazeBuilder() = default;
};

// Concrete Builder that constructs standard mazes
class StandardMazeBuilder : public MazeBuilder {
public:
    StandardMazeBuilder() {
        _currentMaze = nullptr;
    }

    void BuildMaze() override {
        _currentMaze = new Maze;
    }

    void BuildRoom(int roomNo) override {
        if (!_currentMaze->RoomNo(roomNo)) {
            Room* room = new Room(roomNo);
            _currentMaze->AddRoom(room);

            room->SetSide(North, new Wall);
            room->SetSide(South, new Wall);
            room->SetSide(East, new Wall);
            room->SetSide(West, new Wall);
        }
    }

    void BuildDoor(int roomFrom, int roomTo) override {
        Room* r1 = _currentMaze->RoomNo(roomFrom);
        Room* r2 = _currentMaze->RoomNo(roomTo);
        Door* d = new Door(r1, r2);

        r1->SetSide(CommonWall(r1, r2), d);
        r2->SetSide(CommonWall(r2, r1), d);
    }

    Maze* GetMaze() override {
        return _currentMaze;
    }

private:
    Direction CommonWall(Room* r1, Room* r2) {
        return East; 
    }

    Maze* _currentMaze;
};

// Concrete Builder that counts components instead of building
class CountingMazeBuilder : public MazeBuilder {
public:
    CountingMazeBuilder() : _rooms(0), _doors(0) {}

    void BuildRoom(int roomNo) override {
        _rooms++;
    }

    void BuildDoor(int roomFrom, int roomTo) override {
        _doors++;
    }

    void GetCounts(int& rooms, int& doors) const {
        rooms = _rooms;
        doors = _doors;
    }

private:
    int _rooms;
    int _doors;
};

// Director usage
class BuilderMazeGame {
public:
    Maze* CreateMaze(MazeBuilder& builder) {
        builder.BuildMaze();
        builder.BuildRoom(1);
        builder.BuildRoom(2);
        builder.BuildDoor(1, 2);

        return builder.GetMaze();
    }
};
```

### IV. FACTORY METHOD EXAMPLES

#### A. C++ Maze Game Factory Method Implementation
Subclasses override creation methods to define custom room, door, and wall classes:

```cpp
class FactoryMethodMazeGame {
public:
    Maze* CreateMaze() {
        Maze* aMaze = MakeMaze();
        Room* r1 = MakeRoom(1);
        Room* r2 = MakeRoom(2);
        Door* theDoor = MakeDoor(r1, r2);

        aMaze->AddRoom(r1);
        aMaze->AddRoom(r2);

        r1->SetSide(North, MakeWall());
        r1->SetSide(East, theDoor);
        r1->SetSide(South, MakeWall());
        r1->SetSide(West, MakeWall());

        r2->SetSide(North, MakeWall());
        r2->SetSide(East, MakeWall());
        r2->SetSide(South, MakeWall());
        r2->SetSide(West, theDoor);

        return aMaze;
    }

    // Factory Methods providing default implementations
    virtual Maze* MakeMaze() const { return new Maze; }
    virtual Room* MakeRoom(int n) const { return new Room(n); }
    virtual Wall* MakeWall() const { return new Wall; }
    virtual Door* MakeDoor(Room* r1, Room* r2) const { return new Door(r1, r2); }
};

// Creator Subclass returning bombed components
class BombedMazeGame : public FactoryMethodMazeGame {
public:
    Wall* MakeWall() const override {
        return new BombedWall;
    }

    Room* MakeRoom(int n) const override {
        return new RoomWithABomb(n);
    }
};
```

### V. PROTOTYPE EXAMPLES

#### A. C++ Maze Prototype Factory Implementation
The factory clones pre-configured prototypes rather than subclassing:

```cpp
class MazePrototypeFactory : public MazeFactory {
public:
    MazePrototypeFactory(Maze* m, Wall* w, Room* r, Door* d)
        : _prototypeMaze(m), _prototypeWall(w), _prototypeRoom(r), _prototypeDoor(d) {}

    Wall* MakeWall() const override {
        return _prototypeWall->Clone();
    }

    Door* MakeDoor(Room* r1, Room* r2) const override {
        Door* door = _prototypeDoor->Clone();
        door->Initialize(r1, r2);
        return door;
    }

private:
    Maze* _prototypeMaze;
    Wall* _prototypeWall;
    Room* _prototypeRoom;
    Door* _prototypeDoor;
};
```

### VI. SINGLETON EXAMPLES

#### A. C++ MazeFactory Singleton with Subclass Selection via Environment Variables
Enforces a single global instance, dynamically resolving to the correct subclass:

```cpp
#include <cstdlib>
#include <cstring>

class MazeFactorySingleton {
public:
    static MazeFactorySingleton* Instance() {
        if (_instance == nullptr) {
            const char* style = std::getenv("MAZESTYLE");
            if (style != nullptr && std::strcmp(style, "bombed") == 0) {
                _instance = new BombedMazeFactorySingleton;
            } else {
                _instance = new MazeFactorySingleton;
            }
        }
        return _instance;
    }

    virtual Maze* MakeMaze() { return new Maze; }
    virtual Wall* MakeWall() { return new Wall; }

protected:
    MazeFactorySingleton() = default;

private:
    static MazeFactorySingleton* _instance;
};

MazeFactorySingleton* MazeFactorySingleton::_instance = nullptr;
```

---

## Chapter 4: Structural Patterns

### 1. Adapter Pattern Examples

#### C++ Class Adapter (Multiple Inheritance)
```cpp
class Shape {
public:
    Shape();
    virtual void BoundingBox(Point& bottomSide, Point& topSide) const;
    virtual Manipulator* CreateManipulator() const;
};

class TextView {
public:
    TextView();
    void GetOrigin(Coord& x, Coord& y) const;
    void GetExtent(Coord& width, Coord& height) const;
    virtual bool IsEmpty() const;
};

// Class Adapter: Public Target, Private Adaptee
class TextShape : public Shape, private TextView {
public:
    TextShape();
    virtual void BoundingBox(Point& bottomSide, Point& topSide) const;
    virtual bool IsEmpty() const;
    virtual Manipulator* CreateManipulator() const;
};

void TextShape::BoundingBox(Point& bottomSide, Point& topSide) const {
    Coord x, y, width, height;
    GetOrigin(x, y);
    GetExtent(width, height);
    bottomSide = Point(x, y);
    topSide = Point(x + width, y + height);
}

bool TextShape::IsEmpty() const {
    return TextView::IsEmpty();
}

Manipulator* TextShape::CreateManipulator() const {
    return new TextManipulator(this);
}
```

#### C++ Object Adapter (Composition)
```cpp
class TextShape : public Shape {
public:
    TextShape(TextView*);
    virtual void BoundingBox(Point& bottomSide, Point& topSide) const;
    virtual bool IsEmpty() const;
    virtual Manipulator* CreateManipulator() const;
private:
    TextView* _text;
};

TextShape::TextShape(TextView* t) : _text(t) {}

void TextShape::BoundingBox(Point& bottomSide, Point& topSide) const {
    Coord x, y, width, height;
    _text->GetOrigin(x, y);
    _text->GetExtent(width, height);
    bottomSide = Point(x, y);
    topSide = Point(x + width, y + height);
}

bool TextShape::IsEmpty() const {
    return _text->IsEmpty();
}

Manipulator* TextShape::CreateManipulator() const {
    return new TextManipulator(this);
}
```

---

### 2. Bridge Pattern Examples

#### C++ Window/WindowImp Structural Setup
```cpp
class WindowImp;
class View;

class Window {
public:
    Window(View* contents);
    virtual void DrawContents();
    virtual void DrawRect(const Point& a, const Point& b);
protected:
    WindowImp* GetWindowImp();
    View* GetView();
private:
    WindowImp* _imp;
    View* _contents;
};

class WindowImp {
public:
    virtual void DeviceRect(Coord x0, Coord y0, Coord x1, Coord y1) = 0;
    virtual void DeviceLine(Coord x0, Coord y0, Coord x1, Coord y1) = 0;
protected:
    WindowImp();
};

void Window::DrawRect(const Point& a, const Point& b) {
    WindowImp* imp = GetWindowImp();
    imp->DeviceRect(a.X(), a.Y(), b.X(), b.Y());
}

// X Window Concrete Implementor
class XWindowImp : public WindowImp {
public:
    virtual void DeviceRect(Coord x0, Coord y0, Coord x1, Coord y1) {
        int x = round(min(x0, x1));
        int y = round(min(y0, y1));
        int w = round(abs(x0 - x1));
        int h = round(abs(y0 - y1));
        XDrawRectangle(_dpy, _winid, _gc, x, y, w, h);
    }
private:
    Display* _dpy;
    Drawable _winid;
    GC _gc;
};
```

---

### 3. Composite Pattern Examples

#### C++ Computer Parts Equipment Composition
```cpp
class Equipment {
public:
    virtual ~Equipment();
    const char* Name() const { return _name; }
    virtual Watt Power();
    virtual Currency NetPrice();
    virtual void Add(Equipment*);
    virtual void Remove(Equipment*);
    virtual Iterator* CreateIterator();
protected:
    Equipment(const char* name) : _name(name) {}
private:
    const char* _name;
};

class FloppyDisk : public Equipment {
public:
    FloppyDisk(const char* name) : Equipment(name) {}
    virtual Watt Power() { return 5.0; }
    virtual Currency NetPrice() { return 25.00; }
};

class CompositeEquipment : public Equipment {
public:
    virtual Currency NetPrice() {
        Iterator* i = CreateIterator();
        Currency total = 0.0;
        for (i->First(); !i->IsDone(); i->Next()) {
            total += i->CurrentItem()->NetPrice();
        }
        delete i;
        return total;
    }
    virtual void Add(Equipment* e) { _equipment.Append(e); }
    virtual void Remove(Equipment* e) { _equipment.Remove(e); }
    virtual Iterator* CreateIterator() { return new ListIterator<Equipment*>(&_equipment); }
protected:
    CompositeEquipment(const char* name) : Equipment(name) {}
private:
    List<Equipment*> _equipment;
};
```

---

### 4. Decorator Pattern Examples

#### C++ Graphical User Interface Decorators
```cpp
class VisualComponent {
public:
    virtual void Draw();
    virtual void Resize();
};

class Decorator : public VisualComponent {
public:
    Decorator(VisualComponent* component) : _component(component) {}
    virtual void Draw() { _component->Draw(); }
    virtual void Resize() { _component->Resize(); }
private:
    VisualComponent* _component;
};

class BorderDecorator : public Decorator {
public:
    BorderDecorator(VisualComponent* c, int width) : Decorator(c), _width(width) {}
    virtual void Draw() {
        Decorator::Draw();
        DrawBorder(_width);
    }
private:
    void DrawBorder(int w);
    int _width;
};
```

---

### 5. Facade Pattern Examples

#### C++ Compiler Subsystem Facade
```cpp
class Compiler {
public:
    virtual void Compile(istream& input, BytecodeStream& output) {
        Scanner scanner(input);
        ProgramNodeBuilder builder;
        Parser parser;
        
        parser.Parse(scanner, builder);
        
        RISCCodeGenerator generator(output);
        ProgramNode* parseTree = builder.GetRootNode();
        parseTree->Traverse(generator);
    }
};
```

---

### 6. Flyweight Pattern Examples

#### C++ Character Flyweight Context mapping
```cpp
class Glyph {
public:
    virtual void Draw(Window*, GlyphContext&);
};

class Character : public Glyph {
public:
    Character(char charcode) : _charcode(charcode) {}
    virtual void Draw(Window* w, GlyphContext& gc) {
        w->DrawCharacter(_charcode, gc.GetFont());
    }
private:
    char _charcode; // Intrinsic state
};
```

---

### 7. Proxy Pattern Examples

#### C++ Virtual Proxy (Lazy Loading)
```cpp
class Graphic {
public:
    virtual void Draw(const Point& at) = 0;
    virtual const Point& GetExtent() = 0;
};

class Image : public Graphic {
public:
    Image(const char* file);
    virtual void Draw(const Point& at);
    virtual const Point& GetExtent();
};

class ImageProxy : public Graphic {
public:
    ImageProxy(const char* filename) : _image(0), _extent(Point::Zero) {
        _fileName = strdup(filename);
    }
    virtual void Draw(const Point& at) {
        GetImage()->Draw(at);
    }
    virtual const Point& GetExtent() {
        if (_extent == Point::Zero) {
            _extent = GetImage()->GetExtent();
        }
        return _extent;
    }
protected:
    Image* GetImage() {
        if (_image == 0) {
            _image = new Image(_fileName); // Lazy load
        }
        return _image;
    }
private:
    Image* _image;
    Point _extent;
    char* _fileName;
};
```

---

## Chapter 5: Behavioral Patterns

### 1. Chain of Responsibility C++ Call Invocation
```cpp
class HelpHandler {
public:
    HelpHandler(HelpHandler* s = 0, Topic t = NO_HELP_TOPIC) : _successor(s), _topic(t) {}
    virtual bool HasHelp() { return _topic != NO_HELP_TOPIC; }
    virtual void HandleHelp() {
        if (_successor != 0) {
            _successor->HandleHelp();
        }
    }
private:
    HelpHandler* _successor;
    Topic _topic;
};

// Client call
button->HandleHelp();
```

### 2. Command Pattern C++ Template Command
```cpp
template <class Receiver>
class SimpleCommand : public Command {
public:
    typedef void (Receiver::* Action)();
    SimpleCommand(Receiver* r, Action a) : _receiver(r), _action(a) {}
    virtual void Execute() {
        (_receiver->*_action)();
    }
private:
    Action _action;
    Receiver* _receiver;
};

// Usage
MyClass* receiver = new MyClass;
Command* aCommand = new SimpleCommand<MyClass>(receiver, &MyClass::Action);
aCommand->Execute();
```

### 3. Interpreter Boolean Expression AST Evaluation
```cpp
class BooleanExp {
public:
    virtual bool Evaluate(Context&) = 0;
};

class AndExp : public BooleanExp {
public:
    AndExp(BooleanExp* op1, BooleanExp* op2) : _operand1(op1), _operand2(op2) {}
    virtual bool Evaluate(Context& c) {
        return _operand1->Evaluate(c) && _operand2->Evaluate(c);
    }
private:
    BooleanExp* _operand1;
    BooleanExp* _operand2;
};

// Client parsing tree evaluation
Context context;
VariableExp* x = new VariableExp("X");
VariableExp* y = new VariableExp("Y");
BooleanExp* expression = new AndExp(x, y);
context.Assign(x, true);
context.Assign(y, false);
bool result = expression->Evaluate(context); // false
```

### 4. Iterator Polymorphic Traversal (C++)
```cpp
template <class Item>
class Iterator {
public:
    virtual void First() = 0;
    virtual void Next() = 0;
    virtual bool IsDone() const = 0;
    virtual Item CurrentItem() const = 0;
};

void PrintEmployees(Iterator<Employee*>& i) {
    for (i.First(); !i.IsDone(); i.Next()) {
        i.CurrentItem()->Print();
    }
}
```

### 5. Mediator FontDialogDirector Coordination (C++)
```cpp
class DialogDirector {
public:
    virtual void WidgetChanged(Widget*) = 0;
};

class FontDialogDirector : public DialogDirector {
public:
    virtual void WidgetChanged(Widget* w) {
        if (w == _fontList) {
            _fontNameEntry->SetText(_fontList->GetSelection());
        } else if (w == _okButton) {
            ApplyFontChange();
            DismissDialog();
        }
    }
private:
    ListBox* _fontList;
    EntryField* _fontNameEntry;
    Button* _okButton;
};
```

### 6. Memento Undo Checkpoint saving (C++)
```cpp
class MoveCommand {
public:
    MoveCommand(Graphic* target, const Point& delta) : _target(target), _delta(delta) {}
    void Execute() {
        ConstraintSolver* solver = ConstraintSolver::Instance();
        _state = solver->CreateMemento(); // Checkpoint state
        _target->Move(_delta);
        solver->Solve();
    }
    void Unexecute() {
        ConstraintSolver* solver = ConstraintSolver::Instance();
        _target->Move(-_delta);
        solver->SetMemento(_state); // Restore state
        solver->Solve();
    }
private:
    ConstraintSolverMemento* _state;
    Point _delta;
    Graphic* _target;
};
```

### 7. Observer ClockTimer updates (C++)
```cpp
class Subject {
public:
    virtual void Attach(Observer* o) { _observers.Append(o); }
    virtual void Notify() {
        for (Observer* o : _observers) o->Update(this);
    }
private:
    List<Observer*> _observers;
};

class DigitalClock : public Widget, public Observer {
public:
    DigitalClock(ClockTimer* s) : _subject(s) { _subject->Attach(this); }
    virtual void Update(Subject* s) {
        if (s == _subject) Draw();
    }
};
```

### 8. State TCPConnection class switching (C++)
```cpp
class TCPState;

class TCPConnection {
public:
    void ActiveOpen() { _state->ActiveOpen(this); }
    void ChangeState(TCPState* s) { _state = s; }
private:
    TCPState* _state;
};

class TCPEstablished : public TCPState {
public:
    static TCPState* Instance();
    virtual void Close(TCPConnection* t) {
        // Send FIN, receive ACK...
        t->ChangeState(TCPClosed::Instance());
    }
};
```

### 9. Strategy Compositor algorithm selection (C++)
```cpp
class Composition {
public:
    Composition(Compositor* c) : _compositor(c) {}
    void Repair() {
        _compositor->Compose(_natural, _stretch, _shrink, _componentCount, _lineWidth, _breaks);
    }
private:
    Compositor* _compositor;
};
```

### 10. Template Method View rendering skeleton (C++)
```cpp
class View {
public:
    void Display() {
        SetFocus();
        DoDisplay(); // Primitive Hook
        ResetFocus();
    }
protected:
    virtual void DoDisplay() {} // Default empty implementation
};

class CustomView : public View {
protected:
    virtual void DoDisplay() {
        // Concrete rendering logic
    }
};
```

### 11. Visitor Double Dispatch element processing (C++)
```cpp
class EquipmentVisitor {
public:
    virtual void VisitFloppyDisk(FloppyDisk*) = 0;
    virtual void VisitChassis(Chassis*) = 0;
};

void FloppyDisk::Accept(EquipmentVisitor& v) {
    v.VisitFloppyDisk(this);
}

void Chassis::Accept(EquipmentVisitor& v) {
    for (Equipment* e : _parts) e->Accept(v);
    v.VisitChassis(this);
}
```

---

## Appendices

### C++ Foundation Class Interface Definitions (Appendix C)

```cpp
// Coordinate system typedef
typedef float Coord;

// ==========================================
// C.1 List template class interface
// ==========================================
template <class Item>
class List {
public:
    // Construction, Destruction, Initialization, and Assignment
    List(long size = 10);
    List(const List& other);
    ~List();
    List& operator=(const List& other);

    // Accessing
    long Count() const;
    Item& Get(long index) const;
    Item& First() const;
    Item& Last() const;

    // Adding
    void Append(const Item& item);
    void Prepend(const Item& item);

    // Removing
    void Remove(const Item& item);
    void RemoveFirst();
    void RemoveLast();
    void RemoveAll();

    // Stack Interface
    Item& Top() const;
    void Push(const Item& item);
    Item& Pop();
};

// ==========================================
// C.2 Iterator abstract class template interface
// ==========================================
template <class Item>
class Iterator {
public:
    virtual ~Iterator() {}
    virtual void First() = 0;
    virtual void Next() = 0;
    virtual bool IsDone() const = 0;
    virtual Item CurrentItem() const = 0;
protected:
    Iterator() {}
};

// ==========================================
// C.3 ListIterator concrete subclass interface
// ==========================================
template <class Item>
class ListIterator : public Iterator<Item> {
public:
    ListIterator(const List<Item>* list);
    
    virtual void First();
    virtual void Next();
    virtual bool IsDone() const;
    virtual Item CurrentItem() const;

private:
    const List<Item>* _list;
    long _current;
};

// ==========================================
// C.4 Point class interface
// ==========================================
class Point {
public:
    static const Point Zero;

    Point(Coord x = 0.0, Coord y = 0.0);

    Coord X() const;
    void X(Coord x);
    Coord Y() const;
    void Y(Coord y);

    Point& operator+=(const Point& other);
    Point& operator-=(const Point& other);
    Point& operator*=(double scalar);
    Point& operator/=(double scalar);
    Point operator-() const;

    friend Point operator+(const Point& p1, const Point& p2);
    friend Point operator-(const Point& p1, const Point& p2);
    friend Point operator*(const Point& p, double scalar);
    friend Point operator*(double scalar, const Point& p);
    friend Point operator/(const Point& p, double scalar);
    friend bool operator==(const Point& p1, const Point& p2);
    friend bool operator!=(const Point& p1, const Point& p2);
};

// ==========================================
// C.5 Rect class interface
// ==========================================
class Rect {
public:
    static const Rect Zero;

    Rect(Coord x, Coord y, Coord w, Coord h);
    Rect(const Point& origin, const Point& extent);

    Coord Width() const;
    void Width(Coord w);
    Coord Height() const;
    void Height(Coord h);

    Point Origin() const;
    void Origin(const Point& origin);
    Point Extent() const;
    void Extent(const Point& extent);

    Coord Left() const;
    Coord Bottom() const;
};
```

### Concrete Usage Example: Traversing a polymorphic collection of Shape objects

```cpp
#include <iostream>

// Abstract Shape class
class Shape {
public:
    virtual ~Shape() {}
    virtual void Draw() = 0;
};

// Concrete Circle shape
class Circle : public Shape {
public:
    virtual void Draw() {
        std::cout << "Drawing a Circle.\n";
    }
};

// Concrete Square shape
class Square : public Shape {
public:
    virtual void Draw() {
        std::cout << "Drawing a Square.\n";
    }
};

int main() {
    // Create a heterogeneous list of Shapes using the custom List class
    List<Shape*> shapes;
    
    Circle c;
    Square s;
    
    shapes.Append(&c);
    shapes.Append(&s);
    
    // Instantiate a ListIterator to traverse the List polymorphically
    ListIterator<Shape*> iterator(&shapes);
    
    for (iterator.First(); !i.IsDone(); iterator.Next()) {
        Shape* shape = iterator.CurrentItem();
        shape->Draw();
    }
    
    return 0;
}
```
