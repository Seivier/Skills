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

This range contains the praise/endorsement section of the book, featuring testimonials from three prominent software architects (Nathaniel Schutta, Rebecca J. Parsons, and Cassie Shum). The quotes commend the authors for condensing complex architectural knowledge into a comprehensive guide suitable for architects at all career levels. This is front matter with no substantive technical content.

## Fundamentals of Software Architecture

This range contains the title page and copyright information for "Fundamentals of Software Architecture: An Engineering Approach" by Mark Richards and Neal Ford, published by O'Reilly Media in February 2020. It lists publication details, copyright notice, and production credits. No substantive architectural content is present in this section.

## Revision History for the First Edition

This range is the revision history, legal disclaimer, copyright notice, and publisher information section from the front matter of the book. It contains no substantive architectural content—only the first release date (2020-01-27), references to the O'Reilly errata page, trademark declarations, liability disclaimers, and ISBN details (978-1-492-04345-4).

## Preface: Invalidating Axioms

This preface establishes the central thesis that software architects must continuously invalidate and re-examine outdated axioms inherited from previous eras, as the software ecosystem exists in dynamic equilibrium with constantly shifting fundamentals. The authors argue that while mathematicians build theories on immutable axioms, software is "softer"—fundamental assumptions change rapidly due to innovations like containerization, Kubernetes, and cloud computing. Architects bear responsibility to question inherited beliefs in light of modern engineering practices, operational ecosystems, and new capabilities. Rather than relying on books written in fundamentally different times, architects must rethink axioms through the lens of today's landscape.

## Conventions Used in This Book

This section is front-matter documentation that explains the typographical and visual conventions used throughout the book. It provides reference information for readers on how to interpret different text styles and elements (italics, code formatting, tips) as they appear in the book. This is not substantive architectural content but rather a guide to the book's presentation style.

## Using Code Examples

This range is not substantive authorial content. It is O'Reilly's standard legal and administrative notice covering: where to download supplemental code examples (fundamentalsofsoftwarearchitecture.com), contact information for technical questions, and licensing terms governing use of code examples provided with the book. No architectural patterns, principles, or design concepts are discussed.

## O’Reilly Online Learning

This section is a promotional note about O'Reilly Media and its learning platform. It appears in the book's front matter and contains no substantive content about software architecture, design patterns, or engineering principles. It is purely descriptive material about O'Reilly's corporate offerings, services, and online learning resources, formatted as a note to readers about available training and educational materials.

## How to Contact Us

This section is O'Reilly Media's standard back-matter contact information for readers. It provides the publisher's mailing address, phone and fax numbers, along with web resources including the book's official page, website, and social media accounts. No architectural patterns, design principles, or technical content are discussed — this is purely publisher metadata and reader support information.

## Acknowledgments

The Acknowledgments section is a traditional book element in which the authors thank individuals and organizations who contributed to the development and publication of "Fundamentals of Software Architecture." The section includes collective thanks to conference attendees, the publishing team, and the broader technical community, followed by personalized acknowledgments from each co-author recognizing family members and mentors who supported the writing effort.

## Chapter 1. Introduction

Chapter 1 introduces software architecture as a discipline without a clear career path, rejecting simplistic definitions like "blueprint" or "roadmap." The authors propose a comprehensive definition combining four elements: system structure (the architectural style), architecture characteristics ("-ilities"), architecture decisions (rules for construction), and design principles (guidelines). The chapter establishes eight core expectations of architects—from making decisions and analyzing systems to possessing interpersonal skills and navigating politics—while emphasizing that software architecture is inherently dynamic and context-dependent. It explores how architecture intersects with engineering practices, operations/DevOps, development processes, and data management, culminating in two foundational laws: everything in architecture is a trade-off, and "why" matters more than "how."

## Part I. Foundations

This range constitutes a part divider and introductory page for Part I of the book. It is not substantive authorial content but rather a structural element that announces the topic and scope of the forthcoming chapters. The introduction states that to understand important architectural trade-offs, developers must grasp basic concepts and terminology concerning components, modularity, coupling, and connascence.

## Chapter 2. Architectural Thinking

