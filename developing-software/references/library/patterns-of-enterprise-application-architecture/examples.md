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

No code examples or concrete pattern demonstrations appear in this preface range. The section is entirely expository and editorial in nature, containing only prose explanation and attributions.

## Introduction

This range contains no code examples or concrete case study implementations. Fowler discusses the structure of pattern examples extensively (lines 1837–1878), explaining that examples appear in Java or C# in the actual pattern descriptions later in the book, but the Introduction itself presents no executable code, pseudo-code, or working sample implementations. He explicitly states that code examples are not downloadable because they are surrounded with simplification scaffolding unsuitable for production use. The closest to exemplification are the three enterprise application scenarios (B2C retailer, leasing system, expense tracking) which are described in prose rather than code, and the Swordfish/Camel performance comparison (lines 1664–1673), which presents numerical data (throughput in tps, servers, scaling rates) rather than implementation code.

## Chapter 1. Layering

No code examples are present in this section of the chapter. The author illustrates concepts through prose descriptions and architectural narratives rather than code snippets. The highlighted product example demonstrates separation of concerns: domain logic determines whether a product's sales improved more than 10% (returns Boolean), while presentation logic calls this Boolean method and applies red highlighting if true—separating the business decision from the presentation decision. The chapter references architectural patterns by name (Transaction Script, Domain Model, Remote Facades, Data Transfer Objects) and discusses Alistair Cockburn's Hexagonal Architecture pattern conceptually without code illustrations.

## Chapter 2. Organizing Domain Logic

The chapter uses revenue recognition calculation as the recurring example problem to illustrate pattern differences. Different product types have different algorithms for recognizing revenue on a given contract; the calculation must determine the product type, apply the correct algorithm, and create revenue recognition objects to capture results.

In the Transaction Script approach (Figure 2.1), the script method does all work. Underlying objects are only Table Data Gateways, passing data to the transaction script. The sequence flows directly: the script controls the entire logic sequence.

In the Domain Model approach (Figure 2.2), multiple objects forward behavior to each other until a strategy object creates the results. For example, a contract object might delegate to product objects, which delegate to strategy objects, which perform the final calculation. This distributes responsibility across classes aligned with domain concepts.

In the Table Module approach (Figure 2.3), a single contract module object receives a Record Set from a database query. The client creates the module instance and passes it the Record Set. The module then operates on the set, with the client passing specific IDs for individual record operations.

The chapter references several supporting patterns: Row Data Gateway and Table Data Gateway for data access with Transaction Script; Data Mapper for complex Domain Model mapping to relational databases; Record Set as the data structure for Table Module and GUI integration; Active Record for simple Domain Model persistence; and strategy pattern objects for encapsulating different algorithms (like different revenue recognition strategies).

Figure 2.4 illustrates the complexity-effort relationship graphically, showing Transaction Script and Table Module staying relatively flat in effort as complexity grows until hitting a wall, while Domain Model has higher initial costs but scales better with increasing complexity.

## Chapter 3. Mapping to Relational Databases

No code examples appear in this specific range (lines 2800-4007). The chapter describes five conceptual diagrams referenced as Figure 3.1 through Figure 3.10 (Row Data Gateway structure, Table Data Gateway structure, Active Record with customer domain objects, Data Mapper insulating objects and database, Foreign Key Mapping for single-valued fields, Foreign Key Mapping for collections, Association Table Mapping for many-to-many, Single Table Inheritance, Concrete Table Inheritance, and Class Table Inheritance), but the diagrams themselves are referenced only as images without embedded code or pseudocode listings. The metadata example appears as: <field name="customer" targetClass="Customer" dbColumn="custID" targetTable="customers" lowerBound="1" upperBound="1" setter="loadCustomer"/> demonstrating metadata structure. Finder method signatures are referenced generically as `find(id)` and `findForCustomer(customer)` but without complete implementation code.

## Chapter 4. Web Presentation

This range contains no complete code fragments, no case study code, or detailed diagram specifications that could be extracted verbatim. The text references several diagram figures (Figure 4.1 showing the MVC broad-brush architecture with request/controller/model/view/response flow; Figure 4.2 showing single-stage view structure; Figure 4.3 showing two-stage view structure) but these are image references only. Technologies mentioned include CGI scripts, Java servlets (with keyword interfaces for request parsing), Perl regular expression searching, XSLT stylesheets applied to XML, and server page technologies (ASP, JSP, PHP), but no actual code syntax is provided in lines 4008-4323.

## Chapter 5. Concurrency

No code examples appear in this chapter range. The chapter is exclusively conceptual and architectural. Fowler and Rice illustrate concurrency problems and solutions through running examples of Martin and David editing shared files and code, and an example of Martin counting classes across packages while David adds new classes—but these are narrative scenarios, not code specimens. The section "Table 5.1. Isolation Levels and the Inconsistent Read Errors They Allow" references a table (![Image](patterns-of-enterprise-application-architecture/media/graphics/05tab01.jpg)) comparing read errors across SQL isolation levels, but the table image itself is not included in the text range. No patterns are shown with class definitions, interface contracts, or implementation code.

## Chapter 6. Session State

No code examples or formal pattern diagrams appear in this range. The chapter uses narrative case studies and architectural scenarios: (1) A Web server returning book information by ISBN as a stateless example; (2) A shopping cart system as the canonical inherently-stateful business process; (3) An insurance policy editing scenario where a customer's zip code change creates inconsistent reads; (4) A flight itinerary booking scenario illustrating session isolation requirements; (5) A leasing system with large amounts of data moving between application and database, contrasted against public retail systems with many idle users; (6) An AOL proxy scenario where client IP-based server affinity concentrates traffic on a single server. These are narrative explanations of design trade-offs rather than code implementations or formal diagrams.

## Chapter 7. Distribution Strategies

Figure 7.1 depicts the problematic distribution pattern: a single application with separate remote objects for customers, orders, products, and deliveries placed on different processing nodes—the design that "sucks like an inverted hurricane." Each component is isolated for independent scaling but incurs excessive remote calls.

Figure 7.2 illustrates the recommended clustering approach: multiple copies of the same complete application (containing all classes) run on different nodes. Rather than distributing individual classes, the entire application is replicated.

The address class example demonstrates interface granularity: a local fine-grained interface provides separate methods—getCity(), getState(), setCity(), setState()—for flexible composition. A remote coarse-grained interface instead provides getAddressDetails() and updateAddressDetails(), bundling multiple pieces of information in single calls to minimize remote overhead.

The Remote Facade pattern is exemplified by a coarse-grained facade object that exists solely to delegate to internal fine-grained objects, making distribution costs explicit: developers calling the facade know they're incurring remote overhead, while code calling fine-grained objects internally remains unaware and unimpacted by distribution concerns.

Data Transfer Objects transfer address information as a single bundled object rather than as a domain object graph, containing only the data needed and references only to other transfer objects and primitive types (strings, etc.), preventing navigation across distribution boundaries.

## Chapter 8. Putting It All Together

The chapter contains no complete code fragments or detailed code examples. Rather, it presents comparative architectural decision trees based on domain complexity and tool availability, and references comparison tables showing different layering schemes (Brown, CoreJ2EE, Microsoft DNA, Marinescu, Nilsson). Specific pattern examples are referenced via cross-references to chapters where detailed patterns are described elsewhere in the book.

## Chapter 9. Domain Logic Patterns

Transaction Script Revenue Recognition example (Java): Database schema with three tables (products, contracts, revenueRecognitions). Gateway class using Table Data Gateway pattern wraps SQL queries: findRecognitionsFor(long contractID, MfDate asof) executes "SELECT amount FROM revenueRecognitions WHERE contract = ? AND recognizedOn <= ?". RecognitionService implements two transaction scripts: recognizedRevenue(long contractNumber, MfDate asOf) sums recognized amounts from ResultSet by iterating rows and adding Money objects. calculateRevenueRecognitions(long contractNumber) reads contract, calculates total revenue and recognition date, then splits revenue three ways for spreadsheets (allocation at 0, 60, 90 days) or databases (allocation at 0, 30, 60 days) using Money.allocate(3) to prevent penny loss, inserting each recognition via db.insertRecognition().

Domain Model Revenue Recognition example (Java): RevenueRecognition class holds amount and date, with isRecognizableBy(MfDate asOf) returning true if asOf is after or equal to date. Contract maintains List revenueRecognitions and implements recognizedRevenue(MfDate asOf) by iterating recognitions calling isRecognizableBy() to accumulate matching amounts. Product associates with RecognitionStrategy interface, using factory methods newWordProcessor(), newSpreadsheet(), newDatabase() to create instances with appropriate strategy: CompleteRecognitionStrategy for word processors (creates single recognition), ThreeWayRecognitionStrategy for spreadsheets (with offsets 60, 90) and databases (with offsets 30, 60). ThreeWayRecognitionStrategy holds firstRecognitionOffset and secondRecognitionOffset, overriding calculateRevenueRecognitions() to allocate revenue and add three RevenueRecognition objects at calculated dates. Contract.calculateRecognitions() delegates to product.calculateRevenueRecognitions(this), then product delegates to strategy, eliminating conditionals through object structure wiring.

