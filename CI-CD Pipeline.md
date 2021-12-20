# Understanding CI/CD Pipeline:
> CI - Continuous Integration  
CD - Continoous Delivery  

`CI/CD` practices are currently the widely accepted choice `to reduce the software development and the delivery cycle time`  

**Challanges:**  
In today’s fast-evolving landscape, one of the top challenges for software companies is `to respond quickly to market and customer demands`  

**Solution:**  
The `CI/CD methodology` emerged as the key solution to this challenge  

**What is `CI`:**  
In CI practice,  

We, the developers, build, run, and test code on our own local machines before we commit our codechanges  to the version control repository (GitHub, BitBucket etc).  
Once the changes are merged into the repository, a chain of events get triggered.  

A typical first step in this chain is:
- the creation of the latest version of the source code.  
- If the build is successful, the unit tests will be carried out.  
- If unit testing is successful, the build is deployed in test environments where system testing is performed (usually by automated testing).  
- a status report of this whole activity will be shared back to the team/developers,  
such as build number, defects, and number of tests.  

Continuous integration (CI) helps ensure that the software is fully integrated.

Typically, the CI pipeline involves the following tasks:  
- `Detect changes` to the source code repository (new commits appear)
- Analysis of the `quality` of source code
- `Project build`
- Perform all `unit tests`
- Run all `integration tests`
- Generate `deployable artifacts`
- Status of `report`

and, if if one of the steps above fails:  
- Integration may stop or continue depending on the severity and configuration of the defect.
- Results are reported to the team via email or chat system.
- Team fixes the defect and commits it again
- Tasks are carried out again

**What is `CD`:**  
CD is followed by CI activity!  

`CI` is the process to build and test automatically,  
`CD` deploys all code changes to the testing or staging environment in the build.  

CD enables builds to be released to the production environment when needed.  
This allows us to deploy on our own, no support needed from other teams.  
Thus, this reduces the overall time from developent to release into production, this way we achieve lightening-fast delivery to the customers!  

Before deploying software for production,  the CD process includes automated system testing, unit testing, and integration testing.  
The steps from CI to CD are usually completed automatically, including automated unit testing, integration, and system level.  
As testing can fail at any level and environment, CI / CD must include a feedback channel to quickly report failures to developers  

**`A CI / CD pipeline is a method for delivering a change unit that begins from development to delivery`,**  
It usually consisting of the following main phases:  
1. Commit
2. Build
3. Execute Tests (Unit/Regression/Automation)
4. Deploy

**Conclusion:**  
`CI / CD` are two of the best practices of `DevOps` in addressing misalignment between developers and the operational team.  
With the presence of `automation`, developers can release changes and new features more frequently,  
while operation teams have better overall stability.  

There are several tools out there in the market which can be used for implementing CI/CD pipeline,  out of which the most famous ones are:  
`Jenkins`, AWS `CodeBuild` etc.  

**Reference:**  
1. https://medium.com/devops-dudes/what-is-ci-cd-continuous-integration-continuous-delivery-in-2020-988765f5d116

