# Software Architecture in Practice

## Índice de capítulos
- [Preface](#preface)
- [Acknowledgments](#acknowledgments)
- [Chapter 1. What Is Software Architecture?](#chapter-1-what-is-software-architecture)
- [Chapter 2. Why Is Software Architecture Important?](#chapter-2-why-is-software-architecture-important)
- [Chapter 3. Understanding Quality Attributes](#chapter-3-understanding-quality-attributes)
- [Chapter 4. Availability](#chapter-4-availability)
- [Chapter 5. Deployability](#chapter-5-deployability)
- [Chapter 6. Energy Efficiency](#chapter-6-energy-efficiency)
- [Chapter 7. Integrability](#chapter-7-integrability)
- [Chapter 8. Modifiability](#chapter-8-modifiability)
- [Chapter 9. Performance](#chapter-9-performance)
- [Chapter 10. Safety](#chapter-10-safety)
- [Chapter 11. Security](#chapter-11-security)
- [Chapter 12. Testability](#chapter-12-testability)
- [Chapter 13. Usability](#chapter-13-usability)
- [Chapter 14. Working with Other Quality Attributes](#chapter-14-working-with-other-quality-attributes)
- [Chapter 15. Software Interfaces](#chapter-15-software-interfaces)
- [Chapter 16. Virtualization](#chapter-16-virtualization)
- [Chapter 17. The Cloud and Distributed Computing](#chapter-17-the-cloud-and-distributed-computing)
- [Chapter 18. Mobile Systems](#chapter-18-mobile-systems)
- [Chapter 19. Architecturally Significant Requirements](#chapter-19-architecturally-significant-requirements)
- [Chapter 20. Designing an Architecture](#chapter-20-designing-an-architecture)
- [Chapter 21. Evaluating an Architecture](#chapter-21-evaluating-an-architecture)
- [Chapter 22. Documenting an Architecture](#chapter-22-documenting-an-architecture)
- [Chapter 23. Managing Architecture Debt](#chapter-23-managing-architecture-debt)
- [Chapter 24. The Role of Architects in Projects](#chapter-24-the-role-of-architects-in-projects)
- [Chapter 25. Architecture Competence](#chapter-25-architecture-competence)
- [Chapter 26. A Glimpse of the Future: Quantum Computing](#chapter-26-a-glimpse-of-the-future-quantum-computing)
- [References](#references)

## Preface

This Preface contains no code examples, diagrams, or case study tables. It is an argumentative section justifying the book's relevance and the need for a fourth edition. The only concrete reference is the book registration information: ISBN 9780136886099 on informit.com/register. New chapters added to the fourth edition address virtualization, interfaces, mobility, and cloud systems—representing the architectural shifts discussed, but no architectural models or tactical examples are presented in this range.

## Acknowledgments

This chapter contains no code examples, case studies, tactic tables, or architecture diagrams. It is exclusively a prose acknowledgments section listing names and affiliations of contributors.

## Chapter 1. What Is Software Architecture?

Figure 1.2 C&C Structure (banking system): Client teller 1 (ellipse) connects to account server-main and account server-backup (rectangles), both connecting to account database (cylinder), which connects to administrative block (rounded rectangle). Client tellers communicate via publish-subscribe connector (double vertical lines with double horizontal line). Notation key: clients as ellipses; interfaces as small shaded squares; servers as rectangles; publish-subscribe as described connector; databases as cylinders; database applications as rounded rectangles; client-server request/reply with automatic failover as triangular dashed line with downward-pointing triangle; database access as horizontal line.

Figure 1.3 Module Elements (UML): System.IO.Log (package with small rectangle), CommonDialog (abstract class), SaveFileDialog (concrete class), UIElement (class with circle-marked IAnimatable interface), class with three compartments showing name (SaveFileDialog), attributes (FileName, Filter), and operations (ShowDialog(), OnFileOk(...)).

Figure 1.4 Module Relations (UML): is-part-of (package com.sun.ebank.web.taglib nested in com.sun.ebank.web containing dispatcher and context listener), depends-on (dashed downward arrow from dispatcher to BeanManager), is-a relations (Account parent with CheckingAccount and SavingsAccount children; Observer interface realization by AdminAccountView).

Figure 1.5 Decomposition Structure: ATIA-M package containing Windows apps (common code for thick clients, TDDT Windows app, UTMC Windows app) and server-side modules (ATIA server-side web modules, ATIA server-side Java modules).

Figure 1.6 Uses Structure: Nine packages (estore.webapp, web::estore, admin.client, web::shared, web::accessControl, admin.core, estore.core, util, dao) with <<use>> dependencies. Highlighted: admin.client, admin.core, dao, util as required in increment if admin.client present.

Figure 1.7 Layer Structure (UNIX System V): User-level (User programs → User-level libraries, System call interface) → Kernel-level (System call interface → File subsystem, Process control subsystem [IPC, scheduler, memory management]) → File subsystem (Character device drivers, Buffering mechanism) → Buffering mechanism (Block I/O device drivers); Process control (Hardware control); device drivers (Hardware control). User-level shown as lightly shaded, Kernel-level as dark shaded. Down arrows represent "allowed to use."

Figure 1.8 Generalization Structure: Classes ScenarioVO, FunctionVO, ScenarioRespVO, FunctionRespVO, ResponsibilityVO, RelationshipVO, ParameterVO, QuestionToUserVO inherit from Fact (id: int, type: String), which inherits from java.util.observable.

Figure 1.9 Data Model: Legend shows entity as three-column table (PK/FK/index in first column, column names [bold=required] in second, data types in third); relationship notation with cardinality—0 or more B's per A, each B to exactly one A, A's PK in B's PK. Example: PurchaseOrder, OrderItem, CatalogItem entities where PurchaseOrder:OrderItem and CatalogItem:OrderItem form the relationships.

Figure 1.10 Deployment Structure (UML): Internet user PC → (internet) → win server application server (WebSphere execution environment) → (intranet) → Linux server database server and win desktop admin user PC (1-to-1). Artifacts app-client.jar deployed to win desktop, EnterpriseWebApp.ear to win server.

Figure 1.11 Two Views of Client-Server System: Decomposition view shows two modules (client, server as rectangles). Client-server runtime view shows one central S1 server component with ten client components C1-C10 connected via request-reply connectors (double-headed arrows).

Table 1.1 Architectural Structures Summary:

Module structures—Decomposition: Module elements, "is-a-submodule-of" relations; useful for resource allocation, project structuring, encapsulation; affects Modifiability. Uses: Module elements, "uses (requires correct presence of)" relations; useful for designing subsets and extensions; affects Subsetability, Extensibility. Layers: Layer elements, "allowed to use services of, provides abstraction to" relations; useful for incremental development and virtual machine implementation; affects Portability, Modifiability. Class: Class/object elements, "is-instance-of, is-generalization-of" relations; useful for factoring commonality and planning functional extensions; affects Modifiability, Extensibility. Data model: Data entity elements, "{one,many}-to-{one,many}, generalizes, specializes" relations; useful for engineering global data structures; affects Modifiability, Performance.

C&C structures—Service: Service, service registry elements, "attachment (via message-passing)" relations; useful for scheduling, performance, and robustness analysis; affects Interoperability, Availability, Modifiability. Concurrency: Processes, threads elements, "attachment (via communication and synchronization mechanisms)" relations; useful for identifying resource contention and parallelism opportunities; affects Performance.

Allocation structures—Deployment: Components, hardware elements, "allocated-to, migrates-to" relations; useful for mapping software to system elements; affects Performance, Security, Energy, Availability, Deployability. Implementation: Modules, file structure elements, "stored-in" relations; useful for configuration control, integration, test; affects Development Efficiency. Work assignment: Modules, organizational units elements, "assigned-to" relations; useful for project management and expertise utilization; affects Development Efficiency.

## Chapter 2. Why Is Software Architecture Important?

The chapter contains one primary case study: "What Happens When I Push This Button?: Architecture as a Vehicle for Stakeholder Communication." A young architect presents a government-sponsored system's software architecture at a marathon review session to about 30 government representatives. The slide shows box-and-line notation of major software elements with acronymic names, data flow, message passing, and process synchronization. A user representative interrupts asking what happens when the mode select button is pushed. The architect responds by explaining how it triggers an event in the device driver, reads a register, interprets an event code, and signals a blackboard that signals subscribed objects. When pressed for what the system does (whether it resets displays and what happens during reconfiguration), the architect explains that in setup mode displays reset; otherwise an error message goes to the control console and the signal is ignored. This sparks a 45-minute audience debate on correct system behavior in various states—a critical conversation that should have occurred during requirements formulation but did not. The case study illustrates that architecture, even invisibly to users, serves as a tool for system understanding by presenting systems in a new way that surfaces previously unconsidered questions and improves clarity.

Key design decisions explored include: Will the system run on one processor or be distributed across multiple processors? Will software be layered; if so, how many layers and what does each do? Will components communicate synchronously or asynchronously, transferring control or data or both? Will flowing information be encrypted? Which operating system? Which communication protocol?

Three categories of changes are defined: A local change modifies a single element (adding a business rule to a pricing logic module). A nonlocal change requires multiple element modifications but preserves the underlying architectural approach (adding a pricing rule, updating database fields, revealing results in the user interface). An architectural change affects fundamental element interactions and requires changes throughout the system (converting from single-threaded to multi-threaded).

Examples of skeletal systems extended via plug-ins include: R language, Visual Studio Code, and web browsers. Building infrastructure tools mentioned include: Apache Ant, Apache Maven, MSBuild, and Jenkins. AUTOSAR is cited as a good example of an open systems architecture standard developed for the automotive industry (autosar.org).

## Chapter 3. Understanding Quality Attributes

Figure 3.1 depicts the six-part structure of a quality attribute scenario: a stimulus source (e.g., a finger pressing a point) generates a stimulus (e.g., a user request or system event) that arrives within an environment (outer rectangle), targeting an artifact (inner rectangle). The system responds, with the success of the response measured by a response measure (indicated by numbers and symbols showing range, timing, and threshold metrics).

Figure 3.2 presents a general scenario template for availability. Source includes internal and external entities (people, hardware, software, physical infrastructure, physical environment). Stimulus is a fault (omission, crash, incorrect timing, incorrect response). Artifact includes processors, communication channels, storage, processes, and affected systems in the environment. Environment states include normal operation, startup, shutdown, repair mode, degraded operation, and overloaded operation. Response activities are to prevent a fault from becoming a failure, detect the fault, or recover from the fault. Response measures include time intervals of required availability, availability percentage (e.g., 99.99%), and time-to-detect metrics.

Figure 3.3 shows a simple schematic: a stimulus (right arrow) enters a block labeled "Tactics," and the system produces a response (right arrow exiting the block). This illustrates that tactics are mechanisms for controlling responses to stimuli.

Concrete tactical examples mentioned: Schedule resources is a performance tactic (refined into shortest-job-first, round-robin, or other scheduling strategies); Use an intermediary is a modifiability tactic (realized as layers, brokers, proxies, or tiers); Manage sampling rate is a performance tactic relevant only in specific real-time contexts; Monitoring is a "super-tactic" appearing across multiple quality attributes (energy efficiency, performance, availability, safety). A load balancer exemplifies an intermediary tactic used for performance scheduling.

A sidebar case study describes an architecture analysis at Lawrence Livermore National Laboratory. Despite the organization's heavy focus on security (nuclear security, international security, environmental security), system stakeholders did not identify security as a quality attribute concern. They mentioned performance, modifiability, evolvability, interoperability, configurability, and portability instead. The reason: their systems were isolated from external networks and protected by physical security (barbed-wire fences, armed guards). The lesson illustrates that architects may not bear responsibility for every quality attribute requirement—responsibility depends on organizational context and risk assignment.

## Chapter 4. Availability

Table 4.1 - System Availability Requirements:
```
Availability | Downtime/90 Days    | Downtime/Year
99.0%        | 21 hr, 36 min       | 3 days, 15.6 hr
99.9%        | 2 hr, 10 min        | 8 hr, 0 min, 46 sec
99.99%       | 12 min, 58 sec      | 52 min, 34 sec
99.999%      | 1 min, 18 sec       | 5 min, 15 sec
99.9999%     | 8 sec               | 32 sec
```

Figure 4.1 - Sample concrete availability scenario:
Source: a server in a server farm
Stimulus: server fails
Artifact: the server
Environment: normal operation
Response: the system informs the operator and the system continues to operate
Response Measure: no downtime

Availability Formula:
MTBF / (MTBF + MTTR)
where MTBF = mean time between failures, MTTR = mean time to repair

Amazon EC2 SLA Example:
"AWS will use commercially reasonable efforts to make the Included Services each available for each AWS region with a Monthly Uptime Percentage of at least 99.99%, in each case during any monthly billing cycle (the 'Service Commitment'). In the event any of the Included Services do not meet the Service Commitment, you will be eligible to receive a Service Credit as described below."

Figure 4.3 - Availability Tactics Hierarchy:
Availability Tactics divided into:
1. Detect Faults: monitor, ping/echo, heartbeat, timestamp, condition monitoring, sanity checking, voting, exception detection, self-test
2. Recover from Faults:
   a. Preparation and Repair: redundant spare, rollback, exception handling, software upgrade, retry, ignore faulty behavior, graceful degradation, reconfiguration
   b. Reintroduction: shadow, state resynchronization, escalating restart, nonstop forwarding
3. Prevent Faults: removal from service, transactions, predictive model, exception prevention, increase competence set

Table 4.2 - Availability General Scenario with six portions (Source, Stimulus, Artifact, Environment, Response, Response Measure) and their descriptions and possible values

Table 4.3 - Tactics-Based Questionnaire for Availability with columns for Tactics Group, Tactics Question, Support? (Y/N), Risk, Design Decisions and Location, and Rationale and Assumptions, covering all detect fault, recovery preparation/repair, recovery reintroduction, and prevent fault tactics

Parameter Fence Detection Example: Known data pattern 0xDEADBEEF placed immediately after variable-length parameters to detect runtime overwriting

Escalating Restart Levels Example:
Level 0: Kill and recreate child threads (warm spare impact, only thread data freed)
Level 1: Free and reinitialize unprotected memory (protected memory untouched)
Level 2: Free and reinitialize all memory, forcing application reload
Level 3: Completely reload and reinitialize executable image and data segments

## Chapter 5. Deployability

Table 5.1 - General Scenario for Deployability:
| Portion of Scenario | Description | Possible Values |
| Source | The trigger for deployment | End user, developer, system administrator, operations personnel, component marketplace, product owner |
| Stimulus | What causes the trigger | A new element is available (new version, bug fix, security patch, library upgrade, framework upgrade, internally produced element). New element is approved. Existing element(s) need rollback |
| Artifacts | What is to be changed | Specific components/modules, system platform, user interface, environment, or interoperating systems. May be single element, multiple elements, or entire system |
| Environment | Staging or production | Full deployment or subset deployment to specified VMs, containers, servers, platforms |
| Response | What should happen | Incorporate new components. Deploy new components. Monitor new components. Roll back previous deployment |
| Response measure | Cost, time, process effectiveness | Cost: number/size/complexity of artifacts, average/worst-case effort, elapsed time, money. Impact on other functions/QAs. Failed deployment count. Repeatability. Traceability. Cycle time |

Concrete Deployability Scenario (Figure 5.1): "A new release of an authentication/authorization service (which our product uses) is made available in the component marketplace and the product owner decides to incorporate this version into the release. The new service is tested and deployed to the production environment within 40 hours of elapsed time and no more than 120 person-hours of effort. The deployment introduces no defects and no SLA is violated."

Figure 5.2 describes the relationship between deployment stimulus (new elements arrive) and response goal (elements deployed within time, cost, quality constraints), showing how tactics control this response.

Figure 5.3 presents the Deployability Tactics taxonomy: Manage Deployment Pipeline (scale rollouts, script deployment commands, rollback) and Manage Deployed System (manage service interactions, package dependencies, toggle features).

Table 5.2 - Tactics-Based Questionnaire for Deployability contains six rows with columns for Tactics Groups, Tactics Question, Supported (Y/N), Risk, Design Decisions and Location, Rationale and Assumptions. Questions address each of the six tactics: scaling rollouts gradually vs all-or-nothing, automatic rollback capability, deployment script automation, simultaneous multi-version service management, packaging dependencies with services, and feature toggle employment.

Figure 5.4 illustrates Netflix's rolling upgrade implementation via the Asgard tool on Amazon EC2: update auto-scaling group, sort instances, confirm upgrade spec, then iteratively remove and de-register old instance from elastic load balancer, terminate old instance, wait for ASG to start new instance, register new instance with elastic load balancer.

## Chapter 6. Energy Efficiency

Table 6.1 - Energy Efficiency General Scenario framework with six portions: Source (end user, manager, administrator, automated agent), Stimulus (total usage, maximum instantaneous usage, average usage), Artifacts (specific devices, servers, VMs, clusters), Environment (runtime, connected, battery-powered, low-battery mode, power-conservation mode), Response options (disable services, deallocate runtime services, change service allocation, run at lower consumption mode, allocate/deallocate servers, change service levels, change scheduling), and Response measure (maximum/average kilowatt load, average/total energy saved, total kilowatt hours, time period powered on, while maintaining functionality and other quality attributes).

Figure 6.1 - Concrete energy efficiency scenario: A manager initiates a request to save energy at runtime during non-peak periods by deallocating unused resources. The system responds by deallocating resources while maintaining worst-case latency of 2 seconds on database queries, saving on average 50 percent of total energy required.

Figure 6.3 - Energy efficiency tactics flowchart hierarchically organized: Monitor Resources (metering, static classification, dynamic classification); Allocate Resources (reduce usage, discovery, schedule resources); Reduce Resource Demand (manage event arrival, limit event response, prioritize events, reduce computational overhead, bound execution times, increase resource usage efficiency).

Table 6.2 - Tactics-Based Questionnaire for Energy Efficiency with six rows querying: (1) Does system meter energy use via sensors? (2) Does system statically classify devices with reference values for estimation? (3) Does system dynamically classify based on varying load/conditions? (4) Does system reduce usage via deactivation, spinning down drives, darkening displays, adjusting CPU clock rates, or consolidation? (5) Does system schedule resources considering task constraints and priorities, switching among providers for efficiency or cost? (6) Does system use discovery service to match requests to providers annotated with energy requirements? Each row includes columns for Supported (Y/N), Risk, Design Decisions and Location, and Rationale and Assumptions.

## Chapter 7. Integrability

Table 7.1 - General Scenario for Integrability includes the following dimensions:

Source: Mission/system stakeholder, Component marketplace, Component vendor
Stimulus: Add new component, Integrate new version of existing component, Integrate existing components together in a new way
Artifact: Entire system, Specific set of components, Component metadata, Component configuration
Environment: Development, Integration, Deployment, Runtime
Response: Changes are {completed, integrated, tested, deployed}; Components in the new configuration are successfully and correctly (syntactically and semantically) exchanging information; Components in the new configuration are successfully collaborating; Components in the new configuration do not violate any resource limits
Response measure: Cost (components changed, percentage of code changed, lines of code changed, effort, money, calendar time); Effects on other quality attribute response measures

Figure 7.1 - Sample Integrability Scenario: "A new data filtering component has become available in the component marketplace. The new component is integrated into the system and deployed in 1 month, with no more than 1 person-month of effort."

Figure 7.3 - Integrability Tactics Structure:
├─ Limit Dependencies
│  ├─ Encapsulate
│  ├─ Use an Intermediary
│  ├─ Restrict Communication Paths
│  ├─ Adhere to Standards
│  └─ Abstract Common Services
├─ Adapt
│  ├─ Discover
│  ├─ Tailor Interface
│  └─ Configure Behavior
└─ Coordinate
   ├─ Orchestrate
   └─ Manage Resources

Table 7.2 - Tactics-Based Questionnaire for Integrability with rows for each tactic group and columns for: Tactics Group, Tactics Question, Supported? (Y/N), Risk, Design Decisions and Location, Rationale and Assumptions.

Key Questions from Table 7.2:
- Does the system encapsulate functionality of each element by introducing explicit interfaces?
- Does the system broadly use intermediaries for breaking dependencies between components?
- Does the system abstract common services, providing a general, abstract interface for similar services?
- Does the system provide a means to restrict communication paths between components?
- Does the system adhere to standards in terms of how components interact and share information?
- Does the system provide the ability to tailor interfaces—add or hide capabilities without changing API or implementation?
- Does the system provide a discovery service, cataloguing and disseminating information about services?
- Does the system provide a means to configure the behavior of components at build, initialization, or runtime?
- Does the system include an orchestration mechanism that coordinates and manages the invocation of components?
- Does the system provide a resource manager that governs access to computing resources?

## Chapter 8. Modifiability

Table 8.1 (General Scenario for Modifiability) specifies scenario components: Source (agent causing change—end user, developer, system administrator, product line owner, or the system itself); Stimulus (the change—directive to add/delete/modify functionality, change quality attributes/capacity/platform/technology, add product to product line, or change service location); Artifacts (items modified—components, modules, platform, user interface, environment, code, data, interfaces, resources, test cases, configurations, documentation); Environment (lifecycle phase—runtime, compile time, build time, initiation time, design time); Response (make and incorporate change through modification, testing, deployment, or self-modification); Response measure (cost resources including number/size/complexity of affected artifacts, effort, elapsed time, money, extent of side effects on other functions/qualities, new defects introduced, adaptation time).

Table 8.2 (Tactics-Based Questionnaire for Modifiability) presents a structured analysis table with columns for Tactics Group, Tactics Question, Supported (Y/N), Risk, Design Decisions and Location, and Rationale and Assumptions. Questions address: for Increase Cohesion—do you split modules (breaking complex modules into cohesive submodules) and redistribute responsibilities (grouping similar responsibilities); for Reduce Coupling—do you encapsulate functionality, use intermediaries to avoid tight coupling (introducing abstraction between concrete components), restrict dependencies systematically (limiting module interactions, as in layered architectures), and abstract common services (providing similar services via common interfaces for portability); for Defer Binding—does the system regularly defer binding of important functionality through plug-ins, add-ons, resource files, or configuration files that can extend system functionality later in the lifecycle.

Figure 8.2 depicts the goal of modifiability tactics as controlling the response to changes arriving as stimuli within time and budget constraints. Figure 8.3 presents a hierarchical flowchart of modifiability tactics organized into three branches: Increase Cohesion (containing Split module and Redistribute responsibilities), Reduce Coupling (containing Encapsulate, Use an intermediary, Abstract common services, and Restrict dependencies), and Defer Binding (subdividing into compile-time/build-time tactics of Component replacement, Compile-time parameterization, and Aspects; deployment/startup/initialization-time tactics of Configuration-time binding and Resource files; and runtime tactics of Discovery, Interpret parameters, Shared repositories, and Polymorphism).

## Chapter 9. Performance

Table 9.1 — Performance General Scenario components and possible values:

Portion of Scenario | Description | Possible Values
---|---|---
Source | The stimulus can come from a user (or multiple users), from an external system, or from some portion of the system under consideration. | External: User request, Request from external system, Data arriving from a sensor or other system. Internal: One component may make a request of another component, A timer may generate a notification.
Stimulus | The stimulus is the arrival of an event. The event can be a request for service or a notification of some state of either the system under consideration or an external system. | Arrival of a periodic, sporadic, or stochastic event: A periodic event arrives at a predictable interval, A stochastic event arrives according to some probability distribution, A sporadic event arrives according to a pattern that is neither periodic nor stochastic.
Artifact | The artifact stimulated may be the whole system or just a portion of the system. For example, a power-on event may stimulate the whole system. A user request may arrive at (stimulate) the user interface. | Whole system, Component within the system
Environment | The state of the system or component when the stimulus arrives. Unusual modes—error mode, overloaded mode—will affect the response. For example, three unsuccessful login attempts are allowed before a device is locked out. | Runtime. The system or component can be operating in: Normal mode, Emergency mode, Error correction mode, Peak load, Overload mode, Degraded operation mode, Some other defined mode of the system
Response | The system will process the stimulus. Processing the stimulus will take time. This time may be required for computation, or it may be required because processing is blocked by contention for shared resources. Requests can fail to be satisfied because the system is overloaded or because of a failure somewhere in the processing chain. | System returns a response, System returns an error, System generates no response, System ignores the request if overloaded, System changes the mode or level of service, System services a higher-priority event, System consumes resources
Response measure | Timing measures can include latency or throughput. Systems with timing deadlines can also measure jitter of response and ability to meet the deadlines. Measuring how many of the requests go unsatisfied is also a type of measure, as is how much of a computing resource (e.g., a CPU, memory, thread pool, buffer) is utilized. | The (maximum, minimum, mean, median) time the response takes (latency), The number or percentage of satisfied requests over some time interval (throughput) or set of events received, The number or percentage of requests that go unsatisfied, The variation in response time (jitter), Usage level of a computing resource

Concrete Performance Scenario Example (Figure 9.1): "Five hundred users initiate 2,000 requests in a 30-second interval, under normal operations. The system processes all of the requests with an average latency of two seconds."

Concurrency example demonstrating race conditions:
```
Thread 1:          Thread 2:
x = 1;             x = 1;
x++;               x++;
```
The final value of x could be either 2 or 3 depending on execution interleaving. If both threads execute independently, the result is 3. If execution sequences as: Thread 1 reads x=1, Thread 2 reads x=1, Thread 1 writes x=2, Thread 2 writes x=2, the result is 2—a race condition.

Map-Reduce playing card example: Given 1 billion playing cards, the map function hashes by suit (clubs, diamonds, hearts, spades) as the key, filters to keep only numeric cards (discarding A, K, Q, J, jokers), and distributes processing to thousands of parallel map instances, each processing different card portions. The infrastructure shuffles output buckets, then reduce instances perform analysis—such as counting cards per suit or summing numeric values per suit. Output sets are much smaller than input (hence "reduce").

Performance Tactics on the Road analogy:
- Manage event rate: Highway entrance ramp lights control car arrival rate via queuing.
- Prioritize events: Emergency vehicles (ambulances, police) bypass via HOV/priority lanes.
- Maintain multiple copies: Add traffic lanes or build parallel routes.
- Increase resources: Purchase faster vehicle.
- Increase efficiency: Find shorter/quicker route.
- Reduce computational overhead: Drive closer to car ahead or carpool (load more per vehicle).

## Chapter 10. Safety

Table 10.1 Safety General Scenario: Rows include Source (sensor, software component, communication channel, device, clock), Stimulus (omissions: "value never arrives," "function never performed"; commissions: "function performed incorrectly," "device produces spurious event," "device produces incorrect data"; incorrect data: "sensor reports incorrect data," "software component produces incorrect results"; timing: "data arrives too late/early," "event occurs too late/early or wrong rate," "events occur in wrong order"), Environment (normal/degraded/manual/recovery modes), Artifacts (safety-critical portions), Response (recognize unsafe state and avoid/recover/continue degraded/safe/shut down/switch manual/switch backup/notify/log), Response measure (percentage of avoided unsafe entries, percentage of recoverable states, risk exposure: size(loss) × prob(loss), percentage time recovering, time in degraded/safe/shutdown, elapsed time to enter and recover). Concrete scenario: "A sensor in the patient monitoring system fails to report a life-critical value after 100 ms. The failure is logged, a warning light is illuminated on the console, and a backup (lower-fidelity) sensor is engaged. The system monitors the patient using the backup sensor after no more than 300 ms."

Table 10.2 Tactics-Based Questionnaire for Safety lists fifteen questions organized by tactic group (Unsafe State Avoidance: substitution, predictive model; Unsafe State Detection: timeouts, timestamps, condition monitoring, sanity checking, comparison; Containment—Redundancy: replication, functional redundancy, analytic redundancy; Containment—Limit Consequences: abort, degradation, masking/voting; Containment—Barrier: firewall, interlock; Recovery: rollback, repair state, reconfiguration), each with columns for Supported (Y/N), Risk, Design Decisions and Location, and Rationale/Assumptions. The questionnaire is preceded by guidance: perform hazard analysis or FTA beforehand to identify what constitutes unsafe states, since designing for safety without this analysis is less effective.

Design Assurance Levels sidebar: DO-178C defines five DAL categories—A (Catastrophic: "Failure may cause deaths, usually with loss of the airplane"), B (Hazardous: "Failure has a large negative impact on safety or performance, or reduces the crew's ability to operate the aircraft due to physical distress or a higher workload, or causes serious or fatal injuries among the passengers"), C (Major: "Failure significantly reduces the safety margin or significantly increases crew workload, and may result in passenger discomfort (or even minor injuries)"), D (Minor: "Failure slightly reduces the safety margin or slightly increases crew workload. Examples might include causing passenger inconvenience or a routine flight plan change"), E (No effect: "Failure has no impact on safety, aircraft operation, or crew workload").

## Chapter 11. Security

Table 11.1 Security General Scenario components: Source (human or another system; inside/outside organization; previously identified or unknown); Stimulus (unauthorized attempts to display/capture/change or delete data, access services, change behavior, or reduce availability); Artifact (system services, internal data, components, produced/consumed data); Environment (online/offline; connected/disconnected; behind firewall/open; fully/partially/non-operational); Response (protecting from unauthorized access, preventing unauthorized manipulation, identifying parties with assurance, preventing repudiation, ensuring availability, tracking through logging and notifications); Response Measure (resource compromise/assurance amounts, attack detection accuracy, detection time, attacks resisted count, recovery duration, vulnerable data scope).

Figure 11.1 Sample concrete scenario: "A disgruntled employee at a remote location attempts to improperly modify the pay rate table during normal operations. The unauthorized access is detected, the system maintains an audit trail, and the correct data is restored within one day." Source: disgruntled employee at remote location. Stimulus: attempts to improperly modify pay rate table. Artifact: database. Environment: normal operations. Response: unauthorized access detected, audit trail maintained. Response Measure: correct data restored within one day.

Figure 11.2 depicts security tactics goal showing stimulus (an attack) leading to system response (detect/resist/recover).

Figure 11.3 flowchart organizes security tactics into four categories: Detect attacks (detect intrusion, detect service denial, verify message integrity, detect message delivery anomalies); Resist attacks (identify actors, authenticate actors, authorize actors, limit access, limit exposure, encrypt data, separate entities, validate input, change credential settings); React to attacks (revoke access, restrict login, inform actors); Recover from attacks (audit and nonrepudiation).

Table 11.2 Tactics-Based Questionnaire for Security lists detection tactics (intrusion detection, DoS detection, message integrity verification, message delay detection), resistance tactics (actor identification through user IDs/access codes/IP addresses/protocols/ports, authentication via passwords/certificates/two-factor/biometrics, authorization for data/service access, access limiting via point restriction or traffic type restriction, exposure limiting via single-point data reduction, data encryption for transit/rest, entity separation via physical servers/networks/virtual machines/air gaps, credential setting changes, input validation via filtering/canonicalization/sanitization), reaction tactics (revoke access, restrict login, inform actors), and recovery tactics (audit trails, nonrepudiation, fault recovery mechanisms from Chapter 4).

## Chapter 12. Testability

**Table 12.1: Testability General Scenario**
| Portion of Scenario | Description | Possible Values |
|---|---|---|
| Source | The test cases can be executed by a human or an automated test tool | Unit testers, integration testers, system testers, acceptance testers, end users; manual or automated testing tools |
| Stimulus | A test or set of tests is initiated | Validate system functions; validate qualities; discover emerging threats to quality |
| Environment | Testing occurs at various events or life-cycle milestones | Completion of a coding increment; completed integration of a subsystem; complete implementation of the whole system; deployment into production; delivery to customer; a testing schedule |
| Artifacts | The artifact is the portion of the system being tested and any required test infrastructure | A unit of code; components; services; subsystems; the entire system; the test infrastructure |
| Response | The system and its test infrastructure can be controlled to perform the desired tests, and the results from the test can be observed | Execute test suite and capture results; capture activity that resulted in the fault; control and monitor the state of the system |
| Response measure | Response measures are aimed at representing how easily a system under test "gives up" its faults or defects | Effort to find a fault; effort to achieve a given percentage of state space coverage; probability of a fault being revealed by the next test; time to perform tests; effort to detect faults; length of time to prepare test infrastructure; effort required to bring the system into a specific state; reduction in risk exposure: size(loss) × probability(loss) |

**Concrete Testability Scenario (Figure 12.2):** The developer completes a code unit during development and performs a test sequence whose results are captured and that gives 85 percent path coverage within 30 minutes.

**Netflix's Simian Army Case Study** (sidebar): Netflix uses a suite of runtime fault-injection and monitoring tools for testability in their cloud-based streaming system. The Chaos Monkey randomly kills processes to test failure handling. The Latency Monkey induces artificial network delays to verify service degradation responses. The Conformity Monkey identifies instances not adhering to best practices and shuts them down (e.g., instances not in auto-scaling groups). The Doctor Monkey monitors health checks and external signs (e.g., CPU load) to detect unhealthy instances. The Janitor Monkey cleans unused resources. The Security Monkey extends conformity checking for security violations and certificate validity. The 10-18 Monkey (L10n-i18n) detects configuration and runtime problems in multi-region, multi-language instances. Netflix's approach illustrates fault injection in controlled, monitored fashion and specialized monitoring for targeted high-severity faults.

**Figure 12.3: The Goal of Testability Tactics** (diagram showing input stimulus "tests executed" flowing through a control response box to output "faults detected")

**Table 12.2: Tactics-Based Questionnaire for Testability**
| Tactics Group | Tactics Question | Supported? (Y/N) | Risk | Design Decisions and Location | Rationale and Assumptions |
|---|---|---|---|---|---|
| Control and Observe System State | Does your system have specialized interfaces for getting and setting values? | | | | |
| | Does your system have a record/playback mechanism? | | | | |
| | Is your system's state storage localized? | | | | |
| | Does your system abstract its data sources? | | | | |
| | Can some or all of your system operate in a sandbox? | | | | |
| | Is there a role for executable assertions in your system? | | | | |
| Limit Complexity | Does your system limit structural complexity in a systematic way? | | | | |
| | Is there nondeterminism in your system, and is there a way to control or limit this nondeterminism? | | | | |

**Figure 12.4: Testability Tactics Hierarchy** (flowchart diagram)
Testability Tactics branches into two categories:
1. Control and Observe System State: includes specialized interfaces, record/playback, localize state storage, abstract data sources, sandbox, executable assertions
2. Limit Complexity: includes limit structural complexity, limit nondeterminism

## Chapter 13. Usability

Table 13.1 (Usability General Scenario) specifies scenario components: Source (end user in specialized roles like system/network administrator, or external events); Stimulus (desires to use efficiently, learn, minimize errors, adapt, configure); Environment (runtime or configuration time); Artifacts (GUI, command-line interface, voice interface, touch screen); Response (provide needed features, anticipate needs, appropriate feedback); Response Measure (task time, number of errors, learning time, ratio of learning to task time, tasks accomplished, user satisfaction, user knowledge gain, ratio of successful to total operations, time/data lost on error).

Figure 13.1 presents a concrete usability scenario: "The user downloads a new application and is using it productively after 2 minutes of experimentation" (source: user, stimulus: downloads new application, artifact: existing platform, environment: runtime, response: using it productively, response measure: after 2 minutes of experimentation).

Table 13.2 (Tactics-Based Questionnaire for Usability) presents a structured analysis table with columns for Tactics Group, Tactics Question, Supported (Y/N), Risk, Design Decisions and Location, and Rationale and Assumptions. Support User Initiative questions address: "Is the system able to listen to and respond to a cancel command?", "Is it possible to undo the last command, or the last several commands?", "Is it possible to pause and then resume long-running operations?", "Is it possible to aggregate UI objects into a group and apply operations on the group?". Support System Initiative questions address: "Does the system maintain a model of the task?", "Does the system maintain a model of the user?", "Does the system maintain a model of itself?".

Figure 13.2 (The goal of usability tactics) illustrates that stimulus (user interaction) flows to usability tactics, which control response (the user is given appropriate feedback and assistance).

Figure 13.3 (Usability tactics) presents a hierarchical flowchart showing usability tactics divided into Support User Initiative (cancel, undo, pause/resume, aggregate) and Support System Initiative (maintain task model, maintain user model, maintain system model).

## Chapter 14. Working with Other Quality Attributes

ISO/IEC FCD 25010 Product Quality Characteristics definitions:
- Functional suitability: Degree to which a product or system provides functions that meet stated and implied needs when used under specified conditions
- Performance efficiency: Performance relative to the amount of resources used under stated conditions
- Compatibility: Degree to which a product, system, or component can exchange information with other products, systems, or components, and/or perform required functions while sharing the same hardware or software environment
- Usability: Degree to which a product or system can be used by specified users to achieve specified goals with effectiveness, efficiency, and satisfaction in specified context of use
- Reliability: Degree to which a system, product, or component performs specified functions under specified conditions for a specified period of time
- Security: Degree to which a product or system protects information and data so that persons or other products or systems have the degree of data access appropriate to their types and levels of authorization
- Maintainability: Degree of effectiveness and efficiency with which a product or system can be modified by intended maintainers
- Portability: Degree of effectiveness and efficiency with which a system, product, or component can be transferred from one hardware, software, or other operational or usage environment to another

Queuing Model Parameters for Performance: The generic queuing model identifies seven parameters affecting latency: (1) Arrival rate, (2) Queuing discipline, (3) Scheduling algorithm, (4) Service time, (5) Topology, (6) Network bandwidth, (7) Routing algorithm. Each can be influenced by architectural decisions such as fixed versus load-balancing routing, choice of scheduling algorithm, or dynamic server topology changes.

Figure 14.2 description: A generic queuing model showing arrivals sent to a queue block connected to a server with a scheduling algorithm. The routing of messages is performed with output from the scheduling algorithm sent into two different queues, each followed by a scheduling algorithm server, with final results output from the final server.

Concrete domain-specific example: An architecture designed with the conscious goal of retaining key staff and attracting talented new hires to a quiet region of the American Midwest incorporated a quality attribute called "Iowability," achieved by bringing in state-of-the-art technology and giving development teams wide creative latitude—demonstrating how organizations may require QAs not found in standard lists but equally important to success.

## Chapter 15. Software Interfaces

TABLE 15.1 - Most Important Commands in HTTP and Their Relationship to CRUD Database Operations:

| HTTP Command | CRUD Operation Equivalent |
| --- | --- |
| post | create |
| get | read |
| put | update/replace |
| patch | update/modify |
| delete | delete |

FIGURE 15.1 - Interface Evolution Patterns:
(a) The original interface: An element exposes a single interface serving actors 1 through N.
(b) Extending the interface: The same element exposes both the original interface and a new extended interface to actors 1 through N.
(c) Using an intermediary: The element implements an internal interface; a mediator translates between external interfaces (original and extension) and the internal interface, serving actors 1 through N who may request either interface version.

For the apartment number address incompatibility example: the original interface assumes apartment numbers are embedded in the address parameter; the extended interface separates apartment numbers as a distinct parameter. The mediator invoked from the original interface parses the address to extract any apartment number, while invocation through the extended interface passes the separate apartment number parameter unchanged to the internal interface.

INTERACTION STYLE SPECIFICATIONS:

Remote Procedure Call (RPC) evolution: Early 1980s versions used synchronous operation with text-based parameters. Modern gRPC (the latest RPC version) provides: binary parameter transfer, asynchronous operation, authentication support, bidirectional streaming, flow control, blocking or nonblocking bindings, cancellation and timeout mechanisms, and HTTP 2.0 transport.

REST (Representational State Transfer) six constraints:
1. Uniform interface: HTTP interactions using URIs; consistent naming; least-surprise principle
2. Client-server: Actors are clients; resource providers are servers using the client-server pattern
3. Stateless: All client-server interactions are stateless; authorization encoded in tokens passed with each request
4. Cacheable: Resources cached when applicable, on server or client side
5. Tiered system architecture: "Server" decomposable into multiple independent elements deployed independently (business logic and database deployable separately)
6. Code on demand (optional): Server provides executable code to client (JavaScript example)

## Chapter 16. Virtualization

LAMP Stack Container Layering Process (from section 16.4): (1) Create a container image containing a Linux distribution (downloadable from a library using a container management system); (2) execute (instantiate) the image; (3) use that container to load services—Apache, in the example, using Linux features; (4) exit the container and inform the container management system this is a second image; (5) execute this second image and load MySQL; (6) exit the container and give this third image a name; (7) repeat this process one more time and load PHP. The final image holds the entire LAMP stack created in layers. When PHP updates to a newer version and moves to production, the container management system moves only the PHP layer, saving effort compared to moving the entire stack. Updating MySQL requires executing steps 5-7 again.

VM and Container Comparison (section 16.5):
VMs virtualize physical hardware (CPU, disk, memory, network) and include a complete operating system; containers share an operating system kernel through the runtime engine. VMs can run almost any operating system and almost any program not requiring direct hardware interaction; containers are limited to Linux, Windows, or IOS. Services within VMs are started, stopped, and paused through OS functions; container services through container runtime engine functions. Multiple services can run efficiently in a single VM; containers typically run one service to prevent image bloat and startup delays. VMs persist beyond service termination; containers do not. Port usage restrictions exist for containers but not VMs.

Architectural Diagrams Referenced:
Figure 16.1: Bare-metal (Type 1) hypervisor architecture—shows host computer containing multiple VMs (VM1, VM2, VM3) with hypervisor at the bottom, running directly on physical hardware, typical of data centers and cloud.

Figure 16.2: Hosted (Type 2) hypervisor architecture—shows host computer with an operating system at bottom, hypervisor running as a service on the OS, and multiple VMs executing within the hypervisor; used on desktop and laptop computers to run incompatible applications or replicate production environments.

Figure 16.3: Container architecture—shows host computer with hypervisor (or bare metal) at bottom, operating system above it, container runtime engine above the OS, and multiple containers (container 1, 2, 3) at the top, all sharing the same OS kernel.

Figure 16.4: Kubernetes Pod hierarchy—shows a node (hardware or VM) containing multiple Pods (Pod 1 and Pod 2); Pod 1 contains two containers (container 1 and 2), Pod 2 contains one container (container 3). Containers within a Pod share IP address, port space, and ephemeral storage volumes.

Virtualization Technologies Mentioned:
Bare-metal (Type 1) hypervisors: run directly on physical hardware in data centers and clouds. Hosted (Type 2) hypervisors: run atop host OS on desktops and laptops. Emulators (QEMU): simulate cross-processor execution, can emulate complete systems (BIOS, x86 processor, memory, sound, graphics, floppy). Container runtime engines: Docker, containerd, Mesos (all implement Open Container Initiative standards). Kubernetes: orchestration software for container deployment, management, and scaling. Function-as-a-Service (FaaS): cloud provider feature offering rapid container instantiation.

## Chapter 17. The Cloud and Distributed Computing

Figure 17.1: A cloud data center showing rows of large supercomputers in racks, representing the tens of thousands of physical computers (closer to 100,000 than 50,000) organized with high-speed network switches connecting the racks. Each rack contains more than 25 computers with multiple CPUs.

Figure 17.2: Gateways into a public cloud diagram showing a client system connecting to a management gateway via management UI (for VM allocation and management), and a separate message gateway (for service communication).

Figure 17.3: Long tail distribution histogram of 1,000 "launch instance" requests to AWS. The distribution peaks at 22 seconds (mode), median is 23 seconds, mean is 28 seconds, and the 95th percentile is 57 seconds, with some requests extending to 220+ seconds. This illustrates how 5 percent of requests take 2 to 10 times longer than average.

Figure 17.4: Load balancer architecture showing two client systems sending requests through a load balancer to two service instance systems, with the load balancer using round-robin distribution (alternating requests between instances).

Figure 17.5: Autoscaler monitoring system showing an autoscaler at the top right monitoring the utilization of three service instances at the bottom, which are connected to the autoscaler.

Autoscaler configuration example: AWS "launch instance" rule: "Create a new VM when CPU utilization is above 80 percent for 5 minutes."

Timeout mechanism example: 200 milliseconds timeout interval with failure recovery triggered after 3 missed messages over a 1-second interval.

Cloud failure statistics (Amazon): In a data center with approximately 64,000 computers with two spinning disk drives, approximately 5 computers and 17 disks fail every day.

AWS launch instance latency statistics from Figure 17.3:
- Mode (histogram peak): 22 seconds
- Median: 23 seconds
- Mean: 28 seconds
- 95th percentile: 57 seconds
- Maximum observed: 220+ seconds

NTP (Network Time Protocol) accuracy:
- Local area networks: approximately 1 millisecond
- Public networks: approximately 10 milliseconds
- Congestion-induced errors: 100+ milliseconds

Distributed coordination software options for shared state management: Apache Zookeeper, Consul, etcd (proven, open-source implementations that should be used rather than custom solutions).

## Chapter 18. Mobile Systems

Wireless Protocol Categories by Distance:
- Within 4 centimeters: Near Field Communication (NFC) for keycards and contactless payments
- Within 10 meters: IEEE 802.15 family (Bluetooth, Zigbee)
- Within 100 meters: IEEE 802.11 family (Wi-Fi)
- Within several kilometers: IEEE 802.16 standards (WiMAX)
- More than several kilometers: Cellular or satellite communication

Energy Throttling Tactics:
- Reducing display brightness or refresh rate on smartphones
- Reducing the number of active processor cores or clock rate of cores
- Reducing frequency of sensor readings (e.g., GPS location every minute instead of every few seconds)
- Selecting fewer location data sources (GPS and cell towers instead of both)

Sensor Stack Functions:
- Reading raw data: Driver queries sensor periodically; frequency is adjustable parameter affecting processor load and accuracy
- Smoothing data: Moving averages and Kalman filters reduce noise from voltage variations, sensor contamination
- Converting data: Transforming various sensor formats (millivolts, feet, degrees Celsius) to common meaningful forms
- Sensor fusion: Automobile pedestrian recognition combines thermal imagers, radar, lidar, and cameras to detect pedestrians in all conditions

Four-Level Testing Hierarchy (Lane Keep Assist Example):
1. Software component level: Unit and end-to-end testing of lane detection component for stability and correctness
2. Function level: Testing lane detection together with mapping component in simulated environment to validate interfacing and safe concurrency
3. Device level: Deploying integrated function on target ECU with simulated external inputs (messages from other ECUs, sensor inputs) for performance and stability
4. System level: Full-size configurations in test labs and prototypes, testing lane keep assist with steering and acceleration/braking functions using projected or video road imagery to confirm integrated subsystems work together

Display Resolution Constraints:
- 320 × 320 pixel display: Requires significant effort to minimize information density for GPS-style mapping
- 1,280 × 720 pixels: Allows richer, more informative display strategy

Power Loss Tolerance Requirements (example specification):
- Restore power and have system operational within 30 seconds
- Hardware must survive power cuts at any time without permanent damage
- OS must start robustly when sufficient power is provided
- Software scheduled to launch as soon as OS is ready
- Runtime environment can be killed without compromising binary, configuration, and operational data integrity or state consistency
- Applications need strategy for handling data arriving during inoperativity
- Startup time from power-on to software ready state under specified period

## Chapter 19. Architecturally Significant Requirements

Table 19.1 presents a tabular form of a utility tree for a healthcare system:

Quality Attribute | Attribute Refinement | ASR Scenario
Performance | Transaction response time | A user updates a patient's account in response to a change-of-address notification while the system is under peak load, and the transaction completes in less than 0.75 seconds. (H, H)
Performance | Throughput | At peak load, the system is able to complete 150 normalized transactions per second. (M, M)
Usability | Proficiency training | A new hire with two or more years' experience in the business can learn, with 1 week of training, to execute any of the system's core functions in less than 5 seconds. (M, L)
Usability | Efficiency of operations | A hospital payment officer initiates a payment plan for a patient while interacting with that patient and completes the process with no input errors. (M, M)
Configurability | Data configurability | A hospital increases the fee for a particular service. The configuration team makes and tests the change in 1 working day; no source code needs to change. (H, L)
Maintainability | Routine changes | A maintainer encounters response-time deficiencies, fixes the bug, and distributes the bug fix with no more than 3 person-days of effort. (H, M)
Maintainability | Routine changes | A reporting requirement requires a change to the report-generating metadata. Change is made and tested in 4 person-hours of effort. (M, L)
Maintainability | Upgrades to commercial components | The database vendor releases a new major version that is successfully tested and installed in less than 3 person-weeks. (H, M)
Maintainability | Adding new feature | A feature that tracks blood bank donors is created and successfully integrated within 2 person-months. (M, M)
Security | Confidentiality | A physical therapist is allowed to see that part of a patient's record dealing with orthopedic treatment, but not other parts or any financial information. (H, M)
Security | Resisting attacks | The system repels an unauthorized intrusion attempt and reports the attempt to authorities within 90 seconds. (H, M)
Availability | No down time | The database vendor releases new software, which is hot-swapped into place, with no downtime. (H, L)
Availability | No down time | The system supports 24/7/365 web-based account access by patients. (M, M)

Figure 19.1 illustrates relationships between business goals and architecture: solid arrows show business goals leading to quality attributes, which then lead to architecture; slanting arrows show business goals leading directly to architectural decisions; and dashed arrows show business goals leading to non-architectural solutions. The diagram demonstrates that business goals are a critical input source alongside QAs, and not all business goals produce architectural effects.

The Quality Attribute Workshop produces specific outputs: a list of architectural drivers and a set of prioritized QA scenarios collectively ranked by stakeholders. These enable subsequent refinement of system and software requirements, clarification of architectural drivers, justification of design decisions, guidance for prototype and simulation development, and influence over the order of architecture development.

## Chapter 20. Designing an Architecture

Table 20.1 (Elements and Responsibilities) provides an example structure: the Data Stream element collects data from all data sources in real time and dispatches it to both the Batch Component and Speed Component for processing; the Batch component is responsible for storing raw data and pre-computing Batch Views to be stored in the Serving Component. The accompanying diagram (Figure 20.4) shows a batch/speed architecture with elements including Data Stream, Master Dataset, Pre-Computing, Real-Time Viewer, and Query and Reporting, with data flows connecting them.

The Value of Information (VoI) example illustrates decision analysis under uncertainty: a team choosing between a traditional three-tier architecture ($500,000 cost) versus microservices ($650,000 cost) must consider refactoring costs if wrong: $300,000 for three-tier vs. $100,000 for microservices. VoI calculates expected value of perfect information (EVPI) and expected value of sample information (EVSI) using Bayes's Theorem to determine how much to invest in prototyping.

The Kanban board (Figure 20.5) tracks design progress with three columns: "Not Yet Addressed" contains high-priority QA scenarios and constraints at the top; "Partially Addressed" shows medium-priority items and use cases with various priorities; "Completely Addressed" shows resolved high-priority concerns. Drivers move across columns as iterations address them, providing visual confirmation that high-priority drivers are progressing toward completion.

## Chapter 21. Evaluating an Architecture

Table 21.1 - ATAM Evaluation Team Roles:
- Team Leader: Sets up the evaluation; coordinates with the client, making sure the client's needs are met; establishes the evaluation contract; forms the evaluation team; sees that the final report is produced and delivered.
- Evaluation Leader: Runs the evaluation; facilitates elicitation of scenarios; administers the scenario prioritization process; facilitates the evaluation of scenarios against the architecture.
- Scenario Scribe: Writes scenarios in a sharable, public form during scenario elicitation; captures the agreed-on wording of each scenario, halting discussion until the exact wording is captured.
- E-Scribe: Captures the proceedings in electronic form: raw scenarios, issue(s) that motivate each scenario (often lost in the wording of the scenario itself), and the results of each scenario's analysis; also generates a list of adopted scenarios for distribution to all participants.
- Questioner: Asks probing quality attribute-based questions.

Table 21.2 - ATAM Phases and Their Characteristics:
Phase 0: Partnership and preparation | Evaluation team leadership and key project decision makers | Proceeds informally as required, perhaps over a few weeks
Phase 1: Evaluation | Evaluation team and project decision makers | 1-2 days
Phase 2: Evaluation (continued) | Evaluation team, project decision makers, and stakeholders | 2 days
Phase 3: Follow-up | Evaluation team and evaluation client | 1 week

Figure 21.1 - Architecture Approach Analysis Template: The example shows a scenario "detect and recover from the HW failure of the main switch" with attributes, environment, stimulus, and response listed. The architectural decision involves a primary CPU at the top and backup CPU with a watchdog at the bottom, connected to a switch CPU on the right. A heartbeat of one second is sent from primary to backup CPU. The template captures the architectural decision, sensitivity point (frequency of heartbeats affects detection time), tradeoff (higher heartbeat frequency improves availability but consumes more processing and bandwidth), risk (some heartbeat frequencies result in unacceptable detection times), and non-risk (certain frequency assignments are safe).

Table 21.3 - A Typical Agenda for Lightweight Architecture Evaluation:
Step 1: Present the method steps - May be omitted if participants are familiar with the process
Step 2: Review the business goals - Brief review to ensure goals and priorities are fresh with no surprises
Step 3: Review the architecture - Brief overview of module and C&C views, highlighting changes, tracing 1-2 scenarios
Step 4: Review the architectural approaches - Architect highlights approaches for specific quality attribute concerns, typically as part of step 3
Step 5: Review the quality attribute utility tree - Team reviews existing tree and updates with new scenarios, response goals, or priorities and risk assessments
Step 6: Brainstorm and prioritize scenarios - Brief brainstorming to determine whether new scenarios merit analysis
Step 7: Analyze the architectural approaches - Mapping highly ranked scenarios onto architecture, focusing on recent changes or previously unanalyzed portions; if architecture changed, reanalyze high-priority scenarios in light of these changes
Step 8: Capture the results - Review existing and newly discovered risks, non-risks, sensitivities, tradeoffs, discuss new risk themes

Security Tactics-Based Questionnaire Example: In a healthcare data management system, when asked "Does the system support data encryption?", the architect paused and admitted that the system had a requirement that no data could be passed over a network "in the clear" (without encryption). They XOR'd all data before sending it over the network. This is a risk that the tactics-based questionnaire uncovered quickly and inexpensively—they had met the requirement in a strict sense, but their encryption algorithm could be cracked by a high school student with modest abilities.

## Chapter 22. Documenting an Architecture

Table 22.1 (Module Views): Elements are modules providing coherent responsibilities; Relations are is-part-of (part/whole), depends-on (dependency), is-a (generalization/specialization); Constraints include topological limitations on visibility; Usage includes blueprint for construction, impact analysis of changes, incremental development planning, requirements traceability, communicating functionality, work assignment support, showing data model.

Table 22.2 (C&C Views): Elements are components (principal processing units and data stores) and connectors (pathways of interaction); Relations are attachments (components to connectors forming a graph); Constraints state components attach only to connectors and vice versa, attachments require compatible components/connectors, connectors cannot appear isolated; Usage is showing how system works, guiding development by specifying runtime element structure/behavior, reasoning about performance and availability.

Table 22.3 (Allocation Views): Elements are software elements with required properties and environmental elements with provided properties; Relations are allocated-to (software element mapping to environmental element); Constraints vary by view type; Usage includes reasoning about performance/availability/security/safety, distributed development and team work allocation, concurrent access to software versions, system installation form and mechanisms.

Table 22.4 (Example Design Decisions Table):
- Design Decision: Introduce concurrency (tactic) in TimeServerConnector and FaultDetectionService | Rationale: Concurrency enables receiving and processing multiple events (traps) simultaneously.
- Design Decision: Use messaging pattern with message queue in communications layer | Rationale: Despite performance penalty, message queue was chosen for high-performance implementations and to support quality attribute scenario QA-3.

Figure 22.1 shows a combined view overlay of client-server, multi-tier, and deployment views with admin user PC and internet user PC as client tier on intranet and internet respectively, app server 1 with web tier (web UI web component), app server 2 with component tier (stateful session beans: account controller, customer controller, tx controller; entity beans: account, customer, tx), and database server with back-end tier containing bank DB relational data source, connected via HTTP, remote component calls, and JDBC database access.

Figure 22.2 (UML Sequence Diagram): Shows user actor sending login synchronous message (filled arrowhead) to login page; login page sends login function to login controller; login controller sends check pwd function to user direct access object; after execution occurrence, return message (dashed arrow) sent back; login controller creates user session and sends asynchronous message (open arrowhead) to logger to register user login; execution returns to login page then user.

Figure 22.3 (Activity Diagram): Shows depth meter, dive tracker, and thermometer columns; read pressure block; decision diamond for underwater; if yes, enter dive mode in dive tracker column with check depth (passing to read pressure in depth meter) and check water temperature; if ascending too fast decision, beep alarm in dive tracker; if not underwater, exit dive mode; fork nodes (thick bars) split concurrent flows; join nodes synchronize them; sleep operations indicate concurrent execution.

Figure 22.4 (UML State Machine Diagram): Car stereo system with off state transitioning via power button to radio playing state; within radio playing state, H state (history) with FM tuner playing and AM tuner playing substates connected by FM/AM button; CD button transitions to CD loading state; CD loading transitions to CD playing state via CD insert; ejectDisc action (shown with slash) and guard conditions on transitions; invalid CD or ejectDisc return to radio playing; final transition via power button off.

## Chapter 23. Managing Architecture Debt

Design Structure Matrix Examples from Apache Camel:

Figure 23.1 shows a 32x32 DSM of Apache Camel files with structural dependencies marked as "dp" (dependency), "im" (implementation), and "ex" (extension). For instance, MethodCallExpression.java (row 9) depends on and extends ExpressionDefinition.java (column 1), and AssertionClause.java (row 11) depends on MockEndpoint.java (column 10). The sparse nature of this matrix indicates relatively low structural coupling and minimal architecture debt.

Figure 23.2 overlays evolutionary co-change information on the same files. Cell (8,3) is marked with "4", indicating that BeanExpression.java and MethodNotFoundException.java have no structural relation but changed together four times. Cell (22,1) shows "dp, 3", meaning XMLTokenizerExpression.java structurally depends on ExpressionDefinition.java and they co-changed three times. The resulting dense matrix with annotations above the diagonal reveals strong evolutionary coupling despite low structural coupling, confirming the project suffers from high architecture debt.

Figure 23.3 illustrates a clique from Apache Cassandra: locator.AbstractReplicationStrategy (row 8) depends on service.WriteResponseHandler (row 4) and aggregates locator.TokenMetadata (row 5). Files 4 and 5 both depend on file 8, forming a strongly connected cycle.

Figure 23.4 demonstrates unhealthy inheritance from Cassandra: io.sstable.SSTableReader (row 14) inherits from io.sstable.SSTable (row 12), indicated by "ih" notation. However, SSTable depends on SSTableReader (marked "dp" at cell 12,14), and cells (12,14) and (14,12) both show "68", representing 68 co-commits. This excessively high co-change count signals debt resolvable by moving functionality from child to parent.

SS1 Case Study Quantification:
- System size: 797 source files
- Period analyzed: 2 years
- Total issues recorded: 2,756 (1,079 bugs)
- Total commits: 3,262
- Hotspot clusters identified: 3 clusters
- Files in hotspots: 291 files (36.5% of project)
- Defects in hotspots: 265 (89% of total project defects)
- Estimated refactoring effort: 14 person-months
- Average bug fixes per file (project-wide): 0.33 annually
- Average bug fixes per file (in hotspots): 237.8 annually
- Expected bug fixes post-refactoring (hotspot files): 96 annually
- Expected annual savings: 41.35 person-months
- ROI ratio: 3:1 (savings-to-effort ratio in first year)

## Chapter 24. The Role of Architects in Projects

Table 24.1: Architect's Role in Supporting Project Management Knowledge Areas
PMBOK Knowledge Area | Description | Software Architect Role
Project Integration Management | Ensuring that the various elements of the project are properly coordinated | Create design and organize team around design; manage dependencies. Implement the capture of metrics. Orchestrate requests for changes.
Project Scope Management | Ensuring that the project includes all of the work required and only the work required | Elicit, negotiate, and review runtime requirements and generate development requirements. Estimate cost, schedule, and risk associated with meeting requirements.
Project Time Management | Ensuring that the project completes in a timely fashion | Help define the work breakdown structure. Define tracking measures. Recommend assignment of resources to software development teams.
Project Cost Management | Ensuring that the project is completed within the required budget | Gather costs from individual teams; make recommendations regarding build/buy and resource allocations.
Project Quality Management | Ensuring that the project will satisfy the needs for which it was undertaken | Design for quality and track the system against the design. Define quality metrics.
Project Human Resource Management | Ensuring that the project makes the most effective use of the people involved with the project | Define the required technical skill sets. Mentor developers about career paths. Recommend training. Interview candidates.
Project Communications Management | Ensuring timely and appropriate generation, collection, dissemination, storage, and disposition of project information | Ensure communication and coordination among developers. Solicit feedback as to progress, problems, and risks. Oversee documentation.
Project Risk Management | Identifying, analyzing, and responding to project risk | Identify and quantify risks; adjust the architecture and processes to mitigate risk.
Project Procurement Management | Acquiring goods and services from outside the organization | Determine technology requirements; recommend technology, training, and tools.

Table 24.2: Agile Principles and Architecture-centric Perspective
Agile Principle | Architecture-centric View
"Our highest priority is to satisfy the customer through early and continuous delivery of valuable software." | Absolutely.
"Welcome changing requirements, even late in development. Agile processes harness change for the customer's competitive advantage." | Absolutely. This principle is served by architectures that provide high degrees of modifiability and deployability.
"Deliver working software frequently, from a couple of weeks to a couple of months, with a preference for the shorter time scale." | Absolutely, as long as this principle is not seen as precluding a thoughtful architecture. DevOps has a large role to play here, and architectures can support DevOps.
"Business people and developers must work together daily throughout the project." | Business goals lead to quality attribute requirements, which the architecture's primary duty is to fulfill.
"Build projects around motivated individuals. Give them the environment and support they need, and trust them to get the job done." | While we agree in principle, many developers are inexperienced. So make sure to include a skilled, experienced, and motivated architect to help guide these individuals.
"The most efficient and effective method of conveying information to and within a development team is face-to-face conversation." | This is nonsense for nontrivial systems. Humans invented writing because our brains can't remember everything we need to remember. Interfaces, protocols, architectural structures, and more need to be written down. This is also nonsense for any system that has a maintenance phase in which the original team is nowhere to be found.
"Working software is the primary measure of progress." | Yes, as long as "primary" is not taken to mean "only," and as long as this principle is not used as an excuse to eliminate all work except coding.
"Agile processes promote sustainable development. The sponsors, developers, and users should be able to maintain a constant pace indefinitely." | Absolutely.
"Continuous attention to technical excellence and good design enhances agility." | Absolutely.
"Simplicity—the art of maximizing the amount of work not done—is essential." | Yes, of course, as long as it is understood that the work we are not doing can actually be jettisoned safely without detriment to the system being delivered.
"The best architectures, requirements, and designs emerge from self-organizing teams." | No, they don't. The best architectures are consciously designed by skilled, talented, trained, and experienced architects.
"At regular intervals, the team reflects on how to become more effective, and then tunes and adjusts its behavior accordingly." | Absolutely.

Figure 24.1 Description: Three approaches to architectural design are depicted as graphs with design effort on the horizontal axis and development cycles on the vertical axis. The BDUF approach shows an open downward curve that decreases on the right side, concentrating design effort upfront. The emergent approach shows a wave pattern with development cycles, where design effort fluctuates with each cycle. The Iteration 0 approach shows wave patterns where the first wave (design iteration) is higher and decreases as subsequent waves move rightward, indicating concentrated initial design followed by smaller design iterations aligned with development cycles.

Figure 24.2 Description: Coordination between teams and modules is represented as a diagram with two human icons representing Team A and Team B standing on their respective module blocks. A double-headed arrow between teams A and B represents the coordination requirement. An arrow from Module A to Module B represents the dependency, illustrating that when Module A uses an interface from Module B, the teams must coordinate any interface changes.

## Chapter 25. Architecture Competence

Table 25.1 - Technical Duties of a Software Architect:

General Duty Area: Architecting
- Creating an architecture: Design or select an architecture. Create a software architecture design plan. Build a product line or product architecture. Make design decisions. Expand details and refine the design to converge on a final design. Identify the patterns and tactics, and articulate the principles and key mechanisms of the architecture. Partition the system. Define how the components fit together and interact. Create prototypes.
- Evaluating and analyzing an architecture: Evaluate an architecture (for your current system or for other systems) to determine the satisfaction of use cases and quality attribute scenarios. Create prototypes. Participate in design reviews. Review the designs of the components designed by junior engineers. Review designs for compliance with the architecture. Compare software architecture evaluation techniques. Model alternatives. Perform tradeoff analysis.
- Documenting an architecture: Prepare architectural documents and presentations useful to stakeholders. Document or automate the documentation of software interfaces. Produce documentation standards or guidelines. Document variability and dynamic behavior.
- Working with and transforming existing system(s): Maintain and evolve an existing system and its architecture. Measure architecture debt. Migrate existing system to new technology and platforms. Refactor existing architectures to mitigate risks. Examine bugs, incident reports, and other issues to determine revisions to existing architecture.
- Performing other architecting duties: Sell the vision. Keep the vision alive. Participate in product design meetings. Give technical advice on architecture, design, and development. Provide architectural guidelines for software design activities. Lead architecture improvement activities. Participate in software process definition and improvement. Provide architecture oversight of software development activities.

General Duty Area: Duties concerned with life-cycle activities other than architecting
- Managing the requirements: Analyze functional and quality attribute software requirements. Understand business, organizational, and customer needs. Listen to and understand the scope of the project. Understand the client's key design needs and expectations. Advise on the tradeoffs between software design choices and requirements choices.
- Evaluating future technologies: Analyze the current IT environment and recommend solutions for deficiencies. Work with vendors to represent the organization's requirements and influence future products. Develop and present technical white papers.
- Selecting tools and technology: Manage the introduction of new software solutions. Perform technical feasibility studies of new technologies and architectures. Evaluate commercial tools and software components from an architectural perspective. Develop internal technical standards and contribute to the development of external technical standards.

Table 25.2 - Nontechnical Duties of a Software Architect:

General Duty Area: Management
- Supporting project management: Provide feedback on the appropriateness and difficulty of the project. Help with budgeting and planning. Follow budgetary constraints. Manage resources. Perform sizing and estimation. Perform migration planning and risk assessment. Take care of or oversee configuration control. Create development schedules. Measure results using metrics. Identify and schedule architectural releases. Serve as a "bridge" between the technical team and the project manager.
- Managing the people on the architect's team: Build "trusted advisor" relationships. Coordinate. Motivate. Advocate. Train. Act as a supervisor. Allocate responsibilities.

General Duty Area: Organization- and business-related duties
- Supporting the organization: Grow an architecture evaluation capability in the organization. Review and contribute to research and development efforts. Participate in the hiring process for the team. Help with product marketing. Institute cost-effective and appropriate software architecture design reviews. Help develop intellectual property.
- Supporting the business: Understand and evaluate business processes. Translate business strategy into technical strategy. Influence the business strategy. Understand and communicate the business value of software architecture. Help the organization meet its business goals. Understand customer and market trends.

General Duty Area: Leadership and team building
- Providing technical leadership: Be a thought leader. Produce technology trend analysis or roadmaps. Mentor other architects.
- Building a team: Build the development team and align them with the architecture vision. Mentor developers and junior architects. Educate the team on the use of the architecture. Foster the professional development of team members. Coach teams of software design engineers for planning, tracking, and completion of work. Mentor and coach staff in the use of software technologies. Maintain morale, both within and outside the architecture group. Monitor and manage team dynamics.

Table 25.3 - Skills of a Software Architect:

General Skill Area: Communication skills
- Outward communication (beyond the team): Ability to make oral and written communications and presentations. Ability to present and explain technical information to diverse audiences. Ability to transfer knowledge. Ability to persuade. Ability to see from and sell to multiple viewpoints.
- Inward communication (within the team): Ability to listen, interview, consult, and negotiate. Ability to understand and express complex topics.

General Skill Area: Interpersonal skills
- Team relationships: Ability to be a team player. Ability to work effectively with superiors, subordinates, colleagues, and customers. Ability to maintain constructive working relationships. Ability to work in a diverse team environment. Ability to inspire creative collaboration. Ability to build consensus. Ability to be diplomatic and respect others. Ability to mentor others. Ability to handle and resolve conflict.

General Skill Area: Work skills
- Leadership: Ability to make decisions. Ability to take initiative and be innovative. Ability to demonstrate independent judgment, be influential, and command respect.
- Workload management: Ability to work well under pressure, plan, manage time, and estimate. Ability to support a wide range of issues and work on multiple complex tasks concurrently. Ability to effectively prioritize and execute tasks in a high-pressure environment.
- Skills to excel in the corporate environment: Ability to think strategically. Ability to work under general supervision and under constraints. Ability to organize workflow. Ability to detect where the power is and how it flows in an organization. Ability to do what it takes to get the job done. Ability to be entrepreneurial, to be assertive without being aggressive, and to receive constructive criticism.
- Skills for handling information: Ability to be detail-oriented while maintaining overall vision and focus. Ability to see the big picture.
- Skills for handling the unexpected: Ability to tolerate ambiguity. Ability to take and manage risks. Ability to solve problems. Ability to be adaptable, flexible, open-minded, and resilient.
- Ability to think abstractly: Ability to look at different things and find a way to see how they are, in fact, just different instances of the same thing. (The authors note this may be one of the most important skills for an architect.)

Table 25.4 - Knowledge Areas of a Software Architect:

General Knowledge Area: Computer science knowledge
- Knowledge of architecture concepts: Knowledge of architecture frameworks, architectural patterns, tactics, structures and views, reference architectures, relationships to system and enterprise architecture, emerging technologies, architecture evaluation models and methods, and quality attributes.
- Knowledge of software engineering: Knowledge of software development knowledge areas, including requirements, design, construction, maintenance, configuration management, engineering management, and software engineering process. Knowledge of systems engineering.
- Design knowledge: Knowledge of tools and design and analysis techniques. Knowledge of how to design complex multi-product systems. Knowledge of object-oriented analysis and design, and UML and SysML diagrams.
- Programming knowledge: Knowledge of programming languages and programming language models. Knowledge of specialized programming techniques for security, real time, safety, etc.

General Knowledge Area: Knowledge of technologies and platforms
- Specific technologies and platforms: Knowledge of hardware/software interfaces, web-based applications, and Internet technologies. Knowledge of specific software/operating systems.
- General knowledge of technologies and platforms: Knowledge of the IT industry's future directions and the ways in which infrastructure impacts an application.

General Knowledge Area: Knowledge about the organization's context and management
- Domain knowledge: Knowledge of the most relevant domains and domain-specific technologies.
- Industry knowledge: Knowledge of the industry's best practices and industry standards. Knowledge of how to work in onshore/offshore team environments.
- Business knowledge: Knowledge of the company's business practices, and its competition's products, strategies, and processes. Knowledge of business and technical strategy, and business reengineering principles and processes. Knowledge of strategic planning, financial models, and budgeting.
- Leadership and management techniques: Knowledge of how to coach, mentor, and train software team members. Knowledge of project management. Knowledge of project engineering.

## Chapter 26. A Glimpse of the Future: Quantum Computing

No complete code examples, architectural diagrams, or tactic tables are present in this chapter range. The chapter is a conceptual introduction to quantum computing fundamentals presented through prose explanation and mathematical notation rather than implementation examples. The authors acknowledge that detailed algorithm mechanics (e.g., the full HHL algorithm) are too complex for inclusion and direct readers to references like "Programming Quantum Computers" by Johnston, Harrigan, and Gimeno-Segovia for more thorough treatment. The mathematical expressions shown (e.g., |α|² + |β|² = 1, 2¹²⁸ iterations for Grover's algorithm, log(bit count) runtime for Shor's algorithm) are notation within prose rather than executable code or pseudocode samples.

## References

No examples. The References section contains only bibliographic citations. No code examples, case studies, tables, diagrams, or architectural descriptions are present—only formatted reference entries with author names, publication titles, publishers, dates, and URLs where applicable (e.g., http://sei.cmu.edu/, http://research.google.com/, etc.).
