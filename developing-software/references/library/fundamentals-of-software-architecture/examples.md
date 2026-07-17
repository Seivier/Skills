# Fundamentals of Software Architecture: An Engineering Approach

## Índice de capítulos
- [Praise for *Fundamentals of Software Architecture*](#praise-for-fundamentals-of-software-architecture)
- [Fundamentals of Software Architecture](#fundamentals-of-software-architecture)
- [Revision History for the First Edition](#revision-history-for-the-first-edition)
- [Preface: Invalidating Axioms](#preface-invalidating-axioms)
- [Conventions Used in This Book](#conventions-used-in-this-book)
- [Using Code Examples](#using-code-examples)
- [O’Reilly Online Learning](#oreilly-online-learning)
- [How to Contact Us](#how-to-contact-us)
- [Acknowledgments](#acknowledgments)
- [Chapter 1. Introduction](#chapter-1-introduction)
- [Part I. Foundations](#part-i-foundations)
- [Chapter 2. Architectural Thinking](#chapter-2-architectural-thinking)
- [Chapter 3. Modularity](#chapter-3-modularity)
- [Chapter 4. Architecture Characteristics Defined](#chapter-4-architecture-characteristics-defined)
- [Chapter 5. Identifying Architectural Characteristics](#chapter-5-identifying-architectural-characteristics)
- [Chapter 6. Measuring and Governing Architecture Characteristics](#chapter-6-measuring-and-governing-architecture-characteristics)
- [Chapter 7. Scope of Architecture Characteristics](#chapter-7-scope-of-architecture-characteristics)
- [Chapter 8. Component-Based Thinking](#chapter-8-component-based-thinking)
- [Part II. Architecture Styles](#part-ii-architecture-styles)
- [Chapter 9. Foundations](#chapter-9-foundations)
- [Chapter 10. Layered Architecture Style](#chapter-10-layered-architecture-style)
- [Chapter 11. Pipeline Architecture Style](#chapter-11-pipeline-architecture-style)
- [Chapter 12. Microkernel Architecture Style](#chapter-12-microkernel-architecture-style)
- [Chapter 13. Service-Based Architecture Style](#chapter-13-service-based-architecture-style)
- [Chapter 14. Event-Driven Architecture Style](#chapter-14-event-driven-architecture-style)
- [Chapter 15. Space-Based Architecture Style](#chapter-15-space-based-architecture-style)
- [Chapter 16. Orchestration-Driven Service-Oriented Architecture](#chapter-16-orchestration-driven-service-oriented-architecture)
- [Chapter 17. Microservices Architecture](#chapter-17-microservices-architecture)
- [Chapter 18. Choosing the Appropriate Architecture Style](#chapter-18-choosing-the-appropriate-architecture-style)
- [Part III. Techniques and Soft Skills](#part-iii-techniques-and-soft-skills)
- [Chapter 19. Architecture Decisions](#chapter-19-architecture-decisions)
- [Chapter 20. Analyzing Architecture Risk](#chapter-20-analyzing-architecture-risk)
- [Chapter 21. Diagramming and Presenting Architecture](#chapter-21-diagramming-and-presenting-architecture)
- [Chapter 22. Making Teams Effective](#chapter-22-making-teams-effective)
- [Chapter 23. Negotiation and Leadership Skills](#chapter-23-negotiation-and-leadership-skills)
- [Chapter 24. Developing a Career Path](#chapter-24-developing-a-career-path)
- [Index](#index)
- [About the Authors](#about-the-authors)
- [Colophon](#colophon)

## Praise for *Fundamentals of Software Architecture*

No technical examples, code, patterns, or architectural diagrams are present in this praise section. This is purely endorsement and promotional material containing no concrete architectural case studies or illustrative material.

## Fundamentals of Software Architecture

No code examples, case studies, or technical diagrams are present in this range. This section contains exclusively publication and copyright metadata.

## Revision History for the First Edition

No code examples or architectural patterns are present in this range. The section contains only metadata, legal text, and HTML formatting for copyright and revision information.

## Preface: Invalidating Axioms

Kubernetes—cited as a tool that didn't exist a decade ago yet now has entire software conferences devoted to its users, exemplifying how the software ecosystem exhibits dynamic behavior. The evolution of the formal definition of software architecture itself: "the stuff that's hard to change later" (the old definition) versus microservices architecture where "change is a first-class design consideration" (the new paradigm). The progression of engineering practices and methodologies: Extreme Programming, Continuous Delivery, the DevOps revolution, microservices, containerization, and cloud-based resources. The contrast between craft and engineering disciplines: craft involves skilled artisans creating one-off works, while engineering implies repeatability, rigor, and effective analysis.

## Conventions Used in This Book

Italic example: filenames and URLs. Constant width example: variable or function names, databases, data types. Constant width bold example: `$ command-to-type`. Constant width italic example: `path/to/user-supplied-value`. Tip element: a visually distinct block labeled 'Tip' that signifies a tip or suggestion.

## Using Code Examples

No code examples, diagrams, or technical case studies appear in this range. The section is purely administrative and legal in nature, containing no architectural, technical, or illustrative material to extract.

## O’Reilly Online Learning

No code examples, diagrams, or case studies are present in this range. The section contains only promotional and informational text about O'Reilly's services and does not include any technical architecture examples.

## How to Contact Us

No code fragments, diagrams, or technical examples are present in this section. This is standard publisher colophon material containing only contact information and web URLs.

## Acknowledgments

Named individuals and organizations acknowledged: Rebecca Zimmerman (Mark Richards' wife), Jay Zimmerman (No Stuff Just Fluff director), O'Reilly (publishing team), ThoughtWorks (Neal Ford's employer), Rebecca Parsons, Martin Fowler, Candy (Neal Ford's wife). Communities mentioned: Pasty Geeks and Hacker B&B (described as "random oases of sanity-preserving and idea-sparking groups"), neighborhood cocktail club.

## Chapter 1. Introduction

Architectural patterns and styles mentioned: microservices, layered architecture, microkernel, Space-Based Architecture, ESB-driven SOA, application silos (where each application database is only accessible from the application owning that database).

Design patterns: Strangler Pattern (referenced as https://oreil.ly/ZRpCc), strategy pattern, feature toggles (referenced as trunkbaseddevelopment.com).

Technology frameworks: React.js, Angular, Elm, Vue (all cited as examples of reactive-based frameworks for frontend development).

Specific architecture decision example: "only the business and services layers within a layered architecture can access the database, restricting the presentation layer from making direct database calls."

Design principle example: "the development teams should leverage asynchronous messaging between services within a microservices architecture to increase performance."

Fitness function example: "page load time test measuring load time for each page and running the test as part of continuous integration for the project."

Historical example: Pets.com, which failed during its Christmas rush because it had invested in marketing (a famous sock puppet mascot) rather than elastic scale infrastructure to handle demand surge.

Quote on unknown unknowns from Donald Rumsfeld: "there are known knowns; there are things we know we know...known unknowns...But there are also unknown unknowns—the ones we don't know we don't know."

Quote from Mark (co-author): "All architectures become iterative because of unknown unknowns, Agile just recognizes this and does it sooner."

## Part I. Foundations

No code examples, case studies, diagrams, or concrete patterns are present in this range. This is a structural part divider, not an instructional or analytical section.

## Chapter 2. Architectural Thinking

The auction system case study is the primary concrete example. A Bid Producer generates bids and sends them to three services: Bid Capture, Bid Tracking, and Bid Analytics. The chapter diagrams two approaches: using a topic where the Bid Producer connects once and services subscribe (publish-and-subscribe model), versus using three separate queues (point-to-point model). When the requirement arises to add a Bid History service, the topic approach requires no changes to existing infrastructure (the new service simply subscribes), while the queue approach requires adding a new queue and modifying the Bid Producer for an additional connection. Table 2-1 summarizes the trade-offs: Topic advantages include architectural extensibility and service decoupling; topic disadvantages include data access and data security concerns, no heterogeneous contracts support, and lack of monitoring and programmatic scalability. A sidebar example (Frozen Caveman Anti-Pattern) describes an architect who persistently asks "But what if we lose Italy?" in every design review, stemming from a freak communication failure years prior that prevented headquarters from reaching stores in Italy. Tools mentioned include ArchUnit (Java platform for automating architectural compliance) and fitness functions (custom code ensuring architectural compliance).

## Chapter 3. Modularity

Code example from the Connascence of Execution section (lines 3031-3038):
```
email = new Email();
email.setRecipient("foo@example.com");
email.setSender("me@me.com");
email.send();
email.setSubject("whoops");
```
This code fails because properties must be set in order before sending the email.

Connascence of Position example (lines 2999-3002): A method updateSeat(String name, String seatLocation) called with updateSeat("14D", "Ford, N") where the types are correct (both strings) but semantics are wrong—the seat number and person name are reversed.

Connascence of Meaning example (lines 2989-2992): Hard-coded integer values like int TRUE = 1; int FALSE = 0, where problems arise if values are flipped.

Logical cohesion example (lines 2535-2538): StringUtils package containing static methods operating on String but otherwise unrelated to each other.

Four LCOM diagrams are referenced: Figure 3-1 illustrates LCOM using octagons for fields and squares for methods in three classes (X with low LCOM, Y with high lack of cohesion, Z with mixed cohesion). Figures 3-2, 3-3, 3-4 illustrate the Main Sequence relationship: Figure 3-2 graphs the ideal abstractness-instability relationship; Figure 3-3 shows normalized distance calculation for a particular class; Figure 3-4 shows zones of uselessness (upper-right) and pain (lower-left). Figure 3-5 displays strength rankings of different connascence types for refactoring guidance. Figure 3-6 unifies coupling concepts (afferent/efferent on left) with connascence characteristics (right).

## Chapter 4. Architecture Characteristics Defined

Payment security structural impact example: When handling third-party payment processor integration, architecture doesn't require special structural considerations—standard security hygiene (encryption, hashing) suffices. When processing payments in-application, the architect designs a specific module, component, or service structurally isolating critical security concerns.

Italy-ility case study: A firm operating centralized architecture experienced communication loss with Italian branches during a freak outage, proving organizationally traumatic. Future architectures required a unique characteristic the team called 'Italy-ility'—combining availability, recoverability, and resilience to ensure losing branch communication doesn't cripple operations.

UDP vs. TCP availability/reliability distinction: UDP is available over IP (underlying TCP) but unreliable—packets may arrive out of order and the receiver must request missing packets again, illustrating that availability and reliability, though overlapping, differ meaningfully.

Interoperability vs. compatibility: Interoperability implies published, documented APIs enabling easy integration with other systems; compatibility concerns industry and domain standards adherence—though systems may treat them equivalently, the distinction matters for architecture design.

Figure 4-1 illustrates that software solutions consist of both domain requirements and architectural characteristics as separate, co-equal concerns. Figure 4-2 depicts architecture characteristics as a triangle where three components (nondomain design consideration, structural influence, critical to success) support each other mutually, with trade-offs emerging from their interaction.

## Chapter 5. Identifying Architectural Characteristics

The Vasa case study: A Swedish warship built 1626-1628 by King Adolphus was designed to be both a troop transport and gunship with two decks and double-sized cannons (when most ships had one deck and standard cannons). Despite expert shipbuilders' concerns, the project proceeded. The ship capsized on its maiden voyage in Stockholm harbor after firing a cannon salute, then sat on the bay bottom until early 20th-century salvage recovered it for a museum—illustrating the failure of over-specifying architecture characteristics.

Table 5-1 (translated domain concerns to architectural characteristics):
- Mergers and acquisitions → Interoperability, scalability, adaptability, extensibility
- Time to market → Agility, testability, deployability
- User satisfaction → Performance, availability, fault tolerance, testability, deployability, agility, security
- Competitive advantage → Agility, testability, deployability, scalability, availability, fault tolerance
- Time and budget → Simplicity, feasibility

Silicon Sandwiches kata description: "A national sandwich shop wants to enable online ordering (in addition to its current call-in service). Users: Thousands, perhaps one day millions. Requirements: Users place orders, receive pickup times and directions integrating external mapping services with traffic; conditional delivery service dispatch; mobile-device accessibility; national daily promotions/specials; local daily promotions/specials; payment acceptance online, in-person, or upon delivery. Additional context: Franchised locations with different owners; near-future overseas expansion plans; corporate goal of hiring inexpensive labor to maximize profit."

Explicit characteristics extraction examples:
- "Thousands, perhaps one day millions" users → Scalability (concurrent user handling without performance degradation)
- Peak mealtime traffic patterns (inferred from sandwich shop domain knowledge) → Elasticity (handling traffic bursts)
- Mobile-device requirement → Performance characteristics for mobile page load times
- National and local promotions plus custom mapping → Customizability

The authors distinguish scalability (measuring performance of concurrent users shown as a linear graph) from elasticity (measuring bursts of traffic shown as spiky graph).

Implicit characteristics:
- Availability: Making sure users can access the site
- Reliability: Maintaining connections without forcing re-authentication
- Security: Implicit in every system but may not require structural design if payments handled by third party

Design vs. Architecture trade-off example: Customizability could be implemented as: (1) Microkernel architecture style with structural plug-in support for customization, or (2) Another architecture style with Template Method design pattern allowing parent classes to define workflow overridden in child classes. The choice depends on performance/coupling trade-offs, other desirable characteristics, and implementation costs.

Quote: "There are no wrong answers in architecture, only expensive ones" (Mark Richards)

## Chapter 6. Measuring and Governing Architecture Characteristics

Code snippet from Example 6-1 (Sample code for cyclomatic complexity evaluation):
```
public void decision(int c1, int c2) {
    if (c1 < 100)
        return 0;
    else if (c1 + C2 > 500)
       return 1;
    else
      return -1;
}
```
This function has cyclomatic complexity of 3 (= 5 nodes – 4 edges + 2).

Code snippet from Example 6-2 (Fitness function to detect component cycles using JDepend):
```
public class CycleTest {
    private JDepend jdepend;

    @BeforeEach
    void init() {
	  jdepend = new JDepend();
	  jdepend.addDirectory("/path/to/project/persistence/classes");
	  jdepend.addDirectory("/path/to/project/web/classes");
	  jdepend.addDirectory("/path/to/project/thirdpartyjars");
    }

    @Test
    void testAllPackages() {
	  Collection packages = jdepend.analyze();
	  assertEquals("Cycles exist", false, jdepend.containsCycles());
    }
}
```

Code snippet from Example 6-3 (Distance from the main sequence fitness function):
```
@Test
void AllPackages() {
    double ideal = 0.0;
    double tolerance = 0.5; // project-dependent
    Collection packages = jdepend.analyze();
    Iterator iter = packages.iterator();
    while (iter.hasNext()) {
      JavaPackage p = (JavaPackage)iter.next();
      assertEquals("Distance exceeded: " + p.getName(),
	    ideal, p.distance(), tolerance);
    }
}
```

Code snippet from Example 6-4 (ArchUnit fitness function to govern layers):
```
layeredArchitecture()
    .layer("Controller").definedBy("..controller..")
    .layer("Service").definedBy("..service..")
    .layer("Persistence").definedBy("..persistence..")

    .whereLayer("Controller").mayNotBeAccessedByAnyLayer()
    .whereLayer("Service").mayOnlyBeAccessedByLayers("Controller")
    .whereLayer("Persistence").mayOnlyBeAccessedByLayers("Service")
```

Code snippet from Example 6-5 (NetArchTest for layer dependencies in C#):
```
// Classes in the presentation should not directly reference repositories
var result = Types.InCurrentDomain()
    .That()
    .ResideInNamespace("NetArchTest.SampleLibrary.Presentation")
    .ShouldNot()
    .HaveDependencyOn("NetArchTest.SampleLibrary.Data")
    .GetResult()
    .IsSuccessful;
```

Case study: Netflix's Simian Army includes Conformity Monkey (enforces governance rules such as services responding to all RESTful verbs), Security Monkey (checks for known security defects and port/configuration errors), and Janitor Monkey (identifies and disintegrates services with no incoming traffic from collaborators, reducing cloud costs). These emerged from Netflix's migration to AWS where they lost operational control and spawned chaos engineering as a discipline.

## Chapter 7. Scope of Architecture Characteristics

The Payment and Auction services example demonstrates synchronous versus asynchronous connascence: a Payment service that can only handle one payment every 500 ms will face timeout failures if multiple auctions end simultaneously and synchronous calls are made. An architect might instead design asynchronous communication where a message queue temporarily buffers differences, allowing the architecture to be more flexible via asynchronous connascence.

The Going, Going, Gone architecture kata provides a complete case study. The architecture kata description specifies an auction company scaling nationwide with hundreds to thousands of simultaneous participants, real-time auctions, automated credit card charging, reputation tracking, live video streaming, and precise bid ordering. The case analysis identifies three distinct architectural quanta with their respective characteristics: (1) Bidder feedback quantum encompassing the bid stream and video stream requires availability, scalability, and performance; (2) Auctioneer quantum for the live auctioneer requires availability, reliability, scalability, elasticity, performance, and security; (3) Bidder quantum for online bidders and bidding requires reliability, availability, scalability, and elasticity. This decomposition demonstrates that rather than applying a single set of architecture characteristics uniformly across the system, different components require different emphasis and design choices based on their functional scope and operational dependencies.

## Chapter 8. Component-Based Thinking

Component scope examples: libraries (jar files in Java, dll in .NET, gem in Ruby) running in the same memory address space with function call communication as compile-time dependencies; subsystems and layers as architectural components; services running in separate address spaces communicating via TCP/IP, REST, or message queues as standalone deployable units in microservices.

Architecture partitioning styles: layered monolith organizing by technical capabilities (presentation, business rules, services, persistence layers); modular monolith organizing around business domains. The CatalogCheckout workflow example shows how a single business process spans all layers in technical partitioning but resides within a single top-level CatalogCheckout component in domain partitioning.

Silicon Sandwiches case study components: domain-partitioned design includes Purchase, Promotion, MakeOrder, ManageInventory, Recipes, Delivery, and Location with embedded customization subcomponents (common and local variations); technically partitioned design isolates Common and Local as top-level components with Purchase and Delivery remaining as workflow components.

Component identification flow cycle: identify initial components → assign requirements to components → analyze roles and responsibilities → analyze architecture characteristics → restructure components based on feedback.

Component discovery techniques: entity trap anti-pattern of creating Manager components (UserManager, OrderManager, InventoryManager) directly from database entities; Actor/Actions approach identifying bidder/auctioneer/system roles and their actions; Event storming from DDD building components around event and message handlers; Workflow approach identifying roles, their workflows, and building components around activities without explicit messaging constraints.

Going, Going, Gone case study initial components: VideoStreamer (streams live auction), BidStreamer (streams bid updates, read-only), BidCapture (captures bids from both sources), BidTracker (records bids, system of record), AuctionSession (manages auction lifecycle and payment), Payment (third-party processor). Refined design adds AuctioneerCapture (separate component for auctioneer bid input) to accommodate higher reliability and availability requirements for the auctioneer role versus bidders, with BidTracker unifying the single auctioneer stream and multiple bidder streams.

Monolithic architecture: single deployable unit, all functionality in one process, single database; includes layered and modular monolith types.

Distributed architecture: multiple services in separate ecosystems communicating via networking protocols, potentially with independent release cadences and engineering practices per service.

Conway's Law observation: organizations designing systems produce designs copying their communication structures. Inverse Conway Maneuver (coined by Jonny Leroy of ThoughtWorks): evolve team and organizational structure together to promote desired architecture.

## Part II. Architecture Styles

The text provides the following concrete examples: (1) Layers of a monolithic deployment—an organizational structure illustrating one architecture style; (2) Separately deployed services—an organizational structure illustrating a different architecture style; (3) Achieving high scalability within a set of operations or between sets of services—cited as examples of problems that architecture patterns (rather than styles) address within a chosen style.

## Chapter 9. Foundations

Real-world Big Ball of Mud case: Neal's client project created a Java-based web application rapidly over years. The technical visualization showed each dot on a circle's perimeter representing a class, each line representing connections between classes, with bolder lines indicating stronger connections. Any change to a class made it difficult to predict rippling side effects to other classes, making change terrifying.

Stamp coupling example: A wish list service calls a customer profile service to retrieve customer names needed in the response. The customer profile service returns 45 attributes totaling 500 kb, but the wish list service only needs the name (200 bytes). At 2,000 requests per second, this single interservice call consumes 1 Gb of bandwidth. Reducing the return to only needed data (200 bytes) reduces total bandwidth to 400 kb. Stamp coupling resolutions: create private REST API endpoints, use field selectors in contracts, employ GraphQL, use value-driven contracts with consumer-driven contracts (CDCs), or use internal messaging endpoints.

Java serialization sidebar: During Java language design in the three-tier computing era, assuming all future systems would be three-tier, designers built serialization capability into the language core to move objects over networks consistently between systems—solving a C++ pain point. Every Object in Java implements an interface requiring serialization support. That architectural style came and went, yet serialization artifacts remain in Java to this day, greatly frustrating language designers adding modern features that must support serialization for backward compatibility despite virtually no modern usage.

The three-tier architecture correspondence with network-level protocols: CORBA (Common Object Request Broker Architecture) and DCOM (Distributed Component Object Model) facilitated building distributed architectures, capabilities now existing as either tools like message queues or architecture patterns such as event-driven architecture.

## Chapter 10. Layered Architecture Style

The chapter provides the following concrete examples and scenarios:

1. Organizational alignment: "In most organizations there are user interface (UI) developers, backend developers, rules developers, and database experts (DBAs). These organizational layers fit nicely into the tiers of a traditional layered architecture."

2. Customer domain spread across layers: "For example, the domain of 'customer' is contained in the presentation layer, business layer, rules layer, services layer, and database layer, making it difficult to apply changes to that domain."

3. Presentation layer responsibility example: "The presentation layer would be responsible for handling all user interface and browser communication logic" and "the presentation layer doesn't need to know or worry about how to get customer data; it only needs to display that information on a screen in a particular format."

4. Business layer responsibility example: "The business layer would be responsible for executing specific business rules associated with the request" and "the business layer doesn't need to be concerned about how to format customer data for display on a screen or even where the customer data is coming from; it only needs to get the data from the persistence layer, perform business logic against the data (such as calculating values or aggregating data), and pass that information up to the presentation layer."

5. Layers of isolation example: "For example, you can leverage the layers of isolation concept within the layered architecture style to replace your older JavaServer Faces (JSF) presentation layer with React.js without impacting any other layer in the application."

6. Shared objects in business layer: "For example, suppose there are shared objects within the business layer that contain common functionality for business components (such as date and string utility classes, auditing classes, logging classes, and so on)."

7. Architecture sinkhole anti-pattern scenario: "Suppose the presentation layer responds to a simple request from the user to retrieve basic customer data (such as name and address). The presentation layer passes the request to the business layer, which does nothing but pass the request on to the rules layer, which in turn does nothing but pass the request on to the persistence layer, which then makes a simple SQL call to the database layer to retrieve the customer data. The data is then passed all the way back up the stack with no additional processing or logic to aggregate, calculate, apply rules, or transform the data."

## Chapter 11. Pipeline Architecture Style

Unix shell script example from Doug McIlroy demonstrating pipeline architecture power:

tr -cs A-Za-z '\n' |
tr A-Z a-z |
sort |
uniq -c |
sort -rn |
sed ${1}q

Kafka-based telemetry processing example using pipeline architecture with these specific filters: Service Info Capture filter (producer filter) subscribes to the Kafka topic and receives service information. Duration Filter (tester filter) determines whether captured data is related to service request duration in milliseconds. Duration Calculator (transformer filter) calculates duration metrics and passes modified data forward. Uptime Filter (tester filter) checks if data is related to uptime metrics. Uptime Calculator (transformer filter) calculates uptime metrics for the service. Database Output (consumer filter) persists the modified data to a MongoDB database. The example illustrates extensibility: a new tester filter could be easily added after the Uptime Filter to handle additional metrics such as database connection wait time.

## Chapter 12. Microkernel Architecture Style

Electronic device recycling application: original nested if-else logic for assessing devices (iPhone6s, iPad1, Galaxy5) is replaced with a registry lookup and dynamic plug-in invocation using Class.forName() and reflection. Java plug-in registry example with HashMap containing three entries: point-to-point entry mapping "iPhone6s" to "Iphone6sPlugin"; messaging entry mapping "iPhone6s" to "iphone6s.queue"; RESTful entry mapping "iPhone6s" to "https://atlas:443/assess/iphone6s". AssessmentPlugin interface with methods assess(), register(), deregister(); AssessmentOutput class containing fields assessmentReport (String), resell (Boolean), value (Double), resellPrice (Double). Namespace naming convention: app.plugin.assessment.iphone6s, where the second node indicates plug-in status, the third node describes the domain, and the fourth describes the specific context. Real-world examples include Eclipse IDE (basic text editor as core system, plug-ins add IDE functionality), IntelliJ IDEA, PMD, Jira, Jenkins, Chrome and Firefox browsers (core system plus viewer and plug-in extensions). Insurance claims processing example: core system handles standard filing and processing; jurisdiction-specific claims rules for each state (e.g., free windshield replacement in some states but not others) contained in separate plug-in components implemented as source code or rules engine instances. Tax preparation software example: US 1040 tax form as core system (driver), each line item and supporting form/worksheet (such as gross income calculation) implemented as a separate plug-in component, allowing tax law changes to be isolated to independent plug-ins.

## Chapter 13. Service-Based Architecture Style

The electronics recycling system case study illustrates practical service-based topology: a Customer Facing UI and database for external operations, an internal operations section with Receiving and Recycling/Accounting UIs, and domain services including Quoting, Receiving, Assessment, Accounting, ItemStatus, Recycling, and Reporting. The catalog checkout example shows how the OrderService domain service internally orchestrates placing the order, generating an order ID, applying payment, and updating product inventory as a single atomic transaction, contrasting with microservices that would delegate payment to a separate PaymentService. The database partitioning example shows logical domains: common, customer, invoicing, order, and tracking with corresponding shared libraries (common_entities_lib, customer_entities_lib, invoicing_entities_lib, order_entities_lib, tracking_entities_lib). The UI variant patterns show progression from single monolithic UI to domain-partitioned UIs matching domain services. The database variant patterns progress from monolithic to logically partitioned to fully separate databases. The API layer variant adds a reverse proxy or gateway layer for cross-cutting concerns. The service design patterns show either traditional layered architecture (API facade layer, business layer, persistence layer) or modular monolith with sub-domains within each domain service.

## Chapter 14. Event-Driven Architecture Style

Trading firm trade order processing example: A trading advisor batches trade orders (e.g., '12654A87FR4,BUY,AAPL,1254') and asynchronously sends to a large trading firm. Orders follow contract format: ACCOUNT(String),SIDE(String),SYMBOL(String),SHARES(Long). Sample orders:

12654A87FR4,BUY,AAPL,1254
87R54E3068U,BUY,AAPL,3122
6R4NB7609JJ,BUY,AAPL,5433
2WE35HF6DHF,BUY,AAPL,8756 SHARES  (malformed—extra 'SHARES' text)
764980974R2,BUY,AAPL,1211
1533G658HD8,BUY,AAPL,2654

The fourth order triggers NumberFormatException in TradePlacement.execute(). With workflow event pattern, Trade Placement service delegates the error to Trade Placement Error service and continues processing. The error service fixes '8756 SHARES' to '8756' and resubmits.

Retail order entry system (broker topology): PlaceOrder initiating event triggers OrderPlacement processor creating order and publishing order-created event. Three concurrent processors (Notification, Payment, Inventory) listen to order-created. Payment generates payment-applied or payment-denied events. OrderFulfillment listens to payment-applied. Shipping listens to order-fulfilled. Each processor publishes results (email-sent, inventory-updated, payment-applied/denied, order-fulfilled, order-shipped) enabling downstream processors to react.

Retail order entry (mediator topology): Customer mediator receives PlaceOrder initiating event, orchestrates steps serially between parallel steps: Step 1 generates create-order to OrderPlacement; Step 2 sends email-customer, apply-payment, adjust-inventory concurrently; Step 3 sends fulfill-order and order-stock concurrently; Step 4 sends email-customer and ship-order; Step 5 sends final email-customer. Mediator waits for acknowledgments at each step, enabling error recovery (e.g., payment failure stops workflow, records state, and restarts from step 3 when payment is applied).

## Chapter 15. Space-Based Architecture Style

Java code creating a replicated data grid with Hazelcast:
```
HazelcastInstance hz = Hazelcast.newHazelcastInstance();
Map<String, CustomerProfile> profileCache =
    hz.getReplicatedMap("CustomerProfile");
```

Member list logging showing instance discovery (single instance):
```
Instance 1:
Members {size:1, ver:1} [
    Member [172.19.248.89]:5701 - 04a6f863-dfce-41e5-9d51-9f4e356ef268 this
]
```

Member list after a second instance joins:
```
Instance 1:
Members {size:2, ver:2} [
    Member [172.19.248.89]:5701 - 04a6f863-dfce-41e5-9d51-9f4e356ef268 this
    Member [172.19.248.90]:5702 - ea9e4dd5-5cb3-4b27-8fe8-db5cc62c7316
]

Instance 2:
Members {size:2, ver:2} [
    Member [172.19.248.89]:5701 - 04a6f863-dfce-41e5-9d51-9f4e356ef268
    Member [172.19.248.90]:5702 - ea9e4dd5-5cb3-4b27-8fe8-db5cc62c7316 this
]
```

Data collision scenario: Blue widget inventory example where concurrent updates collide. Initial inventory: 500 units. Service A updates to 490 (10 sold). During replication, Service B updates to 495 (5 sold). Service B cache receives A's 490, then A cache receives B's 495. Correct result should be 485 units, but both caches show incorrect values out of sync.

Data collision rate formula with example calculation:
CollisionRate = N*(UR^2)/S*RL
- Update rate (UR): 20 updates/second
- Number of instances (N): 5
- Cache size (S): 50,000 rows
- Replication latency (RL): 100 milliseconds
Result: 72,000 updates per hour with 14.4 probable collisions (0.02%)

Impact of reducing replication latency from 100ms to 1ms:
Same 72,000 updates per hour but only 0.1 collisions per hour (0.0002%)

Domain-based data writer pattern: Four processing unit types (Profile, WishList, Wallet, Preferences) with four corresponding data pumps all feed into a single customer domain data writer that handles all customer-related database updates.

Replicated vs. Distributed Caching Decision Table:
| Criteria         | Replicated Cache | Distributed Cache |
|------------------|------------------|-------------------|
| Optimization     | Performance      | Consistency       |
| Cache size       | Small (<100 MB)  | Large (>500 MB)   |
| Type of data     | Relatively static| Highly dynamic    |
| Update frequency | Relatively low   | High update rate  |
| Fault tolerance  | High             | Low               |

## Chapter 16. Orchestration-Driven Service-Oriented Architecture

Business Services examples mentioned: ExecuteTrade, PlaceOrder.
Enterprise Services examples: CreateCustomer, CalculateQuote.
Application Services example: geo-location service needed by one application.
Infrastructure Services: monitoring, logging, authentication, authorization.

Domain concept example: CatalogCheckout, illustrating how a simple change like "add a new address line to CatalogCheckout" could require modifications across dozens of services in several different tiers, plus changes to the database schema.

Reuse scenario: Insurance company divisions each having a notion of Customer. The canonical approach extracts Customer as a shared Enterprise Service (Figures 16-3 and 16-4 show this extraction). Auto insurance requires driver's license details (a person property, not vehicle property); disability insurance doesn't care about driver's licenses but must inherit the complexity of the unified Customer definition.

Message flow (Figure 16-2): CreateQuote business-level service calls the service bus, which defines workflow calling CreateCustomer and CalculateQuote, each of which calls application services. The service bus serves as both integration hub and orchestration engine.

Architecture Characteristics ratings (Figure 16-5): Documented in a scorecard with one-star (weak support) to five-star (strong support) ratings. Modern engineering goals (deployability, testability) score one star; elasticity and scalability score higher; performance scores low; simplicity and cost show inverse relationship.

## Chapter 17. Microservices Architecture

Service names and examples mentioned include: CatalogCheckout domain with catalog items, customers, and payment; CustomerWishList service; CustomerDemographics service; ReportCustomerInformation service as a mediator. Referenced works include the famous 'Microservices' blog entry by Martin Fowler and James Lewis (March 2014); Building Microservices by Sam Newman (O'Reilly); Microservices vs. Service-Oriented Architecture by Mark Richards (O'Reilly); Microservices AntiPatterns and Pitfalls by Mark Richards (O'Reilly). The chapter includes visual diagrams (Figures 17-1 through 17-13) illustrating topology, the sidecar pattern, service plane in service mesh, service mesh holistic view, microservices with monolithic UI, microfrontend pattern, choreography for coordination, orchestration for coordination, choreography for complex business processes, orchestration for complex business processes, saga pattern in happy path scenario, saga pattern with compensating transactions for errors, and architecture characteristics ratings scorecard. No actual source code fragments are presented in this range.

## Chapter 18. Choosing the Appropriate Architecture Style

Monolithic modular approach: An Override component with a dedicated endpoint where developers upload customizations, with each domain component referencing Override for each customizable characteristic, establishing a fitness function to ensure compliance.

BFF (Backends for Frontends) pattern: The BFF for iOS takes generic backend output and customizes it to iOS native application expectations regarding data format, pagination, and latency.

Going, Going, Gone microservices with specific services:
- BidCapture: Captures online bidder entries, sends asynchronously to BidTracker, requires no persistence
- BidStreamer: High-performance read-only stream of bids to participants
- BidTracker: Unifies bid streams from both Auctioneer Capture and BidCapture, handles asynchronous inbound connections using message queues as buffers
- Auctioneer Capture: Separate from BidCapture due to differing architecture characteristics
- Auction Session: Manages individual auction workflows
- Payment: Third-party provider processing payments after auction completion
- Video Capture: Captures live auction video stream
- Video Streamer: Streams video to online bidders

Quanta boundaries in GGG: Five identified quanta for Payment, Auctioneer, Bidder, Bidder Streams, and BidTracker, with multiple instances indicated by container stacks in the architecture diagram.

## Part III. Techniques and Soft Skills

No concrete examples, code fragments, or case studies are present in this range. This is a part introduction and chapter boundary section.

## Chapter 19. Architecture Decisions

1. Replicated Cache Example: A decision to cache product-related reference data (product description, weight, dimensions) in all service instances using read-only replicated cache, with primary replica owned by catalog service. Changes would be replicated to all other services through replicated (in-memory) cache product. Development teams discovered this required more in-process memory than available, requiring quick adjustment through collaboration.

2. ADR Status Example showing supersession:\nADR 42. Use of Asynchronous Messaging Between Order and Payment Services\nStatus: Superseded by 68\n\nADR 68. Use of REST Between Order and Payment Services\nStatus: Accepted, supersedes 42

3. Email Communication Template:\n"Hi Sandra, I've made an important decision regarding communication between services that directly impacts you. Please see the decision using the following link…"

4. ArchUnit Automated Fitness Function (Java):\n```\n@Test\npublic void shared_services_should_reside_in_services_layer() {\n    classes().that().areAnnotatedWith(SharedService.class)\n        .should().resideInAPackage("..services..")\n        .because("All shared services classes used by business " +\n                 "objects in the business layer should reside in the services " +\n                 "layer to isolate and contain shared logic")\n        .check(myClasses);\n}\n```

5. gRPC Decision Trade-off: Original decision used Google's Remote Procedure Call (gRPC) to reduce latency between services (at cost of tight coupling). Years later, another architect refactored to messaging without understanding the latency rationale, causing significant latency increases and timeouts.

6. ADR Directory Structure:\nApplication (common, ATP application, PSTD application) | Integration | Enterprise\nExample enterprise decision: "All access to a system database will only be from the owning system," preventing database sharing.

7. Going, Going, Gone Auction System Case Study: Illustrates event-driven microservices, split bidder and auctioneer user interfaces, Real-time Transport Protocol (RTP) for video capture, single API layer, and publish-and-subscribe messaging between bid capture, bid streamer, and bid tracker services (documented in ADR 76: Asynchronous Pub/Sub Messaging Between Bidding Services).

## Chapter 20. Analyzing Architecture Risk

Risk Matrix Example: "Suppose there is a concern about availability with regard to a primary central database used in the application. First, consider the impact dimension—what is the overall impact if the database goes down or becomes unavailable? Here, an architect might deem that high risk, making that risk either a 3 (medium), 6 (high), or 9 (high). However, after applying the second dimension (likelihood of risk occurring), the architect realizes that the database is on highly available servers in a clustered configuration, so the likelihood is low that the database would become unavailable. Therefore, the intersection between the high impact and low likelihood gives an overall risk rating of 3 (medium risk)."

Risk Storming Consensus Example: A participant identifies the Elastic Load Balancer as high risk (6) because "if the Elastic Load Balancer goes down, the entire system cannot be accessed." Others convince this participant that while impact is high, the likelihood is low, bringing the consensus rating down to medium (3).

Unproven Technology Case: One risk storming participant identifies the Redis cache as high risk (9) but when asked for the rationale responds, "What is a Redis cache?" This lack of knowledge qualifies the technology as unproven, justifying the highest risk rating (9).

Nurse Diagnostics System Availability Mitigation: "To mitigate the database risk, participants chose to break apart the single physical database into two separate databases: one clustered database containing the nurse profile information, and one single instance database for the case notes."

Elasticity Mitigation with Ambulance Pattern: "Leveraging what is known as the Ambulance Pattern would give nurses a higher priority over self-service. Therefore two message channels would be needed... the participants decided that in addition to the queuing technique to provide back-pressure, caching the particular diagnostics questions related to an outbreak would remove outbreak and flu calls from ever having to reach the diagnostics engine interface." This led to creation of a "Diagnostics Outbreak Cache Server."

Security Mitigation: "The participants all agreed that having separate API gateways for each type of user (admin, self-service/diagnostics, and nurses) would prevent calls from either the admin web user interface or the self-service web user interface from ever reaching the medical records exchange interface."

## Chapter 21. Diagramming and Presenting Architecture

The Irrational Artifact Attachment anti-pattern is defined as: "the proportional relationship between a person's irrational attachment to some artifact and how long it took to produce. If an architect creates a beautiful diagram using some tool like Visio that takes two hours, they have an irrational attachment to that artifact that's roughly proportional to the amount of time invested."

Representational consistency is demonstrated through Figure 21-1, which shows the entire Silicon Sandwiches topology followed by a zoomed view of plugin relationships, explicitly indicating where the detailed view fits within the complete architecture.

Figure 21-2 reproduces microservices communication using color (unique colors for different services) to clarify that two different microservices participate in coordination, not two instances of the same service.

Figures 21-3 and 21-4 illustrate incremental builds for a feature branching anti-pattern slide: Figure 21-3 shows the complete slide with the negative consequences visible immediately, while Figure 21-4 shows the same image partially obscured by a white box, with animations revealing portions sequentially to maintain narrative suspense.

The chapter references the Cookie-Cutter anti-pattern from Presentation Patterns and the Bullet-Riddled Corpse anti-pattern, both from the book "Presentation Patterns" by Neal Ford, Matthew McCullough, and Nathaniel Schutta, which established that ideas don't have predetermined word counts and that overloading one information channel (visual text) while starving the other (speaker's voice) creates dull presentations.

## Chapter 22. Making Teams Effective

Reference Manager component: Architect identifies the component, defines operations (GetData, SetData, ReloadCache, NotifyOnUpdate) and component interactions. The control freak architect wrongly specifies internal implementation using a parallel loader pattern with internal caching—this belongs to developers, not architects.

Trading system architecture: An armchair architect produces an overly high-level diagram showing minimal structure—labeled as too high-level to be useful.

Elastic Leadership scoring scenarios:
- Scenario 1: Team familiarity +20, Team size -20, Overall experience -20, Project complexity -20, Project duration -20 = -60 (armchair approach)
- Scenario 2: Team familiarity -20, Team size +20, Overall experience +20, Project complexity +20, Project duration -20 = -20 (control freak approach, but context-appropriate)

Developer code completion checklist items: Run code cleanup and code formatting, make sure there are no absorbed exceptions, Include @ServiceEntrypoint on service API class, Verify that only public methods are calling setFailure(), and project-specific standards.

Unit and functional testing checklist items: Special characters in text and numeric fields, minimum and maximum value ranges, unusual and extreme test cases, missing fields, and any edge cases previously found by QA (such as testing for negative shares like BUY for -1,000 shares of Apple [AAPL]).

Software release checklist items: Configuration changes in servers or external configuration servers, third-party libraries added to the project (JAR, DLL, etc.), and database updates with corresponding migration scripts.

Layered stack guidance categories: Special purpose (PDF rendering, bar code scanning—developer decision), General purpose (Apache Commons, Guava—overlap analysis and justification required with architect approval), Framework (Hibernate, Spring—architect decision only).

## Chapter 23. Negotiation and Leadership Skills

The chapter includes two detailed scenarios. Scenario 1 involves a senior vice president insisting on five nines of availability for a trading system, while the lead architect believes three nines is sufficient. The architect leverages Table 23-1 (Nines of availability) showing that five nines equals 5 min 35 sec downtime per year (or 1 second per day), while three nines equals 8 hrs 46 min per year (or 86 seconds per day), to reframe the discussion from abstract 'nines' to concrete daily downtime metrics. Scenario 2 depicts a heated debate between two architects about REST versus asynchronous messaging, resolved by running production-like performance comparisons rather than relying on Google searches.

The chapter contrasts two dialogues on architectural decisions. First dialogue: Architect says 'You must go through the business layer to make that call.' Developer responds 'No, it's much faster just to call the database directly.' Second dialogue (improved approach): Architect says 'Since change control is most important to us, we have formed a closed-layered architecture. This means all calls to the database need to come from the business layer.' Developer responds 'OK, I get it, but in that case, how am I going to deal with the performance issues for simple queries?'

Another pair of dialogues demonstrates leading teams on performance issues. Poor approach: Architect says 'What you need to do is use a cache. That would fix the problem.' Developer responds 'Don't tell me what to do.' Improved approach: Architect says 'Have you considered using a cache? That might fix the problem.' Developer responds 'Hmmm, no we didn't think about that. What are your thoughts?'

A third dialogue illustrates turning demands into favors. Direct command: 'I'm going to need you to split the payment service into five different services... to provide better fault tolerance and scalability... It shouldn't take too long.' Developer refuses. Revised favor approach: 'Hi, Sridhar. Listen, I'm in a real bind. I really need to have the payment service split into separate services for each payment type... Is there any way you can squeeze this into this iteration? It would really help me out.' Developer acquiesces: 'I'm really busy this iteration, but I guess so.'

The chapter also references five figures: Figure 23-1 showing Accidental Complexity (an overly complex backend system architecture for a global bank), Figure 23-2 illustrating the 4 C's (communication, collaboration, clarity, conciseness), Figure 23-3 depicting the balance between pragmatism and visionary thinking, Figure 23-4 showing a typical overscheduled architect's calendar, and Figure 23-5 categorizing meeting types (imposed upon vs. imposed by).

## Chapter 24. Developing a Career Path

The Clipper example illustrates the danger of ignoring technological trends: Neal's former company was invested in Clipper, a rapid-application development tool for DOS-based dBASE applications. The company noticed Windows rising but the market remained DOS-focused until it abruptly switched, leaving the company blindsided. This demonstrates what the authors call living in a technology bubble—a memetic echo chamber where developers never hear honest appraisals and don't notice when the bubble collapses until too late. Regarding social networks: strong links are people whose activities you know intimately (you can tell what they had for lunch at least one day last week), while weak links are people you see only a few times a year. McAfee's observation is that someone's next job opportunity more often comes from a weak link than a strong one, because weak links bring information and perspectives from outside your normal circle. The resources mentioned for the 20-Minute Rule include InfoQ, DZone Refcardz, and the ThoughtWorks Technology Radar website. On architecture katas: the authors note that students in training classes created architecture drawings explaining their decisions in class but lacked time to create architecture decision records. The why (trade-offs considered) proved far more valuable than the how (implementation details), because trade-offs reveal the reasoning that makes an architecture decision architecturally significant. The authors quote Fred Brooks ("Great designers design, of course") and Ted Neward's follow-up question ("So how are we supposed to get great architects, if they only get the chance to architect fewer than a half-dozen times in their career?"), emphasizing that practice through katas addresses this gap.

## Index

The Index contains no code examples, diagrams, case studies, or prose-described patterns. It is exclusively a reference list of hyperlinked terms. Sample entries include: "acceleration of rate of change in software development ecosystem" linking to "Shifting 'Fashion' in Architecture"; "ACID transactions" linking to "Distributed transactions"; "architecture decision records (ADRs)" with nested subentries for "as documentation," "basic structure of," "compliance section," "context section," and "decision section"; "Big Ball of Mud anti-pattern" linking to both "Cyclic dependencies" and a separate reference; and numerous entries for architecture characteristics like "analyzability," "auditability," "availability" with links to their respective explanatory sections. No code fragments, architectural diagrams, or illustrative examples appear in this index section.

## About the Authors

No code examples, diagrams, or technical case studies are present in this section. The content consists solely of prose-form biographical information about the two authors.

## Colophon

No code fragments, design patterns, or architectural examples are present in this colophon. The content is descriptive natural history and production documentation only.
