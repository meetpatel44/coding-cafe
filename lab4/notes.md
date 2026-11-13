\# Lab 4 – Git \& GitHub

\*\*Course:\*\* FM102 – Coding Café  

\*\*Name:\*\* Meet Patel  

\*\*Roll Number:\*\* U20260306



\---



\## Question 1: What did `--global` mean here? What would happen if you left it out?



The `--global` option means that the Git configuration is saved at the user level and applies to all repositories for that user. If it is omitted, the configuration is applied only to the current repository, provided the command is executed inside a Git repository.



\## Question 2: What appeared in `ls -a` but not in `ls`? What is inside it?



The `.git` directory appeared when hidden files were displayed using `ls -a` or `Get-ChildItem -Force` in Windows PowerShell. It contains Git's internal information, including commit objects, references, configuration files, logs, hooks and the staging index, which allow Git to manage the repository and maintain its history.



\## Question 3: Roughly how many files and folders is Git offering to track? Does anything in that list look like something you did not write?



Git was offering to track a large number of files and folders, including hundreds of entries from the `.venv` virtual environment. These included automatically generated dependencies and files that I had not personally written, which should not be included in the repository.



\## Question 4: Compare this `git status` with the one from Question 3. What disappeared?



After creating the `.gitignore` file, the files inside `.venv/`, along with matching Python cache files and operating-system metadata, disappeared from the untracked files listed by `git status`. This happened because Git now ignores files and folders matching the specified patterns.



\## Question 5: `.gitignore` itself shows up as untracked. Should it be committed, or ignored too? Why?



The `.gitignore` file itself should be committed rather than ignored. It contains instructions specifying which files and folders Git should exclude, and committing it ensures that everyone using the repository follows the same exclusion rules.



\## Question 6: `README.md` moved from one heading to another in the `git status` output. Which two? In the three-places model from the session, what just happened to it?



`README.md` moved from the untracked files section to the changes to be committed section after executing `git add README.md`. This means the file moved from the working directory into Git's staging area, where it was prepared to be included in the next commit.



\## Question 7: What did Git print after the commit? How many files did it say changed?



Git displayed a confirmation message indicating that the commit was successfully created, along with a summary of the files changed and the number of insertions and deletions. The initial commit included two files, `.gitignore` and `README.md`, according to the previously recorded repository notes.



\## Question 8: What are the first seven characters of your commit called, and what are they for?



The first seven characters are the abbreviated commit hash, derived from the commit's SHA-1 object ID. They provide a convenient way to identify and reference a particular commit in Git commands without having to type its entire hash.



\## Question 9: You now have two commits. Without looking it up: what are the four steps of the loop you just did twice?



The four steps of the Git workflow are edit, stage, commit and repeat. First, files are created or modified in the working directory, then the required changes are staged using `git add`, and finally saved permanently in the repository's history using `git commit`.



\## Question 10: Why does this file get a special name and a special place, rather than being called `notes.md` like everything else?



`README.md` has a special name because GitHub automatically recognises and displays it on the repository's front page. It provides visitors with an introduction to the project, its purpose and the organisation of its contents, making the repository easier to understand.



\## Question 11: What did `gh auth login` do that means you will not be asked for a password when you push?



The `gh auth login` command authenticates the GitHub CLI with my GitHub account. It establishes an authenticated session and configures the required credentials, allowing Git operations over HTTPS to communicate with GitHub without repeatedly asking for my account password.



\## Question 12: Refresh the repository page on GitHub. What is showing on the front page, and why that file?



The `README.md` file is displayed on the GitHub repository's front page as formatted Markdown. GitHub automatically recognises and renders README files to provide visitors with an overview of the repository and its contents.



\## Question 13: Run `git log --oneline` again. Did pushing change your local history in any way?



Pushing did not change my local Git history or create any new commits. It simply transferred the existing local commits to the remote GitHub repository, making the same commit history available online.



\## Question 14: Your repository is private but your TAs can now read it. In your own words, what is the difference between a repository being private and a repository not existing on GitHub at all?



A private repository exists on GitHub but its contents can only be accessed by its owner and people who have been granted permission. A repository that does not exist on GitHub has no hosted online location or repository history available for anyone to access.



\---



\*\*End of Lab 4 – Git \& GitHub\*\*

