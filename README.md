# Slimeline

## Authors

Michael Hackett (hackett123) and Sam Paniccia (paniccia-s)

## About

Slimeline is a social media web app developed to track the important (and unimportant) moments in your life.

## Design

Slimeline is built with Django. The CSS comes from Bulma and Bulmaswatch. All code and ideas are our own.

## Planning 

- Remove the 'create slimeline' button 
	- each user only has one slimeline
	- Filtering can reduce what is shown
- Event: 
	- Author:		Who posted the event
	- Tagged_Users: 	Other users involved in the event
	- Title:		Name of the event
	- Summary: 		Brief explanation 
	- Content:		Whatever the user wants to provide
	- Is_Private:		If true, only the author can see this event
	- Upslimes:		Upvotes
	- Created_At:		Time of creation
	- Start_Time:		Start of the event
	- End_Time:		End of the event
		- Some sort of dropdown/UI-friendly option for discrete/continuous event TBD
	- Tags:			Public tagging by the author to label events etc
		- Primitive for first pass

	
