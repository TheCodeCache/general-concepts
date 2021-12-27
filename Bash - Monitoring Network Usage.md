
# Network Monitoring Management Tools:  

These're just a few following network monitoring tools in Linux -  
- **nload**  
  `nload` is a command-line tool that displays the network usage on the system.  
  It belongs to the category of network monitoring tool in Linux that simply sum up all the network traffic on a network interface.  
- **speedometer**  
  `speedometer` is a network monitoring tool.  
  Similar to `nload`, it doesn’t differentiate the network traffic on a network interface by socket or processes.  
  However, the display of `speedometer` is much more customizable.  
- **iftop**  
  `iftop` is a command-line tool that displays network usage by listening to the interface.  
  In contrast to `nload` and `speedometer`, it monitors the network usage on each socket.  
  
  To install `iftop` on **Debian based Linux**, we'll use `apt-get` as follows:  
```shell
$ apt-get install -y iftop
```  
  To install `iftop` on **RHEL based Linux**, we'll use `apt-get` as follows:  
```shell
$ yum install -y epel-release  
$ yum install -y iftop
```  
- **nethogs**  
  `nethogs` is yet another command-line tool for monitoring network usage.  
  It groups network traffic on a network interface by the process ID that generates or receives the network traffic.  
  As a result, we’ll be able to monitor the network bandwidth consumption of different processes.  
  to install:  
  on Debian based Linux - use `apt-get install -y nethogs`  
  on Redhat based Linux - use `yum install -y nethogs`  

```shell
  $ nethogs
```
  ![image](https://user-images.githubusercontent.com/26399543/147472425-dd85b972-5322-48a5-b499-5119bd74234d.png)  
  
  The above screen shows the bandwidth consumed by each process.  
  
  To change the **refresh interval**, we can use the flag -d:  
```shell
  $ nethogs -d 2
```
  **Trace mode**:
```shell
  $ nethogs -t
```
  In trace mode, the reports are generated and appended to the console output.  
  Therefore, providing us a stream of reports over time that can be used for further processing.  

**Reference:**  
1. https://www.baeldung.com/linux/monitor-network-usage

