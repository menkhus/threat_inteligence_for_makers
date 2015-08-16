## Security Threat Intelligence for Software Builders Testers and Maintainers

### These are the notes for a talk I am giving at the CSTTF
conference in Colorado Sprigns, CO August 19,20 2015.

http://www.fbcinc.com/e/csttf/

### This is a talk meant to share the concepts of directed 
### threat discovery for software projects. The security
### is someone outmoded for software creators. It's better
### to look at the project's composition rather than count on
### a security tool only.
### Mark Menkhus, August 2015

This work is licensed under the Creative Commons Attribution 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by/3.0/

   ** Part 0 ** 
Quote:
    "There is nothing concealed that will not be disclosed, or hidden that will not be made known."

Audience -
    Software people that make or support products and services.
    Intelligence staff in roles that have the opportunity to decrease threat for companies and organizations... if I only knew what to look for.
    Security researchers who want to make a deeper impact on a particular client
    Spies, espionage agents, attackers

   ** Part 1 **

Threat intelligence stems from requirements
    What are were protecting
    What is our obligation
    How do we protect?
    Warning - this is not a magic bullet

Why Intelligence:
Systems are not delivered in isolation
Connectedness creates emergent properties
Defensive postures of our customers are not enough to protect them
Allows for focus on topics that impact the business
Reduces cost
Increases Response

Summary:    
"Choose to use intelligence to make informed risk management choices by reducing the problem domain to what is in scope for our product and responsibility."

focus
picture - http://www.factzoo.com/birds/spectacled-owl-striking-black-yellow-white.html 

Methodology:
Understanding the composition of the software projects
Understand the environment
picture - http://thechicsite.com/2014/07/22/slow-cooker-black-bean-soup/ 
    
Intelligence
    requirements - Strategy, Plan, Scope, Action, Measurement 

Strategy
Strategy We want want an outcome, we want to have
a positive impact based on the customer experience and outcomes.

Plan
For large systems delivery choose times when code can be updated. What is the release vehicle for your updates? What is your ability to fit a fix or series of fixes into your life-cycle. Avoid one off patches.

Scope
Intelligence domain - threats to the systems we use to produce, support and deliver to service to the customer. Threats to the components we delivered to the customer.
Threats to the software you write, your own innovations and IP, ouch!

How
Apply intelligence to inform risk management approaches for the software we are building -or- fix every single bug we hear of?  
Think like the enemy -
What is the easiest approach to find threats
What is the most effective approach to find many targets
Can I cheat and use google?
What could Shodan do?

Think like the bad guy:
What am I attacking
What are it's weaknesses
how do I find this weakness in a sea of systems?

Intelligence is the same whether defensive or offensive        
Compositional analysis defines the direction of search. 
Version analysis defines the shape of the horizon
Latent bugs define the technical debt of your systems
Risk models inform your tolerance for vulnerability
If you are delivering general purpose software, your risk models are soft.

Conventional wisdom: 
The more specialized your software the more you can document the risks, use cases and narrow the
requirement for risk response.
APT and insider threat suggest that this is outmoded.

Measure outcomes:
Being Informed, understanding the depth of technical debt, plan for response, respond, inform the customers, system maintainers, and compliance staff. Be transparent.

Requirements
Design
Implementation
Verification
Maintanence

Vulnerability management in your delivered product
what 3rd party code did you leverage
what services did you implement that has latent security bugs
what services did you implement that has emergent 
security bugs

Delivery as a lump

Delivery as a continuously improved and updated service

    ** Part 2 **

External sources of raw information
News
email lists
Social Sites
NVD CVE data
Exploit databases
Vendors
Security vendors
Breach notifications

Your businesses as a source of information
3rd party software used in your code
License analysis registries
3rd party code lists as part of open source behavior
Libraries
Code management tools
Test tools
Operating environment types
Components used in system integration
    supplier security requirements
Hosting vendors
SaaS used
Tools used to produce software

