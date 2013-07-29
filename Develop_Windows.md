**Overview**

\

This document covers the process to setup the development environment on
a windows machine. The following softwares are configured to build,
deploy and run the applications on the apache tomcat server.

 

​1.Subversion 1.7.9

​2.Maven 3.0.5

​3.Apache Tomcat 7.0.40

\

**System Requirements:**

Java – Apache Tomcat 7.0 requires a Java Standard Edition Runtime
Environment (JRE) version 6 or later. Make sure JDK 1.6 is installed,
“JAVA\_HOME” variable is added in windows environment variable and
%JAVA\_HOME%\\bin is added to the system Path variable.

\

**Pre- Requisite software Install**

***Maven Installation:***

****\

Download the maven zip file from the maven official website, download
link is  HYPERLINK
"http://maven.apache.org/download.cgi"http://maven.apache.org/download.cgi
and the latest version is Maven 3.0.5.

\

Extract the downloaded zip file i.e. Apache-maven-3.0.5-bin.zip to the
directory you wish to install Maven 3.0.5. (Assuming the file was
extracted to C:\\Program Files\\ and the subdirectory
apache-maven-3.0.5)

\

Create M2\_HOME system variable with the value “C:\\Program
Files\\apache-maven-3.0.5” and append %M2\_HOME%\\bin to the Path
environment variable.

\

Create MAVEN\_OPTS environment variable to specify the JVM properties
with the value -Xms512m “-Xmx1024m”.

\

To verify the installation open new command prompt and run “mvn
–version”.

\

***Subversion Installation:***

\

Download the latest Subversion binary installer from  HYPERLINK
"http://subversion.apache.org/packages.html"http://subversion.apache.org/packages.html
(assuming the latest Subversion 1.7.9 is downloaded from the Collabnet)

\

Run the installer and install the product to the default path, the
installer will add the “C:\\Program Files\\CollabNet\\Subversion Client”
to the system Path variable and installed to the default path).

\

To verify the installation open new command prompt and run “svn
–version”

\

***Apache Tomcat 7.0.40 Installation:***

\

Download the binary distribution of the tomcat from:  HYPERLINK
"http://tomcat.apache.org/download-70.cgi"http://tomcat.apache.org/download-70.cgi, 
the latest version is Apache Tomcat 7.0.40.

\

Unzip the binary distribution into the directory of your choice,
assuming HYPERLINK
"C:\\\\Users\\\\apache-tomcat-7.0.40"C:\\apache-tomcat-7.0.40\\ is the
tomcat installed directory and “CATALINA\_HOME” is used to refer to the
full pathname of that directory.

\

**Configure workspace:**

\

Subversion repository is hosted on Unfuddle and to access the project
repository

\

svn checkout https://fast.unfuddle.com/svn/fast\_fs/
C:\\Applications\\FastSpringDev

\

**Build:**

\

Once Maven is installed, open command prompt and change directory to
\~/fs\_workspace/com.bright.build/ and run

\

*mvn -Ptest clean package** *

\

**Configure Tomcat server for Application Deployment:**

\

To increase the memory of the Java JVM, add the following line to
catalina.bat file under *%CATALINA\_HOME%\\bin*.

\

*set JAVA\_OPTS="-Djava.awt.headless=true -Dfile.encoding=UTF-8 -server
-Xms512m -Xmx1024m -XX:PermSize=256m -XX:MaxPermSize=512m" *

\

Delete /webapps/\* and /work/\* 

\

Copy  HYPERLINK
"http://github.com/fastspring/fastspring-dev-docs/blob/master/sections/tomcat/server.development.xml"server.xml
to /conf 

\

Copy  HYPERLINK
"http://github.com/fastspring/fastspring-dev-docs/blob/master/sections/tomcat/context.development.xml"context.xml
to /conf 

\

Copy  HYPERLINK
"http://github.com/fastspring/fastspring-dev-docs/blob/master/sections/tomcat/mail-1.4.jar"mail-1.4.jar
to /lib 

\

Copy  HYPERLINK
"http://github.com/fastspring/fastspring-dev-docs/blob/master/sections/tomcat/hsqldb-2.2.9.jar"hsqldb-2.2.9.jar
to /lib 

\

Copy  HYPERLINK
"http://github.com/fastspring/fastspring-dev-docs/blob/master/sections/tomcat/log4j.development.properties"log4j.properties
to /lib 

\

***To configure SSL support on Tomcat***

\

Create a keystorefile to store the server's private key and self-signed
certificate by executing the following command inside /conf:

*keytool -genkey -alias tomcat -keyalg RSA -keystore conf/keystore
-storepass changeit *

**\

Comment APR lifecycle listener in the server.xml to allow tomcat to use
the Java JSSE implementation.

******\

***Configure SMTP Server:***

\

Download hMailServer binary installer from  HYPERLINK
"http://www.hmailserver.com/index.php?page=download"http://www.hmailserver.com/index.php?page=download.

\

Install according to the instructions from  HYPERLINK
"http://www.hmailserver.com/documentation/latest/?page=howto\_install"http://www.hmailserver.com/documentation/latest/?page=howto\_install** **

\

Change the smtp port number from 3025 to 25 in the mail resource of the
/conf/server.xml. 

\

***Deploy:***

\

Copy the application wars to *%CATALINA\_HOME%\\webapps*

\

To start the server run this command on command prompt

\

*%CATALINA\_HOME%\\bin\\startup.bat*

\

The applications would be located at:

\

API:  HYPERLINK "https://localhost:8443/bm-api" \\t "\_blank"
https://localhost:8443/bm-api\
 Stores:  HYPERLINK "https://localhost:8443/bm-hosted" \\t "\_blank"
https://localhost:8443/bm-hosted\
 SpringBoard:  HYPERLINK "https://localhost:8443/bm-manager" \\t
"\_blank" https://localhost:8443/bm-manager\
 Tests:  HYPERLINK "https://localhost:8443/bm-test" \\t "\_blank"
https://localhost:8443/bm-test

\

\

**Test**

***Steps to test Stores:***

When you startup Tomcat it should initialize a DB environment suitable
for testing.

Connect to the Springboard using the url, HYPERLINK
"https://localhost:8443/bm-manager" \\t
"\_blank"https://localhost:8443/bm-manager and login using the below
credentials.

Company:  Demo\
 User:  Administrator\
 Pass: demo

Click on “Store Testing” in the Products and Settings” section will open
a popup window.

Clicking on a product name in the popup list will open a new window that
loads "/bm-hosted".

***Steps to run Unit test:***

To run the unit tests it is necessary to access it via a web environment
HYPERLINK "http://localhost:8080/bm-test/" \\t
"\_blank"http://localhost:8080/bm-test/

 Click the top link which says "com".  This runs ALL tests (all tests in
the "com" package and descendants).

The tests turn GREEN as they are successfully run and failed tests will
turn RED and report the errors.

\

\

\

\

\

\

\

\

