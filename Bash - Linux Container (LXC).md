# Linux Container — 

A Linux® container is a set of 1 or more processes that are isolated from the rest of the system.  
All the files necessary to run them are provided from a distinct image,  
meaning Linux containers are portable and consistent as they move from development, to testing, and finally to production.  
This makes them much quicker to use than development pipelines that rely on replicating traditional testing environments.  
Because of their popularity and ease of use containers are also an important part of IT security  

**Problem Statement**:  
Imagine you’re developing an application. You do your work on a laptop and your environment has a specific configuration.  
Other developers may have slightly different configurations.  
The application you're developing relies on that configuration and is dependent on specific libraries, dependencies, and files.  
Meanwhile, your business has development and production environments  
that are standardized with their own configurations and their own sets of supporting files.  
You want to emulate those environments as much as possible locally,  
but without all the overhead of recreating the server environments.  
So, how do you make your app work across these environments, 
pass quality assurance, and get your app deployed without massive headaches, rewriting, and break-fixing?  

The answer: containers  

![image](https://user-images.githubusercontent.com/26399543/147829382-3247e7b5-9606-456c-b2fc-a23e2550fda2.png)

The container that holds your application has the necessary libraries, dependencies, and files  
so, you can move it through production without nasty side effects.  

And, Linux containers can be applied to many different problems where portability, configurability, and isolation is needed.  
The point of Linux containers is to develop faster and meet business needs as they arise.  
In some cases, such as real-time data streaming with Apache Kafka, containers are essential  
because they're the only way to provide the scalability an application needs.  
No matter the infrastructure—on-premise, in the cloud, or a hybrid of the two—containers meet the demand.  

**Comparison** -  
**Virtualization** lets your operating systems (Windows or Linux) run simultaneously on a single hardware system.  
**Containers** share the same operating system kernel and isolate the application processes from the rest of the system  

![image](https://user-images.githubusercontent.com/26399543/147829688-15cb4c65-ad10-43ea-901f-e4d940939f63.png)

# What is LXC? 

The Linux Containers project (LXC) is an open source container platform  
that provides a set of tools, templates, libraries, and language bindings.  
LXC has a simple command line interface that improves the user experience when starting containers.  

LXC offers an operating-system level virtualization environment that is available to be installed on many Linux-based systems.  
Your Linux distribution may have it available through its package repository.  

**Basic Steps to start with Linux Containers** -  
1. Install LXC: sudo apt-get install lxc
2. Create a container: sudo lxc-create -t fedora -n fed-01
3. List your containers: sudo lxc-ls
4. Start a container: sudo lxc-start -d -n fed-01
5. Get a console for your container: sudo lxc-console -n fed-01

**Docker:**  

Docker came onto the scene (by way of dotCloud) with their eponymous container technology.  
The docker technology added a lot of new concepts and  
tools—a simple command line interface for running and  
building new layered images, a server daemon, a library of pre-built container images, and  
the concept of a registry server. Combined,  
these technologies allowed users to quickly build new layered containers and easily share them with others.  

**Reference:**  
1. https://linuxcontainers.org/lxc/getting-started/
2. https://www.networkworld.com/article/3250626/exploring-linux-containers.html

