# what_happens_when_your_type_google_com_in_your_browser_and_press_enter
---
When we type google.com and press enter on any web browser url input field, do you imagine what is going on behind ? The secret behind is very wide, it is not easy as the web browser gives immidiate response. There are different things happens or found behind, those are DNS, TCP/IP, Web server, Database server, Application server, 
Load balancer, SSL certicate, Firewall, http/https, Internet, and so on. For simple and single search through web browser almost all this things touched for successful response in a well designined and configured web server. Let's try to deep dive into whats happening behind web browser and how internet is working.

At the time some one type google.com on web browser and press enter, the web browser try to connect with DNS server and ask for Ip of google.com. The process is known as A DNS query (also known as a DNS request).
It is a demand for information sent from a user's computer (DNS client) to a DNS server. In most cases a DNS request is sent, to ask for the IP address associated with a domain name. An attempt to reach a domain, is actually a DNS client querying the DNS servers to get the IP address, related to that domain.
The DNS server gives back IP of google.com or any domain if asked to the web browser.

The web browser now it has the IP of google.com web server and it try's to connect. 
A web server is dedicated software that runs on the server-side. When any user requests their web browser to run any web page, the webserver places all the data materials together into an organized web page and forwards them back to the web browser with the help of the Internet
After successful connection with the web server the next step is requesting for data available in the web server of google.com. Google is a big campany and it have billion's of request for data at atime, so there are thousends of web server's are there working together not only one. But how this thousend web server working with one IP address? Here is another secret, Load balancer comes here in use. Actual thing is the IP assossiated with google.com is IP of google's load balancer. Load balancing refers to efficiently distributing incoming network traffic across a group of backend servers, also known as a server farm or server pool.
Modern high‑traffic websites must serve hundreds of thousands, if not millions, of concurrent requests from users or clients and return the correct text, images, video, or application data, all in a fast and reliable manner. To cost‑effectively scale to meet these high volumes, modern computing best practice generally requires adding more servers.
A load balancer acts as the “traffic cop” sitting in front of your servers and routing client requests across all servers capable of fulfilling those requests in a manner that maximizes speed and capacity utilization and ensures that no one server is overworked, which could degrade performance. If a single server goes down, the load balancer redirects traffic to the remaining online servers. When a new server is added to the server group, the load balancer automatically starts to send requests to it.
After the load balancer directs the web browser to free web server then the connection between web server and web browser is created. The web browser starts to request a data. Web server gives html file to the web browser and then the web browser accepts and render the given html, css and javascript files accordingly. 

Our web browser requests data from server (a computer located very far) through internet. On the internet there is rule or protocol for any device  to communicate with each other, the so called TCP. 
TCP stands for Transmission Control Protocol a communications standard that enables application programs and computing devices to exchange messages over a network. It is designed to send packets across the internet and ensure the successful delivery of data and messages over networks.

TCP organizes data so that it can be transmitted between a server and a client. It guarantees the integrity of the data being communicated over a network. Before it transmits data, TCP establishes a connection between a source and its destination, which it ensures remains live until communication begins. It then breaks large amounts of data into smaller packets, while ensuring data integrity is in place throughout the process.

What is IP?
The Internet Protocol (IP) is the method for sending data from one device to another across the internet. Every device has an IP address that uniquely identifies it and enables it to communicate with and exchange data with other devices connected to the internet.

TCP vs. IP: What is the Difference?
TCP and IP are separate protocols that work together to ensure data is delivered to its intended destination within a network. IP obtains and defines the address—the IP address—of the application or device the data must be sent to. TCP is then responsible for transporting and routing data through the network architecture and ensuring it gets delivered to the destination application or device that IP has defined. 

In other words, the IP address is akin to a phone number assigned to a smartphone. TCP is the computer networking version of the technology used to make the smartphone ring and enable its user to talk to the person who called them. The two protocols are frequently used together and rely on each other for data to have a destination and safely reach it, which is why the process is regularly referred to as TCP/IP.

Security is main issue when working on the internet, there are different mechanisms for this. Lets discuss about  Firewall and SSL. In computing, a firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. A firewall typically establishes a barrier between a trusted network and an untrusted network, such as the Internet.
SSL Certificates are small data files that digitally bind a cryptographic key to an organization’s details. When installed on a web server, it activates the padlock and the https protocol and allows secure connections from a web server to a browser.

Http vs Https:
Http stands for hyper-text transfer protocol and Https stands for Secured hyper-text transfer protocol.
Https is different from Https it has SSL certificates.

The web server holds only static files like, text, photos, vidios, and so on. To make the website dynamic we need database server. Database server is 


In big and commercial websites like google, there is Application server found between web server and database server.
An application server is a modern form of platform middleware. It is system software that resides between the operating system (OS) on one side, the external resources (such as a database management system [DBMS], communications and Internet services) on another side and the users’ applications on the third side. The function of the application server is to act as host (or container) for the user’s business logic while facilitating access to and performance of the business application. The application server must perform despite the variable and competing traffic of client requests, hardware and software failures, the distributed nature of the larger-scale applications, and potential heterogeneity of data and processing resources required to fulfill the business requirements of the applications.

A high-end online-transaction-processing-style application server delivers business applications with guaranteed levels of performance, availability and integrity. An application server also supports multiple application design patterns, according to the nature of the business application and the practices in the particular industry for which the application has been designed. It typically supports multiple programming languages and deployment platforms, although most have a particular affinity to one or two of these. Some application servers that implement standard application interfaces and protocols, such as Java Enterprise Edition (Java EE), are entirely proprietary. At present, the proprietary application servers are typically built into OSs, packaged applications, such as portals and e-commerce solutions, or other products and are not offered as stand-alone products. Proprietary and Java EE-compliant application servers are estimated in our Market Share and Forecast reports.

As the application server market matures, high performance becomes a stronger criterion, and thus where vendors now incorporate extensions to application servers, such as extreme transaction processing and event-based processing capabilities, these are also included in this market segment.

When web browser requests web server to give back dynamic content, by default web sever holds only static data it trys to fetch from database server. A database server is a server which uses a database application that provides database services to other computer programs or to computers, as defined by the client–server model.
A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just database.
After the web server fetching data from database server it gives all the data to the web browser. The web browser again renders the given data for the user according to the the design. This cyle is repeatly done for every search using web browser.

---
***Sources***
```
https://www.gartner.com
https://www.oracle.com
https://en.wikipedia.org
https://www.cloudns.net
https://www.fortinet.com
https://www.javatpoint.com
https://www.google.com

```

---------------------------------------------------------------------------------------------------
