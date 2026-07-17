# Clean Code: A Handbook of Agile Software Craftsmanship - Examples

## Índice de capítulos
- [Contents](#contents)
- [Foreword](#foreword)
- [Introduction](#introduction)
- [On the Cover](#on-the-cover)
- [1 Clean Code](#1-clean-code)
- [2 Meaningful Names](#2-meaningful-names)
- [3 Functions](#3-functions)
- [4 Comments](#4-comments)
- [5 Formatting](#5-formatting)
- [6 Objects and Data Structures](#6-objects-and-data-structures)
- [7 Error Handling](#7-error-handling)
- [8 Boundaries](#8-boundaries)
- [9 Unit Tests](#9-unit-tests)
- [10 Classes](#10-classes)
- [11 Systems](#11-systems)
- [12 Emergence](#12-emergence)
- [13 Concurrency](#13-concurrency)
- [14 Successive Refinement](#14-successive-refinement)
- [15 JUnit Internals](#15-junit-internals)
- [16 Refactoring `SerialDate`](#16-refactoring-serialdate)
- [17 Smells and Heuristics](#17-smells-and-heuristics)
- [Appendix A Concurrency II](#appendix-a-concurrency-ii)
- [Appendix B `org.jfree.date.SerialDate`](#appendix-b-orgjfreedateserialdate)
- [Appendix C Cross References of Heuristics](#appendix-c-cross-references-of-heuristics)
- [Epilogue](#epilogue)
- [Index](#index)

## <span class="calibre10"></span>**Contents**

No code examples in this chapter

## <span class="calibre10"></span>**Foreword**

No code examples in this chapter

## <span class="calibre10"></span>**Introduction**

No code examples in this chapter

## <span class="calibre10"></span>**On the Cover**

No code examples in this chapter

## <span class="calibre10"></span>**1 Clean Code**

No code examples in this chapter

## <span class="calibre10"></span>**2 Meaningful Names**

int elapsedTimeInDays;
int daysSinceCreation;
int daysSinceModification;
int fileAgeInDays;

public List<Cell> getFlaggedCells() {
  List<Cell> flaggedCells = new ArrayList<Cell>();
  for (Cell cell : gameBoard)
    if (cell.isFlagged())
      flaggedCells.add(cell);
  return flaggedCells;
}

class Customer {
  private Date generationTimestamp;
  private Date modificationTimestamp;
  private final String recordId = "102";
}

int realDaysPerIdealDay = 4;
const int WORK_DAYS_PER_WEEK = 5;
int sum = 0;
for (int j=0; j < NUMBER_OF_TASKS; j++) {
  int realTaskDays = taskEstimate[j] * realDaysPerIdealDay;
  int realTaskWeeks = (realTaskDays / WORK_DAYS_PER_WEEK);
  sum += realTaskWeeks;
}

public class Part {
  String description;
  void setDescription(String description) {
    this.description = description;
  }
}

Complex fulcrumPoint = Complex.FromRealNumber(23.0);

public class GuessStatisticsMessage {
  private String number;
  private String verb;
  private String pluralModifier;

  public String make(char candidate, int count) {
    createPluralDependentMessageParts(count);
    return String.format(
      "There %s %s %s%s",
      verb, number, candidate, pluralModifier );
  }

  private void createPluralDependentMessageParts(int count) {
    if (count == 0) {
      thereAreNoLetters();
    } else if (count == 1) {
      thereIsOneLetter();
    } else {
      thereAreManyLetters(count);
    }
  }

  private void thereAreManyLetters(int count) {
    number = Integer.toString(count);
    verb = "are";
    pluralModifier = "s";
  }

  private void thereIsOneLetter() {
    number = "1";
    verb = "is";
    pluralModifier = "";
  }

  private void thereAreNoLetters() {
    number = "no";
    verb = "are";
    pluralModifier = "s";
  }
}

## <span class="calibre10"></span>**3 Functions**

public static String renderPageWithSetupsAndTeardowns(
  PageData pageData, boolean isSuite) throws Exception {
  if (isTestPage(pageData))
    includeSetupAndTeardownPages(pageData, isSuite);
  return pageData.getHtml();
}

public abstract class Employee {
  public abstract boolean isPayday();
  public abstract Money calculatePay();
  public abstract void deliverPay(Money pay);
}

public class EmployeeFactoryImpl implements EmployeeFactory {
  public Employee makeEmployee(EmployeeRecord r) throws InvalidEmployeeType {
    switch (r.type) {
      case COMMISSIONED:
        return new CommissionedEmployee(r);
      case HOURLY:
        return new HourlyEmployee(r);
      case SALARIED:
        return new SalariedEmployee(r);
      default:
        throw new InvalidEmployeeType(r.type);
    }
  }
}

public boolean checkPassword(String userName, String password) {
  User user = UserGateway.findByName(userName);
  if (user != User.NULL) {
    String codedPhrase = user.getPhraseEncodedByPassword();
    String phrase = cryptographer.decrypt(codedPhrase, password);
    if ("Valid Password".equals(phrase)) {
      Session.initialize(); // Side effect!
      return true;
    }
  }
  return false;
}

if (attributeExists("username")) {
  setAttribute("username", "unclebob");
}

public void delete(Page page) {
  try {
    deletePageAndAllReferences(page);
  }
  catch (Exception e) {
    logError(e);
  }
}

private void deletePageAndAllReferences(Page page) throws Exception {
  deletePage(page);
  registry.deleteReference(page.name);
  configKeys.deleteKey(page.name.makeKey());
}

private void logError(Exception e) {
  logger.log(e.getMessage());
}

## <span id="Clean_Code_split_055.html_filepos268850" class="calibre10"></span>**4 Comments**

if (employee.isEligibleForFullBenefits())

// Copyright (C) 2003,2004,2005 by Object Mentor, Inc. All rights reserved.
// Released under the terms of the GNU General Public License version 2 or later.

// format matched kk:mm:ss EEE, MMM dd, yyyy
Pattern timeMatcher = Pattern.compile(
  "\\d*:\\d*:\\d* \\w*, \\w* \\d*, \\d*");

public int compareTo(Object o) {
  if(o instanceof WikiPagePath) {
    WikiPagePath p = (WikiPagePath) o;
    String compressedName = StringUtil.join(names, "");
    String compressedArgumentName = StringUtil.join(p.names, "");
    return compressedName.compareTo(compressedArgumentName);
  }
  return 1; // we are greater because we are the right type.
}

// SimpleDateFormat is not thread safe,
// so we need to create each instance independently.
SimpleDateFormat df = new SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss z");

//TODO-MdM these are not needed
// We expect this to go away when we do the checkout model
protected VersionInfo makeVersion() throws Exception {
  return null;
}

String listItemContent = match.group(3).trim();
// the trim is real important. It removes the starting
// spaces that could cause the item to be recognized
// as another list.
new ListItemWidget(this, listItemContent, this.level + 1);

private void startSending() {
  try {
    doSending();
  }
  catch(SocketException e) {
    // normal. someone stopped the request.
  }
  catch(Exception e) {
    addExceptionAndCloseResponse(e);
  }
}

private void addExceptionAndCloseResponse(Exception e) {
  try {
    response.add(ErrorResponder.makeExceptionString(e));
    response.closeAll();
  }
  catch(Exception e1) {
  }
}

public class PrimeGenerator {
  private static boolean[] crossedOut;
  private static int[] result;

  public static int[] generatePrimes(int maxValue) {
    if (maxValue < 2)
      return new int[0];
    else {
      uncrossIntegersUpTo(maxValue);
      crossOutMultiples();
      putUncrossedIntegersIntoResult();
      return result;
    }
  }

  private static void uncrossIntegersUpTo(int maxValue) {
    crossedOut = new boolean[maxValue + 1];
    for (int i = 2; i < crossedOut.length; i++)
      crossedOut[i] = false;
  }

  private static void crossOutMultiples() {
    int limit = determineIterationLimit();
    for (int i = 2; i <= limit; i++)
      if (notCrossed(i))
        crossOutMultiplesOf(i);
  }

  private static int determineIterationLimit() {
    // Every multiple in the array has a prime factor that
    // is less than or equal to the root of the array size,
    // so we don’t have to cross out multiples of numbers
    // larger than that root.
    double iterationLimit = Math.sqrt(crossedOut.length);
    return (int) iterationLimit;
  }

  private static void crossOutMultiplesOf(int i) {
    for (int multiple = 2*i; multiple < crossedOut.length; multiple += i)
      crossedOut[multiple] = true;
  }

  private static boolean notCrossed(int i) {
    return crossedOut[i] == false;
  }

  private static void putUncrossedIntegersIntoResult() {
    result = new int[numberOfUncrossedIntegers()];
    for (int j = 0, i = 2; i < crossedOut.length; i++)
      if (notCrossed(i))
        result[j++] = i;
  }

  private static int numberOfUncrossedIntegers() {
    int count = 0;
    for (int i = 2; i < crossedOut.length; i++)
      if (notCrossed(i))
        count++;
    return count;
  }
}

## <span class="calibre10"></span>**5 Formatting**

package fitnesse.wikitext.widgets;

import java.util.regex.*;

public class BoldWidget extends ParentWidget {
  public static final String REGEXP = "'''.+?'''";
  private static final Pattern pattern = Pattern.compile("'''(.+?)'''",
    Pattern.MULTILINE + Pattern.DOTALL
  );

  public BoldWidget(ParentWidget parent, String text) throws Exception {
    super(parent);
    Matcher match = pattern.matcher(text);
    match.find();
    addChildWidgets(match.group(1));
  }

  public String render() throws Exception {
    StringBuffer html = new StringBuffer("<b>");
    html.append(childHtml()).append("</b>");
    return html.toString();
  }
}

public class ReporterConfig {
  private String m_className;
  private List<Property> m_properties = new ArrayList<Property>();

  public void addProperty(Property property) {
    m_properties.add(property);
  }
}

public double getMeanLineWidth() {
  return (double)totalChars/lineCount;
}

public int getMedianLineWidth() {
  Integer[] sortedWidths = getSortedWidths();
  int cumulativeLineCount = 0;
  for (int width : sortedWidths) {
    cumulativeLineCount += lineCountForWidth(width);
    if (cumulativeLineCount > lineCount/2)
      return width;
  }
  throw new Error("Cannot get here");
}

public class CommentWidget extends TextWidget {
  public static final String REGEXP = "^#[^\r\n]*(?:(?:\r\n)|\n|\r)?";

  public CommentWidget(ParentWidget parent, String text) {
    super(parent, text);
  }

  public String render() throws Exception {
    return "";
  }
}

while (dis.read(buf, 0, readBufferSize) != -1)
{
  ;
}

## <span id="Clean_Code_split_067.html_filepos399052" class="calibre10"></span>**6 Objects and Data Structures**

public class Point {
  public double x;
  public double y;
}

public interface Point {
  double getX();
  double getY();
  void setCartesian(double x, double y);
  double getR();
  double getTheta();
  void setPolar(double r, double theta);
}

public interface Vehicle {
  double getPercentFuelRemaining();
}

public class Square implements Shape {
  private Point topLeft;
  private double side;

  public double area() {
    return side*side;
  }
}

// Train wreck violation of Law of Demeter
final String outputDir = ctxt.getOptions().getScratchDir().getAbsolutePath();

// Refactored to hide structure
BufferedOutputStream bos = ctxt.createScratchFileStream(classFileName);

public class Address {
  private String street;
  private String city;
  private String state;
  private String zip;

  public Address(String street, String city, String state, String zip) {
    this.street = street;
    this.city = city;
    this.state = state;
    this.zip = zip;
  }

  public String getStreet() { return street; }
  public String getCity() { return city; }
  public String getState() { return state; }
  public String getZip() { return zip; }
}

## <span id="Clean_Code_split_074.html_filepos427733" class="calibre10"></span>**7 Error Handling**

Listing 7-1: Cluttered code using return codes
```java
public class DeviceController {
  public void sendShutDown() {
    DeviceHandle handle = getHandle(DEV1);
    if (handle != DeviceHandle.INVALID) {
      retrieveDeviceDeviceRecord(handle);
      if (record.getStatus() != DEVICE_SUSPENDED) {
        pauseDevice(handle);
        clearDeviceWorkQueue(handle);
        closeDevice(handle);
      } else {
        logger.log("Device suspended. Unable to shut down");
      }
    } else {
      logger.log("Invalid handle for: " + DEV1.toString());
    }
  }
}
```

Listing 7-2: Clean code using exceptions
```java
public class DeviceController {
  public void sendShutDown() {
    try {
      tryToShutDown();
    } catch (DeviceShutDownError e) {
      logger.log(e);
    }
  }
  private void tryToShutDown() throws DeviceShutDownError {
    DeviceHandle handle = getHandle(DEV1);
    DeviceRecord record = retrieveDeviceRecord(handle);
    pauseDevice(handle);
    clearDeviceWorkQueue(handle);
    closeDevice(handle);
  }
  private DeviceHandle getHandle(DeviceID id) {
    throw new DeviceShutDownError("Invalid handle for: " + id.toString());
  }
}
```

Defining a transaction scope using try-catch first
```java
@Test(expected = StorageException.class)
public void retrieveSectionShouldThrowOnInvalidFileName() {
  sectionStore.retrieveSection("invalid - file");
}

public List<RecordedGrip> retrieveSection(String sectionName) {
  try {
    FileInputStream stream = new FileInputStream(sectionName);
    stream.close();
  } catch (FileNotFoundException e) {
    throw new StorageException("retrieval error", e);
  }
  return new ArrayList<RecordedGrip>();
}
```

Wrapping third-party API exceptions into a single common exception
```java
public class LocalPort {
  private ACMEPort innerPort;
  public LocalPort(int portNumber) {
    innerPort = new ACMEPort(portNumber);
  }
  public void open() {
    try {
      innerPort.open();
    } catch (DeviceResponseException e) {
      throw new PortDeviceFailure(e);
    } catch (ATM1212UnlockedException e) {
      throw new PortDeviceFailure(e);
    } catch (GMXError e) {
      throw new PortDeviceFailure(e);
    }
  }
}
```

Simplifying flow using Special Case Pattern
```java
// Cluttered flow:
try {
  MealExpenses expenses = expenseReportDAO.getMeals(employee.getID());
  m_total += expenses.getTotal();
} catch(MealExpensesNotFound e) {
  m_total += getMealPerDiem();
}

// Simplified flow using Special Case:
MealExpenses expenses = expenseReportDAO.getMeals(employee.getID());
m_total += expenses.getTotal();

public class PerDiemMealExpenses implements MealExpenses {
  public int getTotal() {
    // return the per diem default
  }
}
```

Avoiding null checks by returning empty collections and avoiding null arguments
```java
// Instead of returning null:
public List<Employee> getEmployees() {
  if (noEmployees) {
    return Collections.emptyList();
  }
}

// Assertions against null arguments:
public double xProjection(Point p1, Point p2) {
  assert p1 != null : "p1 should not be null";
  assert p2 != null : "p2 should not be null";
  return (p2.x - p1.x) * 1.5;
}
```

## <span class="calibre10"></span>**8 Boundaries**

Encapsulating boundary collection Map inside Sensors class
```java
// Harder to read and maintain, exposes map interface details to everyone:
Map<Sensor> sensors = new HashMap<Sensor>();
Sensor s = sensors.get(sensorId);

// Encapsulated boundary:
public class Sensors {
  private Map sensors = new HashMap();

  public Sensor getById(String id) {
    return (Sensor) sensors.get(id);
  }
}
```

Learning tests for log4j
```java
public class LogTest {
  private Logger logger;
  
  @Before
  public void initialize() {
    logger = Logger.getLogger("logger");
    logger.removeAllAppenders();
    Logger.getRootLogger().removeAllAppenders();
  }
  
  @Test
  public void basicLogger() {
    BasicConfigurator.configure();
    logger.info("basicLogger");
  }
  
  @Test
  public void addAppenderWithStream() {
    logger.addAppender(new ConsoleAppender(
        new PatternLayout("%p %t %m%n"),
        ConsoleAppender.SYSTEM_OUT));
    logger.info("addAppenderWithStream");
  }
  
  @Test
  public void addAppenderWithoutStream() {
    logger.addAppender(new ConsoleAppender(
        new PatternLayout("%p %t %m%n")));
    logger.info("addAppenderWithoutStream");
  }
}
```

## <span id="Clean_Code_split_093.html_filepos486974" class="calibre10"></span>**9 Unit Tests**

SerializedPageResponderTest - Refactored with Build-Operate-Check and Domain-Specific Testing Language
```java
public void testGetPageHierarchyAsXml() throws Exception {
  makePages("PageOne", "PageOne.ChildOne", "PageTwo");

  submitRequest("root", "type:pages");

  assertResponseIsXML();
  assertResponseContains(
    "<name>PageOne</name>", "<name>PageTwo</name>", "<name>ChildOne</name>"
  );
}

public void testSymbolicLinksAreNotInXmlPageHierarchy() throws Exception {
  WikiPage page = makePage("PageOne");
  makePages("PageOne.ChildOne", "PageTwo");

  addLinkTo(page, "PageTwo", "SymPage");

  submitRequest("root", "type:pages");

  assertResponseIsXML();
  assertResponseContains(
    "<name>PageOne</name>", "<name>PageTwo</name>", "<name>ChildOne</name>"
  );
  assertResponseDoesNotContain("SymPage");
}
```

Dual Standard: Testing State via Simple String Concatenation
```java
@Test
public void turnOnLoTempAlarmAtThreshold() throws Exception {
  wayTooCold();
  assertEquals("HBchL", hw.getState());
}

public String getState() {
  String state = "";
  state += heater ? "H" : "h";
  state += blower ? "B" : "b";
  state += cooler ? "C" : "c";
  state += hiTempAlarm ? "H" : "h";
  state += loTempAlarm ? "L" : "l";
  return state;
}
```

One Assert / One Concept per Test Split
```java
// Conceptually distinct tests:
public void testGetPageHierarchyAsXml() throws Exception {
    givenPages("PageOne", "PageOne.ChildOne", "PageTwo");
    whenRequestIsIssued("root", "type:pages");
    thenResponseShouldBeXML();
}
public void testGetPageHierarchyHasRightTags() throws Exception {
    givenPages("PageOne", "PageOne.ChildOne", "PageTwo");
    whenRequestIsIssued("root", "type:pages");
    thenResponseShouldContain(
      "<name>PageOne</name>", "<name>PageTwo</name>", "<name>ChildOne</name>"
    );
}
```

## <span class="calibre10"></span>**10 Classes**

Cohesive Stack implementation
```java
public class Stack {
  private int topOfStack = 0;
  List<Integer> elements = new LinkedList<Integer>();

  public int size() {
    return topOfStack;
  }

  public void push(int element) {
    topOfStack++;
    elements.add(element);
  }

  public int pop() throws PoppedWhenEmpty {
    if (topOfStack == 0)
      throw new PoppedWhenEmpty();
    int element = elements.get(--topOfStack);
    elements.remove(topOfStack);
    return element;
  }
}
```

Splitting Monolithic PrintPrimes into Cohesive Classes
```java
// Refactored entrypoint:
public class PrimePrinter {
  public static void main(String[] args) {
    final int NUMBER_OF_PRIMES = 1000;
    int[] primes = PrimeGenerator.generate(NUMBER_OF_PRIMES);
    
    final int ROWS_PER_PAGE = 50;
    final int COLUMNS_PER_PAGE = 4;
    RowColumnPagePrinter tablePrinter =
      new RowColumnPagePrinter(ROWS_PER_PAGE,
                               COLUMNS_PER_PAGE,
                               "The First " + NUMBER_OF_PRIMES + " Prime Numbers");
    tablePrinter.print(primes);
  }
}
```

Supporting OCP via Subclassing instead of Modifying class
```java
abstract public class Sql {
  public Sql(String table, Column[] columns)
  abstract public String generate();
}

public class CreateSql extends Sql {
  public CreateSql(String table, Column[] columns)
  @Override public String generate()
}

public class SelectSql extends Sql {
  public SelectSql(String table, Column[] columns)
  @Override public String generate()
}

public class InsertSql extends Sql {
  public InsertSql(String table, Column[] columns, Object[] fields)
  @Override public String generate()
  private String valuesList(Object[] fields, final Column[] columns)
}
```

Dependency Inversion (DIP) with StockExchange Interface
```java
public interface StockExchange {
  Money currentPrice(String symbol);
}

public class Portfolio {
  private StockExchange exchange;
  public Portfolio(StockExchange exchange) {
    this.exchange = exchange;
  }
}

public class PortfolioTest {
  private FixedStockExchangeStub exchange;
  private Portfolio portfolio;

  @Before
  protected void setUp() throws Exception {
    exchange = new FixedStockExchangeStub();
    exchange.fix("MSFT", 100);
    portfolio = new Portfolio(exchange);
  }

  @Test
  public void GivenFiveMSFTTotalShouldBe500() throws Exception {
    portfolio.add(5, "MSFT");
    Assert.assertEquals(500, portfolio.value());
  }
}
```

## <span class="calibre10"></span>**11 Systems**

EJB2 Entity Bean (Anti-pattern showing tight coupling to container)
```java
public interface BankLocal extends java.ejb.EJBLocalObject {
  String getStreetAddr1() throws EJBException;
  // ... getters/setters ...
  Collection getAccounts() throws EJBException;
  void addAccount(AccountDTO accountDTO) throws EJBException;
}

public abstract class Bank implements javax.ejb.EntityBean {
  public abstract String getStreetAddr1();
  // ... abstract getters/setters ...
  public void addAccount(AccountDTO accountDTO) {
    InitialContext context = new InitialContext();
    AccountHomeLocal accountHome = context.lookup("AccountHomeLocal");
    AccountLocal account = accountHome.create(accountDTO);
    Collection accounts = getAccounts();
    accounts.add(account);
  }
  // Heavy container lifecycle callbacks required:
  public abstract void setId(Integer id);
  public abstract Integer getId();
  public Integer ejbCreate(Integer id) { return null; }
  public void ejbPostCreate(Integer id) {}
  public void setEntityContext(EntityContext ctx) {}
  public void unsetEntityContext() {}
  public void ejbActivate() {}
  public void ejbPassivate() {}
  public void ejbLoad() {}
  public void ejbStore() {}
  public void ejbRemove() {}
}
```

JDK Dynamic Proxy for Aspect-like Behavior
```java
public interface Bank {
  Collection<Account> getAccounts();
  void setAccounts(Collection<Account> accounts);
}

public class BankImpl implements Bank {
  private List<Account> accounts;
  public Collection<Account> getAccounts() { return accounts; }
  public void setAccounts(Collection<Account> accounts) {
    this.accounts = new ArrayList<Account>(accounts);
  }
}

public class BankProxyHandler implements InvocationHandler {
  private Bank bank;
  public BankProxyHandler(Bank bank) {
    this.bank = bank;
  }
  public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
    String methodName = method.getName();
    if (methodName.equals("getAccounts")) {
      bank.setAccounts(getAccountsFromDatabase());
      return bank.getAccounts();
    } else if (methodName.equals("setAccounts")) {
      bank.setAccounts((Collection<Account>) args[0]);
      setAccountsToDatabase(bank.getAccounts());
      return null;
    } else {
      return method.invoke(bank, args);
    }
  }
}

// Usage:
Bank bank = (Bank) Proxy.newProxyInstance(
  Bank.class.getClassLoader(),
  new Class[] { Bank.class },
  new BankProxyHandler(new BankImpl()));
```

Spring XML Configuration for Dependency Injection Decorators
```xml
<beans>
  <bean id="appDataSource"
        class="org.apache.commons.dbcp.BasicDataSource"
        destroy-method="close"
        p:driverClassName="com.mysql.jdbc.Driver"
        p:url="jdbc:mysql://localhost:3306/mydb"
        p:username="me"/>
  <bean id="bankDataAccessObject"
        class="com.example.banking.persistence.BankDataAccessObject"
        p:dataSource-ref="appDataSource"/>
  <bean id="bank"
        class="com.example.banking.model.Bank"
        p:dataAccessObject-ref="bankDataAccessObject"/>
</beans>
```

EJB3 Entity Bean (Decoupled POJO using Annotations)
```java
@Entity
@Table(name = "BANKS")
public class Bank implements java.io.Serializable {
  @Id @GeneratedValue(strategy=GenerationType.AUTO)
  private int id;

  @Embeddable
  public class Address {
    protected String streetAddr1;
    protected String streetAddr2;
    protected String city;
    protected String state;
    protected String zipCode;
  }
  @Embedded
  private Address address;

  @OneToMany(cascade = CascadeType.ALL, fetch = FetchType.EAGER, mappedBy="bank")
  private Collection<Account> accounts = new ArrayList<Account>();

  public int getId() { return id; }
  public void setId(int id) { this.id = id; }
  public void addAccount(Account account) {
    account.setBank(this);
    accounts.add(account);
  }
  public Collection<Account> getAccounts() { return accounts; }
  public void setAccounts(Collection<Account> accounts) {
    this.accounts = accounts;
  }
}
```

## <span id="Clean_Code_split_119.html_filepos653075" class="calibre10"></span>**12 Emergence**

```java
// Example of removing implementation duplication
boolean isEmpty() {
   return 0 == size();
}

// Example of extracting a shared method to avoid duplication
public void scaleToOneDimension(float desiredDimension, float imageDimension) {
   if (Math.abs(desiredDimension - imageDimension) < errorThreshold)
      return;
   float scalingFactor = desiredDimension / imageDimension;
   scalingFactor = (float)(Math.floor(scalingFactor * 100) * 0.01f);
   replaceImage(ImageUtilities.getScaledImage(image, scalingFactor, scalingFactor));
}
public synchronized void rotate(int degrees) {
   replaceImage(ImageUtilities.getRotatedImage(image, degrees));
}
private void replaceImage(RenderedOp newImage) {
   image.dispose();
   System.gc();
   image = newImage;
}

// Example of the Template Method pattern to eliminate structural duplication
abstract public class VacationPolicy {
   public void accrueVacation() {
      calculateBaseVacationHours();
      alterForLegalMinimums();
      applyToPayroll();
   }
   private void calculateBaseVacationHours() { /* ... */ };
   abstract protected void alterForLegalMinimums();
   private void applyToPayroll() { /* ... */ };
}
public class USVacationPolicy extends VacationPolicy {
   @Override protected void alterForLegalMinimums() {
      // US specific logic
   }
}
public class EUVacationPolicy extends VacationPolicy {
   @Override protected void alterForLegalMinimums() {
      // EU specific logic
   }
}
```

## <span id="Clean_Code_split_128.html_filepos673001" class="calibre10"></span>**13 Concurrency**

```java
// Example of a class vulnerable to concurrency bugs
public class X {
   private int lastIdUsed;
   public int getNextId() {
       return ++lastIdUsed;
   }
}

// Example of hand-coded instrumentation to force threading failures during testing
public synchronized String nextUrlOrNull() {
    if(hasNext()) {
        String url = urlGenerator.next();
        Thread.yield(); // inserted for testing to force task swapping
        updateHasNext();
        return url;
    }
    return null;
}

// Example of automated jiggle point configuration for test environments
public class ThreadJigglePoint {
   public static void jiggle() {
       // In test: randomly chooses to yield, sleep, or do nothing
       // In production: does nothing
   }
}
```

## <span id="Clean_Code_split_140.html_filepos724195" class="calibre10"></span>**14 Successive Refinement**

```java
// Listing 14-1: Simple use of Args
public static void main(String[] args) {
  try {
    Args arg = new Args("l,p#,d*", args);
    boolean logging = arg.getBoolean('l');
    int port = arg.getInt('p');
    String directory = arg.getString('d');
    executeApplication(logging, port, directory);
  }  catch (ArgsException e) {
      System.out.printf("Argument error: %s\n", e.errorMessage());
  }
}

// Listing 14-3: ArgumentMarshaler interface
public interface ArgumentMarshaler {
  void set(Iterator<String> currentArgument) throws ArgsException;
}

// Listing 14-4: BooleanArgumentMarshaler implementation
public class BooleanArgumentMarshaler implements ArgumentMarshaler {
  private boolean booleanValue = false;
  
  public void set(Iterator<String> currentArgument) throws ArgsException {
    booleanValue = true;
  }

  public static boolean getValue(ArgumentMarshaler am) {
    if (am != null && am instanceof BooleanArgumentMarshaler)
      return ((BooleanArgumentMarshaler) am).booleanValue;
    else
      return false;
  }
}

// Listing 14-6: IntegerArgumentMarshaler implementation
public class IntegerArgumentMarshaler implements ArgumentMarshaler {
  private int intValue = 0;
 
  public void set(Iterator<String> currentArgument) throws ArgsException {
    String parameter = null;
    try {
      parameter = currentArgument.next();
      intValue = Integer.parseInt(parameter);
    } catch (NoSuchElementException e) {
      throw new ArgsException(MISSING_INTEGER);
    } catch (NumberFormatException e) {
      throw new ArgsException(INVALID_INTEGER, parameter);
    }
  }
 
  public static int getValue(ArgumentMarshaler am) {
    if (am != null && am instanceof IntegerArgumentMarshaler)
      return ((IntegerArgumentMarshaler) am).intValue;
    else
      return 0;
  }
}
```

## <span class="calibre10"></span>**15 JUnit Internals**

```java
// Listing 15-2: Original ComparisonCompactor.java
public class ComparisonCompactor {
  private static final String ELLIPSIS = "...";
  private static final String DELTA_END = "]";
  private static final String DELTA_START = "[";
  private int fContextLength;
  private String fExpected;
  private String fActual;
  private int fPrefix;
  private int fSuffix;

  public ComparisonCompactor(int contextLength, String expected, String actual) {
    fContextLength = contextLength;
    fExpected = expected;
    fActual = actual;
  }

  public String compact(String message) {
    if (fExpected == null || fActual == null || areStringsEqual())
      return Assert.format(message, fExpected, fActual);
    findCommonPrefix();
    findCommonSuffix();
    String expected = compactString(fExpected);
    String actual = compactString(fActual);
    return Assert.format(message, expected, actual);
  }

  private String compactString(String source) {
    String result = DELTA_START + source.substring(fPrefix, source.length() - fSuffix + 1) + DELTA_END;
    if (fPrefix > 0)
      result = computeCommonPrefix() + result;
    if (fSuffix > 0)
      result = result + computeCommonSuffix();
    return result;
  }

  private void findCommonPrefix() {
    fPrefix = 0;
    int end = Math.min(fExpected.length(), fActual.length());
    for (; fPrefix < end; fPrefix++) {
      if (fExpected.charAt(fPrefix) != fActual.charAt(fPrefix))
        break;
    }
  }

  private void findCommonSuffix() {
    int expectedSuffix = fExpected.length() - 1;
    int actualSuffix = fActual.length() - 1;
    for (; actualSuffix >= fPrefix && expectedSuffix >= fPrefix; actualSuffix--, expectedSuffix--) {
      if (fExpected.charAt(expectedSuffix) != fActual.charAt(actualSuffix))
        break;
    }
    fSuffix = fExpected.length() - expectedSuffix;
  }

  private String computeCommonPrefix() {
    return (fPrefix > fContextLength ? ELLIPSIS : "") + fExpected.substring(Math.max(0, fPrefix - fContextLength), fPrefix);
  }

  private String computeCommonSuffix() {
    int end = Math.min(fExpected.length() - fSuffix + 1 + fContextLength, fExpected.length());
    return fExpected.substring(fExpected.length() - fSuffix + 1, end) + (fExpected.length() - fSuffix + 1 < fExpected.length() - fContextLength ? ELLIPSIS : "");
  }

  private boolean areStringsEqual() {
    return fExpected.equals(fActual);
  }
}
```

## <span id="Clean_Code_split_149.html_filepos992872" class="calibre10"></span>**16 Refactoring <span class="calibre44">`SerialDate`</span>**

```java
// Example of refactored Day enum replacing static constants
public enum Day {
  MONDAY(Calendar.MONDAY),
  TUESDAY(Calendar.TUESDAY),
  WEDNESDAY(Calendar.WEDNESDAY),
  THURSDAY(Calendar.THURSDAY),
  FRIDAY(Calendar.FRIDAY),
  SATURDAY(Calendar.SATURDAY),
  SUNDAY(Calendar.SUNDAY);

  public final int index;
  private static DateFormatSymbols dateSymbols = new DateFormatSymbols();

  Day(int day) { 
    index = day; 
  }

  public static Day make(int index) throws IllegalArgumentException {
    for (Day d : Day.values())
      if (d.index == index)
        return d;
    throw new IllegalArgumentException(String.format("Illegal day index: %d.", index));
  }

  public static Day parse(String s) throws IllegalArgumentException {
    String[] shortWeekdayNames = dateSymbols.getShortWeekdays();
    String[] weekDayNames = dateSymbols.getWeekdays();
    s = s.trim();
    for (Day day : Day.values()) {
      if (s.equalsIgnoreCase(shortWeekdayNames[day.index]) || s.equalsIgnoreCase(weekDayNames[day.index])) {
        return day;
      }
    }
    throw new IllegalArgumentException(String.format("%s is not a valid weekday string", s));
  }

  public String toString() {
    return dateSymbols.getWeekdays()[index];
  }
}
```

## <span id="Clean_Code_split_154.html_filepos1065522" class="calibre10"></span>**17 Smells and Heuristics**

// Example G14: Feature Envy
public class HourlyPayCalculator {
  public Money calculateWeeklyPay(HourlyEmployee e) {
    int tenthRate = e.getTenthRate().getPennies();
    int tenthsWorked = e.getTenthsWorked();
    int straightTime = Math.min(400, tenthsWorked);
    int overTime = Math.max(0, tenthsWorked - straightTime);
    int straightPay = straightTime * tenthRate;
    int overtimePay = (int)Math.round(overTime * tenthRate * 1.5);
    return new Money(straightPay + overtimePay);
  }
}

// Example G15: Eliminating Selector Arguments
public int straightPay() {
  return getTenthsWorked() * getTenthRate();
}
public int overTimePay() {
  int overTimeTenths = Math.max(0, getTenthsWorked() - 400);
  int overTimePay = overTimeBonus(overTimeTenths);
  return straightPay() + overTimePay;
}
private int overTimeBonus(int overTimeTenths) {
  double bonus = 0.5 * getTenthRate() * overTimeTenths;
  return (int) Math.round(bonus);
}

// Example G22: Physicalizing a Logical Dependency
public class HourlyReporter {
  private HourlyReportFormatter formatter;
  private List<LineItem> page;
  public void generateReport(List<HourlyEmployee> employees) {
    for (HourlyEmployee e : employees) {
      addLineItemToPage(e);
      if (page.size() == formatter.getMaxPageSize())
        printAndClearItemList();
    } 
  }
}

// Example G31: Bucket Brigade for Temporal Coupling
public void dive(String reason) {
  Gradient gradient = saturateGradient();
  List<Spline> splines = reticulateSplines(gradient);
  diveForMoog(splines, reason);
}

## <span id="Clean_Code_split_164.html_filepos1177713" class="calibre10"></span>**Appendix A Concurrency II**

// Thread-safe executor scheduling utilizing a thread pool
public class ExecutorClientScheduler implements ClientScheduler {
  Executor executor;
  public ExecutorClientScheduler(int availableThreads) {
    executor = Executors.newFixedThreadPool(availableThreads);
  }
  public void schedule(final ClientRequestProcessor requestProcessor) {
    Runnable runnable = new Runnable() {
      public void run() {
        requestProcessor.process();
      } 
    };
    executor.execute(runnable);
  }
}

// Thread-safe nonblocking counter using AtomicInteger
public class ObjectWithValue {
  private AtomicInteger value = new AtomicInteger(0);
  public void incrementValue() {
    value.incrementAndGet();
  }
  public int getValue() {
    return value.get();
  }
}

// Server-based locking for compound operations
public class ThreadSafeIntegerIterator {
  private IntegerIterator iterator = new IntegerIterator();
  public synchronized Integer getNextOrNull() {
    if (iterator.hasNext())
      return iterator.next();
    return null;
  }
}

## <span id="Clean_Code_split_175.html_filepos1286721" class="calibre10"></span>**Appendix B <span class="calibre44">`org.jfree.date.SerialDate`</span>**

No code examples in this chapter

## <span id="Clean_Code_split_176.html_filepos1300237" class="calibre10"></span>**Appendix C Cross References of Heuristics**

No code examples in this chapter

## <span class="calibre10"></span>**Epilogue**

No code examples in this chapter

## <span class="calibre10"></span>**Index**

No code examples in this chapter
