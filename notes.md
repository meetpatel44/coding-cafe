1. Because -a is a Unix/Linux option. In PowerShell, use ls -Force to display hidden files and folders.

2\. Because D:\\CodingCafe already contained a .git folder. Git reused the existing repository rather than creating a new one.

3.Because README.md didn't exist yet. After you created it with notepad README.md, Git could add it.

4.Because creating a file doesn't automatically make Git track it. git add . staged it along with README.md.

5\. It stages new and modified files in the current directory and its subdirectories, except files ignored by Git.

6\. It records the staged changes as a commit with the message Lab work so far.

7\. 94eb9a6. They form the short commit hash, which identifies your commit and lets you reference it in commands such as git show 94eb9a6.

8.Because the correct option is --oneline, not --online. It displays each commit in a compact, single-line format.

Your repository is now initialized, and your first commit contains both .gitignore and README.md.



