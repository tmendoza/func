## What is it?

Func is a remote execution tool developed by some [folks](https://fedorahosted.org/func/) at Redhat several years ago.  The last commit
to the git repository over at RedHat was well over 2-3 years ago.  I have created my own personal clone of that repo to make sure I have
it going forward.  Who knows, RedHat may purge this project at some point in the future.

## Why keep using it?

Well I think the original func website said it best:

* Have you ever tried to command or query a large number of systems with SSH? Have you wanted a better way?
* Have you wanted a way to audit all of your remote commands on all of your systems?
* Tired of writing shell scripts and parsing command output?
* Are you fed up with CIM, WBEM, and complicated communication systems that prevent you from doing /real/ work?
* Well have we got a solution for you. It's Func. 

I have been using tools such as puppet, chef, cfengine, ansible, salt, Bladelogic, etc., etc.   One thing they have all done is move away
from low-level programming language operations.  I can appreciate the use of a well designed DSL, but when you need to full power of a programming language
at your finger tips, those tools I mentioned become cumbersome to work with.  In my own personal experience, in any non-trivial environment
configuration, you will need the full power of a programming language to be able to perform the tasks needed to get the job done.  This is
why all of the above mentioned tools have a way of executing arbitrary shell code:

| CM/Orchestration Tool | Shell Execution Docs                          							|	
| ---------------------	| ------------------------------------------------------------------------- | 	
| Ansible				| http://docs.ansible.com/shell_module.html 								|
| Puppet				| https://docs.puppetlabs.com/references/latest/type.html					|
| Salt					| http://docs.saltstack.com/en/latest/ref/states/all/salt.states.cmd.html	|
| Chef					| https://docs.chef.io/resource_execute.html								|
| cfengine				| https://docs.cfengine.com/docs/3.5/reference-promise-types-commands.html  |
| Bladelogic			| https://docs.bmc.com/docs/display/bsa86/Working+with+Network+Shell        |

Now anyone that knows me know I love writing shell scripts for administrative tasks, but even I realize that you can only go so far with the shell before
it becomes burdensome.  C/C++ can be burdensome also, so a language between the shell and a strongly typed compiled language was needed.  That is the reason why 
languages like Perl, Python, Tcl and Ruby were developed.  

These languages are easier to work with being that they are dynamic, but powerful enough to be able to build higher level abstractions.  My personal choice
is python.  I will let the Google-verse answer [Why Python](https://www.google.com/search?q=why+python&gws_rd=ssl).

In addition to allowing you to execute arbitrary shell scripts/code these tools also provide some type of API or module system that can be extended.

| CM/Orchestration Tool | Module Development Docs                          								|	
| ---------------------	| -----------------------------------------------------------------------------	| 	
| Ansible				| http://docs.ansible.com/modules.html   										|
| Puppet				| https://docs.puppetlabs.com/puppet/latest/reference/modules_fundamentals.html	|
| Salt					| http://docs.saltstack.com/en/latest/topics/development/modular_systems.html	|
| Chef					| https://supermarket.chef.io/cookbooks/modules									|
| cfengine				| https://docs.cfengine.com/archive/manuals/cf-manuals/cf2-modularize		  	|
| Bladelogic			| na																        	|

Why do they do this?  For the same reason why scripting languages were developed.  Just like the UNIX Shell, these tools are limited in what they can do in
an easy straightforward manner.  Func exposes the full python API to you and also allows you to execute Python code on a remote machines.  Don't get me wrong, 
shell scripts over SSH have there place, but with the SSH/Shell combo you lose the abstraction building power of a language such as Python, it is slow when 
having to execute shells scripts over hundreds if not thousands of servers.

Writing modules to plug into some existing framework, to me anyway, is a waste of time.  Especially if I have to:

1. Learn a new language like Ruby to write a module
2. Write tons of XML/YAML/JSON, templates or whatever to create an extension to an existing system
3. Deal with the [Kingdom of Nouns](http://steve-yegge.blogspot.com/2006/03/execution-in-kingdom-of-nouns.html) phenomenon.  Recipes, knives, States, Renderers, Classes, Oh My!

I find it interesting that the motivation behind using these tools is that it can reduce your workload when it comes to keeping systems up to date and in line
with some formal specification, but we end up with a mish-mash of incomplete DSL's, leaky abstractions, moving language specifications and poor implementations.

Look. Your going to have to write code!  Just choose the language you want, with a secure and reliable communications medium that allows you to execute remote
code.   Throw on top of that some built-in modules written in the core language and an ability to write your own modules in the core language and you get a lot
more flexibility without the chaos of managing another half-assed implementation of poorly designed language/framework.  Or, if you remember these questions about a
language from [SICP](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-10.html):

1. What are the primitives?
2. What are the means of combination? 
3. What are the means of abstraction?

If you cannot easily answer these 3 questions about the system your working with, or if they are not easily recognizable or non-existent, then sooner or later your
going to run into a limitation with the system your using.  Lastly, if you want the features that these systems provide, build them from the bottom up as opposed from
the top down.  You can easily add on top of a system such as func to give you things such as configuration management, convergence, idempotency, etc. but, as you can see,
adding in the low-level flexibility of func on top of a system such as the ones mentioned above is like "[...building a bookshelf out of mashed potatoes.](http://quotes.lifehack.org/quote/jamie-zawinski/using-these-toolkits-is-like-trying-to/)"

## Contributors

* <tmendoza@superbadmofo.com>

## License

[GPLv2](http://www.gnu.org/licenses/gpl-2.0.html)
