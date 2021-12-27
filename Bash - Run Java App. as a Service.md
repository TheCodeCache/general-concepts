# How to `Run a Java Application as a Service on Linux` - 


Any Java application from the system point-of-view is just an instance of the Java Virtual Machine.  
Let us make our applications run as system services on Linux machines.  

We'll use the facilities of the `systemd` software package.  
`systemd` is the initialization and service management system in most modern Linux distributions.  

There're two implementations - 
1. simple service
2. forking service

# Simple Service - 

In the `systemd` world, to create a system service, we need to prepare a `unit file` and `register` it properly.  

```shell
[Unit]
Description=My Java driven simple service
After=syslog.target network.target

[Service]
SuccessExitStatus=143

User=appuser
Group=appgroup

Type=simple

Environment="JAVA_HOME=/path/to/jvmdir"
WorkingDirectory=/path/to/app/workdir
ExecStart=${JAVA_HOME}/bin/java -jar javaapp.jar
ExecStop=/bin/kill -15 $MAINPID

[Install]
WantedBy=multi-user.target
```
We set the `Type of service` to `simple` because the system starts the JVM process directly, without spawning a child process.  

`ExecStop` specifies the service termination command,  
Then, we instruct systemd to send a `15` (SIGTERM) system signal to terminate the process gracefully.  
The JVM designers made Java return a non-zero exit code in case it is terminated by a system signal.  
As a non-zero base, they took `128`, and the resulting exit code is a sum of 128 and the signal numeric value.  

By setting `SuccessExitStatus` to `143`, we tell systemd to handle that value (128+15) as a normal exit.  

# Forking Service - 

The `simple` service `unit file` above could be sufficient for trivial applications,  
but, for more sophisticated or practical cases, we need to include additional settings.  

These can be JVM parameters as well as any other application-specific parameters,  
That may result in writing a wrapper shell script where we can set up all the required parameters before starting the JVM.  

Save below shell-script code in `wrapper.sh` file :   

```shell
#!/bin/bash

JAVA_HOME=/path/to/jvmdir
WORKDIR=/path/to/app/workdir
JAVA_OPTIONS=" -Xms256m -Xmx512m -server "
APP_OPTIONS=" -c /path/to/app.config -d /path/to/datadir "

cd $WORKDIR
"${JAVA_HOME}/bin/java" $JAVA_OPTIONS -jar javaapp.jar $APP_OPTIONS
```
Since, we use a shell script to start the service, the JVM will be started by the shell (bash) process.  
This operation is known as fork, and it’s why we set the service `Type` to `forking`  

```shell
[Unit]
Description=My Java forking service
After=syslog.target network.target
[Service]
SuccessExitStatus=143
User=appuser
Group=appgroup

Type=forking

ExecStart=/path/to/wrapper
ExecStop=/bin/kill -15 $MAINPID

[Install]
WantedBy=multi-user.target
```

# Registering and Running the Service - 

First, we need to name the unit file after the service name we want to have.  
In our examples, that could be `javasimple.service` or `javaforking.service`.  

Then, we put the unit file under one of the locations where systemd can find it.  
For an arbitrary service, `/etc/systemd/system` is a good choice.  

The full path to our system units, in that case, will be:  
- /etc/systemd/system/javasimple.service
- /etc/systemd/system/javaforking.service

Another possible path to place system units is `/usr/lib/systemd/system`.  
This is typically the location used by the system installation packages.  

Next, we'll control the service using the `systemctl utility` and pass either the `start`, `stop`, or `status` command.  

Before that, however, we should notify systemd that it has to rebuild its internal service database.  
Doing this will make it aware of the new system unit we introduced.  
We can do this by passing the daemon-reload command to systemctl.  

now, let us run all the commands we mentioned:  

```shell
sudo systemctl daemon-reload

sudo systemctl start javasimple.service
sudo systemctl status javasimple.service
● javasimple.service - My Java driven simple service
Loaded: loaded (/etc/systemd/system/javasimple.service; <strong>disabled</strong>; vendor preset: disabled)
Active: active (running) since Sun 2021-01-17 20:10:19 CET; 8s ago
Main PID: 8124 (java)
CGroup: /system.slice/javasimple.service
└─8124 /path/to/jvmdir/bin/java -jar javaapp.jar
```

We’ll need to run the `daemon-reload` command each time we modify the unit file.  

Next, we notice the system reports our service running but `disabled`.  
Disabled services will not start automatically when the system boots.  

Let us configure it to start up automatically along with the system - 

```shell
sudo systemctl enable javasimple.service
Created symlink from /etc/systemd/system/multi-user.target.wants/javasimple.service to /etc/systemd/system/javasimple.service
```
let us verify the refleceted changes:  
```shell
sudo systemctl status javasimple.service
● javasimple.service - My Java driven simple service
Loaded: loaded (/etc/systemd/system/javasimple.service; <strong>enabled</strong>; vendor preset: disabled)
Active: active (running) since Sun 2021-01-17 20:10:19 CET; 14min ago
Main PID: 8124 (java)
....
```

**Reference:**  
1. https://www.baeldung.com/linux/run-java-application-as-service



