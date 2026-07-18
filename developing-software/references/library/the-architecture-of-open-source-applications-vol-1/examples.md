# The Architecture of Open Source Applications, Vol. 1

## Índice de capítulos
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Chapter 1. Asterisk](#chapter-1-asterisk)
- [Chapter 2. Audacity](#chapter-2-audacity)
- [Chapter 3. The Bourne-Again Shell](#chapter-3-the-bourne-again-shell)
- [Chapter 4. Berkeley DB](#chapter-4-berkeley-db)
- [Chapter 5. CMake](#chapter-5-cmake)
- [Chapter 6. Continuous Integration](#chapter-6-continuous-integration)
- [Chapter 7. Eclipse](#chapter-7-eclipse)
- [Chapter 8. Graphite](#chapter-8-graphite)
- [Chapter 9. The Hadoop Distributed File System](#chapter-9-the-hadoop-distributed-file-system)
- [Chapter 10. Jitsi](#chapter-10-jitsi)
- [Chapter 11. LLVM](#chapter-11-llvm)
- [Chapter 12. Mercurial](#chapter-12-mercurial)
- [Chapter 13. The NoSQL Ecosystem](#chapter-13-the-nosql-ecosystem)
- [Chapter 14. Python Packaging](#chapter-14-python-packaging)
- [Chapter 15. Riak and Erlang/OTP](#chapter-15-riak-and-erlangotp)
- [Chapter 16. Selenium WebDriver](#chapter-16-selenium-webdriver)
- [Chapter 17. Sendmail](#chapter-17-sendmail)
- [Chapter 18. SnowFlock](#chapter-18-snowflock)
- [Chapter 19. SocialCalc](#chapter-19-socialcalc)
- [Chapter 20. Telepathy](#chapter-20-telepathy)
- [Chapter 21. Thousand Parsec](#chapter-21-thousand-parsec)
- [Chapter 22. Violet](#chapter-22-violet)
- [Chapter 23. VisTrails](#chapter-23-vistrails)
- [Chapter 24. VTK](#chapter-24-vtk)
- [Chapter 25. Battle For Wesnoth](#chapter-25-battle-for-wesnoth)
- [Bibliography](#bibliography)

## Table of Contents

No code, diagrams, or concrete technical examples. The range contains only structural markup: HTML links with chapter titles like `<a href="#dummy_split_007.html_filepos28455" class="calibre4">Chapter 1. Asterisk</a>` and container divs for page breaks, typical of generated EPUB/HTML table of contents structure.

## Introduction

No code examples or architecture diagrams are present in this introduction. The content is purely expository prose establishing the book's conceptual framework and purpose.

## Chapter 1. Asterisk

Dialplan syntax example for handling extension 1234:
```
; Define the rules for what happens when someone dials 1234.
;
exten => 1234,1,Answer()
    same => n,Playback(demo-congrats)
    same => n,Hangup()
```

Example handling inbound digit collection and playback:
```
exten => 5678,1,Answer()
    same => n,Read(DIGITS,beep,4)
    same => n,SayDigits(${DIGITS})
    same => n,Hangup()
```

Application function prototype:
```c
int (*execute)(struct ast_channel *chan, const char *args);
```

Dialplan variable assignment and retrieval:
```
exten => 1234,1,Set(MY_VARIABLE=foo)
    same => n,Verbose(MY_VARIABLE is ${MY_VARIABLE})
```

Accessing CallerID through dialplan function:
```
exten => 1234,1,Verbose(The current CallerID is ${CALLERID(num)})
    same => n,Set(CALLERID(num)=<256>555-1212)
```

CDR (Call Detail Records) access:
```
exten => 555,1,Verbose(Time this call started: ${CDR(start)})
    same => n,Set(CDR(mycustomfield)=snickerdoodle)
```

Voicemail access example:
```
exten => *123,1,Answer()
    same => n,VoicemailMain()
```

Bridged call setup example:
```
exten => 1234,1,Dial(SIP/bob)
```

Architecture diagrams described: Figure 1.1 illustrates a single channel representing one call leg. Figure 1.2 shows two channels for a phone-to-phone call. Figure 1.3 demonstrates native bridging on specialized hardware. Figure 1.4 expands bridged channels to show how channel technology implementations fit with the abstract channel layer. Figure 1.5 shows the call setup sequence when a call arrives. Figure 1.6 depicts the VoicemailMain application execution flow. Figures 1.7 and 1.8 detail the generic bridge block diagram and frame processing sequence during bridging.

## Chapter 2. Audacity

ShuttleGui example showing dialog construction and data shuttling:
```
ShuttleGui S; // GUI Structure
S.StartStatic("Some Title",…);
{
  S.AddButton("Some Button",…);
  S.TieCheckbox("Some Checkbox",…);
}
S.EndStatic();
```
The paired `StartStatic`/`EndStatic` calls define a containing box; curly brackets and indentation (not required for correctness) make the structure obvious. The same code simultaneously builds the dialog, transfers data from disk preferences to the displayed GUI, and transfers back—replacing the previously necessary four separate flows: preferences→intermediate variables, intermediate variables→GUI display, GUI display→intermediate variables, intermediate variables→preferences.

GetLink architectural anti-pattern: Audacity has no abstraction for channel count. Instead it uses `GetLink()` to return the other channel in a stereo pair or NULL for mono. Code resembles mono implementations retrofitted with `(GetLink() != NULL)` tests rather than general code iterating through n channels. Around 100 calls to `GetLink` across at least 26 files would need changes to support surround sound. With hindsight, making `GetLink` private and providing an iterator would have avoided special-case stereo code and made the channel list implementation agnostic. This illustrates how small architectural defects spread widely if allowed.

BlockFile merging/splitting (from Figure 2.5 description): Before deletion, `.aup` file and BlockFiles hold sequence ABCDEFGHIJKLMNO. After deletion of FGHI, two BlockFiles are merged, reducing disk fragmentation and the need for garbage collection.

Figure 2.1 (Layers in Audacity): Shows three layers—wxWidgets (wxString, wxFiles, sizers) reflected and extended in Audacity (ShuttleGui, BlockFiles, command handling). Below is a narrow "Platform Specific Implementation Layers" strip (OS abstraction in wxWidgets and PortAudio). "Other Supporting Libraries" includes dynamically loaded modules that know nothing of wxWidgets. Figure 2.3 (Audacity Interface): Labels custom components—track information panels, time ruler, amplitude rulers, waveform/spectrum/label tracks—all custom drawn within a single wxWidget, not individual wxWidget components. Figure 2.4 (Threads and Buffers): Shows the PortAudio audio thread calling `audacityAudioCallback`, the AudioIO thread filling capture/playback buffers from disk, and the GUI thread with periodic timer updating the display.

## Chapter 3. The Bourne-Again Shell

WORD_DESC structure:
```
typedef struct word_desc {
  char *word;           /* Zero terminated string. */
  int flags;            /* Flags associated with this word. */
} WORD_DESC;
```

WORD_LIST structure:
```
typedef struct word_list {
  struct word_list *next;
  WORD_DESC *word;
} WORD_LIST;
```

Command demonstrating context-sensitive parsing (the word "for" functions as reserved word, variable name in assignment, and loop target):
```
for for in for; do for=for; done; echo $for
```
Output: for

Brace expansion example:
Input: pre{one,two,three}post
Output: preonepost pretwopost prethreepost

## Chapter 4. Berkeley DB

Lock Conflict Matrix (Table 4.2): A 9x9 matrix indexed by [requester][holder] defining conflicts between lock modes: No-Lock, Read, Write, Wait, iWrite (intention-write), iRead (intention-read), iRW (intention-read-write), uRead (update read), and iwasWrite (intention-was-write). Read-Write conflicts shown with checkmarks; for example, a Read lock held conflicts with Write, iWrite, iRW, and wasWrite requesters, while Write locks conflict with all others. This matrix is pluggable; Berkeley DB configures alternative matrices to support concurrent data store mode (locking without full transactions) via the lock_vec interface.

Recovery Algorithm Pseudocode (Section 4.9.2):
```
ckp_record = read(cached_ckp_lsn)
ckp_lsn = ckp_record.checkpoint_lsn
cur_lsn = ckp_record.my_lsn
while (cur_lsn > ckp_lsn) {
    ckp_record = read(ckp_record.prev_ckp)
    cur_lsn = ckp_record.my_lsn
}
```
This loop locates the checkpoint record preceding the checkpoint LSN to reconstruct file mappings at the correct recovery point.

API Layering Pattern: Cursor put operation decomposed into three tiers: __dbc_put_pp (public interface, performs thread tracking and replication state checking), __dbc_put_arg (API-specific error checking: flag validation, parameter verification, option combination validation), and __dbc_put (worker function performing the actual operation, reused by internal operations like table joins).

Mpool File Abstraction (DB_MPOOLFILE): get() and put() methods on file handles; get() ensures a page is cached, acquires a pin, returns a pointer; put() unpins for eviction. Extended to distinguish read-pinning from write-pinning to support multi-version concurrency control: pages pinned for reading can be written to disk if dirty, while pages pinned for writing cannot because they may be inconsistent. Methods set_lsn_offset and set_clearlen allow non-Berkeley-DB clients to configure page format expectations without mandating Berkeley DB's page layout.

Lock Object Structure (DB_LOCK_ILOCK): Contains three fields—fileid (unique 32-bit database identifier assigned at creation), page number, and lock type (DB_PAGE_LOCK for page locks, DB_HANDLE_LOCK for database handles, DB_RECORD_LOCK for queue record-level locking, DB_DATABASE_LOCK for entire-database locking)—allowing the lock manager to identify what resource is locked without enforcing Berkeley DB semantics.

Database Identifiers: Each database is assigned a unique 32-bit fileid at creation time, written to the database metadata page, and reused throughout Mpool, locking, and logging subsystems to enable efficient cross-subsystem reference without transmitting full filenames in log records.

## Chapter 5. CMake

Code example from cmUnsetCommand class showing how CMake commands implement both executable logic and documentation:

```
virtual const char* GetTerseDocumentation()
{
    return "Unset a variable, cache variable, or environment variable.";
}

virtual const char* GetFullDocumentation()
{
    return
      "  unset(<variable> [CACHE])\n"
      "Removes the specified variable causing it to become undefined.  "
      "If CACHE is present then the variable is removed from the cache "
      "instead of the current scope.\n"
      "<variable> can be an environment variable such as:\n"
      "  unset(ENV{LD_LIBRARY_PATH})\n"
      "in which case the variable will be removed from the current "
      "environment.";
}
```

System introspection code contrast: Instead of brittle platform-specific checks like `#ifdef linux`, CMake enables feature-based programming: `#ifdef HAS_FEATURE` (then do something with the feature). This allows code to adapt to compiler capabilities rather than specific OS versions, preserving portability as compilers and operating systems evolve.

Figure 5.1 "Overview of the CMake Process" shows the data flow: CMakeCache.txt and CMakeLists.txt feed into the configure step, producing an in-memory representation of targets; the generate step then converts this representation into either IDE project files (Visual Studio, Xcode) or Makefiles for the target platform.

Figure 5.2 "CMake Objects" depicts the object hierarchy: cmMakefile objects are instantiated for each directory in the source tree, each containing maps of cmTarget objects. cmCommand is the base class for all language commands, and the lex/yacc-based parser converts CMake syntax into command invocations with string arguments.

## Chapter 6. Continuous Integration

A basic CI system can be implemented as a simple seven-line UNIX script that checks out source code from version control, builds it, runs tests, and notifies on failure via email:

```
cd /tmp && \
svn checkout http://some.project.url && \
cd project_directory && \
python setup.py build && \
python setup.py test || \
echo build failed | sendmail notification@project.domain
cd /tmp && rm -fr project_directory
```

Figure 6.1 (Internals of a Continuous Integration System) shows discrete subsystems including checkout, build, test, and reporting components. Arrows represent information flow. A cloud symbol represents potential remote execution. Shaded rectangles indicate coupling points such as build monitoring including process monitoring and system health metrics (CPU load, I/O load, memory usage).

Figure 6.2 illustrates Buildbot's master/slave topology with a central buildmaster connected to multiple buildslaves. Scheduling and control flow from master to slaves; build output streams back to master.

Figure 6.3 shows CDash's reporting architecture where independent client machines run builds and submit XML-formatted results to a central CDash server, which aggregates and presents information.

Figure 6.4 depicts Pony-Build's three-component model: independent clients containing configuration, coupled with a lightweight library; a results server as centralized database; and an optional reporting server with Web interface. Components communicate via webhooks and RPC mechanisms rather than persistent connections. The reporting server interfaces with external systems for VCS change notification redirection and PubSubHubbub-based notification distribution.

## Chapter 7. Eclipse

Plugin manifest example showing dependencies and exports:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<plugin
   id="org.eclipse.ui"
   name="%Plugin.name"
   version="2.1.1"
   provider-name="%Plugin.providerName"
   class="org.eclipse.ui.internal.UIPlugin">
   <runtime>
      <library name="ui.jar">
         <export name="*"/>
         <packages prefixes="org.eclipse.ui"/>
      </library>
   </runtime>
   <requires>
      <import plugin="org.apache.xerces"/>
      <import plugin="org.eclipse.core.resources"/>
      <import plugin="org.eclipse.update.core"/>
      <import plugin="org.eclipse.text" export="true"/>
      <import plugin="org.eclipse.ui.workbench.texteditor" export="true"/>
      <import plugin="org.eclipse.ui.editors" export="true"/>
   </requires>
</plugin>
```

Extension point contribution example (action set):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<plugin id="com.example.helloworld" name="com.example.helloworld" version="1.0.0">
   <runtime>
      <library name="helloworld.jar"/>
   </runtime>
   <requires>
      <import plugin="org.eclipse.ui"/>
   </requires>
   <extension point="org.eclipse.ui.actionSets">
      <actionSet label="Example Action Set" visible="true" id="org.eclipse.helloworld.actionSet">
         <menu label="Example &Menu" id="exampleMenu">
            <separator name="exampleGroup"></separator>
         </menu>
         <action label="&Example Action" icon="icons/example.gif" tooltip="Hello, Eclipse world" class="com.example.helloworld.actions.ExampleAction" menubarPath="exampleMenu/exampleGroup" toolbarPath="exampleGroup" id="org.eclipse.helloworld.actions.ExampleAction"></action>
      </actionSet>
   </extension>
</plugin>
```

Action implementation:
```java
package com.example.helloworld.actions;
import org.eclipse.jface.action.IAction;
import org.eclipse.jface.viewers.ISelection;
import org.eclipse.ui.IWorkbenchWindow;
import org.eclipse.ui.IWorkbenchWindowActionDelegate;
import org.eclipse.jface.dialogs.MessageDialog;

public class ExampleAction implements IWorkbenchWindowActionDelegate {
    private IWorkbenchWindow window;
    
    public ExampleAction() {}
    
    public void run(IAction action) {
        MessageDialog.openInformation(
            window.getShell(),
            "org.eclipse.helloworld",
            "Hello, Eclipse architecture world");
    }
    
    public void selectionChanged(IAction action, ISelection selection) {}
    public void dispose() {}
    public void init(IWorkbenchWindow window) { this.window = window; }
}
```

OSGi 3.0 bundle manifest (META-INF/MANIFEST.MF):
```
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-Name: %Plugin.name
Bundle-SymbolicName: org.eclipse.ui; singleton:=true
Bundle-Version: 3.3.0.qualifier
Bundle-ClassPath: .
Bundle-Activator: org.eclipse.ui.internal.UIPlugin
Bundle-Vendor: %Plugin.providerName
Bundle-Localization: plugin
Export-Package: org.eclipse.ui.internal;x-internal:=true
Require-Bundle: org.eclipse.core.runtime;bundle-version="[3.2.0,4.0.0)",
 org.eclipse.swt;bundle-version="[3.3.0,4.0.0)";visibility:=reexport,
 org.eclipse.jface;bundle-version="[3.3.0,4.0.0)";visibility:=reexport,
 org.eclipse.ui.workbench;bundle-version="[3.3.0,4.0.0)";visibility:=reexport,
 org.eclipse.core.expressions;bundle-version="[3.3.0,4.0.0)"
Eclipse-LazyStart: true
Bundle-RequiredExecutionEnvironment: CDC-1.0/Foundation-1.0, J2SE-1.3
```

Feature file (feature.xml) showing bundles and platform filters:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<feature
      id="org.eclipse.rcp"
      label="%featureName"
      version="3.7.0.qualifier"
      provider-name="%providerName"
      plugin="org.eclipse.rcp"
      image="eclipse_update_120.jpg">
   <description>%description</description>
   <copyright>%copyright</copyright>
   <license url="%licenseURL">%license</license>
   <plugin id="org.eclipse.equinox.launcher" download-size="0" install-size="0" version="0.0.0" unpack="false"/>
   <plugin id="org.eclipse.equinox.launcher.gtk.linux.x86_64" os="linux" ws="gtk" arch="x86_64" download-size="0" install-size="0" version="0.0.0" fragment="true"/>
</feature>
```

Eclipse 4.0 dependency injection example:
```java
@Inject
IStatusLineManager statusLine;
statusLine.setMessage(msg);
```

Help system extension point (org.eclipse.help.toc):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?eclipse version="3.0"?>
<plugin>
   <extension point="org.eclipse.help.toc">
      <toc file="toc.xml" primary="true"></toc>
      <index path="index"/>
   </extension>
   <extension point="org.eclipse.help.toc">
      <toc file="topics_Guide.xml"></toc>
      <toc file="topics_Reference.xml"></toc>
      <toc file="topics_Porting.xml"></toc>
      <toc file="topics_Questions.xml"></toc>
      <toc file="topics_Samples.xml"></toc>
   </extension>
</plugin>
```

Eclipse application extension (org.eclipse.core.runtime.applications):
```xml
<plugin>
    <extension id="org.eclipse.ui.ide.workbench" point="org.eclipse.core.runtime.applications">
      <application>
         <run class="org.eclipse.ui.internal.ide.application.IDEApplication"></run>
      </application>
    </extension>
</plugin>
```

## Chapter 8. Graphite

Data transmission format to carbon:
```
servers.www01.cpuUsage 42 1286269200
products.snake-oil.salesPerMinute 123 1286269200
[one minute passes]
servers.www01.cpuUsageUser 44 1286269260
products.snake-oil.salesPerMinute 119 1286269260
```

Graph rendering URL examples:
```
http://graphite.example.com/render?target=servers.www01.cpuUsage&width=500&height=300&from=-24h
target=movingAverage(servers.www01.cpuUsage,10)
target=integral(sumSeries(products.*.salesPerMinute))&from=midnight
```

Dashboard creation as simple HTML with image tags:
```html
<img src="http://graphite.example.com/render?parameters-for-my-awesome-graph">
```

Whisper file structure: a header section with metadata, followed by archive sections containing consecutive (timestamp, value) pairs stored contiguously on disk. The chapter describes but does not provide source code examples. Figure 8.1 illustrates basic whisper file anatomy (header + archive sections); Figure 8.2 shows data flow (clients → carbon → whisper, with data accessible to webapp); Figure 8.4 illustrates carbon's queueing mechanism (incoming data points mapped to per-metric queues, background thread batching writes via update_many).

## Chapter 9. The Hadoop Distributed File System

Figure 9.1 (HDFS Client Creates a New File) shows the interaction loop: the client queries the NameNode for DataNode list sorted by network topology distance, receives a list of replica locations, then contacts the closest DataNode directly to request block transfer. For writes, the client asks the NameNode to choose DataNodes for the first block replica, organizes a node-to-node pipeline, sends data packets, and requests new DataNode choices for subsequent blocks.

Figure 9.2 (Data Pipeline While Writing a Block) illustrates a 3-stage timeline for a pipeline of three DataNodes (DN1, DN2, DN3) writing five data packets: (1) Pipeline setup (t0–t1): control messages establish the pipeline; (2) Data streaming (t1–t2): packets flow from client to DN1 to DN2 to DN3, with acknowledgments (dashed lines) returning in reverse; intermediate packets can be sent before acknowledgments arrive; an hflush operation carries with packet 2 and is not a separate RPC; (3) Pipeline close (t2–t3): control messages finalize the block. The batching optimization in NameNode journal writes reduces contention: when one thread initiates flush-and-sync, all simultaneously batched transactions commit together; other threads only verify their transactions were saved without initiating their own flush-and-sync.

Figure 9.3 (Cluster Topology) depicts a two-rack cluster where each rack contains three nodes sharing a switch, and both rack switches connect to core switches. Distance calculation: two nodes in the same rack have distance 2 (node → rack switch → node); two nodes in different racks have distance 4 or more (node → rack switch → core switch → rack switch → node). The block placement policy places the first replica on the writer's node, the second and third replicas on two different nodes in a different rack, and remaining replicas on random nodes such that no node hosts more than one replica and no rack hosts more than two replicas if possible.

Concrete operational scale: A 4000-node Yahoo! cluster has ~65 million files, ~80 million blocks, and each DataNode hosts ~60,000 block replicas. Per-day creation: 2 million new files. Hardware: dual quad-core Xeon 2.5 GHz, 4–12 SATA drives (2 TB each), 24 GB RAM, 1 Gbps Ethernet; 40 nodes per rack share one switch. Total cluster storage: 11 PB (3.7 PB usable at 3x replication). Re-replication latency: ~2 minutes for 60,000 blocks after a node failure. Failure rates: 0.8% of nodes fail per month; expected annual block-loss probability <0.005 (less than one in 200,000). Correlated failures: rack or core switch failures; power-loss events typically result in a handful of corrupted blocks per restart.

## Chapter 10. Jitsi

Bundle manifest for ConfigurationService:
```
Bundle-Activator: net.java.sip.communicator.impl.configuration.ConfigActivator
Bundle-Name: Configuration Service Implementation
Bundle-Description: A bundle that offers configuration utilities
Bundle-Vendor: jitsi.org
Bundle-Version: 0.0.1
System-Bundle: yes
Import-Package: org.osgi.framework
Export-Package: net.java.sip.communicator.service.configuration
```

ConfigurationService interface and implementation:
```
public interface ConfigurationService {
  public void setProperty(String propertyName, Object property);
  public Object getProperty(String propertyName);
}

public class ConfigurationServiceImpl implements ConfigurationService {
  private final Properties properties = new Properties();
  public Object getProperty(String name) {
    return properties.get(name);
  }
  public void setProperty(String name, Object value) {
    properties.setProperty(name, value.toString());
  }
}
```

Bundle activator registering the service:
```
public class ConfigActivator implements BundleActivator {
  public void start(BundleContext bc) throws Exception {
    bc.registerService(ConfigurationService.class.getName(),
         new ConfigurationServiceImpl(),
         null);
  }
}
```

Other bundle consuming the service:
```
public class RandomBundleActivator implements BundleActivator {
  public void start(BundleContext bc) throws Exception {
    ServiceReference cRef = bc.getServiceReference(
                              ConfigurationService.class.getName());
    configService = (ConfigurationService) bc.getService(cRef);
    configService.setProperty("propertyName", "propertyValue");
  }
}
```

Ant build target for bundling:
```
<target name="bundle-configuration">
  <jar destfile="${bundles.dest}/configuration.jar" manifest=
    "${src}/net/java/sip/communicator/impl/configuration/conf.manifest.mf" >
    <zipfileset dir="${dest}/net/java/sip/communicator/service/configuration"
        prefix="net/java/sip/communicator/service/configuration"/>
    <zipfileset dir="${dest}/net/java/sip/communicator/impl/configuration"
        prefix="net/java/sip/communicator/impl/configuration" />
  </jar>
</target>
```

Felix startup levels in felix.client.run.properties:
```
felix.auto.start.30= \
  reference:file:sc-bundles/fileaccess.jar

felix.auto.start.40= \
  reference:file:sc-bundles/configuration.jar \
  reference:file:sc-bundles/jmdnslib.jar \
  reference:file:sc-bundles/provdisc.jar
```

ProtocolProviderService operation set discovery:
```
public Map<String, OperationSet> getSupportedOperationSets();
public <T extends OperationSet> T getOperationSet(Class<T> opsetClass);
```

MediaService device and format queries:
```
public List<MediaDevice> getDevices(MediaType mediaType, MediaUseCase useCase);
public List<MediaFormat> getSupportedFormats();
```

Media stream initialization:
```
StreamConnector connector = new DefaultStreamConnector(rtpSocket, rtcpSocket);
MediaStream stream = mediaService.createMediaStream(connector, device, control);
stream.setTarget(target);
stream.setDirection(direction);
stream.setFormat(format);
stream.start();
```

OTR plugin registration in UI:
```
Hashtable<String, String> filter = new Hashtable<String, String>();
filter.put(Container.CONTAINER_ID,
    Container.CONTAINER_CONTACT_RIGHT_BUTTON_MENU.getID());
bundleContext.registerService(PluginComponent.class.getName(),
    new OtrMetaContactMenu(Container.CONTAINER_CONTACT_RIGHT_BUTTON_MENU),
    filter);
```

UI bundle discovering and adding plugin components:
```
String osgiFilter = "(" + Container.CONTAINER_ID + "=" +
    Container.CONTAINER_CONTACT_RIGHT_BUTTON_MENU.getID() + ")";
ServiceReference[] serRefs = GuiActivator.bundleContext.getServiceReferences(
        PluginComponent.class.getName(),
        osgiFilter);
for (int i = 0; i < serRefs.length; i++) {
    PluginComponent component = (PluginComponent) GuiActivator
        .bundleContext.getService(serRefs[i]);
    component.setCurrentContact(metaContact);
    if (component.getComponent() != null)
        this.add((Component)component.getComponent());
}
```

## Chapter 11. LLVM

Example 1: LLVM IR textual format. Two functions showing addition, one direct and one recursive:

define i32 @add1(i32 %a, i32 %b) {
entry:
  %tmp1 = add i32 %a, %b
  ret i32 %tmp1
}

define i32 @add2(i32 %a, i32 %b) {
entry:
  %tmp1 = icmp eq i32 %a, 0
  br i1 %tmp1, label %done, label %recurse

recurse:
  %tmp2 = sub i32 %a, 1
  %tmp3 = add i32 %b, 1
  %tmp4 = call i32 @add2(i32 %tmp2, i32 %tmp3)
  ret i32 %tmp4

done:
  ret i32 %b
}

Example 2: Arithmetic identity simplifications in SimplifySubInst:

// X - 0 -> X
if (match(Op1, m_Zero()))
  return Op0;

// X - X -> 0
if (Op0 == Op1)
  return Constant::getNullValue(Op0->getType());

// (X*2) - X -> X
if (match(Op0, m_Mul(m_Specific(Op1), m_ConstantInt<2>()))
  return Op1;

return 0;  // Nothing matched, return null to indicate no transformation.

Example 3: Pass class structure. A simple Hello pass demonstrating the Pass interface:

namespace {
  class Hello : public FunctionPass {
  public:
    // Print out the names of functions in the LLVM IR being optimized.
    virtual bool runOnFunction(Function &F) {
      cerr << "Hello: " << F.getName() << "\n";
      return false;
    }
  };
}

FunctionPass *createHelloPass() { return new Hello(); }

Example 4: Register class definition in .td (target description language):

def GR32 : RegisterClass<[i32], 32,
  [EAX, ECX, EDX, ESI, EDI, EBX, EBP, ESP,
   R8D, R9D, R10D, R11D, R14D, R15D, R12D, R13D]> { … }

Example 5: Instruction definition in .td:

let Constraints = "$src = $dst" in
def NOT32r : I<0xF7, MRM2r,
               (outs GR32:$dst), (ins GR32:$src),
               "not{l}\t$dst",
               [(set GR32:$dst, (not GR32:$src))]>;

Example 6: Unit test for constant propagation optimization:

; RUN: opt < %s -constprop -S | FileCheck %s
define i32 @test() {
  %A = add i32 4, 5
  ret i32 %A
  ; CHECK: @test()
  ; CHECK: ret i32 9
}

## Chapter 12. Mercurial

**Revlog Record Format (Table 12.1):**
6 bytes – hunk offset
2 bytes – flags
4 bytes – hunk length
4 bytes – uncompressed length
4 bytes – base revision
4 bytes – link revision
4 bytes – parent 1 revision
4 bytes – parent 2 revision
32 bytes – hash

**Changelog Revision Example:**
0a773e3480fe58d62dcc67bd9f7380d6403e26fa
Dirkjan Ochtman <dirkjan@ochtman.nl>
1276097267 -7200
mercurial/discovery.py
discovery: fix description line

The initial line is the manifest hash; following lines contain author, Unix timestamp with timezone offset, affected files list, and commit message. Additional arbitrary metadata may follow the timestamp for backwards compatibility.

**Manifest Revision Example:**
.hgignore\x006d2dc16e96ab48b2fcca44f7e9f4b8c3289cb701
.hgsigs\x00de81f258b33189c609d299fd605e6c72182d7359
.hgtags\x00b174a4a4813ddd89c1d2f88878e05acc58263efa
CONTRIBUTORS\x007c8afb9501740a450c549b4b1f002c803c45193a
COPYING\x005ac863e17c7035f1d11828d848fb2ca450d89794
…

Each line pairs a filename with its node ID (hex-encoded filelog reference) separated by a null byte. Directories are implicit from file path slashes. The manifest is represented internally as a hashtable-like structure with filenames as keys and nodes as values.

**Figure 12.2: Log Structure** describes three nested revlog layers: changelog entries point to specific manifest revisions; manifest entries point to filelog revisions for each file; filelogs contain actual file content deltas. This permits efficient horizontal diffing at the manifest level (only changed files reappear in deltas).

**Figure 12.3: Import Graph** shows dispatch module receiving arguments and instantiating ui object, which loads configuration/extensions and conditionally creates localrepo (or works with remote repositories for some commands). Commands module contains command functions; ui and localrepo are passed to almost every function.

## Chapter 13. The NoSQL Ecosystem

Key design patterns and concrete scenarios:

Key-based access: employee:30 points to an employee record; employee_departments:20 lists all employees in department 20. Joins become application loops retrieving multiple key lookups.

Consistent hash ring example with L=1000: servers A–E hash to positions H(A) mod 1000 = 7, H(B) = 234, H(C) = 447, H(D) = 660, H(E) = 875. Key employee30 with H('employee30') mod 1000 = 899 routes to server E (range [875, 6], wrapping around). Replication factor 3 stores keys [7,233] on servers A, B, C. Virtual nodes (e.g., A_1, A_2, A_3, A_4 per server) balance uneven ranges.

BigTable range partitioning: three-level hierarchy. Client seeking key 900 queries metadata level-0 tablet on server A, learning metadata level-1 tablet containing ranges 500–1500 lives on server B. Query to B reveals tablet 850–950 on server C. Final query to C retrieves row data. Tablets split/merge at 100–200 MB; master reassigns tablets across servers.

Vector clock versioning: three replicas A, B, C holding counter triplet (N_A, N_B, N_C) initialized (0,0,0). After B modifies a key, vector clock becomes (39, 2, 5). When C receives this update, it compares: if its own counters are all less than B's, C has a stale version and overwrites. If C holds (39, 1, 6) and receives (39, 2, 5), the clocks show conflicting updates—some counters higher in each—signaling conflict.

Strong consistency example: replicate employee30:salary across N=3 servers A, B, C. Update from $20,000 to $30,000 requires W=2 confirmations. A and B confirm; C misses update (remains $20,000). On read with R=2: coordinator queries all three, receives $20,000 from C and $30,000 from A and B, detects conflict, and returns $30,000 as majority. Setting R=2, W=2 satisfies R+W=4 > N=3 for strong consistency.

## Chapter 14. Python Packaging

1. Distutils setup.py basic usage:
```python
from distutils.core import setup
setup(name='MyProject', version='1.0', py_modules=['mycode.py'])
```
Building a distribution: `$ python setup.py sdist`
Installing: `$ python setup.py install`
Querying metadata: `$ python setup.py --name`

2. Platform-specific metadata problem (lxml):
```bash
$ python setup.py --name
Building lxml version 2.2.
NOTE: Trying to build without Cython, pre-generated 'src/lxml/lxml.etree.c' needs to be available.
Using build configuration of libxslt 1.1.26
Building against libxml2/libxslt in the following directory: /usr/lib/lxml
```

3. Conditional Windows-only dependency (problematic):
```python
from distutils.core import setup
import sys
if sys.platform == 'win32':
    setup(name='foo', version='1.0', requires=['win32com'])
else:
    setup(name='foo', version='1.0')
```

4. Version ordering specification (PEP 386):
`1.0a1 < 1.0a2.dev456 < 1.0a2 < 1.0a2.1.dev456 < 1.0a2.1 < 1.0b1.dev456 < 1.0b2 < 1.0b2.post345 < 1.0c1.dev456 < 1.0c1 < 1.0.dev456 < 1.0 < 1.0.post456.dev34 < 1.0.post456`

5. Environment markers for conditional dependencies (PEP 345):
```
Requires-Dist: pywin32 (>1.0); sys.platform == 'win32'
Obsoletes-Dist: pywin31; sys.platform == 'win32'
Requires-Dist: foo (1,!=1.3); platform.machine == 'i386'
Requires-Dist: bar; python_version == '2.4' or python_version == '2.5'
Requires-External: libxslt; 'linux' in sys.platform
```

6. Data files mapping in Distutils (problematic approach):
```python
setup(…,
    data_files=[('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),
                ('config', ['cfg/data.cfg']),
                ('/etc/init.d', ['init-script'])]
    )
```

7. Distutils2 setup.cfg format (replacement for setup.py):
```ini
[metadata]
name = MPTools
version = 0.1
author = Tarek Ziade
author-email = tarek@mozilla.com
summary = Set of tools to build Mozilla Services apps
description-file = README
home-page = http://bitbucket.org/tarek/pypi2rpm
project-url: Repository, http://hg.mozilla.org/services/server-devtools
classifier = Development Status :: 3 - Alpha
    License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)

[files]
packages =
        mopytools
        mopytools.tests

extra_files =
        setup.py
        README
        build.py

resources =
    etc/mopytools.cfg {confdir}/mopytools
```

8. Data file access pattern (pkgutil indirection):
```python
import pkgutil
# Developer code: request config file from project
cfg = pkgutil.open('MPTools', 'config/mopy.cfg')
```

9. RESOURCES metadata file format (generated at install time):
```
config/mopy.cfg {confdir}/{distribution.name}
```

10. PyPI XML-RPC query example:
```python
import xmlrpclib
client = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')
client.package_releases('MPTools')  # Returns ['0.1']
client.release_urls('MPTools', '0.1')  # Returns metadata dict with downloads, md5, URL
```

11. PyPI Simple Index HTML structure:
```html
<html><head><title>Links for MPTools</title></head>
<body><h1>Links for MPTools</h1>
<a href="../../packages/source/M/MPTools/MPTools-0.1.tar.gz">MPTools-0.1.tar.gz</a><br/>
<a href="http://bitbucket.org/tarek/mopytools" rel="homepage">0.1 home_page</a><br/>
</body></html>
```

12. Mirror chain detection via CNAME:
```python
import socket
socket.gethostbyname_ex('last.pypi.python.org')[0]  # Returns 'h.pypi.python.org'
```
Indicates 6 mirrors (b through h) currently active, with a being master.

## Chapter 15. Riak and Erlang/OTP

Erlang Factorial with Pattern Matching:
```
-module(factorial).
-export([fac/1]).
fac(0) -> 1;
fac(N) when N>0 ->
   Prev = fac(N-1),
   N*Prev.
```

Message Receive Pattern:
```
receive
   {ok, N} ->
      N+1;
   {error, _} ->
      0
end
```

Generic Server Module Header (riak_core_node_watcher.erl):
```
-module(riak_core_node_watcher).
-behavior(gen_server).
%% API
-export([start_link/0,service_up/2,service_down/1,node_up/0,node_down/0,services/0,
         services/1,nodes/1,avsn/0]).
%% gen_server callbacks
-export([init/1,handle_call/3,handle_cast/2,handle_info/2,terminate/2, code_change/3]).

-record(state, {status=up, services=[], peers=[], avsn=0, bcast_tref,
                bcast_mod={gen_server, abcast}}).
```

Starting a Generic Server:
```
start_link() ->
    gen_server:start_link({local, ?MODULE}, ?MODULE, [], []).
```

Initialization Callback:
```
init([]) ->
    %% Watch for node up/down events
    net_kernel:monitor_nodes(true),
    %% Setup ETS table to track node status
    ets:new(?MODULE, [protected, named_table]),
    {ok, schedule_broadcast(#state{})}.
```

API Functions for Synchronous Calls:
```
service_up(Id, Pid) ->
    gen_server:call(?MODULE, {service_up, Id, Pid}).

service_down(Id) ->
    gen_server:call(?MODULE, {service_down, Id}).
```

Handle Call Callback:
```
handle_call({service_up, Id, Pid}, _From, State) ->
    %% Update the set of active services locally
    Services = ordsets:add_element(Id, State#state.services),
    S2 = State#state { services = Services },
    %% Remove any existing mrefs for this service
    delete_service_mref(Id),
    %% Setup a monitor for the Pid representing this service
    Mref = erlang:monitor(process, Pid),
    erlang:put(Mref, Id),
    erlang:put(Id, Mref),
    %% Update our local ETS table and broadcast
    S3 = local_update(S2),
    {reply, ok, update_avsn(S3)};

handle_call({service_down, Id}, _From, State) ->
    %% Update the set of active services locally
    Services = ordsets:del_element(Id, State#state.services),
    S2 = State#state { services = Services },
    %% Remove any existing mrefs for this service
    delete_service_mref(Id),
    %% Update local ETS table and broadcast
    S3 = local_update(S2),
    {reply, ok, update_avsn(S3)};
```

Terminate Callback:
```
terminate(_Reason, State) ->
    %% Let our peers know that we are shutting down
    broadcast(State#state.peers, State#state { status = down }).
```

Custom OTP Behavior (riak_core_vnode):
```
behavior_info(callbacks) ->
    [{init,1},
     {handle_command,3},
     {handoff_starting,2},
     {handoff_cancelled,1},
     {handoff_finished,2},
     {handle_handoff_command,3},
     {handle_handoff_data,2},
     {encode_handoff_item,2},
     {is_empty,1},
     {terminate,2},
     {delete,1}];
```

Supervisor Module (riak_core_sup.erl):
```
-module(riak_core_sup).
-behavior(supervisor).
%% API
-export([start_link/0]).
%% Supervisor callbacks
-export([init/1]).
-define(CHILD(I, Type), {I, {I, start_link, []}, permanent, 5000, Type, [I]}).
start_link() ->
    supervisor:start_link({local, ?MODULE}, ?MODULE, []).
```

Supervisor Init with Child Specifications:
```
-define(CHILD(I, Type), {I, {I, start_link, []}, permanent, 5000, Type, [I]}).

init([]) ->
    RiakWebs = case lists:flatten(riak_core_web:bindings(http),
                                  riak_core_web:bindings(https)) of
                   [] ->
                       %% check for old settings, in case app.config
                       %% was not updated
                       riak_core_web:old_binding();
                   Binding ->
                       Binding
               end,

    Children =
                 [?CHILD(riak_core_vnode_sup, supervisor),
                  ?CHILD(riak_core_handoff_manager, worker),
                  ?CHILD(riak_core_handoff_listener, worker),
                  ?CHILD(riak_core_ring_events, worker),
                  ?CHILD(riak_core_ring_manager, worker),
                  ?CHILD(riak_core_node_watcher_events, worker),
                  ?CHILD(riak_core_node_watcher, worker),
                  ?CHILD(riak_core_gossip, worker) |
                  RiakWebs
                 ],
    {ok, {{one_for_one, 10, 10}, Children}}.
```

Child Specification Tuple Structure:
```
{Id, {Module, Function, Arguments}, Restart, Shutdown, Type, ModuleList}
```
Where Restart is `permanent`, `temporary`, or `transient`; Shutdown is milliseconds or `infinity`; Type is `worker` or `supervisor`.

Supervision Tree Architecture Description: OTP Riak maintains a hierarchical supervision tree where riak_core_sup (top supervisor) manages static workers including riak_core_vnode_sup (supervisor), riak_core_handoff_manager, riak_core_ring_manager, riak_core_gossip, and riak_core_node_watcher. The vnode_sup manages virtual nodes (storage abstraction). Gossip protocol propagates cluster membership and partition ownership as `{HashRange, Owner}` pairs across all nodes, avoiding centralized configuration servers while enabling fully decentralized cluster management.

## Chapter 16. Selenium WebDriver

**Remote WebDriver Protocol: Command Encoding and Response**

A Java call `element.getAttribute("row")` with opaque element ID "some_opaque_id" maps to a GET request:
```
/session/:sessionId/element/:id/attribute/:name
http://localhost:7055/hub/session/XXX/element/some_opaque_id/attribute/row
```

Command object created by dispatcher:
```json
{
  "name": "getElementAttribute",
  "sessionId": { "value": "XXX" },
  "parameters": {
    "id": "some_opaque_key",
    "name": "rows"
  }
}
```

Response JSON from server:
```json
{
  "sessionId": "BD204170-1A52-49C2-A6F8-872D127E7AE8",
  "status": 7,
  "value": "Unable to locate element with id: foo"
}
```

**Firefox Driver: getAttribute Implementation**

The handler receives a respond object (encapsulating return values and response dispatch) and parameters:
```javascript
FirefoxDriver.prototype.getElementAttribute = function(respond, parameters) {
  var element = Utils.getElementAt(parameters.id,
                                   respond.session.getDocument());
  var attributeName = parameters.name;

  respond.value = webdriver.element.getAttribute(element, attributeName);
  respond.send();
};
```

The second-to-last line delegates to the shared atomic WebDriver library, reducing the Firefox driver's getAttribute method from approximately 50 lines to 6 lines.

**IE Driver: JNI to PInvoke/FFI/ctypes Abstraction**

Flattened C interface with prefixes (wdGet for WebDriver, wdeGetText for WebElement):
```c
int wdeGetAttribute(WebDriver*, WebElement*, const wchar_t*, StringWrapper**)
```

Adapted back to object-oriented Java via JNA:
```java
public String getAttribute(String name) {
  PointerByReference wrapper = new PointerByReference();
  int result = lib.wdeGetAttribute(
      parent.getDriverPointer(), element, new WString(name), wrapper);

  errors.verifyErrorCode(result, "get attribute of");

  return wrapper.getValue() == null ? null : new StringWrapper(lib, wrapper).toString();
}
```

**Browser Automation Atoms: Role-Based Interfaces**

WebDriver uses role-based interfaces to expose optional capabilities without cluttering the main API. A successful cast indicates the driver supports that functionality:
```
JavascriptExecutor executor = (JavascriptExecutor) driver;
// Can now call executor.executeScript(...) safely
```

**Selenium Core: AJAX Long-Polling via XMLHttpRequest**

The Javascript in the browser opens an XMLHttpRequest to `/selenium-server/driver`, first sending the response from the previously executed command (or "OK" on startup). The server keeps the request open until a new command arrives from the user's test client, then sends it as the response. This mechanism (originally dubbed "Response/Request," now called Comet with AJAX long polling) avoids both polling latency and busy-loop CPU costs.

**HTML5 Boolean Attribute Normalization**

The atoms normalize return values across browsers:
```html
<input name="example" checked>
```
The `checked` attribute varies by browser; atoms normalize it to the string "true" or "false" per HTML5 spec, creating temporary confusion when this change was introduced to the codebase.

**Architecture Diagrams (Described in Prose)**

The layered JavaScript library (Figure 16.3) shows: Google Closure Library at the bottom (primitives and modularization), utility library above (getAttribute, visibility checks, synthetic event simulation), Browser Automation Atoms (smallest units), and adapter layers for WebDriver and Selenium Core API contracts.

The Firefox Driver Architecture (Figure 16.4) shows: requests arriving at embedded HTTPD, dispatcher matching URLs and constructing JSON command objects, CommandProcessor XPCOM component executing commands via handlers, respond objects encapsulating return values and dispatch mechanisms, callback functions sending JSON responses back to the HTTP server.

The original IE Driver (Figure 16.5) shows: IE COM Automation interfaces at the bottom, C++ class wrappers, JNI interface layer for Java, and Java classes above.

The modified IE Driver (Figure 16.6) shows: same foundation but exposing C interfaces (wdGet, wdeGetText) callable via PInvoke/FFI/ctypes from any language, with Java adapting them back to object-oriented interfaces.

The IE Driver as of Selenium 2.0 alpha 7 (Figure 16.7) shows: IE instance in a separate thread, PostThreadMessage Win32 API calls across thread boundary from main app server threads, callback mechanisms handling responses within the isolated thread.

## Chapter 17. Sendmail

Configuration routing in early delivermail (character-based precedence):
- Input "foo@bar" → Sent to {Arpanet, bar, foo}
- Input "foo:bar" → Sent to {Berknet, foo, bar}
- Input "foo!bar!baz" → Sent to {Uucp, foo, bar!baz}
- Input "foo!bar@baz" → Sent to {Arpanet, baz, foo!bar}

Rewriting rule patterns (token-based, using $ escape):
- `$+ + $* @ $+ . $={mydomain}` (readable with spaces)
- `$++$*@$+.$={mydomain}` (original unspaced form, much harder to understand)

These patterns matched and transformed addresses for cross-network compatibility. For example:
- From: a:foo → To: a.foo@berkeley.edu (BerkNET to SMTP)
- From: a!b!c → To: b!c@a.uucp (UUCP rewriting)
- From: <@a.net,@b.org:user@c.com> → To: <@b.org:user@c.com> (route list simplification)

Queue file structure: Two files per message—control file (flat text, first character per line indicating meaning) and data file (message body). Specific components mentioned: `/usr/spool/mail` (local mailbox spool), `/bin/mail` command (user agent), `mail.local` (extracted delivery program), `delivermail` (predecessor), SMTP protocol commands (EXPN, VRFY, RCPT), m4 macro processor configuration (`.mc` and `.cf` files), `dbm(3)` database maps, YP/NIS directory services, milter callbacks, Realtime Blackhole Lists (RBL), access tables, TLS (encryption), SMTP authentication, DKIM signing, and submission port 587 (separate from standard SMTP port 25).

## Chapter 18. SnowFlock

The chapter provides no explicit code snippets in traditional programming language syntax. However, it documents the SnowFlock VM Cloning API function signatures as follows:

sf_request_ticket(n)  →  Returns ticket describing allocation for m≤n clones
sf_clone(ticket)  →  Returns clone ID where 0≤ID&lt;m
sf_checkpoint_parent()  →  Prepares immutable checkpoint C of parent VM
sf_create_clones(C, ticket)  →  Clones using checkpoint C, clones begin at sf_checkpoint_parent() instruction point
sf_exit()  →  For children (1≤ID&lt;m), terminates child
sf_join(ticket)  →  For parent (ID=0), blocks until all children reach sf_exit, then discards ticket
sf_kill(ticket)  →  Parent only, immediately kills all associated children and discards ticket

Key memory allocation functions referenced but not implemented in the text include: vmalloc, kzalloc, get_free_page (kernel), and brk (user-space), all ultimately handled by the kernel page allocator.

Architectural components referenced: Xen hypervisor (VMM), domain 0 (dom0) privileged VM, domain U (domU) guest VMs, XenStore (shared-memory control interface), page presence bitmap (flat bit array with atomic mutations), Multicast Distribution System (mcdist), memory server (memserver), memtap process, Clone Enlightenment modifications, VM Descriptor, SnowFlock Local Daemon (SFLD), and SnowFlock Master Daemon (SFMD).

## Chapter 19. SocialCalc

Cell properties (Table 19.1):
datatype: t (text)
datavalue: 1Q84
color: black
bgcolor: white
font: italic bold 12pt Ubuntu
comment: Ichi-Kyu-Hachi-Yon

SocialCalc Commands (Table 19.2):
set sheet defaultcolor blue
set A width 100
set A1 value n 42
set A2 text t Hello
set A3 formula A1*2
set A4 empty
set A5 bgcolor green
merge A1:B2
unmerge A1
erase A2
cut A3
paste A4
copy A5
sort A1:B9 A up B down
name define Foo A1:A5
name desc Foo Used in formulas like SUM(Foo)
name delete Foo
startcmdextension UserDefined args

Rich-text rendering implementation:
var parser = new Document.Parser.Wikitext();
var emitter = new Document.Emitter.HTML();
SocialCalc.Callbacks.expand_wiki = function(val) {
    return parser.parse(val, emitter);
}
// After spreadsheet initialization:
var spreadsheet = new SocialCalc.SpreadsheetControl();
spreadsheet.InitializeSpreadsheetControl("tableeditor", 0, 0, 0);
spreadsheet.ExecuteCommand('set sheet defaulttextvalueformat text-wiki');

Wiki markup examples:
*bold* _italic_ `monospace` {{unformatted}}
> indented text
* unordered list
# ordered list
"Hyperlink with label"<http://softwaregarden.com/>
{image: http://www.socialtext.com/images/logo.png}

Real-time collaboration broadcast:
var hpipe = new Hippie.Pipe();
SocialCalc.ScheduleSheetCommands = function(sheet, cmdstr, saveundo, isRemote) {
    if (SocialCalc.Callbacks.broadcast && !isRemote) {
        SocialCalc.Callbacks.broadcast('execute', {
            cmdstr: cmdstr, saveundo: saveundo
        });
    }
    // …original ScheduleSheetCommands code here…
}
SocialCalc.Callbacks.broadcast = function(type, data) {
    hpipe.send({ type: type, data: data });
};
$(hpipe).bind("message.execute", function (e, d) {
    var sheet = SocialCalc.CurrentSpreadsheetControlObject.context.sheetobj;
    sheet.ScheduleSheetCommands(d.data.cmdstr, d.data.saveundo, true);
});

Remote cursor handling:
editor.MoveECellCallback.broadcast = function(e) {
    hpipe.send({
        type: 'ecell',
        data: e.ecell.coord
    });
};
$(hpipe).bind("message.ecell", function (e, d) {
    var cr = SocialCalc.coordToCr(d.data);
    var cell = SocialCalc.GetEditorCellElement(editor, cr.row, cr.col);
    // …decorate cell with styles specific to the remote user(s) on it…
});
/* Multiple cursors via CSS3 box-shadow: */
box-shadow: inset 0 0 0 4px red, inset 0 0 0 2px green;

MIME save format structure:
socialcalc:version:1.0
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=SocialCalcSpreadsheetControlSave
--SocialCalcSpreadsheetControlSave
Content-type: text/plain; charset=UTF-8

# SocialCalc Spreadsheet Control Save
version:1.0
part:sheet
part:edit
part:audit
--SocialCalcSpreadsheetControlSave
Content-type: text/plain; charset=UTF-8

version:1.5
cell:A1:v:1874
cell:A2:vtf:n:172:2^2*43
cell:A3:vtf:n:2046:SUM(Foo):f:1
sheet:c:1:r:3
font:1:normal bold * *
name:FOO::A1\cA2
--SocialCalcSpreadsheetControlSave
Content-type: text/plain; charset=UTF-8

version:1.0
rowpane:0:1:14
colpane:0:1:16
ecell:A1
--SocialCalcSpreadsheetControlSave
Content-type: text/plain; charset=UTF-8

set A1 value n 1874
set A2 formula 2^2*43
name define Foo A1:A2
set A3 formula SUM(Foo)
--SocialCalcSpreadsheetControlSave--

## Chapter 20. Telepathy

### D-Bus Object Paths and Interfaces

D-Bus objects published by Telepathy services use strictly namespaced paths and interfaces:

Account Manager object path: `/org/freedesktop/Telepathy/AccountManager`

Connection object path: `/org/freedesktop/Telepathy/Connection/gabble/jabber/danielle_2emedley_40collabora_2eco_2euk0`

Channel object paths follow Connection: `/org/freedesktop/Telepathy/Connection/.../.../ChannelDispatcher/...`

Core and optional interfaces for a text channel:
- `ofdT.Channel` - base interface with common features
- `ofdT.Channel.Type.Text` - channel type interface defining text-specific methods
- `ofdT.Channel.Interface.Messages` - rich-text messaging
- `ofdT.Channel.Interface.Group` - for multi-user chats (list, track, invite members)
- `ofdT.Channel.Interface.Room` - chatroom properties (subject, etc.)

Connection interfaces vary by protocol:
- `ofdT.Connection.Interface.Avatars` - if protocol supports user pictures
- `ofdT.Connection.Interface.ContactList` - if protocol provides contact roster
- `ofdT.Connection.Interface.Location` - if protocol provides geolocation

### Channel Property Request (GetContactAttributes)

Request to retrieve multiple contact attributes in one call:

```
connection[CONNECTION_INTERFACE_CONTACTS].GetContactAttributes(
  [ 1, 2, 3 ],  # contact handles
  [ "ofdT.Connection.Interface.Aliasing",
    "ofdT.Connection.Interface.Avatars",
    "ofdT.Connection.Interface.ContactGroups",
    "ofdT.Connection.Interface.Location"
  ],
  False  # don't hold a reference to these contacts
)
```

Reply (map of contact handle to attributes):

```
{ 1: { 'ofdT.Connection.Interface.Aliasing/alias': 'Harvey Cat',
       'ofdT.Connection.Interface.Avatars/token': hex string,
       'ofdT.Connection.Interface.Location/location': location,
       'ofdT.Connection.Interface.ContactGroups/groups': [ 'Squid House' ],
       'ofdT.Connection/contact-id': 'harvey@nom.cat'
     },
  2: { 'ofdT.Connection.Interface.Aliasing/alias': 'Escher Cat',
       'ofdT.Connection.Interface.Avatars/token': hex string,
       'ofdT.Connection.Interface.Location/location': location,
       'ofdT.Connection.Interface.ContactGroups/groups': [],
       'ofdT.Connection/contact-id': 'escher@tuxedo.cat'
     },
  3: { ... }
}
```

### Channel Request Examples

Simple text channel request:

```
ofdT.Channel.ChannelType - value ofdT.Channel.Type.Text
ofdT.Channel.TargetHandleType - value Handle_Type_Contact (1)
ofdT.Channel.TargetID - value escher@tuxedo.cat
```

File transfer channel request (showing qualified property namespaces):

```
ofdT.Channel.ChannelType - value ofdT.Channel.Type.FileTransfer
ofdT.Channel.TargetHandleType - value Handle_Type_Contact (1)
ofdT.Channel.TargetID - value escher@tuxedo.cat
ofdT.Channel.Type.FileTransfer.Filename - value meow.jpg
ofdT.Channel.Type.FileTransfer.ContentType - value image/jpeg
```

Immutable properties returned with channel creation:

```
ofdT.Channel.ChannelType - value Channel.Type.Text
ofdT.Channel.Interfaces - value [ Channel.Interface.Messages, 
                                   Channel.Interface.Destroyable, 
                                   Channel.Interface.ChatState ]
ofdT.Channel.TargetHandleType - value Handle_Type_Contact (1)
ofdT.Channel.TargetID - value escher@tuxedo.cat
ofdT.Channel.InitiatorID - value danielle.madeley@collabora.co.uk
ofdT.Channel.Requested - value True
ofdT.Channel.Interface.Messages.SupportedContentTypes - value [ text/html, text/plain ]
```

### Callback Function Signature (C Binding)

Early Telepathy C bindings used typedef callback functions:

```
typedef void (*tp_conn_get_self_handle_reply) (
    DBusGProxy *proxy,
    guint handle,
    GError *error,
    gpointer userdata
);
```

### D-Bus Type Signatures

Type signatures describe serialized data format:
- `(ii)` — structure containing two int32s
- `a{sa(usuu)}` — map from string to array of structures, where each structure contains uint32, string, uint32, uint32

### Client Filter Example

Channel filter property matching one-to-one text channels:

```
ofdT.Channel.ChannelType - value Channel.Type.Text
ofdT.Channel.TargetHandleType - value Handle_Type_Contact (1)
```

### Connection Manager Architecture (conceptual)

Telepathy-GLib Connection Manager structure:
- Base classes: `BaseConnection`, `BaseChannel`, `Channel Manager`
- Mixins: Properties interface, Contacts interface, Group interface, Presence mixin, Message mixin
- Each Connection publishes: service object (for Account Manager), objects per open connection, objects per open channel

## Chapter 21. Thousand Parsec

TPCL Requirements function example (Scheme subset validating hull constraints):
```scheme
(lambda (design)
  (if (> (designType.MaxSize design) (designType.Size design))
      (if (= (designType.num-hulls design) 1)
          (cons #t "")
          (cons #f "Ship can only have one hull")
      )
      (cons #f "This many components can't fit into this Hull")
  )
)
```
Checks if component size fits design maximum, ensures single hull exists. Returns (boolean, message) pair.

XML property definition for Colonise capability:
```xml
<prop>
<CategoryIDName>Ships</CategoryIDName>
<rank value="0"/>
<name>Colonise</name>
<displayName>Can Colonise Planets</displayName>
<description>Can the ship colonise planets</description>
<tpclDisplayFunction>
    (lambda (design bits) (let ((n (apply + bits))) (cons n (if (= n 1) "Yes" "No")) ) )
</tpclDisplayFunction>
<tpclRequirementsFunction>
    (lambda (design) (cons #t ""))
</tpclRequirementsFunction>
</prop>
```
Rank 0 Ships category property displaying "Yes"/"No" based on component count.

Prose example of Missile and Torpedo Wars game startup: new player receives random home planet with two default Scout fleets (Scout Hull + Alpha Missile Tube, no explosives). Player must Build Weapon orders (converting planet resources to warheads), Load Armament orders (transferring weapons to fleets), then Mine orders (converting mineable resources to surface resources for continued building). Example object hierarchy: Universe → Galaxy → Star Systems → Planets/Fleets containing orders and resources. No complete network exchange code examples present; frame interactions documented procedurally (e.g., "Get Object IDs request → List of Object IDs response → Get Object by ID requests → Object responses").

## Chapter 22. Violet

**Prototype Pattern for Node/Edge Types:**
```java
public class SimpleGraph extends AbstractGraph {
  public Node[] getNodePrototypes() {
    return new Node[] {
      new CircleNode(Color.BLACK),
      new CircleNode(Color.WHITE)
    };
  }
  public Edge[] getEdgePrototypes() {
    return new Edge[] {
      new LineEdge()
    };
  }
}
```

**CircleNode and LineEdge Implementations:**
```java
public class CircleNode extends AbstractNode {
  public CircleNode(Color aColor) {
    size = DEFAULT_SIZE;
    x = 0; y = 0;
    color = aColor;
  }

  public void draw(Graphics2D g2) {
    Ellipse2D circle = new Ellipse2D.Double(x, y, size, size);
    Color oldColor = g2.getColor();
    g2.setColor(color);
    g2.fill(circle);
    g2.setColor(oldColor);
    g2.draw(circle);
  }

  public boolean contains(Point2D p) {
    Ellipse2D circle = new Ellipse2D.Double(x, y, size, size);
    return circle.contains(p);
  }

  public Point2D getConnectionPoint(Point2D other) {
    double centerX = x + size / 2;
    double centerY = y + size / 2;
    double dx = other.getX() - centerX;
    double dy = other.getY() - centerY;
    double distance = Math.sqrt(dx * dx + dy * dy);
    if (distance == 0) return other;
    else return new Point2D.Double(
      centerX + dx * (size / 2) / distance,
      centerY + dy * (size / 2) / distance);
  }

  private double x, y, size, color;
  private static final int DEFAULT_SIZE = 20;
}

public class LineEdge extends AbstractEdge {
  public void draw(Graphics2D g2) {
    g2.draw(getConnectionPoints());
  }

  public boolean contains(Point2D aPoint) {
    final double MAX_DIST = 2;
    return getConnectionPoints().ptSegDist(aPoint) < MAX_DIST;
  }
}
```

**XML Long-Term Persistence Format (ClassDiagramGraph example):**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<java version="1.0" class="java.beans.XMLDecoder">
 <object class="com.horstmann.violet.ClassDiagramGraph">
  <void method="addNode">
   <object id="ClassNode0" class="com.horstmann.violet.ClassNode">
    <void property="name">…</void>
   </object>
   <object class="java.awt.geom.Point2D$Double">
    <double>200.0</double>
    <double>60.0</double>
   </object>
  </void>
  <void method="addNode">
   <object id="ClassNode1" class="com.horstmann.violet.ClassNode">
    <void property="name">…</void>
   </object>
   <object class="java.awt.geom.Point2D$Double">
    <double>200.0</double>
    <double>210.0</double>
   </object>
  </void>
  <void method="connect">
   <object class="com.horstmann.violet.ClassRelationshipEdge">
    <void property="endArrowHead">
     <object class="com.horstmann.violet.ArrowHead" field="TRIANGLE"/>
    </void>
   </object>
   <object idref="ClassNode0"/>
   <object idref="ClassNode1"/>
  </void>
 </object>
</java>
```

**XML Persistence Delegate (Custom Serialization):**
```java
encoder.setPersistenceDelegate(Graph.class, new DefaultPersistenceDelegate() {
  protected void initialize(Class<?> type, Object oldInstance,
    Object newInstance, Encoder out) {
    super.initialize(type, oldInstance, newInstance, out);
    AbstractGraph g = (AbstractGraph) oldInstance;
    for (Node n : g.getNodes())
      out.writeStatement(new Statement(oldInstance, "addNode", new Object[] {
        n, n.getLocation()
      }));
    for (Edge e : g.getEdges())
      out.writeStatement(new Statement(oldInstance, "connect", new Object[] {
        e, e.getStart(), e.getEnd()
      }));
  }
});
encoder.writeObject(graph);
Graph graph = (Graph) decoder.readObject();
```

**JavaBeans Property (Color):**
```java
public void setColor(Color newValue)
public Color getColor()
```

**Shadow Drawing with Java 2D:**
```java
Shape shape = getShape();
if (shape == null) return;
g2.translate(SHADOW_GAP, SHADOW_GAP);
g2.setColor(SHADOW_COLOR);
g2.fill(shape);
g2.translate(-SHADOW_GAP, -SHADOW_GAP);
g2.setColor(BACKGROUND_COLOR);
g2.fill(shape);
```

**PostScript Vector Export:**
```java
DocFlavor flavor = DocFlavor.SERVICE_FORMATTED.PRINTABLE;
String mimeType = "application/postscript";
StreamPrintServiceFactory[] factories = 
  StreamPrintServiceFactory.lookupStreamPrintServiceFactories(flavor, mimeType);
FileOutputStream out = new FileOutputStream(fileName);
PrintService service = factories[0].getPrintService(out);
SimpleDoc doc = new SimpleDoc(new Printable() {
  public int print(Graphics g, PageFormat pf, int page) {
    if (page >= 1) return Printable.NO_SUCH_PAGE;
    double sf1 = pf.getImageableWidth() / (comp.getWidth() + 1);
    double sf2 = pf.getImageableHeight() / (comp.getHeight() + 1);
    double s = Math.min(sf1, sf2);
    Graphics2D g2 = (Graphics2D) g;
    g2.translate((pf.getWidth() - pf.getImageableWidth()) / 2,
        (pf.getHeight() - pf.getImageableHeight()) / 2);
    g2.scale(s, s);
    comp.paint(g);
    return Printable.PAGE_EXISTS;
  }
}, flavor, null);
DocPrintJob job = service.createPrintJob();
job.print(doc, new HashPrintRequestAttributeSet());
```

**FileService WebStart Abstraction:**
```java
FileService service = FileService.getInstance(initialDirectory);
FileService.Open open = service.open(defaultDirectory, defaultName, extensionFilter);
InputStream in = open.getInputStream();
String title = open.getName();
```

**GraphModificationListener Interface (Undo/Redo):**
```java
public interface GraphModificationListener {
  void nodeAdded(Graph g, Node n);
  void nodeRemoved(Graph g, Node n);
  void nodeMoved(Graph g, Node n, double dx, double dy);
  void childAttached(Graph g, int index, Node p, Node c);
  void childDetached(Graph g, int index, Node p, Node c);
  void edgeAdded(Graph g, Edge e);
  void edgeRemoved(Graph g, Edge e);
  void propertyChangedOnNodeOrEdge(Graph g, PropertyChangeEvent event);
}
```

**Plugin Architecture with ServiceLoader:**
```java
ServiceLoader<Graph> graphLoader = ServiceLoader.load(Graph.class, classLoader);
for (Graph g : graphLoader)
  registerGraph(g);
```

**Menu Configuration Properties:**
```
file.save.text=Save
file.save.mnemonic=S
file.save.accelerator=ctrl S
file.save.icon=/icons/16x16/save.png
```

## Chapter 23. VisTrails

**Workflow Module Example** (from Section 23.1.1): The basic workflow pattern shows CSVReader module with parameter /weather/temp_precip.dat feeding into GetTemperature and GetPrecipitation modules, which output to a matplotlib function generating a scatter plot. This demonstrates the dataflow model where nodes represent processes with parameters and edges capture data flow between processes.

**Module Upgrade Path** (from Section 23.4.5):
```
def handle_module_upgrade_request(controller, module_id, pipeline):
   module_remap = {'GetItemsFromDirectory':
                       [(None, '1.6', 'Directory',
                         {'dst_port_remap':
                              {'dir': 'value'},
                          'src_port_remap':
                              {'itemlist': 'itemList'},
                          })],
                   }
  return UpgradeWorkflowHandler.remap_module(controller, module_id, pipeline,
                                             module_remap)
```
This upgrades workflows using GetItemsFromDirectory (versions up to 1.6) to use the Directory module, remapping the 'dir' port to 'value' and 'itemlist' to 'itemList'.

**LaTeX Integration** (from Section 23.4.6):
```
\begin{figure}[t]
{
\vistrail[wfid=119,buildalways=false]{width=0.9\linewidth}
}
\caption{Visualizing a binary star system simulation. This is an image
  that was generated by embedding a workflow directly in the text.}
\label{fig:astrophysics}
\end{figure}
```
When compiled with pdflatex, the \vistrail command invokes a Python script that sends an XML-RPC message to a VisTrails server to execute workflow id 119, downloads results, and embeds them as hyperlinked includegraphics commands.

**Architecture Pattern**: The system uses a three-tier approach for extensibility: the Execution Engine at the core, middleware packages (Persistent Data, Visual Spreadsheet) providing domain-specific features, and the query engine for provenance exploration. The change-based provenance tree enables monotonic multi-user collaboration by allowing simple synchronization algorithms when different users modify workflow versions.

## Chapter 24. VTK

Core accessor macros expand as follows:
```
vtkSetMacro(Tolerance,double);
vtkGetMacro(Tolerance,double);
```
becomes:
```
virtual void SetTolerance(double);
virtual double GetTolerance();
```

Reference counting example:
```
vtkCamera *camera = vtkCamera::New();      //reference count is 1
camera->Register(this);                    //reference count is 2
camera->Unregister(this);                  //reference count is 1
renderer->SetActiveCamera(camera);         //reference count is 2
renderer->Delete();                        //ref count is 1 when renderer is deleted
camera->Delete();                          //camera self destructs
```

Object factory instantiation:
```
vtkLight *a = vtkLight::New();  // Returns vtkOpenGLLight or platform-specific subclass
vtkImageFFT *fft = vtkImageFFT::New();  // May return hardware-accelerated variant
```

Pipeline example with demand-driven execution:
```
vtkPExodusIIReader *reader = vtkPExodusIIReader::New();
reader->SetFileName("exampleFile.exo");

vtkContourFilter *cont = vtkContourFilter::New();
cont->SetInputConnection(reader->GetOutputPort());
cont->SetNumberOfContours(1);
cont->SetValue(0, 200);

vtkQuadricDecimation *deci = vtkQuadricDecimation::New();
deci->SetInputConnection(cont->GetOutputPort());
deci->SetTargetReduction(0.75);

vtkXMLPolyDataWriter *writer = vtkXMLPolyDataWriter::New();
writer->SetInputConnection(deci->GetOuputPort());
writer->SetFileName("outputFile.vtp");
writer->Write();  // Execution triggered here
```

Rendering pipeline example:
```
vtkOBJReader *reader = vtkOBJReader::New();
reader->SetFileName("exampleFile.obj");

vtkTriangleFilter *tri = vtkTriangleFilter::New();
tri->SetInputConnection(reader->GetOutputPort());

vtkQuadricDecimation *deci = vtkQuadricDecimation::New();
deci->SetInputConnection(tri->GetOutputPort());
deci->SetTargetReduction(0.75);

vtkPolyDataMapper *mapper = vtkPolyDataMapper::New();
mapper->SetInputConnection(deci->GetOutputPort());

vtkActor *actor = vtkActor::New();
actor->SetMapper(mapper);

vtkRenderer *renderer = vtkRenderer::New();
renderer->AddActor(actor);

vtkRenderWindow *renWin = vtkRenderWindow::New();
renWin->AddRenderer(renderer);

vtkRenderWindowInteractor *interactor = vtkRenderWindowInteractor::New();
interactor->SetRenderWindow(renWin);

renWin->Render();  // Mapper terminates pipeline and renders
```

Observer pattern example monitoring filter execution:
```
class vtkProgressCommand : public vtkCommand
{
  public:
    static vtkProgressCommand *New() { return new vtkProgressCommand; }
    virtual void Execute(vtkObject *caller, unsigned long, void *callData)
    {
      double progress = *(static_cast<double*>(callData));
      std::cout << "Progress at " << progress<< std::endl;
    }
};

vtkCommand* pobserver = vtkProgressCommand::New();

vtkDecimatePro *deci = vtkDecimatePro::New();
deci->SetInputConnection(byu->GetOutputPort());
deci->SetTargetReduction(0.75);
deci->AddObserver(vtkCommand::ProgressEvent, pobserver);
```

3D widget interaction example:
```
vtkLW2Callback *myCallback = vtkLW2Callback::New();
  myCallback->PolyData = seeds;     // streamlines seed points, updated on interaction
  myCallback->Actor = streamline;   // streamline actor, made visible on interaction

vtkLineWidget2 *lineWidget = vtkLineWidget2::New();
  lineWidget->SetInteractor(iren);
  lineWidget->SetRepresentation(rep);
  lineWidget->AddObserver(vtkCommand::InteractionEvent, myCallback);
```

Piece-based streaming for out-of-core processing:
```
vtkXMLPolyDataWriter *writer = vtkXMLPolyDataWriter::New();
writer->SetInputConnection(deci->GetOuputPort());
writer->SetNumberOfPieces(2);

writer->SetWritePiece(0);
writer->SetFileName("outputFile0.vtp");
writer->Write();

writer->SetWritePiece(1);
writer->SetFileName("outputFile1.vtp");
writer->Write();  // Pipeline re-executes with piece request propagated upstream
```

Data Object class hierarchy shown in Figure 24.1 includes root vtkDataObject with main subclass vtkDataSet, further specialized into vtkPolyData, vtkUnstructuredGrid, vtkImageData, vtkRectilinearGrid, vtkStructuredGrid, and vtkTable. Figure 24.2 shows the vtkDataSet hierarchy. Figure 24.3 depicts a typical pipeline topology with Reader → ContourFilter → DecimationFilter → Writer. Figure 24.4 displays the Display Classes hierarchy showing vtkProp as root with vtkActor, vtkActor2D, vtkVolume specializations, and the evolved "painter" pipeline architecture replacing device-specific mappers.

## Chapter 25. Battle For Wesnoth

**Unit Definition in WML:**
```
[unit_type]
    id=Elvish Fighter
    name= _ "Elvish Fighter"
    race=elf
    image="units/elves-wood/fighter.png"
    profile="portraits/elves/fighter.png"
    hitpoints=33
    movement_type=woodland
    movement=5
    experience=40
    level=1
    alignment=neutral
    advances_to=Elvish Captain,Elvish Hero
    cost=14
    usage=fighter
    {LESS_NIMBLE_ELF}
    [attack]
        name=sword
        description=_"sword"
        icon=attacks/sword-elven.png
        type=blade
        range=melee
        damage=5
        number=4
    [/attack]
[/unit_type]
```

**WML Macro Definitions:**
File inclusion macro: `{gui/default/window/}` includes all .cfg files within gui/default/window/.

Ability modifier macro:
```
#define LESS_NIMBLE_ELF
    [defense]
        forest=40
    [/defense]
#enddef
```

Difficulty-based resource allocation:
```
#define GOLD EASY_AMOUNT NORMAL_AMOUNT HARD_AMOUNT
  #ifdef EASY
    gold={EASY_AMOUNT}
  #endif
  #ifdef NORMAL
    gold={NORMAL_AMOUNT}
  #endif
  #ifdef HARD
    gold={HARD_AMOUNT}
  #endif
#enddef
```
Usage: `{GOLD 50 100 200}` sets opponent gold based on difficulty level.

**Multiplayer Command Structure:**
```
[move]
    x="11,11,10,9,8,7"
    y="6,7,7,8,8,9"
[/move]
```
This WML node represents the path a unit follows, enabling complete game replay by storing the initial state and all subsequent player commands.

## Bibliography

This section contains no code examples, diagrams, or architectural illustrations. It is a bibliography consisting exclusively of formal citations in the format: [citation-key] Author(s): "Title or Reference". Publication venue, additional details, year. Examples of entries include: [CDG+06] Fay Chang et al. on BigTable; [DG04] Dean and Ghemawat on MapReduce; [DHJ+07] DeCandia et al. on Dynamo; [GGL03] Ghemawat, Gobioff, and Leung on Google File System.