Chapter 2 introduces architectural thinking as a distinct mindset requiring four core capabilities: understanding architecture versus design through bidirectional collaboration with developers; developing broad technical knowledge across many solutions rather than deep expertise in few; analyzing and reconciling trade-offs inherent in every architectural decision; and translating business drivers into measurable architectural characteristics. The central thesis is that effective architects see systems differently than developers and must recognize that every solution involves both benefits and trade-offs with no universally correct answers.

## Chapter 3. Modularity

Chapter 3 introduces modularity as a fundamental yet poorly understood organizing principle in software architecture. It defines modularity as the logical grouping of related code and establishes why this concept, though rarely an explicit requirement, is critical for maintainable and sustainable systems. The chapter presents a comprehensive framework for understanding and measuring modularity through three key lens: cohesion (how related parts within a module should be), coupling (incoming and outgoing connections), and connascence (the degree to which changes in one component require changes in another). Ford and Richards emphasize that architects must expend constant energy to preserve good modularity, preventing systems from drifting toward disorder, and they provide practical metrics and analysis tools—including LCOM, abstractness/instability measures, distance from main sequence, and connascence types—to help architects evaluate and improve modular structure. The chapter concludes by bridging modules to components as the next abstraction level.

## Chapter 4. Architecture Characteristics Defined

This chapter introduces architecture characteristics—critical nondomain design considerations that influence system structure and success. The authors reject terms like 'nonfunctional requirements' (self-denigrating) and 'quality attributes' (implying after-the-fact assessment), instead using 'architecture characteristics' to reflect their importance. A characteristic must meet three criteria: specify nondomain design considerations, influence structural aspects, and be critical to application success. The chapter categorizes characteristics into operational (performance, availability, scalability), structural (modularity, maintainability, extensibility), and cross-cutting (security, usability, legal) types. The central principle is trade-offs and least worst architecture: architects must make informed compromises when characteristics conflict, rather than maximizing all simultaneously.

## Chapter 5. Identifying Architectural Characteristics

Chapter 5 addresses the critical first step of architecture: identifying the architectural characteristics ("-ilities") that drive design decisions. Architects must extract these characteristics from three sources—domain concerns, explicit requirements, and implicit domain knowledge—while collaborating with stakeholders. The authors emphasize a core principle: keep the list of driving characteristics as short as possible to maintain design simplicity, avoiding the "Generic Architecture" anti-pattern of attempting to support all possible characteristics simultaneously. Through detailed analysis and practical case studies, they show how to distinguish explicit characteristics (stated in requirements) from implicit ones (inferred from domain context), and how to prioritize them for maximum value with minimal complexity.

## Chapter 6. Measuring and Governing Architecture Characteristics

This chapter addresses the critical challenge of how architects can concretely define, measure, and govern architecture characteristics across software projects. The authors argue that architecture characteristics are too often vaguely defined, leading to inconsistent interpretations across teams and organizations. The chapter establishes three primary measurement approaches—operational measures (performance, scalability), structural measures (complexity metrics), and process measures (testability, deployability)—and then introduces fitness functions as an automated governance mechanism. The authors advocate for objective, measurable definitions of architecture characteristics and positioning fitness functions not as new frameworks but as existing tools (metrics, testing, monitoring, chaos engineering) applied with a governance intent, drawing analogy to checklists in professions like aviation and medicine.

## Chapter 7. Scope of Architecture Characteristics

This chapter fundamentally challenges the traditional assumption that architecture characteristics apply uniformly at the system level, arguing instead for a more granular quantum-based scope. It introduces the concept of architecture quantum—an independently deployable artifact with high functional cohesion and synchronous connascence—as a means to address architecture characteristics within modern distributed systems like microservices. The authors demonstrate through the Going, Going, Gone auction case study how different architectural quanta within a single system may have distinctly different characteristic requirements, enabling architects to make more precise architectural decisions earlier in the design process.

## Chapter 8. Component-Based Thinking

