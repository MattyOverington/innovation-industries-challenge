# innovation-industries-challenge
Dev challenge project for Innovation industries full stack position

## How long did it take you?

I spent roughly 3 hours working.

## What did you find easy?

Using SQLAlchemy and Pydantic to manage database structure was fairly intutive and improves the experience of interacting with SQL for me.
Vue and Vuetify were also quite easy to grasp and I found using Vue's binding feature to be very useful. When compared to other templating languages I have used,
such as Handlebars, I find Vue's functionality to be more complete and obviously more powerful. The fact that it is able to so neatly incorporate Javascript functionality 
in a way that clearly lays out code structure was also very nice to work with.

## What did you find hard?

I ran into an issue towards the end of my work when attempting to test the full functionality.

    ProgrammingError: SQLite objects created in a thread can only be used in that same thread.The object was created in thread id 23508 and this is thread id 22640

These errors prevented me from properly testing the modify and summation functionalities, as this error seemed to prevent /job/job POST requests from adding a job to the 
database. I was unable to determine if I had made some mistake in copying the routes and table definitions from Employee, or if some external factor was causing these errors

I also found Vuetify somewhat cumbersome for a first-timer, and simply pushed out a quick index page without using any of the Vuetify components. The control in styling
I have been used to using with plain HTML/CSS didn't seem readily accessible in Vuetify, and I expect that I'd need to spend some more time with it to relearn finer styling

Two minor pieces of functionality which I could not manage to properly troubleshoot were Vuetify breadcrumbs, and using `:list='this.employeeIDs'` to autofill employee 
primary keys for the `job.lead`Foreign key field. Both of these tasks seemed fairly simple and I couldn't gain much insight into what was going wrong.

## What would you like to learn more about?

Using Vue in conjunction with data structures (as I tried with the Foreign Key in `job`) interested me and I would enjoy putting together/orking with a more functional and elegant 
data interaction interface. Learning more about Vue and getting comfortable with Vuetify also interest me, as I'd like to try some web design that moves away from the use 
of plain HTML and CSS. Spending some more time coding in Windows is also appealing, as most of my personal dev work has used WSL or Linux and I'd be interested to see how
it fares in comparison.