Table Module Revenue Recognition example (C#): TableModule base class holds protected DataTable table initialized in constructor from DataSet via ds.Tables[tableName]. Contract and RevenueRecognition subclasses call base constructor with appropriate table names. C# indexer provides access: this[long key] filters table by "ID = key" and returns first DataRow. Contract.CalculateRecognitions(long contractID) retrieves contractRow via this[contractID], extracts amount and product ID, creates Product and RevenueRecognition Table Modules with same DataSet, checks product type via GetProductType(prodID) returning enum (WP, SS, DB), then allocates revenue and calls rr.Insert() for each recognition at calculated dates. Product.GetProductType() returns (ProductType)Enum.Parse(typeof(ProductType), typeCode). RevenueRecognition.Insert(long contractID, Decimal amount, DateTime date) creates new DataRow, sets values (ID, contractID, amount, date), adds to table.Rows, returns generated ID. RevenueRecognition.RecognizedRevenue(long contractID, DateTime asOf) filters table with "ContractID = {0} AND date <= {1:d}" and Select() to get matching DataRows, summing amounts. Alternative RecognizedRevenue2() uses table.Compute("sum(amount)", filter) with aggregate function.

Service Layer Revenue Recognition example (Java): ApplicationService base class provides getEmailGateway() and getIntegrationGateway() methods. EmailGateway interface: void sendEmailMessage(String toAddress, String subject, String body). IntegrationGateway interface: void publishRevenueRecognitionCalculation(Contract contract). RecognitionService extends ApplicationService, implements calculateRevenueRecognitions(long contractNumber) reading contract via Contract.readForUpdate(contractNumber), calling contract.calculateRecognitions(), then sending email via getEmailGateway().sendEmailMessage(contract.getAdministratorEmailAddress(), "RE: Contract #" + contractNumber, contract + " has had revenue recognitions calculated.") and publishing via getIntegrationGateway().publishRevenueRecognitionCalculation(contract). Second operation recognizedRevenue(long contractNumber, Date asOf) returns Contract.read(contractNumber).recognizedRevenue(asOf). EJB 2.0 variant uses RecognitionServiceBeanImpl with business interface methods declared transactional, achieving distributed transaction control via container while maintaining same operation script logic. Layer Supertype provides default EJB bean implementation methods plus gateway access, with EmailGateway and IntegrationGateway as business interfaces for stateless session beans enabling atomic coordination of contract persistence, message enqueueing, and email sending.

## Chapter 10. Data Source Architectural Patterns

Table Data Gateway C# example with PersonGateway:
class PersonGateway...
   public IDataReader FindAll() {
      String sql = "select * from person";
      return new OleDbCommand(sql, DB.Connection).ExecuteReader();
   }
   public IDataReader FindWithLastName(String lastName) {
      String sql = "SELECT * FROM person WHERE lastname = ?";
      IDbCommand comm = new OleDbCommand(sql, DB.Connection);
      comm.Parameters.Add(new OleDbParameter("lastname", lastName));
      return comm.ExecuteReader();
   }
   public Object[] FindRow (long key) {
      String sql = "SELECT * FROM person WHERE id = ?";
      IDbCommand comm = new OleDbCommand(sql, DB.Connection);
      comm.Parameters.Add(new OleDbParameter("key",key));
      IDataReader reader = comm.ExecuteReader();
      reader.Read();
      Object [] result = new Object[reader.FieldCount];
      reader.GetValues(result);
      reader.Close();
      return result;
   }
   public void Update (long key, String lastname, String firstname, long numberOfDependents){
      String sql = @"
         UPDATE person
            SET lastname = ?, firstname = ?, numberOfDependents = ?
            WHERE id = ?";
      IDbCommand comm = new OleDbCommand(sql, DB.Connection);
      comm.Parameters.Add(new OleDbParameter ("last", lastname));
      comm.Parameters.Add(new OleDbParameter ("first", firstname));
      comm.Parameters.Add(new OleDbParameter ("numDep", numberOfDependents));
      comm.Parameters.Add(new OleDbParameter ("key", key));
      comm.ExecuteNonQuery();
   }
   public long Insert(String lastName, String firstName, long numberOfDependents) {
      String sql = "INSERT INTO person VALUES (?,?,?,?)";
      long key = GetNextID();
      IDbCommand comm = new OleDbCommand(sql, DB.Connection);
      comm.Parameters.Add(new OleDbParameter ("key", key));
      comm.Parameters.Add(new OleDbParameter ("last", lastName));
      comm.Parameters.Add(new OleDbParameter ("first", firstName));
      comm.Parameters.Add(new OleDbParameter ("numDep", numberOfDependents));
      comm.ExecuteNonQuery();
      return key;
   }
   public void Delete (long key) {
      String sql = "DELETE FROM person WHERE id = ?";
      IDbCommand comm = new OleDbCommand(sql, DB.Connection);
      comm.Parameters.Add(new OleDbParameter ("key", key));
      comm.ExecuteNonQuery();
   }

Table Data Gateway using ADO.NET Data Sets:
class DataSetHolder...
   public DataSet Data = new DataSet();
   private Hashtable DataAdapters = new Hashtable();

class DataGateway...
   public DataSetHolder Holder;
   public DataSet Data {
      get {return Holder.Data;}
   }
   protected DataGateway() {
      Holder = new DataSetHolder();
   }
   protected DataGateway(DataSetHolder holder) {
      this.Holder = holder;
   }
   public void LoadAll() {
      String commandString = String.Format("select * from {0}", TableName);
      Holder.FillData(commandString, TableName);
   }
   public void LoadWhere(String whereClause) {
      String commandString = String.Format("select * from {0} where {1}", TableName, whereClause);
      Holder.FillData(commandString, TableName);
   }
   abstract public String TableName {get;}

class DataSetHolder...
   public void FillData(String query, String tableName) {
      if (DataAdapters.Contains(tableName)) throw new MutlipleLoadException();
      OleDbDataAdapter da = new OleDbDataAdapter(query, DB.Connection);
      OleDbCommandBuilder builder = new OleDbCommandBuilder(da);
      da.Fill(Data, tableName);
      DataAdapters.Add(tableName, da);
   }
   public void Update() {
      foreach (String table in DataAdapters.Keys)
         ((OleDbDataAdapter)DataAdapters[table]).Update(Data, table);
   }
   public DataTable this[String tableName] {
      get {return Data.Tables[tableName];}
   }

Row Data Gateway Java example:
create table people (ID int primary key, lastname varchar, firstname varchar, number_of_dependents int)

class PersonGateway...
   private String lastName;
   private String firstName;
   private int numberOfDependents;
   public String getLastName() {
      return lastName;
   }
   public void setLastName(String lastName) {
      this.lastName = lastName;
   }
   public String getFirstName() {
      return firstName;
   }
   public void setFirstName(String firstName) {
      this.firstName = firstName;
   }
   public int getNumberOfDependents() {
      return numberOfDependents;
   }
   public void setNumberOfDependents(int numberOfDependents) {
      this.numberOfDependents = numberOfDependents;
   }
   private static final String updateStatementString = "UPDATE people set lastname = ?, firstname = ?, number_of_dependents = ? where id = ?";
   public void update() {
      PreparedStatement updateStatement = null;
      try {
         updateStatement = DB.prepare(updateStatementString);
         updateStatement.setString(1, lastName);
         updateStatement.setString(2, firstName);
         updateStatement.setInt(3, numberOfDependents);
         updateStatement.setInt(4, getID().intValue());
         updateStatement.execute();
      } catch (Exception e) {
         throw new ApplicationException(e);
      } finally {DB.cleanUp(updateStatement);}
   }

class PersonFinder...
   private final static String findStatementString = "SELECT id, lastname, firstname, number_of_dependents from people WHERE id = ?";
   public PersonGateway find(Long id) {
      PersonGateway result = (PersonGateway) Registry.getPerson(id);
      if (result != null) return result;
      PreparedStatement findStatement = null;
      ResultSet rs = null;
      try {
         findStatement = DB.prepare(findStatementString);
         findStatement.setLong(1, id.longValue());
         rs = findStatement.executeQuery();
         rs.next();
         result = PersonGateway.load(rs);
         return result;
      } catch (SQLException e) {
         throw new ApplicationException(e);
      } finally {DB.cleanUp(findStatement, rs);}
   }
   public List findResponsibles() {
      List result = new ArrayList();
      PreparedStatement stmt = null;
      ResultSet rs = null;
      try {
         stmt = DB.prepare("SELECT id, lastname, firstname, number_of_dependents from people WHERE number_of_dependents > 0");
         rs = stmt.executeQuery();
         while (rs.next()) {
            result.add(PersonGateway.load(rs));
         }
         return result;
      } catch (SQLException e) {
         throw new ApplicationException(e);
      } finally {DB.cleanUp(stmt, rs);}
   }

Active Record Java example:
class Person...
   private String lastName;
   private String firstName;
   private int numberOfDependents;
   private final static String findStatementString = "SELECT id, lastname, firstname, number_of_dependents FROM people WHERE id = ?";
   public static Person find(Long id) {
      Person result = (Person) Registry.getPerson(id);
      if (result != null) return result;
      PreparedStatement findStatement = null;
      ResultSet rs = null;
      try {
         findStatement = DB.prepare(findStatementString);
         findStatement.setLong(1, id.longValue());
         rs = findStatement.executeQuery();
         rs.next();
         result = load(rs);
         return result;
      } catch (SQLException e) {
         throw new ApplicationException(e);
      } finally {
         DB.cleanUp(findStatement, rs);
      }
   }
   public static Person load(ResultSet rs) throws SQLException {
      Long id = new Long(rs.getLong(1));
      Person result = (Person) Registry.getPerson(id);
      if (result != null) return result;
      String lastNameArg = rs.getString(2);
      String firstNameArg = rs.getString(3);
      int numDependentsArg = rs.getInt(4);
      result = new Person(id, lastNameArg, firstNameArg, numDependentsArg);
      Registry.addPerson(result);
      return result;
   }
   private final static String updateStatementString = "UPDATE people set lastname = ?, firstname = ?, number_of_dependents = ? where id = ?";
   public void update() {
      PreparedStatement updateStatement = null;
      try {
         updateStatement = DB.prepare(updateStatementString);
         updateStatement.setString(1, lastName);
         updateStatement.setString(2, firstName);
         updateStatement.setInt(3, numberOfDependents);
         updateStatement.setInt(4, getID().intValue());
         updateStatement.execute();
      } catch (Exception e) {
         throw new ApplicationException(e);
      } finally {
         DB.cleanUp(updateStatement);
      }
   }
   public Money getExemption() {
      Money baseExemption = Money.dollars(1500);
      Money dependentExemption = Money.dollars(750);
      return baseExemption.add(dependentExemption.multiply(this.getNumberOfDependents()));
   }

Data Mapper Java example - basic structure:
class Person...
   private String lastName;
   private String firstName;
   private int numberOfDependents;

class PersonMapper...
   protected String findStatement() {
      return "SELECT id, lastname, firstname, number_of_dependents FROM people WHERE id = ?";
   }
   public static final String COLUMNS = " id, lastname, firstname, number_of_dependents ";
   public Person find(Long id) {
      return (Person) abstractFind(id);
   }

class AbstractMapper...
   protected Map loadedMap = new HashMap();
   abstract protected String findStatement();
   protected DomainObject abstractFind(Long id) {
      DomainObject result = (DomainObject) loadedMap.get(id);
      if (result != null) return result;
      PreparedStatement findStatement = null;
      try {
         findStatement = DB.prepare(findStatement());
         findStatement.setLong(1, id.longValue());
         ResultSet rs = findStatement.executeQuery();
         rs.next();
         result = load(rs);
         return result;
      } catch (SQLException e) {
         throw new ApplicationException(e);
      } finally {
         DB.cleanUp(findStatement);
      }
   }
   protected DomainObject load(ResultSet rs) throws SQLException {
      Long id = new Long(rs.getLong(1));
      if (loadedMap.containsKey(id)) return (DomainObject) loadedMap.get(id);
      DomainObject result = doLoad(id, rs);
      loadedMap.put(id, result);
      return result;
   }

class PersonMapper...
   protected DomainObject doLoad(Long id, ResultSet rs) throws SQLException {
      String lastNameArg = rs.getString(2);
      String firstNameArg = rs.getString(3);
      int numDependentsArg = rs.getInt(4);
      return new Person(id, lastNameArg, firstNameArg, numDependentsArg);
   }

Data Mapper with parameterized finder interface:
interface StatementSource...
   String sql();
   Object[] parameters();

class AbstractMapper...
   public List findMany(StatementSource source) {
      PreparedStatement stmt = null;
      ResultSet rs = null;
      try {
         stmt = DB.prepare(source.sql());
         for (int i = 0; i < source.parameters().length; i++)
            stmt.setObject(i+1, source.parameters()[i]);
         rs = stmt.executeQuery();
         return loadAll(rs);
      } catch (SQLException e) {
         throw new ApplicationException(e);
      } finally {
         DB.cleanUp(stmt, rs);
      }
   }

class PersonMapper...
   public List findByLastName2(String pattern) {
      return findMany(new FindByLastName(pattern));
   }
   static class FindByLastName implements StatementSource {
      private String lastName;
      public FindByLastName(String lastName) {
         this.lastName = lastName;
      }
      public String sql() {
         return "SELECT " + COLUMNS + " FROM people " + " WHERE UPPER(lastname) like UPPER(?) " + " ORDER BY lastname";
      }
      public Object[] parameters() {
         Object[] result = {lastName};
         return result;
      }
   }

Data Mapper update and insert methods:
class AbstractMapper...
   public Long insert(DomainObject subject) {
      PreparedStatement insertStatement = null;
      try {
         insertStatement = DB.prepare(insertStatement());
         subject.setID(findNextDatabaseId());
         insertStatement.setInt(1, subject.getID().intValue());
         doInsert(subject, insertStatement);
         insertStatement.execute();
         loadedMap.put(subject.getID(), subject);
         return subject.getID();
      } catch (SQLException e) {
         throw new ApplicationException(e);
      } finally {
         DB.cleanUp(insertStatement);
      }
   }

class PersonMapper...
   private static final String updateStatementString = "UPDATE people SET lastname = ?, firstname = ?, number_of_dependents = ? WHERE id = ?";
   public void update(Person subject) {
      PreparedStatement updateStatement = null;
      try {
         updateStatement = DB.prepare(updateStatementString);
         updateStatement.setString(1, subject.getLastName());
         updateStatement.setString(2, subject.getFirstName());
         updateStatement.setInt(3, subject.getNumberOfDependents());
         updateStatement.setInt(4, subject.getID().intValue());
         updateStatement.execute();
      } catch (Exception e) {
         throw new ApplicationException(e);
      } finally {
         DB.cleanUp(updateStatement);
      }
   }
   protected String insertStatement() {
      return "INSERT INTO people VALUES (?, ?, ?, ?)";
   }

Empty object construction approach:
class AbstractMapper...
   protected DomainObjectEL load(ResultSet rs) throws SQLException {
      Long id = new Long(rs.getLong(1));
      if (loadedMap.containsKey(id)) return (DomainObjectEL) loadedMap.get(id);
      DomainObjectEL result = createDomainObject();
      result.setID(id);
      loadedMap.put(id, result);
      doLoad(result, rs);
      return result;
   }

class PersonMapper...
   protected DomainObjectEL createDomainObject() {
      return new Person();
   }
   protected void doLoad(DomainObjectEL obj, ResultSet rs) throws SQLException {
      Person person = (Person) obj;
      person.dbLoadLastName(rs.getString(2));
      person.setFirstName(rs.getString(3));
      person.setNumberOfDependents(rs.getInt(4));
   }

class DomainObjectEL...
   private int state = LOADING;
   private static final int LOADING = 0;
   private static final int ACTIVE = 1;
   public void beActive() {
      state = ACTIVE;
   }
   void assertStateIsLoading() {
      Assert.isTrue(state == LOADING);
   }

class Person...
   public void dbLoadLastName(String lastName) {
      assertStateIsLoading();
      this.lastName = lastName;
   }

## Chapter 11. Object-Relational Behavioral Patterns

Unit of Work with Object Registration (Java):
class UnitOfWork...
   private List newObjects = new ArrayList();
   private List dirtyObjects = new ArrayList();
   private List removedObjects = new ArrayList();

class UnitOfWork...
   public void registerNew(DomainObject obj) {
      Assert.notNull("id not null", obj.getId());
      Assert.isTrue("object not dirty", !dirtyObjects.contains(obj));
      Assert.isTrue("object not removed", !removedObjects.contains(obj));
      Assert.isTrue("object not already registered new", !newObjects.contains(obj));
      newObjects.add(obj);
   }
   public void registerDirty(DomainObject obj) {
      Assert.notNull("id not null", obj.getId());
      Assert.isTrue("object not removed", !removedObjects.contains(obj));
      if (!dirtyObjects.contains(obj) && !newObjects.contains(obj)) {
         dirtyObjects.add(obj);
      }
   }
   public void registerRemoved(DomainObject obj) {
      Assert.notNull("id not null", obj.getId());
      if (newObjects.remove(obj)) return;
      dirtyObjects.remove(obj);
      if (!removedObjects.contains(obj)) {
         removedObjects.add(obj);
      }
   }
   public void registerClean(DomainObject obj) {
      Assert.notNull("id not null", obj.getId());
   }

class UnitOfWork...
   private static ThreadLocal current = new ThreadLocal();
   public static void newCurrent() {
      setCurrent(new UnitOfWork());
   }
   public static void setCurrent(UnitOfWork uow) {
      current.set(uow);
   }
   public static UnitOfWork getCurrent() {
      return (UnitOfWork) current.get();
   }

class DomainObject...
   protected void markNew() {
      UnitOfWork.getCurrent().registerNew(this);
   }
   protected void markClean() {
      UnitOfWork.getCurrent().registerClean(this);
   }
   protected void markDirty() {
      UnitOfWork.getCurrent().registerDirty(this);
   }
   protected void markRemoved() {
      UnitOfWork.getCurrent().registerRemoved(this);
   }

class Album...
   public static Album create(String name) {
      Album obj = new Album(IdGenerator.nextId(), name);
      obj.markNew();
      return obj;
   }
   public void setTitle(String title) {
      this.title = title;
      markDirty();
   }

class EditAlbumScript...
   public static void updateTitle(Long albumId, String title) {
      UnitOfWork.newCurrent();
      Mapper mapper = MapperRegistry.getMapper(Album.class);
      Album album = (Album) mapper.find(albumId);
      album.setTitle(title);
      UnitOfWork.getCurrent().commit();
   }

class UnitOfWorkServlet...
   final protected void doGet(HttpServletRequest request, HttpServletResponse response)
         throws ServletException, IOException {
      try {
         UnitOfWork.newCurrent();
         handleGet(request, response);
         UnitOfWork.getCurrent().commit();
      } finally {
         UnitOfWork.setCurrent(null);
      }
   }
   abstract void handleGet(HttpServletRequest request, HttpServletResponse response)
         throws ServletException, IOException;

Identity Map (Java):
private Map people = new HashMap();
public static void addPerson(Person arg) {
   soleInstance.people.put(arg.getID(), arg);
}
public static Person getPerson(Long key) {
   return (Person) soleInstance.people.get(key);
}
public static Person getPerson(long key) {
   return getPerson(new Long(key));
}

Lazy Initialization (Java):
class Supplier...
   public List getProducts() {
      if (products == null) products = Product.findForSupplier(getID());
      return products;
   }

Virtual Proxy (Java):
class SupplierVL...
   private List products;

public interface VirtualListLoader {
   List load();
}

class SupplierMapper...
   public static class ProductLoader implements VirtualListLoader {
      private Long id;
      public ProductLoader(Long id) {
         this.id = id;
      }
      public List load() {
         return ProductMapper.create().findForSupplier(id);
      }
   }

class SupplierMapper...
   protected DomainObject doLoad(Long id, ResultSet rs) throws SQLException {
      String nameArg = rs.getString(2);
      SupplierVL result = new SupplierVL(id, nameArg);
      result.setProducts(new VirtualList(new ProductLoader(id)));
      return result;
   }

class VirtualList...
   private List source;
   private VirtualListLoader loader;
   public VirtualList(VirtualListLoader loader) {
      this.loader = loader;
   }
   private List getSource() {
      if (source == null) source = loader.load();
      return source;
   }

class VirtualList...
   public int size() {
      return getSource().size();
   }
   public boolean isEmpty() {
      return getSource().isEmpty();
   }

Value Holder (Java):
class SupplierVH...
   private ValueHolder products;
   public List getProducts() {
      return (List) products.getValue();
   }

class ValueHolder...
   private Object value;
   private ValueLoader loader;
   public ValueHolder(ValueLoader loader) {
      this.loader = loader;
   }
   public Object getValue() {
      if (value == null) value = loader.load();
      return value;
   }
public interface ValueLoader {
   Object load();
}

class SupplierMapper...
   protected DomainObject doLoad(Long id, ResultSet rs) throws SQLException {
      String nameArg = rs.getString(2);
      SupplierVH result = new SupplierVH(id, nameArg);
      result.setProducts(new ValueHolder(new ProductLoader(id)));
      return result;
   }
   public static class ProductLoader implements ValueLoader {
      private Long id;
      public ProductLoader(Long id) {
         this.id = id;
      }
      public Object load() {
         return ProductMapper.create().findForSupplier(id);
      }
   }

Ghost (C#):
class Domain Object...
   LoadStatus Status;
   public DomainObject (long key) {
      this.Key = key;
   }
   public Boolean IsGhost {
      get {return Status == LoadStatus.GHOST;}
   }
   public Boolean IsLoaded {
      get {return Status == LoadStatus.LOADED;}
   }
   public void MarkLoading() {
      Debug.Assert(IsGhost);
      Status = LoadStatus.LOADING;
   }
   public void MarkLoaded() {
      Debug.Assert(Status == LoadStatus.LOADING);
      Status = LoadStatus.LOADED;
   }
enum LoadStatus {GHOST, LOADING, LOADED};

class Employee...
   public String Name {
      get {
         Load();
         return  _name;
      }
      set {
         Load();
         _name = value;
      }
   }
   String  _name;

class Domain Object...
   protected void Load() {
      if (IsGhost)
         DataSource.Load(this);
   }

class DataSource...
   public static void Load (DomainObject obj) {
      instance.Load(obj);
   }

class DataSource...
   public interface IDataSource {
      void Load (DomainObject obj);
   }

class MapperRegistry : IDataSource...
   public void Load (DomainObject obj) {
      Mapper(obj.GetType()).Load (obj);
   }
   public static Mapper Mapper(Type type) {
      return (Mapper) instance.mappers[type];
   }
   IDictionary mappers = new Hashtable();

class EmployeeMapper...
   public Employee Find (long key) {
      return (Employee) AbstractFind(key);
   }

class Mapper...
   public DomainObject AbstractFind (long key) {
      DomainObject result;
      result = (DomainObject) loadedMap[key];
      if (result == null) {
         result = CreateGhost(key);
         loadedMap.Add(key, result);
      }
      return result;
   }
   IDictionary loadedMap = new Hashtable();
   public abstract DomainObject CreateGhost(long key);

class EmployeeMapper...
   public override DomainObject CreateGhost(long key) {
      return new Employee(key);
   }

class Mapper...
   public void Load (DomainObject obj) {
      if (! obj.IsGhost) return;
      IDbCommand comm = new OleDbCommand(findStatement(), DB.connection);
      comm.Parameters.Add(new OleDbParameter("key",obj.Key));
      IDataReader reader = comm.ExecuteReader();
      reader.Read();
      LoadLine (reader, obj);
      reader.Close();
   }
   protected abstract String findStatement();
   public void LoadLine (IDataReader reader, DomainObject obj) {
      if (obj.IsGhost) {
         obj.MarkLoading();
         doLoadLine (reader, obj);
         obj.MarkLoaded();
      }
   }
   protected abstract void doLoadLine (IDataReader reader, DomainObject obj);

class EmployeeMapper...
   protected override void doLoadLine (IDataReader reader, DomainObject obj) {
      Employee employee = (Employee) obj;
      employee.Name = (String) reader["name"];
      DepartmentMapper depMapper = (DepartmentMapper) MapperRegistry.Mapper(typeof(Department));
      employee.Department = depMapper.Find((int) reader["departmentID"]);
      loadTimeRecords(employee);
   }

class DomainList...
   IList data {
      get {
         Load();
         return  _data;
      }
      set {_data = value;}
   }
   IList  _data = new ArrayList();
   public int Count {
      get {return data.Count;}
   }

class DomainList...
   public void Load () {
      if (IsGhost) {
         MarkLoading();
         RunLoader(this);
         MarkLoaded();
      }
   }
   public delegate void Loader(DomainList list);
   public Loader RunLoader;

class EmployeeMapper...
   void loadTimeRecords(Employee employee) {
      ListLoader loader = new ListLoader();
      loader.Sql = TimeRecordMapper.FIND_FOR_EMPLOYEE_SQL;
      loader.SqlParams.Add(employee.Key);
      loader.Mapper = MapperRegistry.Mapper(typeof(TimeRecord));
      loader.Attach((DomainList) employee.TimeRecords);
   }

class ListLoader...
   public String Sql;
   public IList SqlParams = new ArrayList();
   public Mapper Mapper;

class ListLoader...
   public void Attach (DomainList list) {
      list.RunLoader = new DomainList.Loader(Load);
   }

class ListLoader...
   public void Load (DomainList list) {
      list.IsLoaded = true;
      IDbCommand comm = new OleDbCommand(Sql, DB.connection);
      foreach (Object param in SqlParams)
         comm.Parameters.Add(new OleDbParameter(param.ToString(),param));
      IDataReader reader = comm.ExecuteReader();
      while (reader.Read()) {
         DomainObject obj = GhostForLine(reader);
         Mapper.LoadLine(reader, obj);
         list.Add (obj);
      }
      reader.Close();
   }
   private DomainObject GhostForLine(IDataReader reader) {
      return Mapper.AbstractFind((System.Int32)reader[Mapper.KeyColumnName]);
   }

## Chapter 12. Object-Relational Structural Patterns

Identity Field: simple integral key in C# with placeholder value: `public const long PLACEHOLDER_ID = -1; public long Id = PLACEHOLDER_ID; public Boolean isNew() {return Id == PLACEHOLDER_ID;}` For finding: `DataRow row = FindRow(id); return (row == null) ? null : Find(row);` with filter `String filter = String.Format("id = {0}", id);` For insertion: `arg.Id = GetNextID(); row["id"] = arg.Id;` Using a key table in Java: create table with `CREATE TABLE keys (name varchar primary key, nextID int)`, then `KeyGenerator` reserves IDs in batches with `SELECT nextID FROM keys WHERE name = ? FOR UPDATE` and `UPDATE keys SET nextID = ? WHERE name = ?` to minimize contention.

Foreign Key Mapping: single-valued reference loading album with artist: `long artistID = rs.getLong(3); Artist artist = MapperRegistry.artist().find(artistID); Album result = new Album(id, title, artist);` Update: `statement.setLong(2, album.getArtist().getID().longValue());` Collection of references (Team with Players): `public IList Players { get {return ArrayList.ReadOnly(playersData);} set {playersData = new ArrayList(value);} }` Loading players for team: `team.Players = MapperRegistry.Player.FindForTeam(team.Id);` Updating: `foreach (Player p in team.Players) { MapperRegistry.Player.LinkTeam(p, team.Id); }`

Association Table Mapping: many-to-many (Employee with Skills): create table `create table employeeSkills (employeeID int, skillID int, primary key (employeeID, skillID))` Loading: `DataRow[] rows = skillLinkRows(emp); foreach (DataRow row in rows) { long skillID = (int)row["skillID"]; emp.AddSkill(MapperRegistry.Skill.Find(skillID)); }` Updating with delete-and-reinsert: `foreach (DataRow r in skillRows) r.Delete(); foreach (Skill s in emp.Skills) { DataRow row = skillLinkTable.NewRow(); row["employeeID"] = emp.Id; row["skillID"] = s.Id; skillLinkTable.Rows.Add(row); }`

Dependent Mapping: Album with Tracks (immutable Track): `class Track { private final String title; public Track(String title) { this.title = title; } }` Album holds tracks: `private List tracks = new ArrayList(); public void addTrack(Track arg) { tracks.add(arg); }` Mapper loads with join: `protected String findStatement() { return "SELECT ID, a.title, t.title as trackTitle FROM albums a, tracks t WHERE a.ID = ? AND t.albumID = a.ID ORDER BY t.seq"; }` Update deletes and reinserts: `deleteTracksStatement.execute(); for (int i = 0; i < arg.getTracks().length; i++) { insertTrack(arg.getTracks()[i], i + 1, arg); }`

Embedded Value: Money value object embedded in ProductOffering: `class ProductOffering { private Money baseCost; }` Load: `BigDecimal baseCostAmount = rs.getBigDecimal("base_cost_amount"); Currency baseCostCurrency = Registry.getCurrency(rs.getString("base_cost_currency")); Money baseCost = new Money(baseCostAmount, baseCostCurrency);` Update: `stmt.setBigDecimal(1, baseCost.amount()); stmt.setString(2, baseCost.currency().code());` mapped to table columns base_cost_amount and base_cost_currency.

Serialized LOB: Customer with Department hierarchy serialized to XML: `class Customer { private List departments = new ArrayList(); }` Insert serializes to XML: `insertStatement.setString(3, XmlStringer.write(departmentsToXmlElement()));` Serialization: `public Element departmentsToXmlElement() { Element root = new Element("departmentList"); Iterator i = departments.iterator(); while (i.hasNext()) { Department dep = (Department) i.next(); root.addContent(dep.toXmlElement()); } return root; }` Department recursive: `Element toXmlElement() { Element root = new Element("department"); root.setAttribute("name", name); Iterator i = subsidiaries.iterator(); while (i.hasNext()) { Department dep = (Department) i.next(); root.addContent(dep.toXmlElement()); } return root; }` Example XML: `<departmentList><department name="US"><department name="New England"><department name="Boston"/></department></department></departmentList>` Load reverses: `String departmentLob = rs.getString("departments"); result.readDepartments(XmlStringer.read(departmentLob));` with `void readDepartments(Element source) { Iterator it = source.getChildren("department").iterator(); while (it.hasNext()) addDepartment(Department.readXml((Element) it.next())); }`

Single Table Inheritance: all players in one table with type code: `class PlayerMapper { public Player Find (long key) { String typecode = (String) row["type"]; switch (typecode) { case BowlerMapper.TYPE_CODE: return (Player) bmapper.Find(row); case CricketerMapper.TYPE_CODE: return (Player) cmapper.Find(row); case FootballerMapper.TYPE_CODE: return (Player) fmapper.Find(row); } } }` Load chains through hierarchy: `class CricketerMapper { protected override void Load(DomainObject obj, DataRow row) { base.Load(obj,row); cricketer.battingAverage = (double)row["battingAverage"]; } }` Save also chains: `class AbstractPlayerMapper { protected override void Save(DomainObject obj, DataRow row) { Player player = (Player) obj; row["name"] = player.name; row["type"] = TypeCode; } }`

Class Table Inheritance: Player table (id, name, type), Footballer table (id, club), Bowler table (id, ballSpeed). Mapper finds across tables: `protected override void Load(DomainObject obj) { base.Load(obj); DataRow row = FindRow (obj.Id, tableFor(TABLENAME)); Footballer footballer = (Footballer) obj; footballer.club = (String)row["club"]; }` Update similarly: `protected override void Save(DomainObject obj) { base.Save(obj); DataRow row = FindRow (obj.Id, tableFor(TABLENAME)); Footballer footballer = (Footballer) obj; row["club"] = footballer.club; }`

Concrete Table Inheritance: separate Cricketer table (id, name, battingAverage), Bowler table (id, name, ballSpeed), Footballer table (id, name, club). To find generic Player: `public Player Find (long key) { Player result = fmapper.Find(key); if (result != null) return result; result = bmapper.Find(key); if (result != null) return result; result = cmapper.Find(key); return result; }` Each concrete mapper finds only its own table, with load/save chaining through hierarchy.

Inheritance Mappers: PlayerMapper delegates to concrete mappers: `public override void Update (DomainObject obj) { MapperFor(obj).Update(obj); } private Mapper MapperFor(DomainObject obj) { if (obj is Footballer) return fmapper; if (obj is Bowler) return bmapper; if (obj is Cricketer) return cmapper; }` Concrete mapper load chains: `class CricketerMapper { protected override void Load(DomainObject obj, DataRow row) { base.Load(obj,row); Cricketer cricketer = (Cricketer) obj; cricketer.battingAverage = (double)row["battingAverage"]; } }` This structure works the same across all three inheritance schemes.

## Chapter 13. Object-Relational Metadata Mapping Patterns

Code structure for Metadata Mapping metadata holders (Java):

class DataMap...
   private Class domainClass;
   private String tableName;
   private List columnMaps = new ArrayList();

class ColumnMap...
   private String columnName;
   private String fieldName;
   private Field field;
   private DataMap dataMap;

PersonMapper initialization:
class PersonMapper...
   protected void loadDataMap(){
      dataMap = new DataMap(Person.class, "people");
      dataMap.addColumn("lastname", "varchar", "lastName");
      dataMap.addColumn("firstname", "varchar", "firstName");
      dataMap.addColumn("number_of_dependents", "int", "numberOfDependents");
   }

Reflective field access with optimization:
class ColumnMap...
   public ColumnMap(String columnName, String fieldName, DataMap dataMap) {
      this.columnName = columnName;
      this.fieldName = fieldName;
      this.dataMap = dataMap;
      initField();
   }
   private void initField() {
      try {
         field = dataMap.getDomainClass().getDeclaredField(getFieldName());
         field.setAccessible(true);
      } catch (Exception e) {
         throw new ApplicationException("unable to set up field: " + fieldName, e);
      }
   }

Metadata-driven find and load (Java):
class Mapper...
   public Object findObject(Long key) {
      if (uow.isLoaded(key)) return uow.getObject(key);
      String sql = "SELECT" + dataMap.columnList() + " FROM " + dataMap.getTableName() + " WHERE ID = ?";
      PreparedStatement stmt = null;
      ResultSet rs = null;
      DomainObject result = null;
      try {
         stmt = DB.prepare(sql);
         stmt.setLong(1, key.longValue());
         rs = stmt.executeQuery();
         rs.next();
         result = load(rs);
      } catch (Exception e) {throw new ApplicationException(e);
      } finally {DB.cleanUp(stmt, rs);
      }
      return result;
   }
   
   public DomainObject load(ResultSet rs) throws InstantiationException, IllegalAccessException, SQLException {
      Long key = new Long(rs.getLong("ID"));
      if (uow.isLoaded(key)) return uow.getObject(key);
      DomainObject result = (DomainObject) dataMap.getDomainClass().newInstance();
      result.setID(key);
      uow.registerClean(result);
      loadFields(rs, result);
      return result;
   }
   
   private void loadFields(ResultSet rs, DomainObject result) throws SQLException {
      for (Iterator it = dataMap.getColumns(); it.hasNext();) {
         ColumnMap columnMap = (ColumnMap)it.next();
         Object columnValue = rs.getObject(columnMap.getColumnName());
         columnMap.setField(result, columnValue);
      }
   }

Query Object structure (Java):
class QueryObject...
   private Class klass;
   private List criteria = new ArrayList();

class Criteria...
   private String sqlOperator;
   protected String field;
   protected Object value;

Criteria factory methods:
class Criteria...
   public static Criteria greaterThan(String fieldName, int value) {
      return Criteria.greaterThan(fieldName, new Integer(value));
   }
   public static Criteria greaterThan(String fieldName, Object value) {
      return new Criteria(" > ", fieldName, value);
   }
   private Criteria(String sql, String field, Object value) {
      this.sqlOperator = sql;
      this.field = field;
      this.value = value;
   }

Query construction and execution (Java):
QueryObject query = new QueryObject(Person.class);
query.addCriteria(Criteria.greaterThan("numberOfDependents", 0));

class QueryObject...
   public Set execute(UnitOfWork uow) {
      this.uow = uow;
      return uow.getMapper(klass).findObjectsWhere(generateWhereClause());
   }

Where clause generation:
class QueryObject...
   private String generateWhereClause() {
      StringBuffer result = new StringBuffer();
      for (Iterator it = criteria.iterator(); it.hasNext();) {
         Criteria c = (Criteria)it.next();
         if (result.length() != 0)
            result.append(" AND ");
         result.append(c.generateSql(uow.getMapper(klass).getDataMap()));
      }
      return result.toString();
   }

class Criteria...
   public String generateSql(DataMap dataMap) {
      return dataMap.getColumnForField(field) + sqlOperator + value;
   }

Pattern-matching criteria (Java):
QueryObject query = new QueryObject(Person.class);
query.addCriteria(Criteria.greaterThan("numberOfDependents", 0));
query.addCriteria(Criteria.matches("lastName", "f%"));

class MatchCriteria extends Criteria...
   public String generateSql(DataMap dataMap) {
      return "UPPER(" + dataMap.getColumnForField(field) + ") LIKE UPPER('" + value + "')";
   }

Repository client usage (Java):
public class Person {
   public List dependents() {
      Repository repository = Registry.personRepository();
      Criteria criteria = new Criteria();
      criteria.equal(Person.BENEFACTOR, this);
      return repository.matching(criteria);
   }
}

PersonRepository subclass:
public class PersonRepository extends Repository {
   public List listDependentsOf(Person aPerson) {
      Criteria criteria = new Criteria();
      criteria.equal(Person.BENEFACTOR, aPerson);
      return matching(criteria);
   }
}

Repository strategy pattern (Java):
abstract class Repository {
   private RepositoryStrategy strategy;
   protected List matching(Criteria aCriteria) {
      return strategy.matching(aCriteria);
   }
}

public class RelationalStrategy implements RepositoryStrategy {
   protected List matching(Criteria criteria) {
      Query query = new Query(myDomainObjectClass());
      query.addCriteria(criteria);
      return query.execute(unitOfWork());
   }
}

public class InMemoryStrategy implements RepositoryStrategy {
   private Set domainObjects;
   protected List matching(Criteria criteria) {
      List results = new ArrayList();
      Iterator it = domainObjects.iterator();
      while (it.hasNext()) {
         DomainObject each = (DomainObject) it.next();
         if (criteria.isSatisfiedBy(each))
            results.add(each);
      }
      return results;
   }
}

## Chapter 14. Web Presentation Patterns

Model View Controller - Principle demonstrated: "The key point in this separation is the direction of the dependencies: the presentation depends on the model but the model doesn't depend on the presentation. People programming in the model should be entirely unaware of what presentation is being used." Observer pattern used for event propagation when multiple presentations exist on a single screen.

Page Controller servlet example (Java):
\
class ArtistController...\
\
   public void doGet(HttpServletRequest request, HttpServletResponse response)\
         throws IOException, ServletException {\
      Artist artist = Artist.findNamed(request.getParameter("name"));\
      if (artist == null)\
         forward("/MissingArtistError.jsp", request, response);\
      else {\
         request.setAttribute("helper", new ArtistHelper(artist));\
         forward("/artist.jsp", request, response);\
      }\
   }

Page Controller helper class:
\
class AlbumController...\
\
   public void doGet(HttpServletRequest request, HttpServletResponse response)\
         throws IOException, ServletException\
   {\
      Album album = Album.find(request.getParameter("id"));\
      if (album == null) {\
         forward("/missingAlbumError.jsp", request, response);\
         return;\
      }\
      request.setAttribute("helper", album);\
      if (album instanceof ClassicalAlbum)\
         forward("/classicalAlbum.jsp", request, response);\
      else\
         forward("/album.jsp", request, response);\
   }

Front Controller servlet (Java):
\
class FrontServlet...\
\
   public void doGet(HttpServletRequest request, HttpServletResponse response)\
         throws IOException, ServletException {\
      FrontCommand command = getCommand(request);\
      command.init(getServletContext(), request, response);\
      command.process();\
   }\
   private FrontCommand getCommand(HttpServletRequest request) {\
      try {\
         return (FrontCommand) getCommandClass(request).newInstance();\
      } catch (Exception e) {\
           throw new ApplicationException(e);\
      }\
   }\
   private Class getCommandClass(HttpServletRequest request) {\
      Class result;\
      final String commandClassName =\
            "frontController." + (String) request.getParameter("command") + "Command";\
      try {\
         result = Class.forName(commandClassName);\
      } catch (ClassNotFoundException e) {\
         result = UnknownCommand.class;\
      }\
      return result;\
   }

Template View with JSP and helper (Java):
\
class ArtistHelper...\
\
   private Artist artist;\
   public ArtistHelper(Artist artist) {\
      this.artist = artist;\
   }\
   public String getName() {\
      return artist.getName();\
   }\
   public String getAlbumList() {\
      StringBuffer result = new StringBuffer();\
      result.append("\<UL\>");\
      for (Iterator it = getAlbums().iterator(); it.hasNext();) {\
         Album album = (Album) it.next();\
         result.append("\<LI\>");\
         result.append(album.getTitle());\
         result.append("\</LI\>");\
      }\
      result.append("\</UL\>");\
      return result.toString();\
   }

Transform View XSLT templates for album data:
\
\<xsl:template match="album"\>\
   \<HTML\>\<BODY bgcolor="white"\>\
   \<xsl:apply-templates/\>\
   \</BODY\>\</HTML\>\
\</xsl:template\>\
\<xsl:template match="album/title"\>\
   \<h1\>\<xsl:apply-templates/\>\</h1\>\
\</xsl:template\>\
\<xsl:template match="trackList"\>\
   \<table\>\<xsl:apply-templates/\>\</table\>\
\</xsl:template\>\
\<xsl:template match="track"\>\
   \<xsl:variable name="bgcolor"\>\
      \<xsl:choose\>\
         \<xsl:when test="(position() mod 2) = 1"\>linen\</xsl:when\>\
         \<xsl:otherwise\>white\</xsl:otherwise\>\
      \</xsl:choose\>\
   \</xsl:variable\>\
   \<tr bgcolor="{\$bgcolor}"\>\<xsl:apply-templates/\>\</tr\>\
\</xsl:template\>

Two Step View—first-stage XSLT transforms domain XML to logical screen XML:
\
\<xsl:template match="album"\>\
   \<screen\>\<xsl:apply-templates/\>\</screen\>\
\</xsl:template\>\
\<xsl:template match="artist"\>\
   \<field label="Artist"\>\<xsl:apply-templates/\>\</field\>\
\</xsl:template\>\
\<xsl:template match="trackList"\>\
   \<table\>\<xsl:apply-templates/\>\</table\>\
\</xsl:template\>

Application Controller state model (Java) for asset leasing:
\
class AssetApplicationController...\
\
   private Response getResponse(String commandString, AssetStatus state) {\
      return (Response) getResponseMap(commandString).get(state);\
   }\
   public DomainCommand getDomainCommand (String commandString, Map params) {\
      Response response = getResponse(commandString, getAssetStatus(params));\
      return response.getDomainCommand();\
   }\
   public String getView (String commandString, Map params) {\
      return getResponse(commandString, getAssetStatus(params)).getViewUrl();\
   }\
   private static void loadApplicationController(AssetApplicationController appController) {\
      appController.addResponse("return", AssetStatus.ON_LEASE,\
                           GatherReturnDetailsCommand.class, "return");\
      appController.addResponse("return", AssetStatus.IN_INVENTORY,\
                           NullAssetCommand.class, "illegalAction");\
      appController.addResponse("damage", AssetStatus.ON_LEASE,\
                           InventoryDamageCommand.class, "leaseDamage");\
      appController.addResponse("damage", AssetStatus.IN_INVENTORY,\
                           LeaseDamageCommand.class, "inventoryDamage");\
   }

## Chapter 15. Distribution Patterns

*Nota: este capítulo se procesó en 3 fragmentos separados (ver history.md) por un bloqueo puntual del filtro de contenido de la API; la numeración de ejemplos abajo es continua a través de los fragmentos, no reinicia. Código extraído literalmente de raw.md (líneas 20458-21830).*

Figure 15.1 ("One call to a facade causes several calls from the facade to the domain object") and Figure 15.2 ("Packages the remote interfaces") are referenced but not reproduced (image references only).

**Remote Facade — EJB/Java example:**

1. AlbumService interface (Java):
```java
class AlbumService...
   String play(String id) throws RemoteException;
   String getAlbumXml(String id) throws RemoteException;
   AlbumDTO getAlbum(String id) throws RemoteException;
   void createAlbum(String id, String xml) throws RemoteException;
   void createAlbum(String id, AlbumDTO dto) throws RemoteException;
   void updateAlbum(String id, String xml) throws RemoteException;
   void updateAlbum(String id, AlbumDTO dto) throws RemoteException;
   void addArtistNamed(String id, String name) throws RemoteException;
   void addArtist(String id, String xml) throws RemoteException;
   void addArtist(String id, ArtistDTO dto) throws RemoteException;
   ArtistDTO getArtist(String id) throws RemoteException;
```

2. AlbumServiceBean implementation (Java):
```java
class AlbumServiceBean...
   public AlbumDTO getAlbum(String id) throws RemoteException {
         return new AlbumAssembler().writeDTO(Registry.findAlbum(id));
   }
   public String getAlbumXml(String id) throws RemoteException {
         AlbumDTO dto = new AlbumAssembler().writeDTO(Registry.findAlbum(id));
         return dto.toXmlString();
   }
   public void createAlbum(String id, AlbumDTO dto) throws RemoteException {
         new AlbumAssembler().createAlbum(id, dto);
   }
   public void createAlbum(String id, String xml) throws RemoteException {
         AlbumDTO dto = AlbumDTO.readXmlString(xml);
         new AlbumAssembler().createAlbum(id, dto);
   }
   public void updateAlbum(String id, AlbumDTO dto) throws RemoteException {
         new AlbumAssembler().updateAlbum(id, dto);
   }
   public void updateAlbum(String id, String xml) throws RemoteException {
         AlbumDTO dto = AlbumDTO.readXmlString(xml);
         new AlbumAssembler().updateAlbum(id, dto);
   }
```

3. XmlTester JUnit test (Java):
```java
class XmlTester...
   private AlbumDTO kob;
   private AlbumDTO newkob;
   private AlbumServiceBean facade = new AlbumServiceBean();
   protected void setUp() throws Exception {
      facade.initializeForTesting();
      kob = facade.getAlbum("kob");
      Writer buffer = new StringWriter();
      kob.toXmlString(buffer);
      newkob = AlbumDTO.readXmlString(new StringReader(buffer.toString()));
   }
   public void testArtist() {
      assertEquals(kob.getArtist(), newkob.getArtist());
   }
```

**Remote Facade — Web Service/C# example:**

4. Album, Artist, Track Domain Model classes (C#):
```csharp
class Album...
      public String Title;
      public Artist Artist;
      public IList Tracks  {
         get {return ArrayList.ReadOnly(tracksData);}
      }
      public void AddTrack  (Track arg) {
         tracksData.Add(arg);
      }
      public void RemoveTrack  (Track arg) {
         tracksData.Remove(arg);
      }
      private IList tracksData = new ArrayList();

class Artist...

      public String Name;

class Track...

      public String Title;
      public IList Performers  {
         get {return ArrayList.ReadOnly(performersData);}
      }
      public void AddPerformer (Artist arg) {
         performersData.Add(arg);
      }
      public void RemovePerformer (Artist arg) {
         performersData.Remove(arg);
      }
      private IList performersData = new ArrayList();
```

5. AlbumDTO and TrackDTO classes (C#):
```csharp
class AlbumDTO...
      public String Title;
      public String Artist;
      public TrackDTO[] Tracks;
class TrackDTO...
      public String Title;
      public String[] Performers;
```

6. XML Schema (WSDL fragment) for the DTOs:
```xml
   <s:complexType name="AlbumDTO"> <s:sequence> <s:element minOccurs="1" maxOccurs="1" name="Title" nillable="true" type="s:string" /> <s:element minOccurs="1" maxOccurs="1" name="Artist" nillable="true" type="s:string" /> <s:element minOccurs="1" maxOccurs="1" name="Tracks" nillable="true" type="s0:ArrayOfTrackDTO" /> </s:sequence> </s:complexType> <s:complexType name="ArrayOfTrackDTO"> <s:sequence> <s:element minOccurs="0" maxOccurs="unbounded" name="TrackDTO" nillable="true" type="s0:TrackDTO" /> </s:sequence> </s:complexType> <s:complexType name="TrackDTO"> <s:sequence> <s:element minOccurs="1" maxOccurs="1" name="Title" nillable="true" type="s:string" /> <s:element minOccurs="1" maxOccurs="1" name="Performers" nillable="true" type="s0:ArrayOfString" /> </s:sequence> </s:complexType> <s:complexType name="ArrayOfString"> <s:sequence> <s:element minOccurs="0" maxOccurs="unbounded" name="string" nillable="true" type="s:string" /> </s:sequence> </s:complexType>
```

7. AlbumAssembler.WriteDTO / WriteTrack (C#):
```csharp
class AlbumAssembler...
      public AlbumDTO  WriteDTO  (Album subject) {
         AlbumDTO result = new AlbumDTO();
         result.Artist = subject.Artist.Name;
         result.Title = subject.Title;
         ArrayList trackList = new ArrayList();
         foreach (Track t  in subject.Tracks) trackList.Add (WriteTrack(t));
         result.Tracks = (TrackDTO[]) trackList.ToArray(typeof(TrackDTO));
         return result;
      }
      public TrackDTO  WriteTrack  (Track subject) {
         TrackDTO result = new TrackDTO();
         result.Title = subject.Title;
         result.Performers = new String[subject.Performers.Count];
         ArrayList performerList = new ArrayList();
         foreach (Artist a  in subject.Performers) performerList.Add (a.Name);
         result.Performers = (String[]) performerList.ToArray(typeof  (String));
         return result;
      }
```

8. AlbumService.GetAlbum Web Method (C#):
```csharp
class AlbumService...
      [ WebMethod ] public AlbumDTO  GetAlbum(String key) {
         Album result = new AlbumFinder()[key];
         if (result == null) throw new SoapException ("unable to find album with key: " + key, SoapException.ClientFaultCode);
         else return new AlbumAssembler().WriteDTO(result);
      }
```

9. WSDL portType/message/schema fragment for GetAlbum/GetAlbumResponse:
```xml
<portType name="AlbumServiceSoap"> <operation name="GetAlbum"> <input message="s0:GetAlbumSoapIn"  /> <output message="s0:GetAlbumSoapOut"  /> </operation> </portType> <message name="GetAlbumSoapIn"> <part name="parameters"  element="s0:GetAlbum"  /> </message> <message name="GetAlbumSoapOut"> <part name="parameters"  element="s0:GetAlbumResponse"  /> </message> <s:element name="GetAlbum"> <s:complexType> <s:sequence> <s:element minOccurs="1"  maxOccurs="1"  name="key"  nillable="true"  type="s:string"  /> </s:sequence> </s:complexType> </s:element> <s:element name="GetAlbumResponse"> <s:complexType> <s:sequence> <s:element minOccurs="1"  maxOccurs="1"  name="GetAlbumResult" nillable="true"  type="s0:AlbumDTO"  /> </s:sequence> </s:complexType> </s:element>
```

10. SOAP envelope XML fragment (GetAlbum request):
```xml
<?xml version="1.0"  encoding="utf-8"?> <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"> <soap:Body> <GetAlbum xmlns="http://martinfowler.com"> <key>aKeyString</key> </GetAlbum> </soap:Body> </soap:Envelope>
```

**Data Transfer Object — Java examples:**

11. AlbumAssembler.writeDTO and helpers (Java):
```java
class AlbumAssembler...

   public AlbumDTO writeDTO(Album subject) {
      AlbumDTO result = new AlbumDTO();
      result.setTitle(subject.getTitle());
      result.setArtist(subject.getArtist().getName());
      writeTracks(result, subject);
      return result;
   }
   private void writeTracks(AlbumDTO result, Album subject) {
      List newTracks = new ArrayList();
      Iterator it = subject.getTracks().iterator();
      while (it.hasNext()) {
         TrackDTO newDTO = new TrackDTO();
         Track thisTrack = (Track) it.next();
         newDTO.setTitle(thisTrack.getTitle());
         writePerformers(newDTO, thisTrack);
         newTracks.add(newDTO);
      }
      result.setTracks((TrackDTO[]) newTracks.toArray(new TrackDTO[0]));
   }
   private void writePerformers(TrackDTO dto, Track subject) {
      List result = new ArrayList();
      Iterator it = subject.getPerformers().iterator();
      while (it.hasNext()) {
         Artist each = (Artist) it.next();
         result.add(each.getName());
      }
      dto.setPerformers((String[]) result.toArray(new String[0]));
   }
```

12. AlbumAssembler.createAlbum and helpers (Java):
```java
class AlbumAssembler...
   public void createAlbum(String id, AlbumDTO source) {
      Artist artist = Registry.findArtistNamed(source.getArtist());
      if (artist == null) throw new RuntimeException("No artist named " + source.getArtist());
      Album album = new Album(source.getTitle(), artist);
      createTracks(source.getTracks(), album);
      Registry.addAlbum(id, album);
   }
   private void createTracks(TrackDTO[] tracks, Album album) {
      for (int i = 0; i < tracks.length;  i++) {
         Track newTrack = new Track(tracks[i].getTitle());
         album.addTrack(newTrack);
         createPerformers(newTrack, tracks[i].getPerformers());
      }
   }
   private void createPerformers(Track newTrack, String[] performerArray) {
      for (int i = 0; i < performerArray.length;  i++) {
         Artist performer = Registry.findArtistNamed(performerArray[i]);
         if (performer == null) throw new RuntimeException("No artist named " + performerArray[i]);
         newTrack.addPerformer(performer);
      }
   }
```

13. AlbumAssembler.updateAlbum and updateTracks (Java):
```java
class AlbumAssembler...
   public void updateAlbum(String id, AlbumDTO source) {
      Album current = Registry.findAlbum(id);
      if (current == null) throw new RuntimeException("Album does not exist: " + source.getTitle());
      if (source.getTitle()  != current.getTitle()) current.setTitle(source.getTitle());
      if (source.getArtist()  != current.getArtist().getName()) {
         Artist artist = Registry.findArtistNamed(source.getArtist());
         if (artist == null) throw new RuntimeException("No artist named " + source.getArtist());
         current.setArtist(artist);
      }
      updateTracks(source, current);
   }
   private void updateTracks(AlbumDTO source, Album current) {
      for (int i = 0; i < source.getTracks().length;  i++) {
         current.getTrack(i).setTitle(source.getTrackDTO(i).getTitle());
         current.getTrack(i).clearPerformers();
         createPerformers(current.getTrack(i), source.getTrackDTO(i).getPerformers());
      }
   }
```

14. TrackDTO.writeMap / readMap (Java):
```java
class TrackDTO...
   public Map writeMap() {
      Map result = new HashMap();
      result.put("title", title);
      result.put("performers", performers);
      return result;
   }
   public static TrackDTO readMap(Map arg) {
      TrackDTO result = new TrackDTO();
      result.title = (String) arg.get("title");
      result.performers = (String[]) arg.get("performers");
      return result;
   }
```

15. DataTransferObject.writeMapReflect / readMapReflect (Java):
```java
class DataTransferObject...

   public Map writeMapReflect() {
      Map result = null;
      try {
         Field[] fields = this.getClass().getDeclaredFields();
         result = new HashMap();
         for (int i = 0; i < fields.length;  i++) result.put(fields[i].getName(), fields[i].get(this));
      } catch (Exception e) {throw new ApplicationException (e);
      }
      return result;
   }
   public static TrackDTO readMapReflect(Map arg) {
      TrackDTO result = new TrackDTO();
      try {
         Field[] fields = result.getClass().getDeclaredFields();
         for (int i = 0; i < fields.length;  i++) fields[i].set(result, arg.get(fields[i].getName()));
      } catch (Exception e) {throw new ApplicationException (e);
      }
      return result;
   }
```

16. AlbumDTO / TrackDTO toXmlElement / readXml (Java, JDOM):
```java
class AlbumDTO...

   Element toXmlElement() {
      Element root = new Element("album");
      root.setAttribute("title", title);
      root.setAttribute("artist", artist);
      for (int i = 0; i < tracks.length;  i++) root.addContent(tracks[i].toXmlElement());
      return root;
   }
   static AlbumDTO readXml(Element source) {
      AlbumDTO result = new AlbumDTO();
      result.setTitle(source.getAttributeValue("title"));
      result.setArtist(source.getAttributeValue("artist"));
      List trackList = new ArrayList();
      Iterator it = source.getChildren("track").iterator();
      while (it.hasNext()) trackList.add(TrackDTO.readXml((Element) it.next()));
      result.setTracks((TrackDTO[]) trackList.toArray(new TrackDTO[0]));
      return result;
   }
class TrackDTO...

   Element toXmlElement() {
      Element result = new Element("track");
      result.setAttribute("title", title);
      for (int i = 0; i < performers.length;  i++) {
         Element performerElement = new Element("performer");
         performerElement.setAttribute("name", performers[i]);
         result.addContent(performerElement);
      }
      return result;
   }
   static TrackDTO readXml(Element arg) {
      TrackDTO result = new TrackDTO();
      result.setTitle(arg.getAttributeValue("title"));
      Iterator it = arg.getChildren("performer").iterator();
      List buffer = new ArrayList();
      while (it.hasNext()) {
         Element eachElement = (Element) it.next();
         buffer.add(eachElement.getAttributeValue("name"));
      }
      result.setPerformers((String[]) buffer.toArray(new String[0]));
      return result;
   }
```

17. AlbumDTO.toXmlString / readXmlString (Java, JDOM):
```java
class AlbumDTO...
   public void toXmlString(Writer output) {
      Element root = toXmlElement();
      Document doc = new Document(root);
      XMLOutputter writer = new XMLOutputter();
      try {
         writer.output(doc, output);
      }catch (IOException e) {
         e.printStackTrace();
      }
   }
   public static AlbumDTO readXmlString(Reader input) {
      try {
         SAXBuilder builder = new SAXBuilder();
         Document doc = builder.build(input);
         Element root = doc.getRootElement();
         AlbumDTO result = readXml(root);
         return result;
      }catch (Exception e) {
         e.printStackTrace();
         throw new RuntimeException();
      }
   }
```

## Chapter 16. Offline Concurrency Patterns

### Optimistic Offline Lock Example: Domain Layer with Data Mappers (Java)

Class DomainObject storing version and modification data:
```java
class DomainObject...
   private Timestamp modified;
   private String modifiedBy;
   private int version;
```

Customer table schema and CRUD SQL:
```sql
create table customer(id bigint primary key, name varchar, createdby varchar,
   created datetime, modifiedby varchar, modified datetime, version int)

INSERT INTO customer VALUES (?, ?, ?, ?, ?, ?, ?)
SELECT * FROM customer WHERE id = ?
UPDATE customer SET name = ?, modifiedBy = ?, modified = ?, version = ?
   WHERE id = ? and version = ?
DELETE FROM customer WHERE id = ? and version = ?
```

AbstractMapper finding records:
```java
class AbstractMapper...
   public DomainObject find(Long id) {
      DomainObject obj = AppSessionManager.getSession().getIdentityMap().get(id);
      if (obj == null) {
         Connection conn = null;
         PreparedStatement stmt = null;
         ResultSet rs = null;
         try {
            conn = ConnectionManager.INSTANCE.getConnection();
            stmt = conn.prepareStatement(loadSQL);
            stmt.setLong(1, id.longValue());
            rs = stmt.executeQuery();
            if (rs.next()) {
               obj = load(id, rs);
               String modifiedBy = rs.getString(columns.length + 2);
               Timestamp modified = rs.getTimestamp(columns.length + 3);
               int version = rs.getInt(columns.length + 4);
               obj.setSystemFields(modified, modifiedBy, version);
               AppSessionManager.getSession().getIdentityMap().put(obj);
            } else {
                throw new SystemException(table + " " + id + "  does not exist");
            }
         } catch (SQLException sqlEx) {
            throw new SystemException("unexpected error finding " + table + " " + id);
         } finally {
            cleanupDBResources(rs, conn, stmt);
         }
      }
      return obj;
   }
```

Delete with version check:
```java
class AbstractMapper...
   public void delete(DomainObject object) {
      AppSessionManager.getSession().getIdentityMap().remove(object.getId());
      Connection conn = null;
      PreparedStatement stmt = null;
      try {
         conn = ConnectionManager.INSTANCE.getConnection();
         stmt = conn.prepareStatement(deleteSQL);
         stmt.setLong(1, object.getId().longValue());
         int rowCount = stmt.executeUpdate();
         if (rowCount == 0) {
            throwConcurrencyException(object);
         }
      } catch (SQLException e) {
           throw new SystemException("unexpected error deleting");
      } finally {
         cleanupDBResources(conn, stmt);
      }
   }
   protected void throwConcurrencyException(DomainObject object) throws SQLException {
      Connection conn = null;
      PreparedStatement stmt = null;
      ResultSet rs = null;
      try {
         conn = ConnectionManager.INSTANCE.getConnection();
         stmt = conn.prepareStatement(checkVersionSQL);
         stmt.setInt(1, (int) object.getId().longValue());
         rs = stmt.executeQuery();
         if (rs.next()) {
            int version = rs.getInt(1);
            String modifiedBy = rs.getString(2);
            Timestamp modified = rs.getTimestamp(3);
            if (version > object.getVersion()) {
               String when = DateFormat.getDateTimeInstance().format(modified);
               throw new ConcurrencyException(table + " " + object.getId() +
                     "  modified by " + modifiedBy + "  at " + when);
            } else {
               throw new SystemException("unexpected error checking timestamp");
            }
         } else {
            throw new ConcurrencyException(table + " " + object.getId() +
                  " has been deleted");
         }
      } finally {
         cleanupDBResources(rs, conn, stmt);
      }
   }
```

UnitOfWork registering reads and checking versions:
```java
class UnitOfWork...
   private List reads = new ArrayList();
   public void registerRead(DomainObject object) {
      reads.add(object);
   }
   public void commit() {
      try {
         checkConsistentReads();
         insertNew();
         deleteRemoved();
         updateDirty();
      } catch (ConcurrencyException e) {
         rollbackSystemTransaction();
         throw e;
      }
   }
   public void checkConsistentReads() {
      for (Iterator iterator = reads.iterator(); iterator.hasNext();) {
         DomainObject dependent = (DomainObject) iterator.next();
         dependent.getVersion().increment();
      }
   }
```

### Pessimistic Offline Lock Example: Simple Lock Manager (Java)

Lock manager interface:
```java
interface ExclusiveReadLockManager...
   public static final ExclusiveReadLockManager INSTANCE =
         (ExclusiveReadLockManager) Plugins.getPlugin(ExclusiveReadLockManager.class);
   public void acquireLock(Long lockable, String owner) throws ConcurrencyException;
   public void releaseLock(Long lockable, String owner);
   public void relaseAllLocks(String owner);
```

Lock table schema and database implementation:
```sql
create table lock(lockableid bigint primary key, ownerid bigint)
```

```java
class ExclusiveReadLockManagerDBImpl implements ExclusiveReadLockManager...
   private static final String INSERT_SQL = "insert into lock values(?, ?)";
   private static final String DELETE_SINGLE_SQL =
         "delete from lock where lockableid = ? and ownerid = ?";
   private static final String DELETE_ALL_SQL = "delete from lock where ownerid = ?";
   private static final String CHECK_SQL =
         "select lockableid from lock where lockableid = ? and ownerid = ?";
   public void acquireLock(Long lockable, String owner) throws ConcurrencyException {
      if (!hasLock(lockable, owner)) {
         Connection conn = null;
         PreparedStatement pstmt = null;
         try {
            conn = ConnectionManager.INSTANCE.getConnection();
            pstmt = conn.prepareStatement(INSERT_SQL);
            pstmt.setLong(1, lockable.longValue());
            pstmt.setString(2, owner);
            pstmt.executeUpdate();
         } catch (SQLException sqlEx) {
            throw new ConcurrencyException("unable to lock " + lockable);
         } finally {
            closeDBResources(conn, pstmt);
         }
      }
   }
   public void releaseLock(Long lockable, String owner) {
      Connection conn = null;
      PreparedStatement pstmt = null;
      try {
         conn = ConnectionManager.INSTANCE.getConnection();
         pstmt = conn.prepareStatement(DELETE_SINGLE_SQL);
         pstmt.setLong(1, lockable.longValue());
         pstmt.setString(2, owner);
         pstmt.executeUpdate();
      } catch (SQLException sqlEx) {
         throw new SystemException("unexpected error releasing lock on " + lockable);
      } finally {
         closeDBResources(conn, pstmt);
      }
   }
```

BusinessTransactionCommand establishing context:
```java
abstract class BusinessTransactionCommand implements Command...
   public void init(HttpServletRequest req, HttpServletResponse rsp) {
      this.req = req;
      this.rsp = rsp;
   }
   protected void startNewBusinessTransaction() {
      HttpSession httpSession = getReq().getSession(true);
      AppSession appSession = (AppSession) httpSession.getAttribute(APP_SESSION);
      if (appSession != null) {
         ExclusiveReadLockManager.INSTANCE.relaseAllLocks(appSession.getId());
      }
      appSession = new AppSession(getReq().getRemoteUser(),
                  httpSession.getId(), new IdentityMap());
      AppSessionManager.setSession(appSession);
      httpSession.setAttribute(APP_SESSION, appSession);
      httpSession.setAttribute(LOCK_REMOVER, new LockRemover(appSession.getId()));
   }
   protected void continueBusinessTransaction() {
      HttpSession httpSession = getReq().getSession();
      AppSession appSession = (AppSession) httpSession.getAttribute(APP_SESSION);
      AppSessionManager.setSession(appSession);
   }
```

Lock cleanup on session timeout:
```java
class LockRemover implements HttpSessionBindingListener...
   private String sessionId;
   public LockRemover(String sessionId) {
      this.sessionId = sessionId;
   }
   public void valueUnbound(HttpSessionBindingEvent event) {
      try {
         beginSystemTransaction();
         ExclusiveReadLockManager.INSTANCE.relaseAllLocks(this.sessionId);
         commitSystemTransaction();
      } catch (Exception e) {
         handleSeriousError(e);
      }
   }
```

Edit and save customer commands:
```java
class EditCustomerCommand implements Command...
   public void process() throws Exception {
      startNewBusinessTransaction();
      Long customerId = new Long(getReq().getParameter("customer_id"));
      ExclusiveReadLockManager.INSTANCE.acquireLock(
            customerId, AppSessionManager.getSession().getId());
      Mapper customerMapper = MapperRegistry.INSTANCE.getMapper(Customer.class);
      Customer customer = (Customer) customerMapper.find(customerId);
      getReq().getSession().setAttribute("customer", customer);
      forward("/editCustomer.jsp");
   }

class SaveCustomerCommand implements Command...
   public void process() throws Exception {
      continueBusinessTransaction();
      Customer customer = (Customer) getReq().getSession().getAttribute("customer");
      String name = getReq().getParameter("customerName");
      customer.setName(name);
      Mapper customerMapper = MapperRegistry.INSTANCE.getMapper(Customer.class);
      customerMapper.update(customer);
      ExclusiveReadLockManager.INSTANCE.releaseLock(customer.getId(),
                             AppSessionManager.getSession().getId());
      forward("/customerSaved.jsp");
   }
```

### Coarse-Grained Lock Example: Shared Optimistic Offline Lock (Java)

Version class with finder and increment:
```java
table version...
   create table version(id bigint primary key, value bigint,
      modifiedBy varchar, modified datetime)

class Version...
   public static Version find(Long id) {
      Version version = AppSessionManager.getSession().getIdentityMap().getVersion(id);
      if (version == null) {
         version = load(id);
      }
      return version;
   }
   public void increment() throws ConcurrencyException {
      if (!isLocked()) {
         Connection conn = null;
         PreparedStatement pstmt = null;
         try {
            conn = ConnectionManager.INSTANCE.getConnection();
            pstmt = conn.prepareStatement(UPDATE_SQL);
            pstmt.setLong(1, value + 1);
            pstmt.setString(2, getModifiedBy());
            pstmt.setTimestamp(3, getModified());
            pstmt.setLong(4, id.longValue());
            pstmt.setLong(5, value);
            int rowCount = pstmt.executeUpdate();
            if (rowCount == 0) {
               throwConcurrencyException();
            }
            value++;
            locked = true;
         } catch (SQLException sqlEx) {
            throw new SystemException("unexpected sql error incrementing version", sqlEx);
         } finally {
           cleanupDBResources(conn, pstmt);
         }
      }
   }
```

Customer and Address creation with shared version:
```java
class Customer extends DomainObject...
   public static Customer create(String name) {
      return new Customer(IdGenerator.INSTANCE.nextId(), Version.create(),
            name, new ArrayList());
   }

class Customer extends DomainObject...
   public Address addAddress(String line1, String city, String state) {
      Address address = Address.create(this, getVersion(), line1, city, state);
      addresses.add(address);
      return address;
   }

class Address extends DomainObject...
   public static Address create(Customer customer, Version version,
      String line1, String city, String state) {
      return new Address(IdGenerator.INSTANCE.nextId(), version, customer,
                     line1, city, state);
   }
```

AbstractMapper update and delete with version increment:
```java
class AbstractMapper...
   public void update(DomainObject object) {
      object.getVersion().increment();
   }

   public void delete(DomainObject object) {
      object.getVersion().increment();
   }

class CustomerMapper extends AbstractMapper...
   public void delete(DomainObject object) {
      Customer cust = (Customer) object;
      for (Iterator iterator = cust.getAddresses().iterator(); iterator.hasNext();) {
         Address add = (Address) iterator.next();
         MapperRegistry.getMapper(Address.class).delete(add);
      }
      super.delete(object);
      cust.getVersion().delete();
   }
```

### Implicit Lock Example: Pessimistic Offline Lock (Java)

Mapper interface and locking decorator:
```java
interface Mapper...
   public DomainObject find(Long id);
   public void insert(DomainObject obj);
   public void update(DomainObject obj);
   public void delete(DomainObject obj);

class LockingMapper implements Mapper...
   private Mapper impl;
   public LockingMapper(Mapper impl) {
      this.impl = impl;
   }
   public DomainObject find(Long id) {
      ExclusiveReadLockManager.INSTANCE.acquireLock(
         id, AppSessionManager.getSession().getId());
      return impl.find(id);
   }
   public void insert(DomainObject obj) {
      impl.insert(obj);
   }
   public void update(DomainObject obj) {
      impl.update(obj);
   }
   public void delete(DomainObject obj) {
      impl.delete(obj);
   }
```

Mapper registry wrapping mappers with locking:
```java
LockingMapperRegistry implements MappingRegistry...
   private Map mappers = new HashMap();
   public void registerMapper(Class cls, Mapper mapper) {
      mappers.put(cls, new LockingMapper(mapper));
   }
   public Mapper getMapper(Class cls) {
      return (Mapper) mappers.get(cls);
   }
```

## Chapter 17. Session State Patterns

No complete code examples or detailed diagrams appear in this chapter range. The text references HTML syntax conceptually (`&lt;INPUT type = "hidden"&gt;` for hidden fields) and SQL clause concepts (`sessionID is not NULL`, pending field Boolean `isPending field`) but these are discussed within prose descriptions of architectural patterns rather than as executable code snippets or working examples. The chapter focuses on design trade-offs and decision logic rather than implementation detail.

## Chapter 18. Base Patterns

Gateway to proprietary messaging service:

class MessageGateway...\
\
   protected static final String CONFIRM = "CNFRM";\
   private MessageSender sender;\
   public void sendConfirmation(String orderID, int amount, String symbol) {\
      Object[] args = new Object[]{orderID, new Integer(amount), symbol};\
      send(CONFIRM, args);\
   }\
   private void send(String msg, Object[] args) {\
      int returnCode = doSend(msg, args);\
      if (returnCode == MessageSender.NULL_PARAMETER)\
         throw new NullPointerException("Null Parameter passed for msg type: " + msg);\
      if (returnCode != MessageSender.SUCCESS)\
         throw new IllegalStateException("Unexpected error from messaging system #:" + returnCode);\
   }\
   protected int doSend(String msg, Object[] args) {\
      Assert.notNull(sender);\
      return sender.send(msg, args);\
   }

Gateway stub for testing:

class MessageGatewayStub...\
\
   protected int doSend(String messageType, Object[] args) {\
      int returnCode = isMessageValid(messageType, args);\
      if (returnCode == MessageSender.SUCCESS) messagesSent++;\
      return returnCode;\
   }\
   private int isMessageValid(String messageType, Object[] args) {\
      if (shouldFailAllMessages) return -999;\
      if (!legalMessageTypes().contains(messageType))\
         return MessageSender.UNKNOWN_MESSAGE_TYPE;\
      for (int i = 0; i < args.length; i++) {\
         Object arg = args[i];\
         if (arg == null) return MessageSender.NULL_PARAMETER;\
      }\
      return MessageSender.SUCCESS;\
   }

Layer Supertype example:

class DomainObject...\
\
   private Long ID;\
   public Long getID() { return ID; }\
   public void setID(Long ID) {\
      Assert.notNull("Cannot set a null ID", ID);\
      this.ID = ID;\
   }\
   public DomainObject(Long ID) { this.ID = ID; }\
   public DomainObject() { }

Registry singleton implementation:

class Registry...\
\
   private static Registry getInstance() { return soleInstance; }\
   private static Registry soleInstance = new Registry();\
   protected PersonFinder personFinder = new PersonFinder();\
   public static PersonFinder personFinder() {\
      return getInstance().personFinder;\
   }\
   public static void initialize() { soleInstance = new Registry(); }

Registry stub for testing:

class RegistryStub extends Registry...\
\
   public RegistryStub() {\
      personFinder = new PersonFinderStub();\
   }

Thread-safe Registry:

class ThreadLocalRegistry...\
\
   private static ThreadLocal instances = new ThreadLocal();\
   public static ThreadLocalRegistry getInstance() {\
      return (ThreadLocalRegistry) instances.get();\
   }\
   public static void begin() {\
      Assert.isTrue(instances.get() == null);\
      instances.set(new ThreadLocalRegistry());\
   }\
   public static void end() {\
      Assert.notNull(getInstance());\
      instances.set(null);\
   }

Money class with rounding-aware arithmetic:

class Money...\
\
   private long amount;\
   private Currency currency;\
   public Money(double amount, Currency currency) {\
      this.currency = currency;\
      this.amount = Math.round(amount * centFactor());\
   }\
   public boolean equals(Money other) {\
      return currency.equals(other.currency) && (amount == other.amount);\
   }\
   public Money add(Money other) {\
      assertSameCurrencyAs(other);\
      return newMoney(amount + other.amount);\
   }\
   public Money multiply(BigDecimal amount, int roundingMode) {\
      return new Money(amount().multiply(amount), currency, roundingMode);\
   }\
   public Money[] allocate(long[] ratios) {\
      long total = 0;\
      for (int i = 0; i < ratios.length; i++) total += ratios[i];\
      long remainder = amount;\
      Money[] results = new Money[ratios.length];\
      for (int i = 0; i < results.length; i++) {\
         results[i] = newMoney(amount * ratios[i] / total);\
         remainder -= results[i].amount;\
      }\
      for (int i = 0; i < remainder; i++) results[i].amount++;\
      return results;\
   }\
   public void testAllocate2() {\
      long[] allocation = {3,7};\
      Money[] result = Money.dollars(0.05).allocate(allocation);\
      assertEquals(Money.dollars(0.02), result[0]);\
      assertEquals(Money.dollars(0.03), result[1]);\
   }

Special Case (Null Object):

class NullEmployee : Employee, INull...\
\
   public override String Name {\
      get { return "Null Employee"; }\
      set { }\
   }\
   public override Decimal GrossToDate {\
      get { return 0m; }\
   }\
   public override Contract Contract {\
      get { return Contract.NULL; }\
   }

Plugin factory with configuration:

class PluginFactory...\
   private static Properties props = new Properties();\
\
   static {\
      try {\
         String propsFile = System.getProperty("plugins");\
         props.load(new FileInputStream(propsFile));\
      } catch (Exception ex) {\
         throw new ExceptionInInitializerError(ex);\
      }\
   }\
\
   public static Object getPlugin(Class iface) {\
      String implName = props.getProperty(iface.getName());\
      if (implName == null)\
         throw new RuntimeException("implementation not specified for " + iface.getName());\
      try {\
         return Class.forName(implName).newInstance();\
      } catch (Exception ex) {\
        throw new RuntimeException("factory unable to construct instance of " + iface.getName());\
      }\
   }

Configuration files:

config file test.properties...\
\
   # test configuration\
   IdGenerator=TestIdGenerator\
\
config file prod.properties...\
\
   # production configuration\
   IdGenerator=OracleIdGenerator

Service Stub for tax calculation:

class FlatRateTaxService implements TaxService...\
\
   private static final BigDecimal FLAT_RATE = new BigDecimal("0.0500");\
   public TaxInfo getSalesTaxInfo(String productCode, Address addr, Money saleAmount) {\
      return new TaxInfo(FLAT_RATE, saleAmount.multiply(FLAT_RATE));\
   }

Dynamic Service Stub with exemptions:

class TestTaxService implements TaxService...\
\
   private static Set exemptions = new HashSet();\
   public TaxInfo getSalesTaxInfo(String productCode, Address addr, Money saleAmount) {\
      BigDecimal rate = getRate(productCode, addr);\
      return new TaxInfo(rate, saleAmount.multiply(rate));\
   }\
   public static void addExemption(String productCode, String stateCode) {\
      exemptions.add(getExemptionKey(productCode, stateCode));\
   }\
   public static void reset() { exemptions.clear(); }

## References

No code examples, diagrams, or case study materials are present in this References chapter. The content consists entirely of bibliographic entries with evaluative annotations explaining the relevance and contribution of each work to enterprise application architecture and patterns discourse.