Chapter 8 explores component-based thinking as the fundamental practice by which architects partition and structure software systems. Components are the physical manifestation of modules—containers for code organized by language-specific mechanisms—and their design represents one of the architect's most critical decisions. The chapter establishes that architecture partitioning can follow either technical partitioning (organizing by capabilities like presentation, business rules, persistence) or domain partitioning (organizing by business workflows and domains), each with distinct trade-offs. The authors argue that component identification is inherently iterative, requiring feedback cycles through initial identification, requirements mapping, role/responsibility analysis, architecture characteristic analysis, and restructuring. They present multiple component discovery techniques—the entity trap anti-pattern to avoid, the actor/actions approach, event storming from domain-driven design, and the workflow approach—and illustrate these with case studies showing how architectural decisions about granularity and partitioning shape the overall system structure and feasibility of future migration between monolithic and distributed architectures.

## Part II. Architecture Styles

This part introduction distinguishes between two foundational concepts: architecture styles, which define the overarching structure of how user interface and backend code are organized and interact with datastores; and architecture patterns, which are lower-level design structures that form specific solutions within a style. The authors assert that architects must deeply understand various styles and their inherent trade-offs to make effective decisions for business problems, as each architecture style embodies a well-known set of trade-offs.

## Chapter 9. Foundations

This chapter introduces architecture styles as named patterns encoding understood topology and characteristics, then explores fundamental patterns including the Big Ball of Mud anti-pattern, unitary architecture, and client/server variants (desktop, browser, and three-tier). The core argument distinguishes monolithic architectures (single deployment unit) from distributed architectures (multiple deployment units via remote protocols), revealing that while distributed systems offer superior performance and scalability, they impose eight foundational fallacies and critical trade-offs absent in monolithic designs. The authors establish that understanding these fallacies and distributed computing challenges is essential for sound architectural decision-making.

## Chapter 10. Layered Architecture Style

The layered (n-tiered) architecture is the most common and de facto standard architecture style, chosen for its simplicity, familiarity, and low cost. It organizes components into logical horizontal layers—typically presentation, business, persistence, and database—with each layer responsible for specific concerns and following a separation of concerns principle. The chapter explores topology variants, the critical concept of closed versus open layers for achieving isolation, important anti-patterns like the architecture sinkhole, and architectural characteristics ratings. While well-suited for small, simple applications and tight budgets, the style suffers from poor deployability, testability, scalability, and performance as applications grow.

## Chapter 11. Pipeline Architecture Style

This chapter introduces the pipeline architecture style (also called pipes and filters architecture), a foundational architectural pattern used across Unix shells, functional programming languages, and business applications. The architecture consists of pipes (unidirectional point-to-point communication channels) and filters (self-contained, stateless processing units) that work together to handle one-way data processing flows. The authors explain four filter types—producer, transformer, tester, and consumer—and present practical applications in ETL tools, EDI systems, and streaming data platforms. While highlighting the architecture's strengths in simplicity, cost, and modularity, the chapter concludes with significant limitations: monolithic deployment prevents scalability and elasticity, fault tolerance is unsupported, and availability suffers from high mean time to recovery.

## Chapter 12. Microkernel Architecture Style

This chapter presents the microkernel architecture style (also called plug-in architecture), a monolithic pattern consisting of a core system providing minimal required functionality and standalone plug-in components that extend and customize behavior. Widely used in product-based software (IDE plugins, web browsers) and increasingly in complex business applications (insurance claims, tax preparation), it provides strong extensibility and adaptability through component isolation. The authors position it as a simple, cost-effective architecture that trades off scalability and fault tolerance for maintainability and feature modularity.

## Chapter 13. Service-Based Architecture Style

Service-based architecture is a pragmatic hybrid of microservices that balances distributed design with operational simplicity. It uses coarse-grained domain services (typically 4-12) sharing a monolithic database, avoiding the complexity and cost of finer-grained architectures. The authors present this as one of the most flexible and cost-effective distributed architecture styles, particularly suited for domain-driven design when organizations need to move beyond monoliths but don't require the extreme scalability of microservices. The central trade-off is accepting modest scalability ratings in exchange for superior data integrity via ACID transactions, simpler orchestration patterns, and lower infrastructure costs.

## Chapter 14. Event-Driven Architecture Style

