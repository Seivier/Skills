# Building Evolutionary Architectures — Ejemplos

## Índice de capítulos
- [Front Matter](#front-matter)
- [Chapter 1. Evolving Software Architecture](#chapter-1-evolving-software-architecture)
- [Chapter 2. Fitness Functions](#chapter-2-fitness-functions)
- [Chapter 3. Engineering Incremental Change](#chapter-3-engineering-incremental-change)
- [Chapter 4. Automating Architectural Governance](#chapter-4-automating-architectural-governance)
- [Chapter 5. Evolutionary Architecture Topologies](#chapter-5-evolutionary-architecture-topologies)
- [Chapter 6. Evolutionary Data](#chapter-6-evolutionary-data)
- [Chapter 7. Building Evolvable Architectures](#chapter-7-building-evolvable-architectures)
- [Chapter 8. Evolutionary Architecture Pitfalls and Antipatterns](#chapter-8-evolutionary-architecture-pitfalls-and-antipatterns)
- [Chapter 9. Putting Evolutionary Architecture into Practice](#chapter-9-putting-evolutionary-architecture-into-practice)

## Front Matter

The Front Matter itself does not contain code examples or formal design diagrams. However, it references several key structural elements used throughout the book:

PenultimateWidgets—a surrogate case study company used to house all practical examples and scenarios drawn from real-world consulting projects. Individual case studies within PenultimateWidgets come from actual client work, but are anonymized under this fictional corporate name.

Fitness functions—mentioned in the Foreword as the central monitoring mechanism for evolutionary architecture. The Foreword notes these are explored in detail within the book to track the state of the architecture during evolutionary change.

Conway's Law—identified as a tower principle that figures heavily throughout the book's treatment of architectural evolution, referring to the correspondence between system organization and organizational structure.

Continuous Delivery—highlighted as the crucial enabling factor that makes evolutionary architecture practical, allowing the small changes and feedback loops essential to guided evolution.

## Chapter 1. Evolving Software Architecture

No syntactic code examples appear in this range of Chapter 1.

Architectural case study—PenultimateWidgets star-rating service: A large widget seller has a catalog page backed by microservices. The star-rating service is shared across multiple teams (customer service, shipping evaluation, etc.). The star-rating team releases a new version (v2) supporting half-star ratings alongside the existing version (v1 with integer-only ratings). Other services do not require immediate migration; each service can adopt v2 at its own pace. PenultimateWidgets' DevOps practices monitor service invocations and architectural routes between services. When no service routes to a particular version within a defined time window, the operations group automatically disintegrates (removes) that version from the ecosystem. This exemplifies incremental change: old and new coexist, consumers migrate asynchronously, and obsolete versions are garbage-collected without manual intervention.

Sidebar scenario—"Why We Didn't Have Microservices in the Year 2000": An architect with a hypothetical time machine pitches microservices to the head of operations in 2000: "I propose designing each service around business capabilities with high decoupling—call it microservices." The operations head asks what is needed. The architect responds: "About 50 new computers, 50 new operating system licenses, 20 additional computers for isolated databases, and database licenses." The operations head replies: "Please leave my office." The scenario illustrates that microservices architecture, while conceptually sound, required an ecosystem that did not exist in 2000: cheap commodity hardware, free operating systems (Linux), and DevOps automation to make operations financially and logistically feasible.

Architectural dimension example (from Figure 1-2 description): An application identifies the following architectural dimensions and characteristics requiring fitness functions: *auditability* (compliance and audit trail integrity), *data* (schema evolution, data consistency), *security* (vulnerability prevention, policy enforcement), *performance* (latency, throughput targets), *legality* (regulatory compliance), and *scalability* (capacity to handle growth). As business requirements evolve, each dimension maintains its own fitness function to ensure characteristics do not degrade.

## Chapter 2. Fitness Functions

**ArchUnit Cycle Prevention (Example 2-1)**
```
public class CycleTest {
    @Test
    public void test_for_cycles() {
        slices().
          matching("com.myapp.(*)..").
          should().beFreeOfCycles()
}
```
This test verifies that packages matching the pattern com.myapp.(*) have no cyclic dependencies, enforceable in continuous build.

**Synthetic Transactions Pattern**
Requests into a microservices architecture carry a synthetic flag. They traverse the normal interaction flow (tracked via correlation ID for forensics) exactly as real transactions would, until the final step where the system checks the flag and rolls back instead of committing. This allows architects to observe real-world performance without side effects. Caveat: if the synthetic flag is accidentally omitted, hundreds of spurious orders (e.g.) appear—itself governable by a fitness function checking that synthetic-flagged transactions have the flag set.

**PenultimateWidgets Case Study**
PenultimateWidgets created a spreadsheet of desirable architecture characteristics (scalability, security, resiliency, and others). Rather than relying on occasional, ad hoc verification, they reformulated each characteristic into objective fitness functions and wired them into the deployment pipeline, ensuring continuous governance as developers add features.

**Orchestrated Microservices Dependency Governance (Figure 2-4 context)**
A system with an orchestrator service holding workflow state requires that only the orchestrator initiates inter-service communication. The continuous fitness function approach: each service publishes monitoring data or messages to a queue indicating which services it calls; the orchestrator monitors this and immediately alerts on illegal communication patterns. The triggered approach: the deployment pipeline periodically calls a fitness function that harvests log files to detect and report disallowed service-to-service communication (detailed in "Communication Governance in Microservices").

## Chapter 3. Engineering Incremental Change

No executable code examples appear in this chapter range. However, the text describes several architectural and tooling patterns in prose:

Service Versioning Pattern (PenultimateWidgets): When deploying the new star rating service, architects use a proxy endpoint routing mechanism. The endpoint accepts version requests (old or new) from calling services and routes accordingly, avoiding forced migration. Services independently decide when to request the new version, allowing gradual ecosystem evolution. Operations monitors routes using architectural monitoring and automatically removes old service versions when no route traffic occurs within a threshold interval (demonstrated by tool Swabbie).

Consumer-Driven Contracts Pattern (Pact): Consuming services create test suites encapsulating their requirements from a provider service. Consumers hand these tests to the provider, who commits to keeping them passing. The provider executes all consumer tests in addition to internal tests in the deployment pipeline, creating an engineering safety net. In the diagram concept: a provider supplies data (JSON) to consumers C1 and C2; each consumer's tests define the contract; the provider runs all three test suites (C1, C2, internal) continuously.

Deployment Pipeline Architecture (PenultimateWidgets Invoicing): Six-stage pipeline: (1) Replicate CI with unit/functional tests; (2) Containerize and deploy to dynamic test environment; (3) Atomic fitness functions—automated scalability, security penetration, code-change metrics for audit tracking; (4) Holistic fitness functions—contract tests (Pact) protecting integration, further scalability tests; (5a) Manual security review stage; (5b) Manual audit stage (regulatory mandate); (6) Automated deployment to production triggered only after manual stages succeed. Weekly automated reporting tracks fitness function success rates.

API Consistency Pattern (openapi.yaml): Stage 1 defines new API in openapi.yaml specification. Spectral and OpenAPI.Tools validate structure. Stage 2 publishes specification to sandbox, runs tests verifying application behavior consistency. Stage 3 uses Pact to test consumer-driven contracts ensuring integration points hold. Stage 4 deploys with feature toggle controlling feature exposure, enabling A/B testing before official release.

Feature Toggle Implementation: Described as a simple if-statement inspecting an environment variable or configuration value to enable/disable features at runtime. More sophisticated implementations support runtime reconfiguration and feature routing by criteria (IP address, access control lists). Teams deploy continuously to production behind toggles, then stage releases separately from deployments.

## Chapter 4. Automating Architectural Governance

**Example 4-1: JDepend test to verify the directionality of package imports**
```
public void testMatch() {
    DependencyConstraint constraint = new DependencyConstraint();

    JavaPackage persistence = constraint.addPackage("com.xyz.persistence");
    JavaPackage web = constraint.addPackage("com.xyz.web");
    JavaPackage util = constraint.addPackage("com.xyz.util");

    persistence.dependsUpon(util);
    web.dependsUpon(util);

    jdepend.analyze();

    assertEquals("Dependency mismatch",
             true, jdepend.dependencyMatch(constraint));
    }
```

**Example 4-2: Sample code for cyclomatic complexity evaluation**
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

**Example 4-3: Package dependency governance (ArchUnit)**
```
noClasses().that().resideInAPackage("..source..")
    .should().dependOnClassesThat().resideInAPackage("..foo..")
```

**Example 4-4: Allowing and restricting package access (ArchUnit)**
```
classes().that().resideInAPackage("..foo..")
    .should().onlyHaveDependentClassesThat()
        .resideInAnyPackage("..source.one..", "..foo..")
```

**Example 4-5: Class dependency rules in ArchUnit**
```
classes().that().haveNameMatching(".*Bar")
    .should().onlyHaveDependentClassesThat().haveSimpleName("Bar")
```

**Example 4-6: Inheritance governance rule expressed in ArchUnit**
```
classes().that().implement(Connection.class)
    .should().haveSimpleNameEndingWith("Connection")
```

**Example 4-7: Governance rules for annotations (ArchUnit)**
```
classes().that().areAssignableTo(EntityManager.class)
    .should().onlyHaveDependentClassesThat().areAnnotatedWith(Transactional.class)
```

**Example 4-8: Layered architecture governance checks (ArchUnit)**
```
layeredArchitecture()
    .consideringAllDependencies()
    .layer("Controller").definedBy("..controller..")
    .layer("Service").definedBy("..service..")
    .layer("Persistence").definedBy("..persistence..")

    .whereLayer("Controller").mayNotBeAccessedByAnyLayer()
    .whereLayer("Service").mayOnlyBeAccessedByLayers("Controller")
    .whereLayer("Persistence").mayOnlyBeAccessedByLayers("Service")
```

**Example 4-9: Sample microservices log format**
```
["OrderOrchestrator", "jdoe", "192.16.100.10", "ABC123",
  "2021-11-05T08:15:30-05:00", "3100ms", "updateOrderState()"]
```

**Example 4-10: Checking communication between services (Ruby)**
```
list_of_services.each { |service|
    service.import_logsFor(24.hours)
     calls_from(service).each { |call|
         unless call.destination.equals("orchestrator")
          raise FitnessFunctionFailure.new()
     }
   }
```

**Example 4-11: Scientist setup for an experiment (Ruby)**
```
require "scientist"

class MyWidget
  include Scientist

  def allows?(user)
    science "widget-permissions" do |e|
      e.use { model.check_user(user).valid? } # old way
      e.try { user.can?(:read, model) } # new way
    end # returns the control value
  end
end
```

**Example 4-12: Experimenting with a new merge algorithm (GitHub Scientist)**
```
def create_merge_commit(author, base, head, options = {})
  commit_message = options[:commit_message] || "Merge #{head} into #{base}"
  now = Time.current

  science "create_merge_commit" do |e|
    e.context :base => base.to_s, :head => head.to_s, :repo => repository.nwo
    e.use { create_merge_commit_git(author, now, base, head, commit_message) }
    e.try { create_merge_commit_rugged(author, now, base, head, commit_message) }
  end
end
```

**Example 4-13: Cucumber assumptions (BDD)**
```
Feature: Is it Friday yet?
  Everybody wants to know when it's Friday

  Scenario: Sunday isn't Friday
    Given today is Sunday
    When I ask whether it's Friday yet
    Then I should be told "Nope"
```

**Example 4-14: Cucumber methods that map to descriptions (Java)**
```
@Given("today is Sunday")
public void today_is_sunday() {
    // Write code here that turns the phrase above into concrete actions
    throw new io.cucumber.java.PendingException();
}
@When("I ask whether it's Friday yet")
public void i_ask_whether_it_s_friday_yet() {
    // Write code here that turns the phrase above into concrete actions
    throw new io.cucumber.java.PendingException();
}
@Then("I should be told {string}")
public void i_should_be_told(String string) {
    // Write code here that turns the phrase above into concrete actions
    throw new io.cucumber.java.PendingException();
}
```

**Neo4j Cypher query for governance (from Jupyter notebook case study)**
```
MATCH (e:Entity)<-[:CONTAINS]-(p:Package)
WHERE p.name <> "model"
RETURN e.fqn as MisplacedEntity, p.name as WrongPackage
```
(Query checks that all Entity classes reside in the "model" package; outputs those violating this rule.)

## Chapter 5. Evolutionary Architecture Topologies

Connascence of Meaning example: hardcoded values without constants (int TRUE = 1; int FALSE = 0) causing problems if values flip; improved through Connascence of Name by creating named constants.

Connascence of Position example: method updateSeat(String name, String seatLocation) called as updateSeat("14D", "Ford, N") where semantics are incorrect despite type matching.

Connascence of Execution example (dynamic):
```
email = new Email();
email.setRecipient("foo@example.com");
email.setSender("me@me.com");
email.send();
email.setSubject("whoops");
```
Fails because properties must be set in order.

Static JSON contract with schema information (Example 5-1):
```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "properties": {
      "acct": {"type": "number"},
      "cusip": {"type": "string"},
      "shares": {"type": "number", "minimum": 100}
   },
    "required": ["acct", "cusip", "shares"]
}
```

GraphQL contract example (Example 5-2) - Wishlist Profile:
```
type Profile {
    name: String
}
```

GraphQL contract example (Example 5-3) - Customer Profile:
```
type Profile {
    name: String
    addr1: String
    addr2: String
    country: String
    . . .
}
```

Loose JSON contract (Example 5-4):
```
{
  "name": "Mark",
  "status": "active",
  "joined": "2003"
}
```

Microservices case study: CatalogCheckout and ShipToCustomer services each maintain own Item representation rather than sharing to avoid coordinated change requirements. PenultimateWidgets service example illustrating sidecar pattern implementation. Hexagonal architecture pattern showing domain logic (center hexagon) with ports and adapters (alternative: Ports and Adapters pattern) surrounding it. Service mesh illustrated as interconnected sidecars enabling unified operational control. Data Mesh domain with Service Alpha containing operational data and adjacent Data Product Quantum for analytical data, with source-aligned, aggregate, and fit-for-purpose DPQ types.

## Chapter 6. Evolutionary Data

Example 6-1: CREATE TABLE customer (id BIGINT GENERATED BY DEFAULT AS IDENTITY (START WITH 1) PRIMARY KEY, firstname VARCHAR(60), lastname VARCHAR(60));

Example 6-2: ALTER TABLE customer ADD COLUMN dateofbirth DATETIME;

Example 6-3 (with undo): ALTER TABLE customer ADD COLUMN dateofbirth DATETIME; --//@UNDO ALTER TABLE customer DROP COLUMN dateofbirth;

Example 6-4 (no integration/no legacy): ALTER TABLE customer ADD firstname VARCHAR2(60); ALTER TABLE customer ADD lastname VARCHAR2(60); ALTER TABLE customer DROP COLUMN name;

Example 6-5 (legacy data, no integrators): ALTER TABLE Customer ADD firstname VARCHAR2(60); ALTER TABLE Customer ADD lastname VARCHAR2(60); UPDATE Customer set firstname = extractfirstname (name); UPDATE Customer set lastname = extractlastname (name); ALTER TABLE customer DROP COLUMN name;

Example 6-6 (complex: legacy data + integrators): ALTER TABLE Customer ADD firstname VARCHAR2(60); ALTER TABLE Customer ADD lastname VARCHAR2(60); UPDATE Customer set firstname = extractfirstname (name); UPDATE Customer set lastname = extractlastname (name); CREATE OR REPLACE TRIGGER SynchronizeName BEFORE INSERT OR UPDATE ON Customer REFERENCING OLD AS OLD NEW AS NEW FOR EACH ROW BEGIN IF :NEW.Name IS NULL THEN :NEW.Name := :NEW.firstname||' '||:NEW.lastname; END IF; IF :NEW.name IS NOT NULL THEN :NEW.firstname := extractfirstname(:NEW.name); :NEW.lastname := extractlastname(:NEW.name); END IF; END;

Contraction phase: ALTER TABLE Customer DROP COLUMN name; (or ALTER TABLE Customer SET UNUSED name; for large tables, followed by optional functional column: ALTER TABLE CUSTOMER ADD (name AS (generatename (firstname,lastname)));)

Figure 6-1: Three applications sharing a single relational database (Shared Database Integration anti-pattern).

Figure 6-2: Expand/Contract pattern showing starting state → transition state (both old/new present) → ending state.

Figures 6-3 through 6-6: PenultimateWidgets routing evolution—initial single route table → expand phase with old/new tables + trigger synchronization → contract phase with only new routing table.

Figure 6-7: Event-based referential integrity—Trader Blotter service publishes trade rejection on durable message queue; interested services consume and update/delete accordingly.

Figures 6-8 through 6-10: Data duplication strategies in microservices—(1) shared tables (coupling), (2) modeling shared data as service (interservice chatter), (3) in-process caching with appropriate update frequency (preferred: service owns data, others cache locally).

Figure 6-11: Migrate Method from Database—Widgets Administration service extracts stored procedure logic; new method acts as pass-through during expand phase, then replaces entirely in contract phase (database Strangler Fig).

Figure 6-12: Broader data context alternative—instead of extracting triggers/stored procedures into services, enlarge service granularity to preserve database code in situ.

Figure 6-13: PenultimateWidgets monolith-to-microservices migration—monolithic relational database (catalog, analytics, operational) splits into graph database (catalog categorization), specialized analytics database (business intelligence), and operational key/value stores (sales, transactions).

## Chapter 7. Building Evolvable Architectures

No explicit code examples or syntax-level code fragments appear in this chapter. However, the following concrete case studies and pattern descriptions in prosa exemplify the concepts: (1) PenultimateWidgets Star Rating Service Evolution (Figures 7-10, 7-11, 7-12): illustrates additive database schema changes and internal resolution routing to version service behavior. The service migrates from whole-star to half-star ratings by adding a column and proxy component, returning the caller's requested format without requiring callers to understand version numbers. (2) Shared Module Decomposition (LCOM—Lack of Cohesion in Methods): demonstrates how Chidamber & Kemerer metrics identify whether a class with low cohesion should be split (e.g., class B with three separate method groups lacks cohesion and could become three distinct classes; class A exhibits higher cohesion with fewer unused fields). (3) Ruby on Rails Car Auction BackgrounDRb Example: shows anticorruption layer evolution. The team deferred a message queue decision, placing BackgrounDRb (simple, relational database-backed) behind an API interface. After two years and three evolving asynchronous needs, they switched to Starling with minimal disruption because the interface isolated the implementation. (4) Monolith-to-Service Architecture Migration (Figures 7-1, 7-2, 7-3 through 7-8): illustrates share-everything monolith decomposition into service-based share-as-little-as-possible architecture, covering shared library migration via JAR extraction (Figure 7-7) versus duplication (Figure 7-8). (5) LMAX Transaction Processing Architecture: uses fitness-function-driven design to achieve six million transactions per second via single-threaded ring buffers and input/output disruptors. (6) Feature Routing in Service Versioning: the star rating service proxy routes requests to whole-star or half-star logic based on caller context, avoiding explicit version numbers in calling code. No language-specific implementation details (pseudocode or executable syntax) are present; the chapter emphasizes design principles and architectural patterns rather than implementation syntax.

## Chapter 8. Evolutionary Architecture Pitfalls and Antipatterns

No code examples appear in this range. Concrete architectural cases include: (1) PenultimateWidgets shared grid component bottleneck—resolution allowed teams to fork code or opt out entirely, decoupling the rigid coupling point. (2) Technology stack evolution: 2005 stacks were simple (OS → database → application framework); 2016+ stacks exploded with dozens of specialized components, increasing "primordial abstraction ooze" risk. (3) Vendor King ERP pattern illustrates how multimillion-dollar implementations fail under the "Let's Stop Working and Call It a Success" principle. (4) PenultimateWidgets "just enough" governance model: Ruby on Rails + MySQL (small projects, simple persistence); GoLang + Cassandra/MongoDB/MySQL (medium projects, flexible data stores); Java + Oracle (large projects, variable architectural concerns). (5) Cycle Time formula: velocity ∝ cycle time; example threshold: three-hour baseline with fitness function alerting if four hours exceeded. (6) Reporting architecture evolution: monolithic problem (single schema couples transactional and analytical); microservices solution (event streaming populates domain databases via eventual consistency; separate reporting services consume streams into denormalized databases).

## Chapter 9. Putting Evolutionary Architecture into Practice

Case Studies and Diagrams: The chapter provides four detailed PenultimateWidgets case studies on fitness functions:

1. UDP Communications Monitoring (Figures 9-6 and 9-7): Custom ETL monitoring tool losing messages. Fitness function calculated estimated message volume from PreProd/UAT, created Mock Service simulating that load, read processed messages from Monitor Service database, stored results in JSON, and analyzed with Pandas. Finding: 40% message loss at high scale.

2. Security Scanning (Figure 9-8): CI/CD pipeline stage scanning library dependencies against a real-time blocklist, failing builds and alerting the security team if affected libraries detected.

3. Concurrency Fitness Function (Figure 9-9): Using Strangler Fig pattern, new microservice crashed despite capacity tests showing 300 req/s capability. Fitness function: (1) Calculate incoming calls in production via New Relic to determine max requests and auto-scaling factor; (2) Query New Relic for calls/second; (3) Run load and concurrency tests with actual numbers; (4) Monitor memory/CPU to find stress point; (5) Insert into pipeline for continuous monitoring. Discovery: actual load was 1,200 req/s, not the estimated 120 req/s.

4. Fidelity Fitness Function (Figure 9-10): Running old and new system implementations side-by-side with thresholds, ensuring equivalence during gradual migration. Unexpected benefit: discovered undocumented data sources in legacy system.

Architectural Diagrams: Figures 9-1 through 9-14 illustrate layered architectures with technical silos, layered architectures with microservices (showing increased cross-layer messaging), team structure inversions, connection network growth (Equation 9-1: n(n-1)/2 connections for n people—14 people = 91 links, 50 people = 1,225 links), bounded contexts within layered architectures, and fitness function enforcement within layered designs.

Named Tools and Frameworks: Puppet (provisioning automation), Pandas (data analysis), New Relic (monitoring), snyk and Dependabot (supply chain governance), Netflix's Simian Army (continuous fitness functions), GitHub's Scientist framework (data-driven testing with side-by-side code comparison), Apache Struts (Java framework with CVE-2017-5638 zero-day), ArchUnit (mentioned implicitly for architectural constraint enforcement).

Domain Examples: Amazon's two-pizza teams and scaling problems, Facebook's photo-flagging A/B testing, mobile.de UI multivariate testing, Equifax data breach timeline (March 7 patch announced, March 15 scans found most affected systems, July 29 breach identified), PayPal/Mastercard/Visa payment scheme complexity as cognitive load example.
