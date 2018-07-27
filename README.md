From https://realpython.com/documenting-python-code/ .

Why comment / document?

* "Code is more often read than written" - Guido Van Rossum, so it's important to document it for others AND yourself when you come back to it and have no idea why you did what you did.
* If you think it's difficult to remember the code that YOU wrote, imagine how difficult it is for others who have no context.


Commenting vs. Documenting

* Comments describe your code for other developers. "Code tells you how; Comments tell you why" - Jeff Atwood
* Documentation describes how to use the code for other users. Documentation describes interfaces and high-level usage.

A few use cases for commenting:

* Why you chose a particular algorithm over another.
* A high-level description of how a complex algorithm works, if it's difficult to interpret the code.
* High-level, human-readable description of a section of code (why are we doing this?)
* Stubs that describe your plan before you write code
* Tagging: TODO, BUG, FIXME, etc. How much should we really be doing this? Good to at least leave a note if you truly don't have the time to fix it.


Code should stand on its own. The best comment is no comment. Readers of your code should know the language, so for simple operations, no comment should be necessary.