Event-driven architecture is a distributed asynchronous style for building highly scalable, responsive systems. It contrasts the traditional request-based model (deterministic, synchronous) with event-based models that react to situations asynchronously. The chapter explains two primary topologies: broker topology, which is highly decoupled with fire-and-forget message processing but lacks workflow control, and mediator topology, which manages event workflows but introduces coupling. Key concerns include asynchronous communication benefits, error handling complexity, data loss prevention, and fundamental trade-offs between responsiveness/scalability and control/certainty.

## Chapter 15. Space-Based Architecture Style

Space-based architecture directly addresses the database bottleneck that emerges when traditional web-based applications scale. Named after the tuple space concept (multiple parallel processors sharing memory), this style removes the database as a synchronous constraint by maintaining replicated in-memory data grids across processing units, using asynchronous messaging-based data pumps for eventual database consistency, and dynamically scaling processing units based on load. The authors position it as the primary architectural solution for extreme-scale applications (10,000+ concurrent users) requiring high elasticity and performance, while explicitly highlighting significant trade-offs: increased complexity, difficult testability, high cost, and reliance on eventual consistency rather than immediate transactional guarantees.

## Chapter 16. Orchestration-Driven Service-Oriented Architecture

Orchestration-Driven Service-Oriented Architecture emerged in the late 1990s when enterprises faced expensive OS and database licensing, driving a philosophy of aggressive service reuse. The architecture layers services into Business Services (domain-level entry points), Enterprise Services (fine-grained reusable implementations), Application Services (one-offs), Infrastructure Services (operational concerns), and an Orchestration Engine coordinating them via a centralized service bus. Though logically motivated, the authors argue this became a cautionary tale: the pursuit of reuse created severe coupling, spread domain concepts too thinly across technical boundaries, and made the orchestration engine a political and technical bottleneck, ultimately hindering rather than enabling rapid change.

## Chapter 17. Microservices Architecture

Microservices is a distributed architecture style that advocates extreme decoupling through physical embodiment of domain-driven design's bounded context concept. Named and popularized in 2014 by Martin Fowler and James Lewis, the style emphasizes single-purpose services operating independently with isolated data stores, favoring duplication over coupling. The chapter addresses the central challenge of finding appropriate service granularity, discusses data isolation strategies, covers communication patterns including choreography and orchestration, and examines transactional coordination via the saga pattern. Microservices excels in scalability, elasticity, and evolutionary support but suffers in performance and reliability when inter-service communication is excessive.

## Chapter 18. Choosing the Appropriate Architecture Style

Chapter 18 addresses the fundamental challenge of selecting an appropriate architecture style from the numerous available options. The authors emphasize that architecture style selection is inherently contextual—dependent on organizational factors, domain characteristics, strategic goals, and architecture requirements—and therefore has no universal "correct" answer. The chapter explores why architectural fashions shift over time, establishes decision criteria architects must consider, and demonstrates practical decision-making through two contrasting case studies: a monolithic system with modular and microkernel variations, and a distributed microservices system with multiple operational quanta.

## Part III. Techniques and Soft Skills

This range contains the part divider and introduction for Part III of the book, which shifts focus from technical architecture patterns to the human and interpersonal dimensions of the role. The authors establish that software architects must master not only technical knowledge but also soft skills—including how to think architecturally, guide teams, and communicate effectively with diverse stakeholders. This section signals the transition from architectural techniques to the practical, people-facing competencies required for success.

## Chapter 19. Architecture Decisions

Chapter 19 addresses the core responsibility of software architects: making effective architecture decisions. The authors explain that good architecture decisions require gathering relevant information, justifying choices, documenting decisions, and communicating them to stakeholders. The chapter outlines three major anti-patterns that emerge during decision-making (Covering Your Assets, Groundhog Day, and Email-Driven Architecture), defines what makes decisions architecturally significant using Michael Nygard's framework, and presents Architecture Decision Records (ADRs) as the primary method for documenting and managing decisions. The authors take the stance that decisions must be justified with both technical and business rationale, properly documented, and effectively communicated.

## Chapter 20. Analyzing Architecture Risk

