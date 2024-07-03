# Methodology

This workshop is based on two styles of teaching programming: Live Coding modeling and the PRIMM method. These two are valuable in deepening understanding of code concepts in young developers and avoiding misconcep[tions about best practices regarding code. Feel free to take the concepts in this workshop and change them to fit your groups particular needs. It's expected that the presenter is familiar with Python, GitHub UI like Merge Requests, using Codespaces, forking repos, git commans, and more. 

## Getting Started

It's important that every participant have a GitHub account before starting. Participants should be able to log in and access either the repo where code is stored or the project they can fork later on. For the beggining, however, participants will pay attention to the presenter and, at presenters choice, copy the code or simply follow along. 

The Presenter is going to live build the code for the 8 ball in front of the participants. This should be done so that participants can see the code as it's being typed as well as the presenter. If it's live, project the code on a wall or TV so everyone can see. If virtual, share your screen and encourage viewers to keep your face up on screen as well. 

## Process 

1. Open GitHub and create a new repo. Open the WEB IDE in that repo and add a file called `magic_8ball.py`. This is where all the coding will take place for your presentation. 
1. Type out each line or section of [the code](/8_ball.py) while dicsussing why it's done or what effect it will have. It is not important to have the whole code memorized as the presenter; it is perfectly acceptable to have the code off to the side and check it or even copy and paste some sections. What's important is the explanation to participants. 
1. As the lesson progresses, feel free to present the code to participants without explanation and ask for a participant to describe what's happening and why. This can take the form of predictions of what will happen when the code is run. This can be especailly useful if you purposefully include an error (an unfinished function, improper indentation, etc.)
    Sample Questions: 
    - "Can someone help me name this variable?"
    - "What's going to happen if we run the code right now?"
    - "Who can recall how we got a random number earlier?"
    - "What should the parameters be on this function?"
1. Once the code is finished, commit it. Show participants the process for creating a new branch and merge request. 
    - If working locally, ensure your remote is set before you start the workshop. You should be able to use the GUI git functions of your IDE or use git commands in the terminal, whichever you prefer. 
    - If working in WebIDE, use the blue commit botton and create a new branch. Keep "Create new Merge Request" checked and go through the merge request process all the way to merging it into Main.
1. Show participants how to merge. Once it's merged to main, you can open Codespaces or clone the repo locally. Both are good methods to learn. 
1. Eiuther in Copdespaces or locally, run the code and double check for any mistakes. It is perfectly fine, even preferable, to have a few mistakes in the code to model troubleshooting/bug fixes in code. Participants new to programming should know that coding mistakes are normal and part of the process. Additionally, ensuring that participants know how to run the code is important as well. 

At this point you'll have taught how to write the 8 ball and shown it working. From here, it's up to you how to proceed. If participants copied along as you went, they should have a functioning 8ball app. If they merely watched and observed, they haven't written code yet. You can borrow from the PRIMM method here and have participants [fork the repo](https://docs.github.com/ee/user/project/repository/forking_workflow.html#creating-a-fork) (another important skill) and make adjustments to the code to make it their own. You can also have participants work to create the code on their own without looking at your code. Or both! This can be done in groups, pairs, or individually. What's important is participants are reading code, engaging with changes made to the code, and making it their own. 

While participants are building their apps, walk around and offer advice, help, or ask questions about what they're building. 

## Ideas for expanding

- Have the participants use the concepts in this workshop (functions, variables, input statements, etc) to build a related project. 
- Have partcipants build a function that asks the user to build the answers to the 8 ball before running the 8 ball function. 
- Have participants try to break each others apps with different inputs. Have participants try to protect against these breaks. 