What is the intersection between sources of information and your business
    Mashup
    Lookup
    Set theory
    Word association
    Sounds like
    Histogram

Threat models
network attacker
web attacker
reuse or replay of access controls
escalation of access controls

Leverage
indicators of threat - vulnerability lexicon
mashup vulnerability lexicon with open source material
database lookup

    ** Part 3 **

Case studies

Simple
Periodic CVE analysis, read it like a news paper
** at least 100 CVEs per week
** score from 0-10
** Eliminate the noise, create a don't care list
** Choose a level of criticality
** use a maven, wizard, guru
** throw away architectures, vendors not used
** cascade and evaluate what is left

More complex:
Create and Use the source inventory look up in database
Search for newest products impacted
Try a SQL CPE match
Manually evaluate reported versions against what is actually used
Email a report and hold a meeting to evaluate

Automated Analysis:
    ** Search Package Name and Version information 
    ** leverage CPE
    ** count the depth of technical debt in years
    ** count the depth in number of CVEs
    ** look at the severity
    ** Validate and file bug reports

Putting Automation Intelligence into the build environment
    ** Victims - https://github.com/victims
    ** OWASP dependency-check - https://jeremylong.github.io/DependencyCheck/
    ** JavaScript retire.js - https://github.com/victims/victims-enforcer
    ** falco https://github.com/menkhus/falco

Intelligence - Chatter, Noise, feeds, news, conferences
    ** Look for vulnerability news
    ** Look for relevancy
    ** Look for your company names
    ** Look for supplier names
    ** Daily reporting

The numbers - automation can read hundreds of thousands of articles a minute.
    ** 

Really? Does this work?
    Yes
Is it hard?
    Well at first

Sources:
    Wateringholes or evaporation ponds
    https://news.ycombinator.com/
    https://www.reddit.com/r/netsec
    http://slashdot.org/
    http://theregister.co.uk
    http://www.informationweek.com/

For pay services:
    Data scientists
    User interfaces
    Graphs and charts
    Trending
    API's
    Feeds
    Customized reports for your needs
    Meet the need of IT operations threat intelligence

Making Friends
    Threat intelligence teams in Company
    Patch teams
    Customers
    Mavens

Case studies are hard to share about live companies
    names changed

***********************************************************************
sqlite3 $vfeed_db 'select distinct cveid from cve_cpe where cpeid like "%openssl%" order by cveid;' | grep CVE-2015 | wc -l
-- Loading resources from /Users/menkhus/.sqliterc
      21
sting:~ menkhus$ sqlite3 $vfeed_db 'select distinct cveid from cve_cpe where cpeid like "%openssl%" order by cveid;' | grep CVE-2014 | wc -l
-- Loading resources from /Users/menkhus/.sqliterc
      26
sting:~ menkhus$ sqlite3 $vfeed_db 'select distinct cveid from cve_cpe where cpeid like "%openssl%" order by cveid;' | grep CVE-2013 | wc -l
-- Loading resources from /Users/menkhus/.sqliterc
       6
sting:~ menkhus$ sqlite3 $vfeed_db 'select distinct cveid from cve_cpe where cpeid like "%openssl%" order by cveid;' | grep CVE-2012 | wc -l
-- Loading resources from /Users/menkhus/.sqliterc
       8
sting:~ menkhus$ sqlite3 $vfeed_db 'select distinct cveid from cve_cpe where cpeid like "%openssl%" order by cveid;' | grep CVE-2011 | wc -l
-- Loading resources from /Users/menkhus/.sqliterc
      12
sting:~ menkhus$ sqlite3 $vfeed_db 'select distinct cveid from cve_cpe where cpeid like "%openssl%" order by cveid;' | grep CVE-2010 | wc -l
-- Loading resources from /Users/menkhus/.sqliterc
      10
sting:~ menkhus$ sqlite3 $vfeed_db 'select distinct cveid from cve_cpe where cpeid like "%openssl%" order by cveid;' | grep CVE-2009 | wc -l
-- Loading resources from /Users/menkhus/.sqliterc
      14