Chapter 20 introduces systematic techniques for identifying, qualifying, and mitigating architecture risk. The central pattern is the risk matrix, which uses two dimensions (impact and likelihood, each rated 1–3) and multiplies them to produce objective risk scores (1–2: low, 3–4: medium, 6–9: high). The chapter advocates for risk storming—a collaborative, three-phase practice (identification, consensus, mitigation) involving architects, developers, and stakeholders—as the primary method to surface risks that individual architects would miss. The authors' stance is that continuous risk analysis is essential throughout a system's lifecycle, not a one-time activity.

## Chapter 21. Diagramming and Presenting Architecture

This chapter addresses the critical soft skills architects need for success: effective diagramming and presentation. While architects' technical brilliance matters little if they cannot communicate ideas to managers and developers, the chapter establishes that these skills are learnable through deliberate practice. The authors advocate for representational consistency—always showing how architectural parts relate to the whole when changing views—as a foundational principle for both diagrams and presentations. Diagramming requires mastering tools and standards, while presenting demands understanding how to control time and information flow using visual and verbal channels strategically.

## Chapter 22. Making Teams Effective

This chapter addresses how software architects can guide development teams through effective architecture implementation. It introduces the concept that architects must establish appropriate boundaries or constraints for teams—neither too tight nor too loose—and identifies three personality types that architects typically embody: control freak (overly restrictive), armchair (disconnected and permissive), and effective (balanced). The authors present Elastic Leadership as a framework for dynamically determining how much control to exert based on five key factors: team familiarity, team size, overall experience level, project complexity, and project duration. The chapter concludes that effective architects differentiate themselves not just through technical guidance but through close collaboration with teams, using techniques like checklists, observation for warning signs (process loss, pluralistic ignorance, diffusion of responsibility), and communicating design principles clearly.

## Chapter 23. Negotiation and Leadership Skills

Chapter 23 examines the critical soft skills that software architects must develop to lead effectively: negotiation, communication, and people management. Through concrete scenarios and techniques, the authors argue that roughly 50% of being an effective architect involves these interpersonal skills, not just technical expertise. The chapter presents actionable methods for negotiating with business stakeholders, peer architects, and development teams, alongside leadership principles such as the 4 C's of Architecture (communication, collaboration, clarity, conciseness), balancing pragmatism with vision, and leading by example rather than by title.

## Chapter 24. Developing a Career Path

Chapter 24 addresses the challenge of managing a software architect's career path after achieving architect status, arguing that continuous learning is essential given the rapid pace of technological change. The authors present practical, implementable techniques for maintaining technical breadth: the 20-Minute Rule (dedicating at least 20 minutes daily to learning), creating a personal technology radar based on the ThoughtWorks model, strategically using social media to discover emerging technologies and innovations, and practicing architecture through katas. The central principle is treating a technology portfolio like a financial portfolio—with deliberate diversification, ongoing assessment, and regular rebalancing to avoid being blindsided by technological shifts.

## Index

This is the Index section of the book—a comprehensive alphabetical reference tool, not a narrative chapter with architectural content. It lists major terms, concepts, patterns, anti-patterns, methodologies, and case studies from throughout the book, with hyperlinks pointing readers to the specific chapters where each topic is discussed in detail. The index is organized alphabetically by entry name and serves as a lookup mechanism for readers seeking information on particular architectural subjects.

## About the Authors

The About the Authors section provides brief professional biographies of the two authors of this architecture textbook. Mark Richards is presented as a hands-on software architect with expertise in microservices and distributed architectures, and founder of DeveloperToArchitect.com. Neal Ford is identified as director and software architect at ThoughtWorks, a global software development consultancy, bringing prior experience as CTO of a training and development firm. Together, their combined experience in architecture practice and thought leadership informs the book's perspective.

## Colophon

This range contains the book's colophon, a publisher's note describing production and design choices rather than architectural content. It identifies the red-fan parrot (Deroptyus accipitrinus) as the cover animal and provides biographical and ecological details about the species. The section concludes with credits for the cover illustration and typography choices, reflecting O'Reilly's standard practice of featuring endangered or significant wildlife on technical book covers.
